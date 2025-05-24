from dash import Input, Output, State, no_update
from layouts import home, finanzas, ventas, inventario, nomina, login
from callbacks.chatbot_callbacks import register_chatbot_callbacks

VALID_USERS = {
    "admin": "1234",
    "laura": "1234",
    "juan": "pass123"
}

def register_callbacks(app):
    # Callback para login - redirige a home después de login correcto
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
            # Login correcto -> guardamos sesión y redirigimos a home
            return {"logged_in": True, "username": username}, "", "/home"
        elif not username or not password:
            return no_update, "", no_update
        return no_update, "Usuario o contraseña incorrectos.", no_update

    # Callback para mostrar página según ruta y sesión
    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname'),
        State('session-store', 'data')
        # no prevent_initial_call para que se ejecute al cargar la app
    )
    def display_page(pathname, session_data):
        if not session_data or not session_data.get("logged_in"):
            # No está logueado, mostrar login
            return login.login_layout

        # Mostrar layout según la url
        if pathname == '/finanzas':
            return finanzas.get_layout()
        elif pathname == '/ventas':
            return ventas.get_layout()
        elif pathname == '/inventario':
            return inventario.get_layout()
        elif pathname == '/nomina':
            return nomina.get_layout()
        elif pathname == '/home':
            return home.get_layout()
        else:
            # Ruta no reconocida, mostrar home
            return home.get_layout()



    # Mostrar u ocultar botón logout según ruta
    @app.callback(
        Output("logout-button", "style"),
        Input("url", "pathname")
    )
    def toggle_logout_visibility(pathname):
        if pathname == "/login" or pathname == "/":
            return {"display": "none"}
        return {"display": "block"}

    register_chatbot_callbacks(app)
