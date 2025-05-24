import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_mantine_components as dmc

def create_chatbot():
    return html.Div(
        id="chatbot-container",
        className="chatbot-container",
        children=[
            # Encabezado del chatbot - Más grande
            dbc.CardHeader(
                [
                    html.Div(
                        [
                            dmc.Avatar(
                                src="/assets/chatbot-icon.png",
                                size="xl",  # Tamaño más grande
                                radius="xl",
                                className="me-3"  # Más margen
                            ),
                            html.H2("NiloBot", className="mb-0", style={"fontSize": "1.8rem"}),  # Texto más grande
                        ],
                        className="d-flex align-items-center"
                    ),
                    dbc.Badge(
                        "En línea",
                        color="success",
                        className="ms-auto",
                        pill=True,
                        style={"fontSize": "1rem"}  # Badge más grande
                    )
                ],
                className="d-flex align-items-center p-3",  # Más padding
                style={"backgroundColor": "#f8f9fa", "borderBottom": "1px solid #dee2e6"}
            ),
            
            # Área de mensajes con scroll interno
            dbc.CardBody(
                id="chat-messages",
                className="chat-messages",
                style={
                    "overflowY": "auto",
                    "height": "calc(100% - 150px)",  # Altura calculada
                    "padding": "1.5rem"
                },
                children=[
                    dbc.Alert(
                        "¡Hola! Soy NiloBot, tu asistente de inteligencia artificial. "
                        "Pregúntame lo que necesites sobre los datos del dashboard.",
                        color="primary",
                        className="chat-message bot-message",
                        style={"fontSize": "1rem"}
                    ),
                    dbc.Alert(
                        "Por ejemplo, puedes preguntar: '¿Cuál fue el crecimiento de ventas este mes?'",
                        color="light",
                        className="chat-message bot-message",
                        style={"fontSize": "1rem"}
                    )
                ]
            ),
            
            # Pie del chatbot fijo en la parte inferior
            dbc.CardFooter(
                [
                    dbc.InputGroup(
                        [
                            dbc.Input(
                                id="chat-input",
                                placeholder="Escribe tu pregunta...",
                                type="text",
                                className="chat-input",
                                style={"height": "50px", "fontSize": "1rem"}
                            ),
                            dbc.Button(
                                "Enviar",
                                id="chat-send-button",
                                color="primary",
                                n_clicks=0,
                                style={"height": "50px", "fontSize": "1rem"}
                            ),
                        ],
                        className="w-100"
                    )
                ],
                className="p-3",
                style={
                    "backgroundColor": "#f8f9fa",
                    "borderTop": "1px solid #dee2e6",
                    "position": "sticky",
                    "bottom": "0"
                }
            )
        ],
        style={
            "height": "calc(100vh - 120px)",  # Altura completa menos navbar
            "display": "flex",
            "flexDirection": "column"
        }
    )