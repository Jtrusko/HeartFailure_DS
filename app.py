import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load and clean data
df = pd.read_csv(r"C:\Users\trusk\OneDrive\Desktop\heart.csv")

# Encode categorical data for consistency (if needed for plots)
df['Sex'] = df['Sex'].map({'M': 'Male', 'F': 'Female'})
df['HeartDisease'] = df['HeartDisease'].map({1: 'Yes', 0: 'No'})

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Heart Failure Dashboard"

# Layout
app.layout = html.Div([
    html.H1("❤️ Heart Failure Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Filter by Sex:"),
        dcc.Dropdown(
            id='sex_filter',
            options=[{'label': sex, 'value': sex} for sex in df['Sex'].unique()],
            value=None,
            placeholder='Select Sex',
            clearable=True
        )
    ], style={'width': '30%', 'margin': 'auto'}),

    html.Br(),

    dcc.Graph(id='heart-disease-bar'),

    html.Br(),

    dcc.Graph(id='age-boxplot'),
])


# Callbacks
@app.callback(
    Output('heart-disease-bar', 'figure'),
    Output('age-boxplot', 'figure'),
    Input('sex_filter', 'value')
)
def update_graphs(selected_sex):
    filtered_df = df[df['Sex'] == selected_sex] if selected_sex else df

    fig1 = px.histogram(
        filtered_df,
        x='HeartDisease',
        color='HeartDisease',
        title='Heart Disease Count',
        text_auto=True
    )

    fig2 = px.box(
        filtered_df,
        x='HeartDisease',
        y='Age',
        color='HeartDisease',
        title='Age Distribution by Heart Disease'
    )

    return fig1, fig2


# Run app
if __name__ == '__main__':
    app.run(debug=True)
