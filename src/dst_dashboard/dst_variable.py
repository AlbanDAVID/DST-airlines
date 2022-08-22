from dash import Dash, dcc, html, Input, Output, dash_table, dependencies
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from datetime import date
import query_data as qd
from dashboard import app
from dashboard import dbc
import plotly.graph_objects as go
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

header_filter = html.H4(
    "DST Filter", className="bg-primary text-white p-2 mb-2 text-center"
)

iata_dropdown = html.Div(
    [
        dbc.Label("by Flight IATA"),
        dcc.Dropdown(
            id="flight_iata",
            options=\
            [
                {'label': flight_iata, 'value': flight_iata}
                for flight_iata in qd.df_flights_summary['flight_iata'].unique()
            ],
            clearable=True,
            multi=True
        ),
    ],
    className="mb-4",
)

source_airport = html.Div(
    [
        dbc.Label("Source"),
        dcc.Dropdown(
            id="source",
            options=qd.df_airports['airport_name'],
            value=qd.df_airports['iata_code'],
            clearable=False,
        ),
    ],
    className="mb-4",
)

destination_airport = html.Div(
    [
        dbc.Label("Destination"),
        dcc.Dropdown(
            id="destination",
            options=qd.df_airports['airport_name'],
            value=qd.df_airports['iata_code'],
            clearable=False,
        ),
    ],
    className="mb-4",
)



datepicker = html.Div(
    dcc.DatePickerRange(
        id='start_end',
        start_date=date(2022, 8, 5),
        end_date=date(2022, 8, 25),
        className="mb-2"
    )
)

date_range = html.Div(
    [
        dbc.Label("Date Range"),
        datepicker
    ],

    className="dbc",
)

data_list = dash_table.DataTable(
    id='data_list',
    columns=[{"name": i, "id": i} for i in qd.df_summary_metrics.columns],
    data=None,
    row_selectable=False,
    row_deletable=False,
    editable=False,
    sort_action="native",
    style_table={"overflowX": "auto"},
    page_size=10,
            )


tab1 = dbc.Tab([dcc.Graph(id="Live", className='dbc')], label="Live")
tab3 = dbc.Tab([data_list], label="Table", className="p-4")
tab2 = dbc.Tab([dcc.Graph(id="Trajectories", className='dbc')], label="Trajectories")


tabs = dbc.Tabs([tab1, tab2, tab3])
filter_menu = dbc.Card(
    [
        dbc.Row(iata_dropdown),
        dbc.Row(
            [
                dbc.Col(source_airport),
                dbc.Col(destination_airport),
            ]),

        dbc.Row(tabs),
        # dbc.Row(datepicker),
    ],
    body=True,
)


@app.callback(
    dependencies.Output('source', 'value'),
    dependencies.Output('destination', 'value'),
    dependencies.Input('flight_iata', 'value')
)
def update_source_and_destination_drop_downs(flight_iata):
    if flight_iata is None or len(flight_iata) > 1:
        return None,None
    dep = qd.df_flights_summary[qd.df_flights_summary['flight_iata'] == flight_iata[0]]['dep_iata'].iloc[0]
    arr = qd.df_flights_summary[qd.df_flights_summary['flight_iata'] == flight_iata[0]]['arr_iata'].iloc[0]
    dep = qd.df_airports[qd.df_airports['iata_code'] == dep]['airport_name'].iloc[0]
    arr = qd.df_airports[qd.df_airports['iata_code'] == arr]['airport_name'].iloc[0]
    return arr, dep

@app.callback(

    dependencies.Output("data_list", "data"),
    dependencies.Output("Trajectories", "figure"),
    dependencies.Input('flight_iata', 'value'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def tabs_update(flight_iatas, theme):
    df = qd.df_summary_metrics.set_index(qd.df_summary_metrics['flight_iata']).loc[flight_iatas].drop_duplicates(subset=['flight_iata'])
    df_sma = qd.df_summary_metrics_airports.drop_duplicates(subset='flight_iata')

    fig = go.Figure(data=go.Scattergeo(
        mode='lines',
        line=dict(width=2, color='blue'),
    ))
    for i in flight_iatas:
        dep_lng = df_sma[df_sma['flight_iata'] == i]['dep_airport_lng'].iloc[0]
        dep_lat = df_sma[df_sma['flight_iata'] == i]['dep_airport_lat'].iloc[0]
        arr_lng = df_sma[df_sma['flight_iata'] == i]['arr_airport_lng'].iloc[0]
        arr_lat = df_sma[df_sma['flight_iata'] == i]['arr_airport_lat'].iloc[0]
        dep_airport_name = df_sma[df_sma['flight_iata'] == i]['dep_airport_name'].iloc[0]
        arr_airport_name = df_sma[df_sma['flight_iata'] == i]['arr_airport_name'].iloc[0]

        fig.add_trace(
            go.Scattergeo(
                locationmode='USA-states',
                lon=[dep_lng, arr_lng],
                lat=[dep_lat, arr_lat],
                mode='lines',
                line=dict(width=2, dash = 'solid'),
                name=i,
                hovertext = [dep_airport_name, arr_airport_name],
            )
        )
    fig = go.Figure(go.Scattergeo())
    fig.update_layout(
        title_text='Contour lines over globe<br>(Click and drag to rotate)',
        showlegend=True,
        geo=dict(
            showland=True,
            showcountries=True,
            showocean=True,
            countrywidth=0.5,
            landcolor='rgb(230, 145, 56)',
            lakecolor='rgb(0, 255, 255)',
            oceancolor='rgb(0, 255, 255)',
            projection=dict(
                type='orthographic',
                rotation=dict(
                    lon=-100,
                    lat=40,
                    roll=0
                )
            ),
            lonaxis=dict(
                showgrid=True,
                gridcolor='rgb(102, 102, 102)',
                gridwidth=0.5
            ),
            lataxis=dict(
                showgrid=True,
                gridcolor='rgb(102, 102, 102)',
                gridwidth=0.5
            ),
        )
    )

    return df.to_dict('records'), fig

@app.callback(
    Output('Live', 'figure'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def live_update(theme):
    df_sma = qd.df_summary_metrics_airports.drop_duplicates(subset='flight_iata')
    live_fig = px.scatter_mapbox(
        df_sma,
        lon='lng',
        lat='lat',
        hover_name="flight_iata",
        color="status_lufthansa",
        zoom=3,
        template=template_from_url(theme),

        )

    live_fig.update_layout(mapbox_style="carto-positron")
    return live_fig