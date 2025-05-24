
# layouts/home.py
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go
from components.cards import create_card
from components.alerts import create_alert
from data.data_home import kpi_data, resumen_data, eficiencia_data, alertas_data, acciones_data

def get_layout():
    # Crear cards KPI desde el DataFrame
    kpi_cards = []
    for _, row in kpi_data.iterrows():
        kpi_cards.append(
            dbc.Col(
                create_card(row['kpi'], row['valor'], row['icono'], row['color']),
                md=3
            )
        )
    
    # Procesar alertas del resumen (separadas por ;)
    alertas_resumen = resumen_data['alertas'][0].split(';')
    
    # Crear alertas desde el DataFrame
    alertas = []
    for _, row in alertas_data.iterrows():
        alertas.append(create_alert(row['mensaje'], row['tipo']))
    
    # Crear listado de acciones desde el DataFrame
    acciones = []
    for _, row in acciones_data.iterrows():
        acciones.append(dbc.ListGroupItem(row['accion']))
    
    # Procesar niveles de eficiencia
    niveles_eficiencia = [
        {'range': [int(x) for x in eficiencia_data['nivel_1_rango'][0].split('-')], 
         'color': eficiencia_data['nivel_1_color'][0]},
        {'range': [int(x) for x in eficiencia_data['nivel_2_rango'][0].split('-')], 
         'color': eficiencia_data['nivel_2_color'][0]},
        {'range': [int(x) for x in eficiencia_data['nivel_3_rango'][0].split('-')], 
         'color': eficiencia_data['nivel_3_color'][0]}
    ]
    
    return html.Div([
        # Sección superior con presentación extendida del bot
        # Sección superior con presentación del bot (versión ajustada)
dbc.Row([
    dbc.Col([
        dbc.Card(
            [
                dbc.CardBody([
                    html.Div(
                        [
                            html.Div(
                                html.Img(
                                    src="/assets/chatbot-icon.png",
                                    height="70px",  # Reducido de 80px
                                    className="me-3",  # Reducido de me-4
                                    style={
                                        "borderRadius": "50%",
                                        "border": "2px solid #00bfff",  # Cambiado a tu color azul
                                        "padding": "4px",
                                        "boxShadow": "0 0 8px rgba(0, 191, 255, 0.2)"  # Ajustado a tu sombra
                                    }
                                ),
                                className="flex-shrink-0"
                            ),
                            html.Div(
                                [
                                    html.H5("NiloBot", className="mb-2", style={"color": "#00bfff"}),  # Cambiado de H4 a H5
                                    html.P(
                                        "¡Hola! Soy tu asistente de inteligencia artificial. "
                                        f"La empresa muestra un crecimiento del {resumen_data['crecimiento'][0]} en ventas "
                                        f"con margen bruto del {resumen_data['margen_bruto'][0]}. "
                                        f"Flujo de caja: {resumen_data['flujo_caja'][0]}. "
                                        "Áreas clave:",
                                        className="mb-2",  # Reducido espacio
                                        style={"fontSize": "0.9rem"}  # Tamaño consistente
                                    ),
                                    html.Ul([
                                        html.Li(
                                            alerta, 
                                            className="mb-1",  # Espaciado reducido
                                            style={"fontSize": "0.85rem"}  # Tamaño más pequeño
                                        ) for alerta in alertas_resumen
                                    ]),
                                    html.P(
                                        "Consulta el panel izquierdo para interactuar.",
                                        className="text-muted mt-2 mb-0",  # Ajuste de márgenes
                                        style={"fontSize": "0.8rem"}  # Texto más pequeño
                                    ),
                                    html.P(
                                        "Recuerda conversaciones simples, decisiones inteligentes <3",
                                        className="mb-2", style={"color": "#00bfff"}  # Texto más pequeño
                                    )
                                ],
                                className="flex-grow-1"
                            )
                        ],
                        className="d-flex align-items-center"
                    )
                ])
            ],
            className="mb-3",  # Cambiado de mb-4
            style={
                "borderLeft": "3px solid #00bfff",  # Ajustado a tu estilo
                "background": "rgba(230, 247, 255, 0.7)",  # Usando tu color de fondo
                "borderRadius": "8px"  # Bordes más suaves
            }
        )
    ])
]),
        
      
        
        # Fila 2: Alertas y próximas acciones
        dbc.Row([
            dbc.Col([
                html.H3("Alertas Prioritarias", className="mb-3"),
                *alertas
            ], md=6),
            
            dbc.Col([
                html.H3("Próximas Acciones", className="mb-3"),
                dbc.ListGroup(acciones)
            ], md=6)
        ], className="mt-4")
    ])