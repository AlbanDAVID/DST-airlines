from dash import html
from dashboard import dbc
import dst_variable as dv
import dst_static as ds
from dashboard import app
from dash_bootstrap_templates import ThemeChangerAIO

app.layout = html.Div(
    [
        html.Img(src=app.get_asset_url("airbus.jpg"), style={'width': '100%'}),
            dbc.Row(
                [
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Flight Information", style={'background':'#0f1744', 'color':'white'}),
                            dbc.CardBody(dv.filter_menu)
                        ]),
                        dbc.Card([
                            dbc.CardHeader("Statistics", style={'background': '#0f1744', 'color': 'white'}),
                            dbc.CardBody(dv.stat)
                        ]),
                    ],
                        width=6
                    ),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Airport and destination information", style={'background':'#0f1744', 'color':'white'}),
                            dbc.CardBody(ds.map)
                            ])
                        ],
                        width=6),
                ],
            ),
            ThemeChangerAIO(aio_id="theme", radio_props={"value": dbc.themes.SPACELAB}),

    ],
    className='dbc'

)

if __name__ == "__main__":
    app.run_server(debug=False)