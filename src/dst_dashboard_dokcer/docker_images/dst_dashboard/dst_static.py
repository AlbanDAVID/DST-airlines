from dash import  Input, Output, html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from datetime import date
import query_data as qd
from dashboard import app
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import plotly.graph_objects as go

map_list_menu = dcc.Dropdown(
    id="menuList",
    clearable=False
)
map_choice = dcc.Dropdown(
            id="type",
            options=
            [
                {'label': 'By City', 'value': "Cities"},
                {'label': 'By Country', 'value': "Countries"}
            ],
            clearable=False,
        )
map = html.Div([
        dbc.Row([
            dbc.Col(map_choice, width=3),
            dbc.Col(map_list_menu),
        ]),
        dcc.Graph(id="graph", className='dbc'),
    ],
    className='dbc'
)


@app.callback(
    Output("menuList", "placeholder"),
    Output("menuList", "options"),
    Input("type", "value")
)
def update_menu_list(value):
    if value == "Cities":
        options_ret=qd.df_cities['city_name']
        placeholder='Select a City'
    else:
        options_ret=qd.df_countries['name']
        placeholder='Select a Country'
    return placeholder, options_ret
@app.callback(
    Output("graph", "figure"),
    Input("type", "value"),
    Input("menuList", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def generate_chart(values, location, theme):
    if values is None:
        fig = px.scatter_mapbox(
            pd.merge(qd.df_airports, qd.df_countries, on='country_code'),
            hover_name="airport_name",
            zoom=1,
            template=template_from_url(theme)
        )
        fig.update_layout(mapbox_style="carto-positron")
    if values == "Cities":
        fig = px.scatter_mapbox(
            qd.df_airports,
            lon='airport_lng',
            lat='airport_lat',
            hover_name="airport_name",
            color="country_code",
            center={'lon': qd.df_cities[qd.df_cities['city_name'] == location]['city_lng'].iloc[0],
                    'lat': qd.df_cities[qd.df_cities['city_name'] == location]['city_lat'].iloc[0]},
            zoom=9,
            template=template_from_url(theme)

        )
        fig.update_layout(mapbox_style="carto-positron")

    elif values == "Countries":
        fig = px.scatter_mapbox(
            pd.merge(qd.df_airports, qd.df_countries, on='country_code'),
            lon='airport_lng',
            lat='airport_lat',
            hover_name="airport_name",
            color="country_code3",
            zoom=3,
            template=template_from_url(theme)

        )
        fig.update_layout(mapbox_style="carto-positron")
    return fig
