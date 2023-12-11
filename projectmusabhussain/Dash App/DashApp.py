# DashApp.py
import dash
from dash import html, dcc, Input, Output
import home, share, trend, sentiment, about

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Br(),
        html.H1("UnMashable", style={'textAlign': 'center', 'fontSize': '70px', 'marginBottom': '5px', 'color': '#FFF'}),
        html.P("A Data Analysis Mash-tape!", style={'textAlign': 'center', 'fontSize': '40px', 'marginTop': '10px', 'marginBottom': '5px', 'color': '#FFF'}),
        html.P("Unraveling news articles, one byte at a time!", style={'textAlign': 'center', 'fontSize': '40px', 'marginTop': '10px', 'color': '#FFF'}),      
        html.Hr(style={'width': '100%'}),
    ]),
    html.Br(),
    html.Div([
        dcc.Link(
            'Home', 
            href='/home', 
            style={
                'marginRight':'10px',
                'padding': '10px',
                'backgroundColor': '#3C3C3C',
                'border': '1px solid #FFF',
                'textDecoration': 'none',
                'color': '#F3F3F3'
            }
        ),
        dcc.Link(
            'Shares Analysis', 
            href='/share', 
            style={
                'marginRight':'10px',
                'padding': '10px',
                'backgroundColor': '#3C3C3C',
                'border': '1px solid #FFF',
                'textDecoration': 'none',
                'color': '#FFF'
            }
        ),
        dcc.Link(
            'Trend Analysis', 
            href='/trend', 
            style={
                'backgroundColor': '#3C3C3C',
                'border': '1px solid #FFF',
                'textDecoration': 'none',
                'color': '#FFF',
                'marginRight':'10px',
                'padding': '10px',

            }
        ),
        dcc.Link(
            'Sentiment Analysis', 
            href='/sentiment',
            style={
                'marginRight':'10px',
                'padding': '10px',
                'backgroundColor': '#3C3C3C',
                'border': '1px solid #FFF',
                'textDecoration': 'none',
                'color': '#FFF'
            }
        ),
        dcc.Link(
            'About', 
            href='/about',
            style={
                'padding': '10px',
                'backgroundColor': '#3C3C3C',
                'border': '1px solid #FFF',
                'textDecoration': 'none',
                'color': '#FFF'
            }
        ),
        
    ], style={
        'display':'flex', 
        'justifyContent':'center',
        'backgroundColor': '#1E1E1E',
    }),
    html.Hr(style={'width': '100%'}),
    html.Div(id='page-content'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
], style={
    'backgroundColor': '#1E1E1E',
    'color': '#FFF'  # White text
})

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/share':
        return share.layout
    elif pathname == '/trend':
        return trend.layout
    elif pathname == '/sentiment':
        return sentiment.layout
    elif pathname == '/about':
        return about.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)