import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd

from layout.forecast import create_layout
from plot.forecast import create_forecast_plot_data


dash.register_page(__name__, path="/")


@callback(Output("chart", "children"), Input("url", "href"))
def update_chart(_, **kwarg):
    past_df = pd.read_csv("./data/past.csv")
    forecast_df = pd.read_csv("./data/forecast.csv")

    return dcc.Graph(
        figure={
            "data": create_forecast_plot_data(past_df, forecast_df),
            "layout": create_layout(past_df, forecast_df),
        }
    )


layout = html.Div(
    [
        html.H1(children="Forecast", style={"textAlign": "center"}),
        dcc.Location(id="url", refresh=False),
        dbc.Container([dbc.Row([dbc.Col(id="chart", lg=12)])]),
    ]
)
