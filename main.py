import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from apps.app import app 
from apps import covid19

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return covid19.layout
    else:
        print(pathname)
        return '404'



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8080)

