import json
import logging
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from dotenv import load_dotenv

from chatbot.llm import human_query_to_sql, build_answer
from chatbot.database import query



load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BACKEND_SERVER = os.getenv("SERVER_URL")
app = FastAPI(servers=[{"url": BACKEND_SERVER}])

class PostHumanQueryPayload(BaseModel):
    human_query: str

class PostHumanQueryResponse(BaseModel):
    result: list

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(servers=[{"url": BACKEND_SERVER}])

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O puedes restringirlo a ["http://localhost:3000"] si tienes frontend ahí
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/human_query",
    name="Human Query",
    operation_id="post_human_query",
    description="Gets a natural language query, internally transforms it to a SQL query, queries the database, and returns the result.",
)
async def human_query(payload: PostHumanQueryPayload):
    sql_query = await human_query_to_sql(payload.human_query)

    if not sql_query:
        return {"error": "Falló la generación de la consulta SQL"}

    result_dict = json.loads(sql_query)
    result = await query(result_dict["sql_query"])

    answer = await build_answer(result, payload.human_query)
    if not answer:
        return {"error": "Falló la generación de la respuesta"}

    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

