from dash import Dash, dcc, html, Input, Output, dash_table, dependencies
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from datetime import date
import query_data as qd
from dashboard import app
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

map_choice=dcc.Dropdown(
    id="type",
    options=["airports"],
    value="airports",
    clearable=False,
    className='dbc'
    )
map = dbc.Card(
    [
        dbc.Label("Static Data"),
        map_choice,
        dcc.Graph(id="graph", className='dbc'),
    ],
    body=True,
)
@app.callback(
    Output("graph", "figure"),
    Input("type", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def generate_chart(values, theme):
    if values == "cities":
        fig = px.scatter_geo(
            qd.df_cities,
            lon='city_lng',
            lat='city_lat',
            color="country_code",
            color_continuous_scale=px.colors.cyclical.IceFire,
            projection="orthographic",
            fitbounds=True,
            template=template_from_url(theme)
        )

        fig.update_layout(mapbox_style="open-street-map")
#       fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    elif values == "airports":
        fig = px.scatter_mapbox(
            pd.merge(qd.df_airports, qd.df_countries, on='country_code'),
            lon='airport_lng',
            lat='airport_lat',
            hover_name="airport_name",
            color="country_code3",
            zoom=3,
            template=template_from_url(theme)

        )
        fig.update_layout(mapbox_style="open-street-map")
    return fig
