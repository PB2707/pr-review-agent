import sqlite3
import os

API_KEY = "demo-secret-key"


def execute_query(query):
    pass


def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    result = execute_query(query)

    return result