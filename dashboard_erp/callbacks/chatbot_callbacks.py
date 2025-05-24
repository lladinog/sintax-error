# callbacks/chatbot_callbacks.py
from dash import Input, Output, State, html
import dash_bootstrap_components as dbc

def register_chatbot_callbacks(app):
    @app.callback(
        Output("chat-messages", "children"),
        Input("chat-send-button", "n_clicks"),
        Input("chat-input", "n_submit"),
        State("chat-input", "value"),
        State("chat-messages", "children"),
        prevent_initial_call=True
    )
    def update_chat(n_clicks, n_submit, user_input, current_messages):
        if user_input and (n_clicks or n_submit):
            # Mensaje del usuario
            user_message = dbc.Alert(
                user_input,
                color="primary",
                className="chat-message user-message"
            )
            
            # Respuesta del bot (simulada)
            bot_response = dbc.Alert(
                "Esta es una respuesta simulada. Conecta esta función con tu backend de chatbot.",
                color="light",
                className="chat-message bot-message"
            )
            
            current_messages.extend([user_message, bot_response])
            return current_messages
        
        return current_messages

