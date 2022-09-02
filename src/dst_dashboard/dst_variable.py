import dash
from dash import Dash, dcc, html, Input, Output, dash_table, dependencies
import plotly.express as px
from dash import dcc
import pandas as pd
import query_data as qd
from dashboard import app
from dashboard import dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import datetime
import plotly.graph_objects as go

header_filter = html.H4(
    "DST Filter", className="bg-primary text-white p-2 mb-2 text-center"
)
start_date_picker = dcc.DatePickerSingle(
    id='start_date',
    clearable=True,
    className="dbc",

)
end_date_picker = dcc.DatePickerSingle(
    id='end_date',
    clearable=True,
    className="dbc",
)
iata_dropdown = html.Div(
    [
        dbc.Label("Flight IATA"),
        dcc.Dropdown(
            id="flight_iata",
            options=\
            [
                {'label': flight_iata, 'value': flight_iata}
                for flight_iata in qd.df_flights_summary['flight_iata'].unique()
            ],
            clearable=True,
        ),
    ],
    className="mb-4",
)

source_airport = html.Div(
    [
        dbc.Label("Departure Airport"),
        dcc.Dropdown(
            id="source",
            options=qd.df_airports['airport_name'],
            clearable=False,
        ),
        start_date_picker
    ],
    className="mb-4",
)

destination_airport = html.Div(
    [
        dbc.Label("Arrival Airport"),
        dcc.Dropdown(
            id="destination",
            options=qd.df_airports['airport_name'],
            clearable=False,
        ),
        end_date_picker
    ],
    className="mb-4",
)

flight_table = dash_table.DataTable(
    id='flight_table',
    columns=[{"name": i, "id": i} for i in qd.df_flights_summary.columns],
    data=None,
    row_selectable=False,
    row_deletable=False,
    editable=False,
    sort_action="native",
    style_table={"overflowX": "auto"},
    page_size=10,
            )

stat_figure = px.pie(qd.df_flights_summary, values=qd.df_flights_summary['status_lufthansa'].value_counts(normalize=True),
                     names = qd.df_flights_summary['status_lufthansa'].unique(), hole=.1)
stat = dcc.Graph(id="stat",figure=stat_figure, className='dbc')

tab1 = dbc.Tab([dcc.Graph(id="Trajectories", className='dbc')], label="Trajectories")
tab2 = dbc.Tab([dcc.Graph(id="Live", className='dbc')], label="Live")


flight_information_tab = dbc.Tab(
    [
        dbc.Card([
            dbc.CardHeader("General information"),
            dbc.CardBody([
                dbc.Row(
                    [
                        dbc.Col(html.H3(id='flight_icao', style={'color':'#0f1744'}), width='auto'),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H3(id='flight_status', style={'color': '#0f1744'}), width='auto'),
                    ]
                ),

                dbc.Row([
                    dbc.Col([
                        dbc.Row([
                            dbc.Col(html.Img(id='dep_country_img', style={'width': '100%'}), width=4),
                        ]),
                        dbc.Row([
                            dbc.Col(html.H4(id='dep_airport'), width='auto', style={'color': '#0f1744'}),
                        ])
                    ],
                    width=6),

                    dbc.Col([
                        dbc.Row([
                            dbc.Col(html.Img(id='arr_country_img', style={'width': '100%'}), width=4),
                        ]),
                        dbc.Row([
                            dbc.Col(html.H4(id='arr_airport'), width='auto', style={'color': '#0f1744'}),
                        ])
                    ],width=6)
                    ])])
            ]),
        dbc.Card([
            dbc.CardHeader("Departure and Arrival time"),
            dbc.CardBody(
                dbc.Row([
                    dbc.Col([
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=app.get_asset_url('clock2.png'), style={'width': '70%'}), width=2),
                                dbc.Col(html.H6("Scheduled :"), width='auto'),
                                dbc.Col(html.H6(id='dep_time'), width='auto')
                            ]),
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=app.get_asset_url('clock2.png'), style={'width': '70%'}), width=2),
                                dbc.Col(html.H6("Actual :"), width='auto'),
                                dbc.Col(html.H6(id='dep_time_real'), width='auto')
                            ]),
                    ],
                        width=6),
                    dbc.Col([
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=app.get_asset_url('clock2.png'), style={'width': '70%'}), width=2),
                                dbc.Col(html.H6("Scheduled :"), width='auto'),
                                dbc.Col(html.H6(id='arr_time'), width='auto')
                           ]),
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=app.get_asset_url('clock2.png'), style={'width': '70%'}), width=2),
                                dbc.Col(html.H6("Actual :"), width='auto'),
                                dbc.Col(html.H6(id='arr_time_real'), width='auto')
                            ]),

                    ],
                        width=6),
                ]))
        ]),

        dbc.Card([
            dbc.CardHeader("Flight Metrics"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H6('Speed = ', style={'color': '#0f1744'}), width ='auto'),
                    dbc.Col(html.H6(id='speed', style={'color': '#0f1744'}), width='auto'),
                    dbc.Col(html.H6('km/h', style={'color': '#0f1744'}), width='auto'),
                ]),
                dbc.Row([
                    dbc.Col(html.H6('Direction = ', style={'color': '#0f1744'}), width='auto'),
                    dbc.Col(html.H6(id='direction', style={'color': '#0f1744'}), width='auto'),
                    dbc.Col(html.H6('°', style={'color': '#0f1744'}), width='auto'),
                ]),
                dbc.Row([
                    dbc.Col(html.H6('Altitude = ', style={'color': '#0f1744'}), width='auto'),
                    dbc.Col(html.H6(id='altitude', style={'color': '#0f1744'}), width='auto'),
                    dbc.Col(html.H6('m', style={'color': '#0f1744'}), width='auto'),
                ]),
                dbc.Row(dcc.Graph(id="position", className='dbc'))


            ])
        ])

    ],
    label="Flight"
)

tabs = dbc.Tabs([flight_information_tab, tab2])
filter_menu = html.Div (
    [
        dbc.Row(
            [
                dbc.Col(html.Img(src=app.get_asset_url("takeoff.png"), style={'width': '10%'}), width=6),
                dbc.Col(html.Img(src=app.get_asset_url("landing.png"), style={'width': '10%'}), width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(source_airport),
                dbc.Col(destination_airport),
            ]),
        dbc.Row(iata_dropdown),
        dbc.Row(flight_table),
        dbc.Row(tabs),

    ],
    className='dbc'
)

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

@app.callback(
    Output('flight_table', 'data'),
    Output('source', 'value'),
    Output('destination', 'value'),
    Output('flight_iata', 'value'),
    Output('dep_country_img', 'src'),
    Output('arr_country_img', 'src'),
    Output('dep_airport', 'children'),
    Output('arr_airport', 'children'),
    Output('dep_time', 'children'),
    Output('arr_time', 'children'),
    Output('dep_time_real', 'children'),
    Output('arr_time_real', 'children'),
    Output('flight_icao', 'children'),
    Output('flight_status', 'children'),
    Output('direction', 'children'),
    Output('speed', 'children'),
    Output('altitude', 'children'),
    Output('position', 'figure'),
    Input('start_date', 'date'),
    Input('end_date', 'date'),
    Input('source', 'value'),
    Input('destination', 'value'),
    Input('flight_iata', 'value'),
)
def update_flight_filter_list(start_date, end_date, src, dst, flight_iata):
    res_src=src
    res_dst=dst
    res_iata=flight_iata
    df = qd.df_flights_summary
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if trigger_id == 'source':
        src_iata=qd.df_airports[qd.df_airports['airport_name'] == src]['iata_code'].iloc[0]
        df = df[df['dep_iata'] == src_iata]
        if dst is not None:
            dst_iata=qd.df_airports[qd.df_airports['airport_name'] == dst]['iata_code'].iloc[0]
            df = df[df['arr_iata'] == dst_iata]
        res_iata = df['flight_iata'].iloc[0]
        if res_iata is None:
            res_iata=flight_iata
        res_dst = dst
        res_src = src
    if trigger_id =='destination' :
        dst_iata = qd.df_airports[qd.df_airports['airport_name'] == dst]['iata_code'].iloc[0]
        df = df[df['arr_iata'] == dst_iata]
        if src is not None:
            src_iata = qd.df_airports[qd.df_airports['airport_name'] == src]['iata_code'].iloc[0]
            df = df[df['dep_iata'] == src_iata]
        res_iata = df['flight_iata'].iloc[0]
        if res_iata is None:
            res_iata=flight_iata
        res_dst = dst
        res_src = src
    elif trigger_id == 'flight_iata':
        df = df[df['flight_iata'] == flight_iata]
        src_iata = df['dep_iata'].iloc[0]
        dst_iata = df['arr_iata'].iloc[0]
        res_src = qd.df_airports[qd.df_airports['iata_code'] == src_iata]['airport_name'].iloc[0]
        res_dst = qd.df_airports[qd.df_airports['iata_code'] == dst_iata]['airport_name'].iloc[0]
        res_iata = flight_iata
    if start_date is not None:
        df = df[df['schedule_date_deps'] == start_date]
        print (df)
    if end_date is not None:
        df = df[df['schedule_date_arrs'] == end_date]

    src_img="countries/" + qd.df_airports[qd.df_airports['iata_code'] == src_iata]['country_code'].iloc[0].lower()+".png"
    dst_img="countries/" + qd.df_airports[qd.df_airports['iata_code'] == dst_iata]['country_code'].iloc[0].lower()+".png"

    dep_time= (datetime.datetime.min + df['schedule_time_deps'].iloc[0]).time()
    arr_time= (datetime.datetime.min + df['schedule_time_arrs'].iloc[0]).time()

    dep_time_real = (datetime.datetime.min + df['actual_time_deps'].iloc[0]).time()
    arr_time_real = (datetime.datetime.min + df['actual_time_arrs'].iloc[0]).time()
    flight_icao = df[df['flight_iata'] == res_iata]['flight_icao'].iloc[0]
    flight_status = df[df['flight_iata'] == res_iata]['status_lufthansa'].iloc[0]
    flight_direction = qd.df_flights_metrics[qd.df_flights_metrics['flight_iata'] == res_iata]['dir'].iloc[0]
    flight_speed = qd.df_flights_metrics[qd.df_flights_metrics['flight_iata'] == res_iata]['speed'].iloc[0]
    flight_altitude = qd.df_flights_metrics[qd.df_flights_metrics['flight_iata'] == res_iata]['alt'].iloc[0]

    ## Code for fight direction
    # fig = go.Figure(go.Barpolar(
    #     r=[100],
    #     theta=[flight_direction]
    #     width=[20],
    #     marker_color=["#E4FF87"],
    #     marker_line_color="black",
    #     marker_line_width=2,
    #     opacity=0.8
    # ))
    #
    # fig.update_layout(
    #     template=None,
    #     polar=dict(
    #         radialaxis=dict(range=[0, 5], showticklabels=False, ticks=''),
    #         angularaxis=dict(showticklabels=False, ticks='')
    #     )
    # )

    dff=qd.df_summary_metrics_airports[qd.df_summary_metrics_airports['flight_iata'] == res_iata]
    dep_airport_lon= dff['dep_airport_lng'].iloc[0]
    dep_airport_lat= dff['dep_airport_lat'].iloc[0]

    arr_airport_lon = dff['arr_airport_lng'].iloc[0]
    arr_airport_lat = dff['arr_airport_lat'].iloc[0]

    lon = dff['lng'].iloc[0]
    lat = dff['lat'].iloc[0]

    fig = go.Figure(data=go.Scattergeo(
        mode='lines',
        line=dict(width=2, color='blue'),
    ))

    fig.add_trace(
        go.Scattergeo(
            locationmode='USA-states',
            lon=[dep_airport_lon, arr_airport_lon],
            lat=[dep_airport_lat, arr_airport_lat],
            mode='lines+markers',
            marker=dict(size=12, opacity=0.5, symbol='diamond'),
            hovertext = [res_src, res_dst],
            name=''
        )
    )
    fig.add_trace(
        go.Scattergeo(
            lon=[lon],
            lat=[lat],
            mode='markers',
            hovertext=res_iata,
            marker=dict(size=12, opacity=1, symbol='triangle-up'),
            name=''
        )
    )
    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        geo=dict(
            showcountries=True, countrycolor="RebeccaPurple",
            showcoastlines=True, coastlinecolor="RebeccaPurple",
            showland=True, landcolor="LightGray",
            showocean=True,oceancolor="LightBlue",
            projection_scale=2,  # this is kind of like zoom
            center=dict(lat=lat, lon=lon),  # this will center on the point
            countrywidth=0.5,
            projection=dict(
                rotation=dict(
                    lon=lon,
                    lat=lat,
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



    return df.to_dict('records'), res_src, res_dst, res_iata, app.get_asset_url(src_img),\
           app.get_asset_url(dst_img), res_src, res_dst, dep_time, arr_time, dep_time_real,\
           arr_time_real, flight_icao, flight_status, flight_direction, flight_speed, flight_altitude, fig


def update_pie_chart():
    df = qd.df_summary_metrics_airports
    fig = px.pie(df, values='status_lufthansa', names='status_lufthansa' , hole=.3)
    return fig