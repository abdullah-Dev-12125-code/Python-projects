import dash
from dash import Dash, html
import plotly.express as px
import seaborn as sns
import pandas as pd



app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("My First Dash App"),
        html.P("Dash is running successfully!")
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
