from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


app = Dash(__name__)

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv'
)

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Location(id="url", refresh=False),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
])

if __name__ == '__main__':
    app.run(debug=True)
