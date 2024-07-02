import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('your_dataset.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Data Visualization Dashboard"),
    
    # Dropdown to select a column for x-axis
    html.Label("Select X-axis:"),
    dcc.Dropdown(
        id='x-axis-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0]
    ),
    
# Dropdown to select a column for y-axis
html.Label("Select Y-axis:"),
dcc.Dropdown(
    id='y-axis-dropdown',
    options=[{'label': col, 'value': col} for col in df.columns],
    value=df.columns[1]
),

# Graph to display the selected columns
dcc.Graph(id='graph-output')
])

# Define callback to update the graph based on selected columns
@app.callback(
    Output('graph-output', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
def update_graph(x_axis, y_axis):
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f'{x_axis} vs {y_axis}')
    return fig
    
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)