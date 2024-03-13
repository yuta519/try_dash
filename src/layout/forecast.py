from pandas import DataFrame

def _create_shapes(history_df:DataFrame, forecast_df:DataFrame):
    return [
        {
            "type": "rect",
            "xref": "x",
            "x0": history_df["date"].iloc[0],
            "x1": history_df["date"].iloc[-1],
            "yref": "paper",
            "y0": 0,
            "y1": 1,
            "fillcolor": "rgb(229, 236, 245)",
            "line": {"width": 0},
            "layer": "below",
        },
        {
            "type": "rect",
            "xref": "x",
            "x0": forecast_df["date"].iloc[0],
            "x1": forecast_df["date"].iloc[-1],
            "yref": "paper",
            "y0": 0,
            "y1": 1,
            "fillcolor": "rgb(206, 212, 220)",
            "line": {"width": 0},
            "layer": "below",
        },
    ]

def create_layout(history_df:DataFrame, forecast_df:DataFrame,):
    return dict(
        title='US Inflation',
        height=720,
        xaxis=dict(
            fixedrange=True,
            type="date",
            gridcolor="rgb(255,255,255)",
            range=[
                history_df["date"].iloc[-16],
                forecast_df["date"].iloc[-1]
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
                            count=len(history_df["date"])+len(forecast_df["date"]),
                            label="all",
                            step="month",
                            stepmode="backward",
                        ),
                    ]
                )
            ),
            rangeslider=dict(
                visible=True,
                range=[history_df["date"].iloc[0], forecast_df["date"].iloc[-1]],
            ),
        ),
        yaxis=dict(
            fixedrange=True,
            autorange=True,
            gridcolor="rgb(255,255,255)",
        ),
        shapes=_create_shapes(history_df, forecast_df),
        modebar={"color": "rgba(0,0,0,1)"},
    )
