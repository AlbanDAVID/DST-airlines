from dash import html
from dashboard import dbc,header
import dst_variable as dv
import dst_static as ds
from dashboard import app
from dash_bootstrap_templates import ThemeChangerAIO

app.layout = html.Div(
    [
        header,
        dbc.Card(
            [

                dbc.Row(
                    [
                        dbc.Col(dv.filter_menu, width=6),
                        dbc.Col(ds.map, width=6),
                    ],
                ),
                ThemeChangerAIO(aio_id="theme", radio_props={"value": dbc.themes.VAPOR}),
            ],
            body=True,
            className='dbc'
        ),

    ]
)

if __name__ == "__main__":
    app.run_server(debug=False)