# Summary of the provided code:

# This code demonstrates a basic Dash web application that utilizes data visualization with Plotly Express. The application loads a dataset containing information about various countries and their population over the years. The goal of the application is to allow users to select a country from a dropdown menu and visualize its population trends using a line chart.

# Summary of the code:

# 1. Import necessary libraries:
#    - `Dash` for creating the web application.
#    - `html` and `dcc` modules from Dash for creating HTML elements and Dash Core Components, respectively.
#    - `callback`, `Output`, and `Input` from Dash for creating interactive callbacks.
#    - `plotly.express` as `px` for data visualization.
#    - `pandas` for data manipulation.

# 2. Load the dataset:
#    - The dataset is loaded using the `pd.read_csv` function from the Pandas library. It contains information about countries and their population data.

# 3. Create a Dash application instance:
#    - An instance of the Dash class is created and stored in the `app` variable.

# 4. Define the layout:
#    - The layout of the web application is defined using HTML elements and Dash Core Components.
#    - The layout includes a title, a dropdown menu (using `dcc.Dropdown`), and a graph (using `dcc.Graph`).

# 5. Create a callback function:
#    - The `@app.callback` decorator is used to define a callback function.
#    - The callback function takes the selected value from the dropdown menu (`'dropdown-selection'`) as an input.
#    - Inside the function, the dataset is filtered based on the selected country, and a line chart (using Plotly Express) is generated to display the population trends over the years.

# 6. Run the application:
#    - The application is run using the `app.run_server(debug=True)` command.
#    - When the application is executed, users can select a country from the dropdown menu, and the corresponding population trends will be displayed in the line chart.

# Overall, this code showcases the creation of a simple interactive web application using Dash, allowing users to explore and visualize population data for different countries over time.


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': country, 'value': country} for country in df['country'].unique()],
                 value='Canada',
                 id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

print(df.country.unique())

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run_server(debug=True)
