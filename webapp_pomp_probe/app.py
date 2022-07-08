# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import os

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


def layout():
    return dbc.Container(
        [
            html.H1("ポンプ・プローブ解析")
        ],
        fluid=True
    )


URL_BASE_PATH = os.environ.get("URL_BASE_PATH", "/")
app = dash.Dash(
    __name__,
    url_base_pathname=URL_BASE_PATH,
    external_stylesheets=[dbc.themes.MATERIA]
)
app.layout = layout
