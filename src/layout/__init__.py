from dash import html, dcc
import dash_bootstrap_components as dbc

from dash import dcc

def _forecast_info_layout():
    return dbc.Col(
        [
            dbc.Label("Forecast Method"),
            dcc.Dropdown(
                id="model_selector",
                clearable=False,
            ),
            html.A(
                "Download Forecast Data",
                id="forecast_data_download_link",
                download="forecast_data.xlsx",
                href="",
                target="_blank",
            ),
            dcc.Loading(
                html.Div(
                    id="meta_data_list",
                    className="py-3",
                )
            ),
        ],
        lg=6,
    )


def _forecast_performance_layout():
    return dbc.Col(
        [
            dbc.Row(
                [dbc.Label("Model Cross Validation Scores")],
            ),
            dbc.Row(
                [
                    dbc.Checklist(
                        options=[
                            {"label": "Raw Scores", "value": 1},
                        ],
                        value=[0],
                        id="display_scores_input",
                        switch=True,
                    ),
                ]
            ),
            dbc.Row(
                [
                    dcc.Loading(html.Div(id="CV_scores_table")),
                ]
            ),
        ],
        lg=6,
    )
