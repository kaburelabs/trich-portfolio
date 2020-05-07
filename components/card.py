import dash_bootstrap_components as dbc
import dash_html_components as html


def Card(image, title, description, link, tech):
    card = html.Div(
        html.Div([
            html.Div(
                html.Img(src=image, alt=title),
                className="bottom16 portfolio_card_img"),
            html.Div([
                html.H4(title, className="font-xs bold uppercase"),
                html.P(description, className="font-xxs"),
            ], className="portfolio_card_text"),
            html.Div([
                html.Div([
                    html.Div(
                        dbc.Badge(
                            t, className="mr-1 self_center default_inverse primary_bg"),
                        className="inline-block"
                    ) for t in tech
                ]),
                html.A(
                    html.I(className="fab fa-github font-sm terciary"),
                    href=link, target="_blank"),
            ], className="font-xs flex_row_btw portfolio_card_footer")
        ], className="second_bg padding16 radius8 portfolio_card"),
        className="padding16"
    )
    return card
