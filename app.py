from typing import Any, Union

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.express as px
import json
import plotly.graph_objects as go
import pandas as pd
import geopandas as gpd
#-------------------------------------------------
#    READ DATA
#-------------------------------------------------
iran_map = gpd.read_file('map_iran.geojson')

with open('usa_map.geojson') as k:
    us_map = json.load(k)

scatter_map = pd.read_csv('F://dashboard//product analyse//City_Product_lat_lon.csv', low_memory=False)
Data_Product= pd.read_csv('F://dashboard//product analyse//prudoct maping.csv', low_memory=False)

#------------------------------------------------------
# build APP
#------------------------------------------------------
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
server=app.server
#-----------------------------------------------------------------------------------------------------------------------
# content CODE
#-----------------------------------------------------------------------------------------------------------------------
#
#
#------------------------------------------------------
# select_product
#------------------------------------------------------
select_product= dbc.Card(
                        [
                        dbc.CardBody(
                            [
                                dcc.Dropdown(
                                    id='select-product-dropdown',
                                    options=[
                                        {'label': 'Coca Cola'       , 'value': 'product A'},
                                        {'label': 'Pepsi'           , 'value': 'product B'},
                                        {'label': 'Redbull'         , 'value': 'product C'},
                                        {'label': 'Monster Energy'  , 'value': 'product D'}
                                    ],
                                   value="product C"
                                ),
                            ]
                        ),
                        ],style={'width':'100%','height':'100%',
                        'text-color':'#DC7633','color':'#DC7633'},
)
#
#------------------------------------------------------
# world sale
#------------------------------------------------------
world_sale=  dbc.Card(
                [
                    dbc.CardHeader("world_sale"),
                    dbc.CardBody(
                            [
                                dbc.ListGroup(
                                [
                                    dbc.ListGroupItem( html.H4(id = "show-world-sale") ),
                                ],
                            )
                            ]
                    )
                ],style={'width':'100%','height':'100%',
                        'text-color':'#DC7633','color':'#DC7633'}
            )

#------------------------------------------------------
# sale Grows
#------------------------------------------------------
sale_grows = dbc.Card(
                [
                    dbc.CardHeader("sale_grows"),
                    dbc.CardBody(
                            [
                                dbc.ListGroup(
                                [
                                    dbc.ListGroupItem( html.H4(id = "show-sale-grows") ),
                                ],
                            )
                            ]
                    )
                ],style={'width':'100%','height':'100%',
                        'text-color':'#DC7633','color':'#DC7633'}
            )
#----------------
@app.callback(
    Output('show-world-sale', 'children'),
    Output('show-sale-grows', 'children'),
    Input( 'select-product-dropdown' , 'value' )
    )
def show_world_sale(product):
    x = Data_Product[Data_Product["product type"]== product]["sale"]
    y = Data_Product[Data_Product["product type"]== product]["grows sale"]
    return x , y
#------------------------------------------------------
# Iran map
#------------------------------------------------------
iran_map_component = dcc.Graph(id="choropleth")

@app.callback(
    Output('choropleth', 'figure'),
    Input( 'select-product-dropdown' , 'value' )
)
def iran_choropleth(value):
    fig = px.choropleth_mapbox(
        Data_Product, geojson=iran_map, color=value,
        locations="province iran", featureidkey="properties.NAME_1",
        range_color=[500000, 15000000], mapbox_style="carto-positron",
        center={"lat":32.34, "lon":54.36 } ,zoom=3.75
    )
    fig.update_geos(fitbounds="locations", visible=True )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

#------------------------------------------------------
# tehran Map show sell
#------------------------------------------------------
city_map=dcc.Graph(id="city_map")
@app.callback(
    Output('city_map', 'figure'),
    Input( 'select-product-dropdown' , 'value' )
)
def show_city_map(value):
    scatter_map_selected= scatter_map[scatter_map["product"]==value]
    fig = px.scatter_mapbox(scatter_map_selected, lat="lat", lon="lon",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=9,
                            mapbox_style="open-street-map", color="sale", size="sale", hover_name="reagon"
                            )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

#------------------------------------------------------
# Satisfaction Gage
#------------------------------------------------------
Satisfaction = dcc.Graph(id="Satisfaction")

@app.callback(
    Output('Satisfaction', 'figure'),
    Input( 'select-product-dropdown' , 'value' )
)
def Satisfaction_gage(value):
    satis_value = Data_Product[Data_Product["product type"] == value]["Satisfaction"]
    fig = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = float(satis_value),
            mode = "gauge+number+delta",
            title = {'text': "Satisfaction"},
            delta = {'reference': 8},
            gauge = {'axis': {'range': [None, 10]},
                     'steps' : [
                         {'range': [0, 3], 'color': "red"},
                         {'range': [3, 7.5], 'color': "orange"},
                         {'range': [7.5, 10], 'color': "green"}],
                     'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 8}}))
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return  fig

#------------------------------------------------------
# WORLD Sale Piechart Component
#------------------------------------------------------
world_sale_pi=dcc.Graph(id="world_sale_pichart")
@app.callback(
    Output('world_sale_pichart', 'figure'),
    Input( 'select-product-dropdown' , 'value' )
)
def pichart_show(value):
    Africa = Data_Product[Data_Product["product type"] == value]["Africa percent"]
    Europe  = Data_Product[Data_Product["product type"] == value]["Europe percent"]
    Asia  = Data_Product[Data_Product["product type"] == value]["Asia percent"]
    North_America  = Data_Product[Data_Product["product type"] == value]["North America percent"]
    South_America  = Data_Product[Data_Product["product type"] == value]["South America percent"]
    Qceania  = Data_Product[Data_Product["product type"] == value]["Qceania percent"]

    labels = ['Africa', 'Europe', 'Asia', 'North_America' ,'North_America', 'South_America', 'Qceania' ]
    values = [float(Africa),float(Europe),float(Asia),float(North_America),float(South_America),float(Qceania)]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig




#------------------------------------------------------
# Set Layout Component
#------------------------------------------------------
layout = html.Div(
[
    html.Div( #------------------------------------------------------------------------------------------------- ROW 1
               children=[
                    html.Div(#-------------------------------------------------------------------------- ROW 1 - col 1
                        id='select_product',
                        children=[select_product],
                        style={'width':'36%','height':'100%' ,'backgroundColor':'#FF0000','display':'inline-block','border-radius':'8px'}

                    ),
                    html.Div(#-------------------------------------------------------------------------- ROW 1 - col 2
                        id='world_sale',
                        children=[ world_sale],
                        style={'width':'32%','height':'100%' ,'backgroundColor':'#0000FF','display':'inline-block','border-radius':'8px'}

                    ),
                    html.Div(#-------------------------------------------------------------------------- ROW 1 - col 3
                        id='grows_sale',
                        children=[sale_grows],
                        style={'width':'32%','height':'100%' ,'backgroundColor':'#C0C0C0','display':'inline-block','border-radius':'8px'}

                    )

                ],style={'width':'100%','height':'20%' ,'backgroundColor':'#5da4d4','border-radius':'8px' ,'margin':'5px', 'padding':'5px'}
    ),
    html.Div(#------------------------------------------------------------------------------------------------- ROW 2
               children=[
                    html.Div(#------------------------------------------------------------------------- ROW 2 - col 1

                        children=[iran_map_component],
                        id='iran_map',
                        style={'width':'35%','height':'100%' ,'backgroundColor':'#A03C78','border-width':' 1px',
                               'display':'inline-block','border-radius': '10px','margin':'5px', 'padding':'5px'}
                    ),
                   html.Div(  # ------------------------------------------------------------------------- ROW 2 - col 2
                       [
                           html.Div(  # --------------------------------------------------------- ROW 2 - col 2 - row 1
                               id='Satisfaction_component',
                               children=[Satisfaction],
                               style={'width': '95%', 'height': '30%', 'backgroundColor': '#800080',
                                      'display': 'block',
                                      'border-width': ' 1px', 'border-radius': '10px', 'margin': '5px',
                                      'padding': '5px'}
                           ),
                           html.Div(  # --------------------------------------------------------- ROW 2 - col 2 - row 2
                               id='sale_world_percent',
                               children=[world_sale_pi],
                               style={'width': '95%', 'height': '66%', 'backgroundColor': '#008080',
                                      'display': 'block',
                                      'border-width': ' 1px', 'border-radius': '10px', 'margin': '5px',
                                      'padding': '5px'}
                           )
                       ],
                       style={'width': '25%', 'height': '100%', 'backgroundColor': '#FF7F50', 'display': 'inline-block',
                              'border-width': ' 1px', 'border-radius': '10px', 'margin': '5px', 'padding': '5px'}

                   ),
                    html.Div(#------------------------------------------------------------------------- ROW 2 - col 3
                        id='tehran_map_line',
                        children=[city_map],
                        style={'width':'35%','height':'100%' ,'backgroundColor':'#808000','display':'inline-block',
                               'border-width':' 1px','border-radius': '10px' ,'margin':'5px', 'padding':'5px'}

                    )
               ],style={'width':'100%','height':'60%' ,'backgroundColor':'#FFD700','border-radius':'8px'}
    ),
    html.Div(#------------------------------------------------------------------------------------------------- ROW 3
            children=[
                html.Div(#------------------------------------------------------------------------------ROW 3 - col 1
                    id="price",
                    children=[html.P(" ROW 3 - col 1 ")],
                    style={'width':'22%','height':'98%' ,'backgroundColor':'#6B8E23','display':'inline-block',
                                'border-width':' 1px','border-radius': '10px' ,'margin':'5px', 'padding':'5px'}
                ),
                html.Div(#------------------------------------------------------------------------------ROW 3 - col 2
                    id="branch",
                    children=[html.P(" ROW 3 - col 2 ")],
                    style={'width': '22%', 'height': '98%', 'backgroundColor': '#7CFC00', 'display': 'inline-block',
                           'border-width': ' 1px', 'border-radius': '10px', 'margin': '5px', 'padding': '5px'}
                ),
                html.Div(#------------------------------------------------------------------------------ROW 3 - col 3
                    id="cost",
                    children=[html.P(" ROW 3 - col 3 ")],
                    style={'width': '22%', 'height': '98%', 'backgroundColor': '#00FA9A', 'display': 'inline-block',
                           'border-width': ' 1px', 'border-radius': '10px', 'margin': '5px', 'padding': '5px'}
                ),
                html.Div(#------------------------------------------------------------------------------ROW 3 - col 4
                    id="profit",
                    children=[html.P(" ROW 3 - col 4 ")],
                    style={'width': '22%', 'height': '98%', 'backgroundColor': '#20B2AA', 'display': 'inline-block',
                           'border-width': ' 1px', 'border-radius': '10px', 'margin': '5px', 'padding': '5px'}
                ),

            ],
            style={'width':'100%','height':'20%' ,'backgroundColor':'#9ACD32','display':'inline-block',
                                'border-width':' 1px','border-radius': '8px' ,'margin':'5px', 'padding':'5px'}
    ),

]
)




#------------------------------------------------------
# Set Layout in APP
#------------------------------------------------------
app.layout = html.Div(
    [
    layout
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True , port=2027)