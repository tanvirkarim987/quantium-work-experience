from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

# 1. Load and prepare data
df = pd.read_csv('formatted_data.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash(__name__)

# 2. Define the Layout
app.layout = html.Div(style={
    'backgroundColor': '#f2f4f7',
    'padding': '40px',
    'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
}, children=[
    
    html.Div(style={
        'backgroundColor': 'white',
        'padding': '40px',
        'borderRadius': '20px',
        'boxShadow': '0px 10px 30px rgba(0, 0, 0, 0.05)',
        'maxWidth': '1000px',
        'margin': 'auto'
    }, children=[
        
        html.H1(
            "Pink Morsel Sales Data",
            style={'textAlign': 'center', 'color': '#1a1a1a', 'fontWeight': 'bold'}
        ),

        # Radio Button Section
        html.Div(style={'textAlign': 'center', 'marginBottom': '30px'}, children=[
            html.Label("Filter by Region:", style={'fontWeight': '600', 'marginRight': '15px'}),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all', # Default value
                inline=True,
                inputStyle={"margin-left": "20px", "margin-right": "5px"}
            )
        ]),

        dcc.Graph(id='sales-line-chart')
    ])
])

# 3. The Callback: This connects the RadioItems to the Graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(region_selected):
    if region_selected == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region_selected]
    
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Sales Trend: {region_selected.capitalize()} Region",
        template="plotly_white",
        labels={"date": "Date", "sales": "Sales ($)"}
    )
    
    # Keep the line color consistent and pretty
    fig.update_traces(line_color='#e74c3c', line_width=2)
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)