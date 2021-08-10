import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
#------------------------------------------------------
# build APP
#------------------------------------------------------
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
server=app.server
#------------------------------------------------------
# Set Layout Component
#------------------------------------------------------
layout = html.Div(
[
    html.Div( #------------------------------------------------------------------------------------------------- ROW 1
               children=[
                    html.Div(#-------------------------------------------------------------------------- ROW 1 - col 1
                        id='select_product',
                        children=[html.P('ROW 1 - col 1')],
                        style={'width':'36%','height':'100%' ,'backgroundColor':'#FF0000','display':'inline-block','border-radius':'8px'}

                    ),
                    html.Div(#-------------------------------------------------------------------------- ROW 1 - col 2
                        id='world_sale',
                        children=[ html.P('ROW 1 - col 2')],
                        style={'width':'32%','height':'100%' ,'backgroundColor':'#0000FF','display':'inline-block','border-radius':'8px'}

                    ),
                    html.Div(#-------------------------------------------------------------------------- ROW 1 - col 3
                        id='grows_sale',
                        children=[html.P('ROW 1 - col 3')],
                        style={'width':'32%','height':'100%' ,'backgroundColor':'#C0C0C0','display':'inline-block','border-radius':'8px'}

                    )

                ],style={'width':'100%','height':'20%' ,'backgroundColor':'#5da4d4','border-radius':'8px' ,'margin':'5px', 'padding':'5px'}
    ),
    html.Div(#------------------------------------------------------------------------------------------------- ROW 2
               children=[
                    html.Div(#------------------------------------------------------------------------- ROW 2 - col 1

                        children=[html.P(' ROW 2 - col 1')],
                        id='iran_map',
                        style={'width':'35%','height':'100%' ,'backgroundColor':'#A03C78','border-width':' 1px',
                               'display':'inline-block','border-radius': '10px','margin':'5px', 'padding':'5px'}
                    ),
                    html.Div(#------------------------------------------------------------------------- ROW 2 - col 2
                        id='tehran_map_line',
                        children=[html.P(' ROW 2 - col 2')],
                        style={'width':'35%','height':'100%' ,'backgroundColor':'#808000','display':'inline-block',
                               'border-width':' 1px','border-radius': '10px' ,'margin':'5px', 'padding':'5px'}

                    ),
                    html.Div(#------------------------------------------------------------------------- ROW 2 - col 3
                        [
                            html.Div(#--------------------------------------------------------- ROW 2 - col 3 - row 1
                                id='Satisfaction',
                                children=[ html.P(' ROW 2 - col 3 - row 1')],
                                style={'width': '35%', 'height': '100%', 'backgroundColor': '#800080', 'display': 'inline-block',
                                       'border-width': ' 1px','border-radius': '10px', 'margin': '5px', 'padding': '5px'}
                            ),
                            html.Div(#--------------------------------------------------------- ROW 2 - col 3 - row 2
                                id='sale_world_percent',
                                children=[html.P(' ROW 2 - col 3 - row 1')],
                                style={'width':'35%','height':'100%' ,'backgroundColor':'#008080','display':'inline-block',
                                'border-width':' 1px','border-radius': '10px' ,'margin':'5px', 'padding':'5px'}
                            )
                        ],style={'width':'25%','height':'100%' ,'backgroundColor':'#FF7F50','display':'inline-block',
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