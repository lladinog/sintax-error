import os
import logging
from typing import Any
from database import get_schema
import google.generativeai as gemini

gemini.api_key = os.getenv("OPEN_AI_API_KEY")
logger = logging.getLogger(__name__)

async def human_query_to_sql(human_query: str) -> str:
    database_schema = get_schema()

    system_message = f"""
    Given the following schema, write a SQL query that retrieves the requested information. 
    Return the SQL query inside a JSON structure with the key "sql_query".
    <example>{{
        "sql_query": "SELECT * FROM users WHERE age > 18;",
        "original_query": "Show me all users older than 18 years old."
    }}</example>
    <schema>
    {database_schema}
    </schema>
    """

    response = gemini.chat.completions.create(
        model="gemini-2.0-flash",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": human_query},
        ],
    )

    return response.choices[0].message.content

async def build_answer(result: list[dict[str, Any]], human_query: str) -> str | None:
    system_message = f"""
    Given a user's question and the SQL rows response from the database, write a response to the user's question.
    <user_question> 
    {human_query}
    </user_question>
    <sql_response>
    {result}
    </sql_response>
    """

    response = gemini.chat.completions.create(
        model="gemini-2.0-flash",
        messages=[
            {"role": "system", "content": system_message},
        ],
    )

    return response.choices[0].message.content
