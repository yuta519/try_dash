from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


app = Dash(__name__)


def _series_layout(title=None):
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Row([dbc.Col(id="chart", lg=12)]),
                    # _forecast_info_layout(),
                    # _forecast_performance_layout(),
                ]
            ),
        ]
    )

past_df = pd.read_csv('./data/past.csv')
forecast_df = pd.read_csv('./data/forecast.csv')

shapes = [
    {
        "type": "rect",
        # x-reference is assigned to the x-values
        "xref": "x",
        "x0": past_df["date"][0],
        "x1": past_df["date"][len(past_df)-1],
        # y-reference is assigned to the plot paper [0,1]
        "yref": "paper",
        "y0": 0,
        "y1": 1,
        "fillcolor": "rgb(229, 236, 245)",
        "line": {"width": 0},
        "layer": "below",
    },
    {
        "type": "rect",
        # x-reference is assigned to the x-values
        "xref": "x",
        "x0": forecast_df["date"][0],
        "x1": forecast_df["date"][len(forecast_df)-1],
        # y-reference is assigned to the plot paper [0,1]
        "yref": "paper",
        "y0": 0,
        "y1": 1,
        "fillcolor": "rgb(206, 212, 220)",
        "line": {"width": 0},
        "layer": "below",
    },
]

layout = dict(
    title='US Inflation',
    height=720,
    xaxis=dict(
        fixedrange=True,
        type="date",
        gridcolor="rgb(255,255,255)",
        range=[
            past_df["date"][len(past_df)-50],
            forecast_df["date"][len(forecast_df)-1]
        ],
        rangeselector=dict(
            buttons=list(
                [
                    dict(
                        count=5,
                        label="5y",
                        step="year",
                        stepmode="backward",
                    ),
                    dict(
                        count=10,
                        label="10y",
                        step="year",
                        stepmode="backward",
                    ),
                    dict(
                        count=60,  # 'all' or 'alltime' or 'alltime'
                        label="all",
                        step="year",
                        stepmode="backward",
                    ),
                ]
            )
        ),
        rangeslider=dict(
            visible=True,
            range=[
                past_df["date"][len(past_df)-50],
                forecast_df["date"][len(forecast_df)-1]
            ],
        ),
    ),
    yaxis=dict(
        # Will disable all zooming and movement controls if True
        fixedrange=True,
        autorange=True,
        gridcolor="rgb(255,255,255)",
    ),
    shapes=shapes,
    modebar={"color": "rgba(0,0,0,1)"},
)


@callback(
    Output('graph', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = pd.read_csv('./data/past.csv')
    return px.line(dff, x='date', y='value')

@callback(
    Output('chart', 'children'),
    Input('dropdown-selection', 'value')
)
def update_chart(_, **kwarg):
    forecast_error_x = list(forecast_df["date"]) + list(reversed(forecast_df["date"]))

    line_history = dict(
        type="scatter",
        x=past_df["date"],
        y=past_df["value"],
        name="Historical",
        mode="lines+markers",
        line=dict(color="rgb(0, 0, 0)"),
    )
    line_forecast = dict(
        type="scatter",
        x=forecast_df["date"],
        y=forecast_df["value"],
        name="Forecast",
        mode="lines",
        line=dict(color="rgb(0,0,0)", dash="2px"),
    )
    error_50 = dict(
        type="scatter",
        x=forecast_error_x,
        y=list(forecast_df["UB_50"]) + list(reversed(forecast_df["LB_50"])),
        fill="tozeroy",
        fillcolor="rgb(226, 87, 78)",
        line=dict(color="rgba(255,255,255,0)"),
        name="50% CI",
    )
    error_75 = dict(
        type="scatter",
        x=forecast_error_x,
        y=list(forecast_df["UB_75"]) + list(reversed(forecast_df["LB_75"])),
        fill="tozeroy",
        fillcolor="rgb(234, 130, 112)",
        line=dict(color="rgba(255,255,255,0)"),
        name="75% CI",
    )

    # Plot CI95
    error_95 = dict(
        type="scatter",
        x=forecast_error_x,
        y=list(forecast_df["UB_95"]) + list(reversed(forecast_df["LB_95"])),
        fill="tozeroy",
        fillcolor="rgb(243, 179, 160)",
        line=dict(color="rgba(255,255,255,0)"),
        name="95% CI",
    )

    return dcc.Graph(
        figure={
            'data': [error_95, error_75, error_50, line_history, line_forecast],
            'layout': layout,
        }
    )


df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv'
    # './src/data.csv'
)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    # dcc.Location(id="url", refresh=False),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph'),
    _series_layout(),
])

if __name__ == '__main__':
    app.run(debug=True)
