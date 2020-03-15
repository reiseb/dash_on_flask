import dash_core_components as dcc
import dash_html_components as html


def build_layout():
    lo = html.Div([
        html.H1('Stock Tickers'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Graph(id='my-graph')
    ], style={'width': '500'})
    return lo
