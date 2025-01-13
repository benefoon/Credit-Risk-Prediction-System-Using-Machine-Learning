import dash
from dash import dcc, html
import pandas as pd

# Load data
data = pd.read_csv("data/credit_risk_data.csv")

# Create Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        figure={
            'data': [
                {'x': data['feature1'], 'y': data['feature2'], 'type': 'scatter', 'name': 'Data'}
            ],
            'layout': {
                'title': 'Feature Interaction'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
