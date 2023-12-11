from dash import html

layout= html.Div([
        html.H1("Welcome to UnMashable!", style={'textAlign': 'center','fontsize': '30px'}),
        html.P("UnMashable is a data analysis project focused on unraveling news articles, one byte at a time!", style={'textAlign': 'center'}),
        html.P("We use advanced data analysis techniques to provide insights into trends and sentiments in news articles published by Mashable.", style={'textAlign': 'center'}),
        html.P("Feel free to explore the dahsboard!", style={'textAlign': 'center'}),
    ])