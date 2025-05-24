import dash
from dash import Input, Output, State, no_update
from layouts import home, finanzas, ventas, inventario, nomina, login
# Luego en main_callbacks.py, importa y registra estos callbacks:
from callbacks.chatbot_callbacks import register_chatbot_callbacks



# Credenciales de ejemplo
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

VALID_USERS = {
    "admin": "1234",
    "maria": "clave1",
    "juan": "pass123"
}

def register_callbacks(app):

    # --- Callback para login ---
    @app.callback(
        Output("session-store", "data"),
        Output("login-error", "children"),
        Output("url", "pathname"), 
        Input("login-button", "n_clicks"),
        State("login-username", "value"),
        State("login-password", "value"),
        prevent_initial_call=True
    )
    def check_login(n_clicks, username, password):
        if username in VALID_USERS and password == VALID_USERS[username]:
            return {"logged_in": True}, False, "/"
        else:
            return no_update, "Usuario o contraseña incorrectos.", no_update 

    # --- Callback para navegación protegida ---
    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname'),
        State('session-store', 'data')
    )
    def display_page(pathname, session_data):
        if not session_data or not session_data.get("logged_in"):
            return login.login_layout

        if pathname == '/finanzas':
            return finanzas.get_layout()
        elif pathname == '/ventas':
            return ventas.get_layout()
        elif pathname == '/inventario':
            return inventario.get_layout()
        elif pathname == '/nomina':
            return nomina.get_layout()
        else:
            return home.get_layout()

    # --- Callback para logout (opcional) ---
    @app.callback(
        Output("session-store", "clear_data"),
        Input("logout-button", "n_clicks"),
        prevent_initial_call=True
    )
    def logout(n):
        return True
    
    register_chatbot_callbacks(app)