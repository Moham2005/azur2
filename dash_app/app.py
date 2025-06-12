from dash import Dash, html, dcc

app = Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

app.layout = html.Div([
    html.H1("Bienvenue sur le dashboard Dash"),
    html.P("Ceci est une application Dash intégrée à FastAPI."),
    
    dcc.Graph(
        id='exmpl_1',
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [6, 9, 4], "type": "bar", "name": "Example 1"},
                {"x": [7, 2, 5], "y": [3, 7, 1], "type": "bar", "name": "Example 2"}
            ]
        }
    )
])
