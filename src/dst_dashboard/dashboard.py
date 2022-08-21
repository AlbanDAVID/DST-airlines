from dash import Dash, html
import dash_bootstrap_components as dbc


# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE, dbc_css, FA])

header = html.H1(
    "DST Airlines ", className="bg-primary text-white p-2 mb-2 text-center"
)


