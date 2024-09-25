import psycopg2
from ..db import get_db_connection, release_db_connection


def create_users_table():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        # query = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
        query = ("""CREATE TABLE users 
                 (id SERIAL PRIMARY KEY, 
                 name VARCHAR(255) NOT NULL , 
                 email VARCHAR(255) UNIQUE )
                 """)
        cur.execute(query)
        conn.commit()
        cur.close()
        return True
    except psycopg2.Error as e:
        print(f"Error is : {e}")
        return False
    finally:
        release_db_connection(conn)
