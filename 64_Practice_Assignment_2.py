# Import required libraries
from dash import no_update, html, dcc, Input, Output, State
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define URL for data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"

# Read data into a pandas DataFrame
auto_data = pd.read_csv(URL)
print(auto_data)

# Create a Dash application
app = dash.Dash(__name__)

# Suppress exceptions until callback execution
app.config.suppress_callback_exceptions = True

# Define the layout of the app
app.layout = html.Div(children=[

    # TASK 3A: Add title to the dashboard
    html.H1('Car Automobile Components',
           style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),

    # Outer division starts
    html.Div([
        # First inner division for dropdown and helper text for Selected Drive wheels
        html.Div(
            # TASK 3B: Add a Label to the dropdown
            [html.H2('Drive Wheels Type:',
                     style={'margin-right': '2em'}),
             ]
        ),

        # TASK 3C: Next lets add the dropdown right below the first inner division.
        dcc.Dropdown(
            id='demo-dropdown',
            options=[
                {'label': 'Rear Wheel Drive', 'value': 'rwd'},
                {'label': 'Front Wheel Drive', 'value': 'fwd'},
                {'label': 'Four Wheel Drive', 'value': '4wd'}
            ],
            value='rwd'

        ),

        # Second inner division for output graphs
        html.Div([
            # TASK 3D: Add two empty divisions for output inside the next inner division.
            html.Div([], id='plot1'),
            html.Div([], id='plot2')

        ], style={'display': 'flex'}),
    ])
    # Outer division ends
])

# Define the callback function
# TASK 3F
@app.callback(
    [Output(component_id='plot1', component_property='children'),
    Output(component_id='plot2', component_property='children')],
    [Input(component_id='demo-dropdown', component_property='value')]
)
def display_selected_drive_charts(value):
    filtered_df = auto_data[auto_data['drive-wheels'] == value]
    
    # Filter the DataFrame to only include numeric data for aggregation
    numeric_columns = ['price']
    numeric_df = filtered_df[numeric_columns]
    
    fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
    fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')
    
    return [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ]

# Run the application
if __name__ == '__main__':
    app.run_server()


 # $ python3 64_Practice_Assignment.py


'''
 Certainly! Here's a step-by-step explanation of the provided Dash code:

1. **Importing Libraries**: The code begins by importing the necessary libraries for creating the Dash application, including `dash`, `html`, `dcc` (Dash core components), and other required libraries like `pandas` and `plotly`.

2. **Data Source**: The URL of the data source is defined using the `URL` variable. The data will be read from this URL into a pandas DataFrame.

3. **Read Data**: The code reads the data from the provided URL into a pandas DataFrame named `auto_data`.

4. **Create Dash Application**: A Dash application is created using the `dash.Dash()` constructor and assigned to the variable `app`.

5. **Suppress Callback Exceptions**: Callback exceptions are suppressed until callback execution using the `app.config.suppress_callback_exceptions` setting.

6. **Layout Definition**: The layout of the Dash app is defined using the `html.Div()` component. It consists of several nested `html.Div()` components to organize the elements on the web page.

7. **Adding Title**: A title is added to the dashboard using the `html.H1()` component. The title is centered and styled using CSS.

8. **Inner Divisions**: The outer `html.Div()` contains two inner divisions. The first inner division contains a label ("Drive Wheels Type:") for a dropdown menu.

9. **Dropdown Component**: A dropdown menu is created using the `dcc.Dropdown()` component. It has options for different drive wheel types, and the default selected value is 'Rear Wheel Drive' (`'rwd'`).

10. **Second Inner Division**: The second inner division contains two empty `html.Div()` components. These empty divs will be populated with plots based on user input from the dropdown.

11. **Callback Definition**: A callback function `display_selected_drive_charts` is defined using the `@app.callback()` decorator. This function takes the selected value from the dropdown (`value`) as an input and returns the two pie and bar charts for display.

12. **Filter Data**: Inside the callback function, the DataFrame `auto_data` is filtered based on the selected drive wheel type (`value`). The filtered data is stored in `filtered_df`.

13. **Numeric Data Filtering**: The DataFrame `filtered_df` is further filtered to include only numeric data columns (e.g., 'price') in the `numeric_columns` list. The resulting DataFrame is stored in `numeric_df`.

14. **Plotting Charts**: Two plots are created using the `px.pie()` and `px.bar()` functions from Plotly Express (`px`). The pie chart (`fig1`) represents the distribution of car body styles based on the selected drive wheel type. The bar chart (`fig2`) shows the average price of different car body styles for the selected drive wheel type.

15. **Callback Output**: The callback function returns a list containing two `dcc.Graph()` components, each with a figure assigned to it.

16. **Run the Application**: The Dash app is run using the `app.run_server()` command. This will start a local development server and display the dashboard in a web browser.

Overall, the code defines a Dash application that allows users to select a drive wheel type from a dropdown menu and displays two plots (pie chart and bar chart) based on the selected value. The plots show the distribution of car body styles and average prices for the selected drive wheel type.
'''