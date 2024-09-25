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

def build_query(find_by=None, value=None, count=None):
    query = """
    SELECT * FROM users
    """
    # columns = {
    #     "id": "id",
    #     "name": "name",
    #     "email": "email",
    # }
    params = tuple()
    if find_by and value:
        encoded_find_by = find_by.split(" ")[0].strip()
        query += f" where {encoded_find_by} = %s"
        # query += f" where {columns[find_by]} = %s"
        params = (value,)
    if count:
        query += f" LIMIT %s"
        params = (*params, count,)
    return query, params


def get_all_users(find_by=None, value=None, count=None):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query, params = build_query(find_by, value, count)
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        users = cur.fetchall()
        return True, users
    except psycopg2.Error as e:
        print(e)
        return False
    finally:
        release_db_connection(conn)