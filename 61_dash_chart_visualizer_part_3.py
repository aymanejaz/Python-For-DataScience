# summary of the Dash application code along with explanations for each part:

# **Summary:**

# This code demonstrates a Dash web application that allows users to interactively visualize random data using either a bar chart or a scatter plot. The application generates random data points and presents a visually appealing layout for user interaction.

# **Explanations:**

# 1. Import Statements: Import necessary libraries including Dash (`Dash` class for creating the app), Dash Core Components (`html` and `dcc` for creating HTML elements and components), and Plotly Express (`px` for data visualization).

# 2. Dash App Setup: Create an instance of the Dash class using `app = Dash(__name__)`.

# 3. Generate Random Data: Generate random data points for the example using Python's `random` module and create a DataFrame (`df`) to hold the data.

# 4. Layout Definition: Define the layout of the app using `app.layout`. It includes an HTML `Div` element containing a title, a label, a dropdown menu (`dcc.Dropdown`), and a graph area (`dcc.Graph`).

# 5. Dropdown Options: Populate the dropdown menu with two options: "Bar Chart" and "Scatter Plot". Set default value to "Bar Chart".

# 6. Callback Function: Define a callback function using `@app.callback` decorator. It takes the selected chart type from the dropdown (`'chart-type'`) as input and returns a Plotly Express figure for either a bar chart or a scatter plot.

# 7. Update Chart: Depending on the selected chart type, the callback function uses Plotly Express (`px`) to generate a bar chart or scatter plot using the randomly generated data.

# 8. Run the App: The `if __name__ == '__main__':` block runs the Dash app in debug mode when the script is executed.

# This code showcases the creation of an interactive Dash application that enables users to select and visualize data using different chart types. The layout and styling make the application user-friendly and visually appealing.



from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import random

app = Dash(__name__)

# Generate random data
num_points = 50
data = {'x': [random.randint(1, 100) for _ in range(num_points)],
        'y': [random.randint(1, 100) for _ in range(num_points)]}
df = pd.DataFrame(data)

print(df)

app.layout = html.Div(
    style={'textAlign': 'center', 'margin': '50px'},
    children=[
        html.H1('Interactive Chart Visualizer', style={'color': 'navy'}),
        html.Label('Select Chart Type:', style={'fontSize': '18px'}),
        dcc.Dropdown(options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Scatter Plot', 'value': 'scatter'}
        ], value='bar', id='chart-type'),
        dcc.Graph(id='chart')
    ]
)

@app.callback(
    Output('chart', 'figure'),
    Input('chart-type', 'value')
)
def update_chart(selected_chart):
    if selected_chart == 'bar':
        return px.bar(df, x='x', y='y', title='Random Bar Chart')
    else:
        return px.scatter(df, x='x', y='y', title='Random Scatter Plot')

if __name__ == '__main__':
    app.run_server(debug=True)

