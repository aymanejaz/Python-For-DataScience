# # Import required libraries
# import pandas as pd
# import dash
# from dash import html, dcc
# from dash.dependencies import Input, Output
# import plotly.express as px

# # Read the airline data into pandas dataframe
# airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
#                             encoding = "ISO-8859-1",
#                             dtype={'Div1Airport': str, 'Div1TailNum': str, 
#                                    'Div2Airport': str, 'Div2TailNum': str})

# # Create a dash application
# app = dash.Dash(__name__)

# # Build dash app layout
# app.layout = html.Div(children=[ html.H1('Flight Delay Time Statistics', 
#                                 style={'textAlign': 'center', 'color': '#503D36',
#                                 'font-size': 30}),
#                                 html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
#                                 type='number', style={'height':'35px', 'font-size': 30}),], 
#                                 style={'font-size': 30}),
#                                 html.Br(),
#                                 html.Br(), 
#                                 # Segment 1
#                                 html.Div([
#                                         html.Div(dcc.Graph(id='carrier-plot')),
#                                         html.Div(dcc.Graph(id='weather-plot'))
#                                 ], style={'display': 'flex'}),
#                                 # Segment 2
#                                 html.Div([
#                                         html.Div(dcc.Graph(id='nas-plot')),
#                                         html.Div(dcc.Graph(id='security-plot'))
#                                 ], style={'display': 'flex'}),
#                                 # Segment 3
#                                 html.Div(dcc.Graph(id='late-plot'), style={'width':'65%'})
#                                 ])

# """ Compute_info function description

# This function takes in airline data and selected year as an input and performs computation for creating charts and plots.

# Arguments:
#     airline_data: Input airline data.
#     entered_year: Input year for which computation needs to be performed.
    
# Returns:
#     Computed average dataframes for carrier delay, weather delay, NAS delay, security delay, and late aircraft delay.

# """
# def compute_info(airline_data, entered_year):
#     # Select data
#     df =  airline_data[airline_data['Year']==int(entered_year)]
#     # Compute delay averages
#     avg_car = df.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index()
#     avg_weather = df.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
#     avg_NAS = df.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
#     avg_sec = df.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
#     avg_late = df.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
#     return avg_car, avg_weather, avg_NAS, avg_sec, avg_late

# """Callback Function

# Function that returns fugures using the provided input year.

# Arguments:

#     entered_year: Input year provided by the user.
    
# Returns:

#     List of figures computed using the provided helper function `compute_info`.
# """
# # Callback decorator
# @app.callback( [
#                Output(component_id='carrier-plot', component_property='figure'),
#                Output(component_id='weather-plot', component_property='figure'),
#                Output(component_id='nas-plot', component_property='figure'),
#                Output(component_id='security-plot', component_property='figure'),
#                Output(component_id='late-plot', component_property='figure')
#                ],
#                Input(component_id='input-year', component_property='value'))
# # Computation to callback function and return graph
# def get_graph(entered_year):
    
#     # Compute required information for creating graph from the data
#     avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_data, entered_year)
            
#     # Line plot for carrier delay
#     carrier_fig = px.line(avg_car, x='Month', y='CarrierDelay', color='Reporting_Airline', title='Average carrrier delay time (minutes) by airline')
#     # Line plot for weather delay
#     weather_fig = px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline', title='Average weather delay time (minutes) by airline')
#     # Line plot for nas delay
#     nas_fig = px.line(avg_NAS, x='Month', y='NASDelay', color='Reporting_Airline', title='Average NAS delay time (minutes) by airline')
#     # Line plot for security delay
#     sec_fig = px.line(avg_sec, x='Month', y='SecurityDelay', color='Reporting_Airline', title='Average security delay time (minutes) by airline')
#     # Line plot for late aircraft delay
#     late_fig = px.line(avg_late, x='Month', y='LateAircraftDelay', color='Reporting_Airline', title='Average late aircraft delay time (minutes) by airline')
            
#     return[carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]

# # Run the app
# if __name__ == '__main__':
#     app.run_server()



# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into a pandas dataframe
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                           encoding="ISO-8859-1",
                           dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                  'Div2Airport': str, 'Div2TailNum': str})
print(airline_data)


# This part imports necessary tools and data. It reads information about airline flights from a file stored on the internet and saves it as a table that we can work with.

# Create a Dash application
app = dash.Dash(__name__)

# Build the layout of the Dash app
app.layout = html.Div(children=[
    # Page title
    html.H1("Flight Delay Analysis"),
    
    # Input field for year selection
    html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
              type='number', style={'height':'35px', 'font-size': 30}),], 
              style={'font-size': 30}),
    html.Br(),
    html.Br(), 
    
    # Grouped graphs for different types of delays
    html.Div([
        html.Div(dcc.Graph(id='carrier-plot')),
        html.Div(dcc.Graph(id='weather-plot'))
    ], style={'display': 'flex'}),
    
    html.Div([
        html.Div(dcc.Graph(id='nas-plot')),
        html.Div(dcc.Graph(id='security-plot'))
    ], style={'display': 'flex'}),
    
    # Graph for late aircraft delay
    html.Div(dcc.Graph(id='late-plot'), style={'width':'65%'})
])

# This above part sets up the layout of our app. It's like creating a webpage with different sections for input and graphs. Users can select a year, and the app will show different graphs about flight delays for that year.

# Helper function to compute delay information
def compute_info(airline_data, entered_year):
    # Select data for the entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]
    # Compute average delay times for different types of delays
    avg_car = df.groupby(['Month', 'Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    avg_weather = df.groupby(['Month', 'Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS = df.groupby(['Month', 'Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_sec = df.groupby(['Month', 'Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late = df.groupby(['Month', 'Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
    return avg_car, avg_weather, avg_NAS, avg_sec, avg_late

# Callback function to update graphs based on user input
@app.callback([
    Output(component_id='carrier-plot', component_property='figure'),
    Output(component_id='weather-plot', component_property='figure'),
    Output(component_id='nas-plot', component_property='figure'),
    Output(component_id='security-plot', component_property='figure'),
    Output(component_id='late-plot', component_property='figure')
], [Input(component_id='input-year', component_property='value')])
def update_graphs(entered_year):
    # Compute delay information using the helper function
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_data, entered_year)
    
    # Create line plots for different types of delays
    carrier_fig = px.line(avg_car, x='Month', y='CarrierDelay', color='Reporting_Airline', title='Average carrier delay time (minutes) by airline')
    weather_fig = px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline', title='Average weather delay time (minutes) by airline')
    nas_fig = px.line(avg_NAS, x='Month', y='NASDelay', color='Reporting_Airline', title='Average NAS delay time (minutes) by airline')
    sec_fig = px.line(avg_sec, x='Month', y='SecurityDelay', color='Reporting_Airline', title='Average security delay time (minutes) by airline')
    late_fig = px.line(avg_late, x='Month', y='LateAircraftDelay', color='Reporting_Airline', title='Average late aircraft delay time (minutes) by airline')
    
    return [carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]




# The `@app.callback` is used in Dash to create a connection between user interactions (inputs) and updates in the app's visual output (outputs). It's like telling the app what to do when a user interacts with it. Let me explain it in simpler terms:

# Imagine you have a button on a website, and when you click that button, the text on the webpage changes. In traditional web development, you would need to write JavaScript code to make this happen. However, with Dash, you use `@app.callback` to achieve the same result, but in a more user-friendly and Pythonic way.

# Here's a breakdown of how it works:

# 1. **User Interaction (Input):** When a user interacts with a component in your Dash app, such as clicking a button or entering text in an input field, that interaction is considered an input.

# 2. **Callback Function:** You create a Python function that specifies what should happen when that input changes. This function is the callback function.

# 3. **Output Update (Output):** In the callback function, you define what changes should occur in the app's visual output based on the input. These changes are specified as outputs.

# 4. **Decorator (@app.callback):** You use the `@app.callback` decorator to "connect" the input and output. You tell Dash which input(s) trigger the callback and which output(s) should be updated when the input changes.

# 5. **Automatic Updates:** When the user interacts with the app and triggers the input change, Dash automatically updates the specified output without needing to write low-level code for handling the interaction and update.

# In the provided code, the `@app.callback` decorator is used to connect the input of selecting a year (`Input(component_id='input-year', component_property='value')`) with the output of updating multiple graphs (`Output(component_id='carrier-plot', component_property='figure')`, `Output(component_id='weather-plot', component_property='figure')`, and so on). When the user enters a new year, the callback function `update_graphs` computes the average delay times for different types of delays and generates new graphs to display the information for the selected year.

# In essence, `@app.callback` is a powerful tool that simplifies the process of creating interactive and responsive web applications in Dash. It abstracts away much of the underlying complexity of handling user interactions and updating the visual content of the app.