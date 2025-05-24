import dash
from dash import html, dcc, Input, Output, State
from datetime import datetime
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc  # ✅ Importar Mantine
from layouts import home, finanzas, ventas, inventario, nomina, login
from callbacks.main_callbacks import register_callbacks
from components.chatbot import create_chatbot

# Inicializar la app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.COSMO],
    suppress_callback_exceptions=True
)
app.title = "Dashboard Empresarial - ERP Analytics"

# Layout principal, envuelto en MantineProvider
app.layout = dmc.MantineProvider(  # ✅ ENVOLVER AQUÍ
    theme={"colorScheme": "light"},
    children=html.Div([
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='session-store', storage_type='session'),

        # Barra de navegación superior
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand("ERP Dashboard", href="/", className="ms-2"),



                html.Div([
                    html.Span(datetime.now().strftime('%d/%m/%Y %H:%M')),
                    dbc.Button("Actualizar", color="light", className="ms-3", id="refresh-btn")
                ], className="d-flex align-items-center"),
                dbc.Button("Login", id="login-button", color="success", className="ms-2", style={"display": "none"}),
                dbc.Button("Cerrar sesión", id="logout-button", color="danger", className="ms-2")
            ]),
            color="#e6f7ff",
            dark=True,
            sticky="top"
        ),

        # Contenido condicional (chatbot solo cuando no es login)
        html.Div(id='main-content')
    ])
)

# Callback para mostrar/ocultar chatbot
@app.callback(
    Output('main-content', 'children'),
    Input('url', 'pathname'),
    State('session-store', 'data')
)
def update_layout(pathname, session_data):
    # Mostrar solo login si no hay sesión
    if not session_data or not session_data.get("logged_in"):
        return login.login_layout

    # Página de login no muestra chatbot
    if pathname == '/login':
        return dbc.Container(
            html.Div(id='page-content', className="page-content py-4"),
            fluid=True
        )

    # Otras páginas muestran chatbot + contenido
    return dbc.Container(
        fluid=True,
        className="main-container",
        children=[
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        create_chatbot(),
                        className="h-100",
                        style={
                            "height": "calc(100vh - 120px)",
                            "display": "flex",
                            "flexDirection": "column"
                        }
                    ),
                    width=3,
                    className="chatbot-column"
                ),
                dbc.Col(
                    html.Div(id='page-content', className="page-content py-4"),
                    width=9,
                    className="content-column"
                )
            ])
        ]
    )

# Registrar callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)

"""
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Finanzas", href="/finanzas")),
                    dbc.NavItem(dbc.NavLink("Ventas", href="/ventas")),
                    dbc.NavItem(dbc.NavLink("Inventario", href="/inventario")),
                    dbc.NavItem(dbc.NavLink("Nómina", href="/nomina")),
                ], className="me-auto"),
"""    