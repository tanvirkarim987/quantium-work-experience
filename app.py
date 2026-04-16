from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Load and prepare data
df = pd.read_csv('formatted_data.csv')
df["date"] = pd.to_datetime(df["date"]) # Convert strings to dates
df = df.sort_values(by="date")

# Create the figure
fig = px.line(df, x="date", y="sales", 
              title="Pink Morsel Sales Over Time",
              labels={"date": "Date", "sales": "Sales ($)"})

# Simple vertical line fix
fig.add_shape(
    type="line", line_color="red", line_dash="dash",
    x0="2021-01-15", x1="2021-01-15", y0=0, y1=1, yref="paper"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(id='sales-chart', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)