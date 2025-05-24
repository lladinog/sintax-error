from dash import Input, Output, State, no_update
from layouts import home, finanzas, ventas, inventario, nomina, login
from callbacks.chatbot_callbacks import register_chatbot_callbacks

VALID_USERS = {
    "admin": "1234",
    "maria": "clave1",
    "juan": "pass123"
}

def register_callbacks(app):
    # Callback para login - Siempre redirige a home después de login
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
        
        # Verifica si el usuario está en la lista
        if username in VALID_USERS and password == VALID_USERS[username]:
            # Autenticación correcta
            return {"logged_in": True, "username": username}, "", "/home"
        elif not username or not password:
            return no_update, "", no_update
        # Credenciales inválidas
        return no_update, "Usuario o contraseña incorrectos.", no_update

    # Callback de navegación
    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname'),
        State('session-store', 'data'),
        prevent_initial_call=True
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
        elif pathname == '/home':  # Nueva ruta para home
            return home.get_layout()
        else:
            return home.get_layout()  # Redirige a home por defecto

    # Callback para logout
    @app.callback(
        Output("session-store", "clear_data"),
        Input("logout-button", "n_clicks"),
        prevent_initial_call=True
    )
    def logout(n):
        return True
    
    register_chatbot_callbacks(app)

    
    @app.callback(
        Output("logout-button", "style"),
        Input("url", "pathname")
    )
    def toggle_logout_visibility(pathname):
        if pathname == "/login":
            return {"display": "none"}
        return {"display": "block"}
    
    