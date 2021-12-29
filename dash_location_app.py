import requests
from urllib.request import urlopen
import json
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

'''
references:
https://dash.plotly.com/dash-core-components/textarea
https://dash.plotly.com/dash-core-components
https://dash.plotly.com/dash-core-components/dropdown
'''


def get_longitude_latitude(location):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'YourAPIKey'  # Acquire from developer.here.com
    PARAMS = {'apikey': api_key, 'q': location}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    # generate location js file
    # Read in the file
    with open('assets\\source.js', 'r') as file:
        filedata = file.read()
    # Replace the target string
    filedata = filedata.replace('latval', str(latitude))
    filedata = filedata.replace('lngval', str(longitude))
    filedata = filedata.replace('rndlat', str(latitude).split(".")[0])
    filedata = filedata.replace('rndlng', str(longitude).split(".")[0])
    # Write the js file out again
    with open('assets\\' + location + '.js', 'w') as file:
        file.write(filedata)
    # generate location html file
    # Write the html file out again
    with open('assets\\demo.html', 'r') as file:
        filedata_2 = file.read()
    # Replace the target string
    filedata_2 = filedata_2.replace('demo.js', location + ".js")
    # Write the file out again
    with open('assets\\' + location + '.html', 'w') as file:
        file.write(filedata_2)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2("Location Map Dashboard", className="display-4"),
    html.Br(),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Amsterdam', 'value': 'Amsterdam'},
            {'label': 'Berlin', 'value': 'Berlin'},
            {'label': 'Boston', 'value': 'Boston'},
            {'label': 'London', 'value': 'London'},
            {'label': 'Montreal', 'value': 'Montreal'},
            {'label': 'Moscow', 'value': 'Moscow'},
            {'label': 'Mumbai', 'value': 'Mumbai'},
            {'label': 'NewYork', 'value': 'NewYork'},
            {'label': 'Ottawa', 'value': 'Ottawa'},
            {'label': 'Paris', 'value': 'Paris'},
            {'label': 'Sydney', 'value': 'Sydney'},
            {'label': 'San Francisco', 'value': 'San Francisco'},
            {'label': 'Wellington', 'value': 'Wellington'},
        ],
        value='New York'
    ),
    html.Br(),
    html.Br(),
    html.Div(id='dd-output-container')

])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    # return 'You have selected "{}"'.format(value)
    # get_longitude_latitude(value)
    return html.Iframe(src="assets/" + value + ".html",
                style={
                    "height": "450px",
                    "width": "100%"
                })


if __name__ == '__main__':
    app.run_server(debug=True)