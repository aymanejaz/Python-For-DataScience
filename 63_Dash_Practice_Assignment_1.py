# Import required packages
import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output

# Add Dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

print(df)
# Add a bar graph figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# fig.show()

# Create a Dash application instance
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center'
        }
    ),

    # Dropdown component for selecting a city
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'  # Providing a default value to the dropdown
    ),

   # Adding a line break to separate the dropdown from the graph
    html.Br(),

    # Bar graph component
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])



# Run the application
if __name__ == '__main__':
    app.run_server()

# python3 63_Dash_Practice_Assignment_1.py



''''
Certainly! Here's a step-by-step explanation of the provided code:

1. **Importing Required Packages:** The code starts by importing the necessary packages: `pandas` for data manipulation, `dash` for creating the web application, and specific modules `html` and `dcc` from `dash` for creating HTML and Dash Core Components, respectively. It also imports `plotly.express` for easy creation of visualizations and the `Input` and `Output` modules from `dash.dependencies` for defining callback inputs and outputs.

2. **Creating a DataFrame (df):** A pandas DataFrame `df` is created containing information about different fruits ("Fruit"), the amount of each fruit ("Amount"), and the city they are associated with ("City").

3. **Printing DataFrame (df):** The contents of the DataFrame `df` are printed to the console using `print(df)`. This displays the data for the fruits, their amounts, and the corresponding cities.

4. **Creating a Bar Graph (fig):** Using Plotly Express (`px`), a bar graph (`fig`) is created from the DataFrame `df`. The x-axis represents the "Fruit," the y-axis represents the "Amount" of each fruit, and different cities are represented by different colors. The bars are grouped together using the "barmode" parameter set to "group."

5. **Creating a Dash Application Instance:** An instance of the Dash application is created using `dash.Dash()` and stored in the variable `app`.

6. **Defining the Layout:** The layout of the Dash application is defined using HTML components provided by `dash.html`. Inside a `html.Div` component, the following elements are included:
   - An `html.H1` component displaying the title "Dashboard" with centered alignment.
   - A `dcc.Dropdown` component for selecting a city. It provides options for New York City (NYC), Montréal (MTL), and San Francisco (SF), with a default value set to NYC.
   - A line break (`html.Br()`) to visually separate the dropdown from the graph.
   - A `dcc.Graph` component with the id "example-graph" to display the bar graph (`fig`) created earlier.

7. **Running the Application:** The code includes a conditional check `if __name__ == '__main__':` to ensure that the following code is executed only when the script is run directly (not when imported as a module). It calls the `run_server()` method of the Dash application instance `app`, which starts the web server and makes the application accessible through a web browser.

8. **Command to Run the Application:** A comment at the end of the script indicates how to run the application using the command `python3 63_Dash_Practice_Assignment_1.py`.

Overall, this code sets up a simple Dash web application that displays a bar graph of fruit amounts based on city selection using a dropdown menu. The application's layout includes a title, a dropdown component, a line break, and a graph component to visualize the data.


'''