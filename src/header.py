import dash_bootstrap_components as dbc
from dash import html


import dash_bootstrap_components as dbc

home_route = ("Business Forecast Lab", "/")

nav_routes = [
    ("Find a Series", "/search/"),
    ("Leaderboard", "/leaderboard/"),
    ("Blog", "/blog"),
    ("Methodology", "/methodology/"),
    ("About", "/about/"),
]



def header():
    return dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.A(
                                [
                                    html.Img(
                                        src="/assets/USYD_coa_reversed.png",
                                        height="30px",
                                    )
                                ],
                                href="https://www.sydney.edu.au/business/",
                            )
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "Forecast Lab",
                                className="ms-2",
                                href="/",
                                external_link=True,
                            )
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                x[0],
                                                href=x[1],
                                                external_link=True,
                                            )
                                        )
                                        for x in nav_routes
                                    ]
                                    + [
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                html.I(
                                                    className="fab fa-github fa-lg"
                                                ),
                                                href="https://github.com/forecastlab/forecast_dash",
                                                external_link=True,
                                            )
                                        )
                                    ],
                                    # make sure nav takes up the full width for auto
                                    # margin to get applied
                                    className="w-100",
                                ),
                                id="navbar-collapse",
                                is_open=False,
                                navbar=True,
                            ),
                        ],
                        # the row should expand to fill the available horizontal space
                        className="flex-grow-1",
                    ),  # close row
                    lg="expand",
                ),  # close col
            ],
        ),  # close containter
        color="dark",
        dark=True,
    )
