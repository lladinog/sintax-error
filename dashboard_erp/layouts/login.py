from dash import html, dcc
import dash_bootstrap_components as dbc

login_layout = dbc.Container([
    html.Div([
        html.H2("Iniciar Sesión", className="login-title"),
        dbc.Input(id="login-username", placeholder="Usuario", type="text", className="mb-3 login-input"),
        dbc.Input(id="login-password", placeholder="Contraseña", type="password", className="mb-3 login-input"),
        dbc.Button("Entrar", id="login-button", className="mb-3 login-button w-100", n_clicks=0),
        html.Div(id="login-error", className="login-error"),
        html.Img(src="/assets/login-no-captcha.png", className="chatbot-icon")
    ], className="login-container")
], className="d-flex justify-content-center align-items-center vh-100")
