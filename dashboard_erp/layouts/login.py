from dash import html, dcc
import dash_bootstrap_components as dbc

login_layout = dbc.Container([
    html.H2("Iniciar Sesión", className="my-4"),
    dbc.Input(id="login-username", placeholder="Usuario", type="text", className="mb-3"),
    dbc.Input(id="login-password", placeholder="Contraseña", type="password", className="mb-3"),
    dbc.Button("Entrar", id="login-button", color="primary", className="mb-3"),
    html.Div(id="login-error", className="text-danger")
], className="p-5")