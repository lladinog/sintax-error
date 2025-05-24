import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_mantine_components as dmc

def create_chatbot():
    return html.Div(
        id="chatbot-container",
        className="chatbot-container",
        style={
            "height": "calc(100vh - 120px)",
            "display": "flex",
            "flexDirection": "column"
        },
        children=[
            # Encabezado
            dbc.CardHeader(
                [
                    html.Div(
                        [
                            dmc.Avatar(
                                src="/assets/chatbot-icon.png",
                                size="xl",
                                radius="xl",
                                className="me-3"
                            ),
                            html.H2("NiloBot", className="mb-0"),
                        ],
                        className="d-flex align-items-center"
                    ),
                    dbc.Badge(
                        "En línea",
                        color="success",
                        className="ms-auto",
                        pill=True
                    )
                ],
                className="d-flex align-items-center p-3"
            ),
            
            # Área de mensajes - Ahora con mejor uso del espacio
            dbc.CardBody(
                id="chat-messages",
                className="chat-messages p-0",  # Quitamos padding interno
                style={
                    "flex": "1",
                    "overflowY": "auto",
                    "display": "flex",
                    "flexDirection": "column",
                    "width": "100%"
                },
                children=[
                    html.Div(
                        className="d-flex flex-column h-100 p-3",  # Contenedor flexible
                        children=[
                            dbc.Alert(
                                "¡Hola! Soy NiloBot, tu asistente de inteligencia artificial.",
                                color="primary",
                                className="chat-message bot-message",
                                style={"fontSize": "1rem"}
                            ),
                            dbc.Alert(
                                "Puedes preguntarme sobre:",
                                color="light",
                                className="chat-message bot-message",
                                style={"fontSize": "1rem"}
                            ),
                            html.Ul([
                                html.Li("¿Cómo van las ventas este mes?"),
                                html.Li("Muéstrame el reporte financiero"),
                                html.Li("¿Cuál es el estado del inventario?"),
                                html.Li("Dame un resumen de nómina")
                            ], className="chat-message bot-message ps-4")
                        ]
                    ),
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
                    
                )