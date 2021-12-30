import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "22rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow": "scroll",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("USA States Geospatial Analysis", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Alabama", href="/", active="exact"),
                dbc.NavLink("Alaska", href="/Alaska", active="exact"),
                dbc.NavLink("Arkansas", href="/Arkansas", active="exact"),
                dbc.NavLink("California", href="/California", active="exact"),
                dbc.NavLink("Colorado", href="/Colorado", active="exact"),
                dbc.NavLink("Connecticut", href="/Connecticut", active="exact"),
                dbc.NavLink("Delaware", href="/Delaware", active="exact"),
                dbc.NavLink("Florida", href="/Florida", active="exact"),
                dbc.NavLink("Georgia", href="/Georgia", active="exact"),
                dbc.NavLink("Hawaii", href="/Hawaii", active="exact"),
                dbc.NavLink("Idaho", href="/Idaho", active="exact"),
                dbc.NavLink("Illinois", href="/Illinois", active="exact"),
                dbc.NavLink("Indiana", href="/Indiana", active="exact"),
                dbc.NavLink("Iowa", href="/Iowa", active="exact"),
                dbc.NavLink("Kansas", href="/Kansas", active="exact"),
                dbc.NavLink("Kentucky", href="/Kentucky", active="exact"),
                dbc.NavLink("Louisiana", href="/Louisiana", active="exact"),
                dbc.NavLink("Maine", href="/Maine", active="exact"),
                dbc.NavLink("Maryland", href="/Maryland", active="exact"),
                dbc.NavLink("Massachusetts", href="/Massachusetts", active="exact"),
                dbc.NavLink("Michigan", href="/Michigan", active="exact"),
                dbc.NavLink("Mississippi", href="/Mississippi", active="exact"),
                dbc.NavLink("Missouri", href="/Missouri", active="exact"),
                dbc.NavLink("Montana", href="/Montana", active="exact"),
                dbc.NavLink("Nebraska", href="/Nebraska", active="exact"),
                dbc.NavLink("Nevada", href="/Nevada", active="exact"),
                dbc.NavLink("New Hampshire", href="/NewHampshire", active="exact"),
                dbc.NavLink("New Jersey", href="/NewJersey", active="exact"),
                dbc.NavLink("New Mexico", href="/NewMexico", active="exact"),
                dbc.NavLink("New York", href="/NewYork", active="exact"),
                dbc.NavLink("North Carolina", href="/NorthCarolina", active="exact"),
                dbc.NavLink("North Dakota", href="/NorthDakota", active="exact"),
                dbc.NavLink("Ohio", href="/Ohio", active="exact"),
                dbc.NavLink("Oklahoma", href="/Oklahoma", active="exact"),
                dbc.NavLink("Oregon", href="/Oregon", active="exact"),
                dbc.NavLink("Pennsylvania", href="/Pennsylvania", active="exact"),
                dbc.NavLink("Rhode Island", href="/RhodeIsland", active="exact"),
                dbc.NavLink("South Carolina", href="/SouthCarolina", active="exact"),
                dbc.NavLink("South Dakota", href="/SouthDakota", active="exact"),
                dbc.NavLink("Tennessee", href="/Tennessee", active="exact"),
                dbc.NavLink("Texas", href="/Texas", active="exact"),
                dbc.NavLink("Utah", href="/Utah", active="exact"),
                dbc.NavLink("Vermont", href="/Vermont", active="exact"),
                dbc.NavLink("Virginia", href="/Virginia", active="exact"),
                dbc.NavLink("Washington", href="/Washington", active="exact"),
                dbc.NavLink("West Virginia", href="/WestVirginia", active="exact"),
                dbc.NavLink("Wisconsin", href="/Wisconsin", active="exact"),
                dbc.NavLink("Wyoming", href="/Wyoming", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Iframe(src="assets/maps/Alabama.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Alaska":
        return html.Iframe(src="assets/maps/Alaska.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Arizona":
        return html.Iframe(src="assets/maps/Arizona.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/California":
        return html.Iframe(src="assets/maps/California.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Colorado":
        return html.Iframe(src="assets/maps/Colorado.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Connecticut":
        return html.Iframe(src="assets/maps/Connecticut.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Delaware":
        return html.Iframe(src="assets/maps/Delaware.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Florida":
        return html.Iframe(src="assets/maps/Florida.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Georgia":
        return html.Iframe(src="assets/maps/Georgia.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Hawaii":
        return html.Iframe(src="assets/maps/Hawaii.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Idaho":
        return html.Iframe(src="assets/maps/Idaho.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Illinois":
        return html.Iframe(src="assets/maps/Illinois.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Indiana":
        return html.Iframe(src="assets/maps/Indiana.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    ################################
    elif pathname == "/Indiana":
        return html.Iframe(src="assets/maps/Indiana.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Iowa":
        return html.Iframe(src="assets/maps/Iowa.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Kansas":
        return html.Iframe(src="assets/maps/Kansas.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Kentucky":
        return html.Iframe(src="assets/maps/Kentucky.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Louisiana":
        return html.Iframe(src="assets/maps/Louisiana.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Maine":
        return html.Iframe(src="assets/maps/Maine.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Maryland":
        return html.Iframe(src="assets/maps/Maryland.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Massachusetts":
        return html.Iframe(src="assets/maps/Massachusetts.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Michigan":
        return html.Iframe(src="assets/maps/Michigan.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Indiana":
        return html.Iframe(src="assets/maps/Indiana.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Minnesota":
        return html.Iframe(src="assets/maps/Minnesota.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Mississippi":
        return html.Iframe(src="assets/maps/Mississippi.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Missouri":
        return html.Iframe(src="assets/maps/Missouri.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Montana":
        return html.Iframe(src="assets/maps/Montana.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Nebraska":
        return html.Iframe(src="assets/maps/Nebraska.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Nevada":
        return html.Iframe(src="assets/maps/Nevada.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/NewHampshire":
        return html.Iframe(src="assets/maps/New Hampshire.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/NewJersey":
        return html.Iframe(src="assets/maps/New Jersey.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/NewMexico":
        return html.Iframe(src="assets/maps/New Mexico.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Indiana":
        return html.Iframe(src="assets/maps/Indiana.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/NewYork":
        return html.Iframe(src="assets/maps/New York.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/NorthCarolina":
        return html.Iframe(src="assets/maps/North Carolina.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/NorthDakota":
        return html.Iframe(src="assets/maps/North Dakota.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Ohio":
        return html.Iframe(src="assets/maps/Ohio.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Oklahoma":
        return html.Iframe(src="assets/maps/Oklahoma.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Oregon":
        return html.Iframe(src="assets/maps/Oregon.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Pennsylvania":
        return html.Iframe(src="assets/maps/Pennsylvania.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/RhodeIsland":
        return html.Iframe(src="assets/maps/Rhode Island.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/SouthCarolina":
        return html.Iframe(src="assets/maps/South Carolina.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/SouthDakota":
        return html.Iframe(src="assets/maps/South Dakota.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Tennessee":
        return html.Iframe(src="assets/maps/Tennessee.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Texas":
        return html.Iframe(src="assets/maps/Texas.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Utah":
        return html.Iframe(src="assets/maps/Utah.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Vermont":
        return html.Iframe(src="assets/maps/Vermont.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Virginia":
        return html.Iframe(src="assets/maps/Virginia.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Washington":
        return html.Iframe(src="assets/maps/Washington.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/WestVirginia":
        return html.Iframe(src="assets/maps/West Virginia.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Wisconsin":
        return html.Iframe(src="assets/maps/Wisconsin.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    elif pathname == "/Wyoming":
        return html.Iframe(src="assets/maps/Wyoming.html",
               style = {
                  "height": "600px",
                  "width": "100%"
               })
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server()