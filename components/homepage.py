import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components.navbar import Navbar
from components.about import About
from components.stacks import Stacks
from components.portfolio import Portfolio
from components.footer import Footer

nav = Navbar()
about = About()
portfolio = Portfolio()
stacks = Stacks()
footer = Footer()

update_date="2023-10-02"
message_extra=html.Div(f"Some of the apps may have changed their URL or have been discontinued since the last update. Last Update: {update_date}", className="messageStyle")

body = dbc.Container([about, stacks, message_extra, portfolio, footer], className="top32")


def Homepage():
    layout = html.Div([nav, body], id="homepage")
    return layout
