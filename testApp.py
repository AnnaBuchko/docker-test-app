import sys

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import os

file_path = sys.argv[1]

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Simple File Write/Read Dash App"),
    dcc.Input(id='input-data', type='text', placeholder='Enter data to write', style={'margin-right': '10px'}),
    html.Button('Write to File', id='write-button', n_clicks=0),
    html.Button('Read from File', id='read-button', n_clicks=0, style={'margin-left': '10px'}),
    html.Div(id='file-content', style={'whiteSpace': 'pre-line', 'margin-top': '20px'}),
])

@app.callback(
    Output('file-content', 'children'),
    [Input('write-button', 'n_clicks'),
     Input('read-button', 'n_clicks')],
    [State('input-data', 'value')]  # Capture the input field's value
)
def update_output(write_clicks, read_clicks, input_data):
    ctx = dash.callback_context

    if not ctx.triggered:
        return "Click a button to interact with the file."

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'write-button':
        if input_data:
            with open(file_path, "w") as f:
                f.write(input_data)
            return f"Data '{input_data}' has been written to the file."
        else:
            return "No data entered. Please enter some data to write to the file."

    elif button_id == 'read-button':
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                file_content = f.read()
            return f"File Content:\n{file_content}"
        else:
            return "File not found. Please write to the file first."

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)