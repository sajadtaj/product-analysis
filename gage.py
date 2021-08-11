import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 3,
    mode = "gauge+number+delta",
    title = {'text': "Satisfaction"},
    delta = {'reference': 8},
    gauge = {'axis': {'range': [None, 10]},
             'steps' : [
                 {'range': [0, 3], 'color': "red"},
                 {'range': [3, 7.5], 'color': "orange"},
                 {'range': [7.5, 10], 'color': "green"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 8}}))


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True , port=2030)