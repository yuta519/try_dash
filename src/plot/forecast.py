
from typing import TypedDict
from pandas import DataFrame


class PlotData(TypedDict):
    type: str
    x: list
    y: list
    fill: str
    fillcolor: str
    line: dict
    name: str


def create_forecast_plot_data(
    history_df: DataFrame, forecast_df: DataFrame
) -> list[PlotData]:
    forecast_error_x = list(forecast_df["date"]) + list(reversed(forecast_df["date"]))

    line_history: PlotData = dict(
        type="scatter",
        x=history_df["date"],
        y=history_df["value"],
        name="Historical",
        mode="lines+markers",
        line=dict(color="rgb(0, 0, 0)"),
    )
    line_forecast: PlotData = dict(
        type="scatter",
        x=forecast_df["date"],
        y=forecast_df["value"],
        name="Forecast",
        mode="lines",
        line=dict(color="rgb(0,0,0)", dash="2px"),
    )
    error_50: PlotData = dict(
        type="scatter",
        x=forecast_error_x,
        y=list(forecast_df["UB_50"]) + list(reversed(forecast_df["LB_50"])),
        fill="tozeroy",
        fillcolor="rgb(226, 87, 78)",
        line=dict(color="rgba(255,255,255,0)"),
        name="50% CI",
    )
    error_75: PlotData = dict(
        type="scatter",
        x=forecast_error_x,
        y=list(forecast_df["UB_75"]) + list(reversed(forecast_df["LB_75"])),
        fill="tozeroy",
        fillcolor="rgb(234, 130, 112)",
        line=dict(color="rgba(255,255,255,0)"),
        name="75% CI",
    )
    error_95: PlotData = dict(
        type="scatter",
        x=forecast_error_x,
        y=list(forecast_df["UB_95"]) + list(reversed(forecast_df["LB_95"])),
        fill="tozeroy",
        fillcolor="rgb(243, 179, 160)",
        line=dict(color="rgba(255,255,255,0)"),
        name="95% CI",
    )

    return [error_95, error_75, error_50, line_history, line_forecast]
