import io

import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import *
from dash.dcc import Download
from dash.exceptions import PreventUpdate

df = pd.read_csv('dataset.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


@app.callback(
    Output("download", "data"),
    Input("save-button", "n_clicks"),
    State("table", "derived_virtual_data"))
def download_as_csv(n_clicks, table_data):
    if not n_clicks:
        raise PreventUpdate
    download_buffer = io.StringIO()
    dff = pd.DataFrame(table_data)
    dff.to_csv(download_buffer, index=False)
    download_buffer.seek(0)
    return dict(content=download_buffer.getvalue(), filename="Analysis.csv")


def header():
    return dbc.NavbarSimple(
        children=[dbc.NavItem()],
        brand="OTA Hotels Dashboard",
        brand_href="#",
        color="primary",
        expand="lg",
        dark=True,
    )


def table():
    return dash.dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns],
        derived_virtual_data=df.to_dict('records'),
        page_size=5,
        filter_action='native',
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        selected_columns=[],
        selected_rows=[],
        style_header={
            'background-color': '#0d6efd',
            'color': 'white'
        },
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in df.columns
        ],
    )


@app.callback(
    Output("trip-type-container", "children"),
    Input('table', "derived_virtual_data")
)
def graph(rows):
    return create_graph(column_name="Trip Type", dff=pd.DataFrame(rows), id="trip-type-graph",
                        title="Group Type")


@app.callback(
    Output("location-type-container", "children"),
    Input('table', "derived_virtual_data")
)
def graph(rows):
    return create_graph(column_name="Location Type", dff=pd.DataFrame(rows), id="location-type-graph",
                        title="Destination Location Type")


@app.callback(
    Output("hotel-continent-container", "children"),
    Input('table', "derived_virtual_data")
)
def graph(rows):
    return create_graph(column_name="Hotel Continent", dff=pd.DataFrame(rows), id="hotel-continent-graph",
                        title="Destination Continent")


@app.callback(
    Output("source-city-container", "children"),
    Input('table', "derived_virtual_data")
)
def graph(rows):
    return create_graph(column_name="Source City", dff=pd.DataFrame(rows), id="source-city-graph", title="Source City")


def create_graph(column_name, dff, id, title):
    x_axis = dff[column_name].unique()
    return [
        dcc.Graph(
            id=id,
            figure={
                "data": [
                    {
                        "x": x_axis,
                        "y": [dff[dff[column_name] == source_city].shape[0] for source_city in
                              x_axis],
                        "type": "bar"
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True, "title": title},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": "Count"}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )

    ]


app.layout = dbc.Container(
    children=dash.html.Div(
        [
            dbc.Row(dbc.Col(header())),
            dbc.Row(dash.html.Br()),
            dbc.Row(dbc.Col(table())),
            Download(id="download"),
            dbc.Row(dbc.Col(dbc.Button("Download", color="success", className="me-1", id="save-button")),
                    style={"float": "right"}, className="ml-auto"),
            dbc.Row(html.Br()),
            dbc.Row(
                [
                    dbc.Col(html.Div(id="trip-type-container")),
                    dbc.Col(html.Div(id="location-type-container")),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div(id="hotel-continent-container")),
                    dbc.Col(html.Div(id="source-city-container")),
                ]
            ),

        ]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
