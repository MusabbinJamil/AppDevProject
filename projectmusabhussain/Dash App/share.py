# share.py
from dash import html, dcc
import pandas as pd
import plotly.express as px
import matplotlib.image as mpimg
import base64


data = pd.read_csv('Final Project Data.csv')

# Box plot
fig1 = mpimg.imread('image.png')
fig1_string = base64.b64encode(open('image.png', 'rb').read()).decode('ascii')


# Pie chart
category_shares = data.groupby('genre')['shares'].sum()
fig2 = px.pie(category_shares, values='shares', names=category_shares.index, template='plotly_dark', title='Distribution of Shares by Category')
# Scatter plot
data = data[data['shares'] <= 200000]
fig3 = px.scatter(data, x='content_word_count', y='shares', template='plotly_dark', color_discrete_sequence=['purple'], labels={'x':'Content Word Count', 'y':'Shares'}, title='Relationship between Shares and Content Word Count (Shares <= 200,000)')

layout = html.Div([
    html.H1('Sentiment Analysis', style={'textAlign': 'center', 'fontSize': '35px', 'marginBottom': '5px', 'color': '#FFF'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('This is a scatter plot of the title sentiment polarity vs. the number of shares the article received.', style={'textAlign': 'center', 'fontSize': '20px', 'marginTop': '10px', 'color': '#FFF'}),
    html.Img(src='data:image/png;base64,{}'.format(fig1_string), style={'height': '700px', 'width': '700px', 'margin': 'auto'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('This is a scatter plot of the average positive polarity of the articles vs. the number of shares the article received.', style={'textAlign': 'center', 'fontSize': '20px', 'marginTop': '10px', 'color': '#FFF'}),
    dcc.Graph(figure=fig2, style={'height': '700px', 'width': '700px', 'margin': 'auto'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('This is a scatter plot of the average negative polarity of the articles vs. the number of shares the article received.', style={'textAlign': 'center', 'fontSize': '20px', 'marginTop': '10px', 'color': '#FFF'}),
    dcc.Graph(figure=fig3, style={'height': '700px', 'width': '700px', 'margin': 'auto'}),
], style={'textAlign': 'center'})