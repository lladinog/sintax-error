import logging
from typing import List, Dict
from sqlalchemy import inspect, text
from sqlalchemy.exc import SQLAlchemyError

from db_connection import get_engine


logger = logging.getLogger(__name__)
engine = get_engine()  # Usamos el motor de conexión centralizado

def get_schema() -> str:
    inspector = inspect(engine)
    schema_str = ""

    try:
        tables = inspector.get_table_names()
        for table in tables:
            schema_str += f"Table: {table}\n"
            columns = inspector.get_columns(table)
            for col in columns:
                col_name = col['name']
                col_type = str(col['type'])
                schema_str += f"  - {col_name}: {col_type}\n"
            schema_str += "\n"
    except SQLAlchemyError as e:
        logger.error(f"Error al inspeccionar la base de datos: {e}")
        schema_str = "No se pudo obtener el esquema de la base de datos."

    return schema_str

async def query(sql_query: str) -> List[Dict]:
    logger.info(f"Ejecutando SQL: {sql_query}")
    try:
        with engine.connect() as connection:
            result_proxy = connection.execute(text(sql_query))
            return [dict(row) for row in result_proxy]
    except SQLAlchemyError as e:
        logger.error(f"Error ejecutando la consulta: {e}")
        return [{"error": str(e)}]
