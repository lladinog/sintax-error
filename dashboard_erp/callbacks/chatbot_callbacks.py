from dash import Input, Output, State, html, no_update
import dash_bootstrap_components as dbc
from data import data_finanzas, data_home, data_inventario, data_nomina, data_ventas

def register_chatbot_callbacks(app):
    @app.callback(
        [Output("chat-messages", "children"),
         Output("url", "pathname", allow_duplicate=True)],
        [Input("chat-send-button", "n_clicks"),
         Input("chat-input", "n_submit")],
        [State("chat-input", "value"),
         State("chat-messages", "children"),
         State("url", "pathname")],
        prevent_initial_call=True
    )
    def update_chat(n_clicks, n_submit, user_input, current_messages, current_path):
        if not user_input or (not n_clicks and not n_submit):
            return no_update, no_update
        
        # Mensaje del usuario
        user_message = dbc.Alert(
            user_input,
            color="primary",
            className="chat-message user-message w-100 mb-2"
        )
        
        # Obtener datos de cada módulo
        home_data = data_home
        finanzas_data = data_finanzas
        ventas_data = data_ventas
        inventario_data = data_inventario
        nomina_data = data_nomina
        
        # Procesar pregunta y generar respuesta
        user_input_lower = user_input.lower()
        bot_response = None
        redireccion = no_update
        
        # Preguntas sobre Finanzas
        if any(palabra in user_input_lower for palabra in ["finanzas", "flujo", "margen", "roi", "cartera"]):
            kpi_finanzas = finanzas_data.kpi_data
            flujo = finanzas_data.financial_data['Flujo_Caja'].iloc[-1]
            
            bot_response = dbc.Alert(
                f"📊 Datos Financieros:\n\n"
                f"• Flujo de caja actual: ${flujo:,.0f}\n"
                f"• Margen bruto: {kpi_finanzas[kpi_finanzas['titulo'] == 'Margen Bruto']['valor'].values[0]}\n"
                f"• ROI: {kpi_finanzas[kpi_finanzas['titulo'] == 'ROI']['valor'].values[0]}\n"
                f"• Días de cartera: {kpi_finanzas[kpi_finanzas['titulo'] == 'Días Cartera']['valor'].values[0]}\n\n"
                f"Alertas recientes:\n- " + "\n- ".join(finanzas_data.alertas_data['mensaje']),
                color="light",
                className="chat-message bot-message w-100"
            )
            redireccion = "/finanzas"
        
        # Preguntas sobre Ventas
        elif any(palabra in user_input_lower for palabra in ["ventas", "venta", "crecimiento", "clientes"]):
            kpi_ventas = ventas_data.get_kpi_data()
            top_clientes = ventas_data.get_top_clientes()
            
            bot_response = dbc.Alert(
                f"🛍️ Datos de Ventas:\n\n"
                f"• Crecimiento mensual: {kpi_ventas['crecimiento_mensual']}\n"
                f"• Ventas totales: {kpi_ventas['ventas_totales']}\n"
                f"• Ticket promedio: {kpi_ventas['ticket_promedio']}\n\n"
                f"Top 3 clientes:\n"
                f"1. {top_clientes[0]['nombre']} (${top_clientes[0]['ventas']:,})\n"
                f"2. {top_clientes[1]['nombre']} (${top_clientes[1]['ventas']:,})\n"
                f"3. {top_clientes[2]['nombre']} (${top_clientes[2]['ventas']:,})",
                color="light",
                className="chat-message bot-message w-100"
            )
            redireccion = "/ventas"
        
        # Preguntas sobre Inventario
        elif any(palabra in user_input_lower for palabra in ["inventario", "stock", "productos"]):
            kpi_inventario = inventario_data.kpi_data
            alertas = inventario_data.alertas_inventario
            
            bot_response = dbc.Alert(
                f"📦 Estado del Inventario:\n\n"
                f"• Valor total: {kpi_inventario[kpi_inventario['titulo'] == 'Valor Total Inventario']['valor'].values[0]}\n"
                f"• Productos bajo mínimo: {kpi_inventario[kpi_inventario['titulo'] == 'Productos Bajo Mínimo']['valor'].values[0]}\n"
                f"• Rotación promedio: {kpi_inventario[kpi_inventario['titulo'] == 'Rotación Promedio']['valor'].values[0]}\n\n"
                f"Alertas de stock:\n- " + "\n- ".join([f"{row['Producto']} ({row['Stock_Actual']}/{row['Stock_Minimo']})" 
                                      for _, row in alertas.iterrows()]),
                color="light",
                className="chat-message bot-message w-100"
            )
            redireccion = "/inventario"
        
        # Preguntas sobre Nómina
        elif any(palabra in user_input_lower for palabra in ["nómina", "nomina", "empleados", "salarios"]):
            kpi_nomina = nomina_data.kpi_data
            dian_status = nomina_data.dian_data
            
            bot_response = dbc.Alert(
                f"👥 Datos de Nómina:\n\n"
                f"• Empleados activos: {kpi_nomina[kpi_nomina['titulo'] == 'Empleados Activos']['valor'].values[0]}\n"
                f"• Costo mensual: {kpi_nomina[kpi_nomina['titulo'] == 'Costo Nómina Mes']['valor'].values[0]}\n"
                f"• Salario promedio: {kpi_nomina[kpi_nomina['titulo'] == 'Salario Promedio']['valor'].values[0]}\n\n"
                f"Estado DIAN:\n"
                f"- Aceptada: {dian_status[dian_status['Estado'] == 'Aceptada']['Porcentaje'].values[0]}%\n"
                f"- Rechazada: {dian_status[dian_status['Estado'] == 'Rechazada']['Porcentaje'].values[0]}%",
                color="light",
                className="chat-message bot-message w-100"
            )
            redireccion = "/nomina"
        
        # Preguntas sobre el Home/Resumen
        elif any(palabra in user_input_lower for palabra in ["resumen", "general", "estado", "dashboard"]):
            kpi_home = home_data.kpi_data
            alertas = home_data.alertas_data
            
            bot_response = dbc.Alert(
                f"🏠 Resumen General:\n\n"
                f"• Ventas mes actual: {kpi_home[kpi_home['kpi'] == 'Ventas Mes Actual']['valor'].values[0]}\n"
                f"• Margen bruto: {kpi_home[kpi_home['kpi'] == 'Margen Bruto']['valor'].values[0]}\n"
                f"• Eficiencia operativa: {kpi_home[kpi_home['kpi'] == 'Eficiencia Operativa']['valor'].values[0]}\n\n"
                f"Alertas prioritarias:\n- " + "\n- ".join(alertas['mensaje']),
                color="light",
                className="chat-message bot-message w-100"
            )
            redireccion = "/home"
        
        # Respuesta por defecto
        else:
            bot_response = dbc.Alert(
                "🤖 Puedo ayudarte con información sobre:\n\n"
                "• Finanzas: flujo de caja, márgenes, ROI\n"
                "• Ventas: crecimiento, clientes, productos\n"
                "• Inventario: niveles de stock, alertas\n"
                "• Nómina: empleados, costos, estado DIAN\n\n"
                "¿Sobre qué área necesitas información?",
                color="light",
                className="chat-message bot-message w-100"
            )
        
        # Actualizar mensajes
        messages = current_messages[0]['props']['children'] if current_messages else []
        messages.extend([user_message, bot_response])
        
        new_layout = html.Div(
            className="d-flex flex-column h-100 p-3",
            children=messages
        )
        
        return [new_layout], redireccion