import psycopg2
from ..db import get_db_connection, release_db_connection

def insert_new_user(data):
    conn = get_db_connection()
    try:
        name = data.get("name")
        email = data.get("email")
        cur = conn.cursor()

        query = """
        INSERT INTO users (name, email)
        VALUES (%s, %s)
        """

        params = (name, email,)

        cur.execute(query, params)
        conn.commit()
        cur.close()
        return True
    except psycopg2.Error as e:
        print(e)
        return False
    finally:
        release_db_connection(conn)



def get_all_users():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query = """
        SELECT * FROM users
        """
        cur.execute(query)
        users = cur.fetchall()
        return True, users
    except psycopg2.Error as e:
        print(e)
        return False
    finally:
        release_db_connection(conn)