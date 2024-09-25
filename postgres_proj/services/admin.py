import psycopg2
from ..db import get_db_connection, release_db_connection
from ..services.logger import log, log_error


def create_users_table(request_info):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        # query = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
        query = ("""CREATE TABLE users 
                 (id SERIAL PRIMARY KEY, 
                 name VARCHAR(255) NOT NULL , 
                 email VARCHAR(255) UNIQUE )
                 """)
        log(f"{request_info}. executing query: {query}")
        cur.execute(query)
        conn.commit()
        cur.close()
        return True
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f"Error is : {e}")
        return False
    finally:
        release_db_connection(conn)


def create_payments_table(request_info):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        # query = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
        query = ("""CREATE TABLE payments 
                 (id SERIAL PRIMARY KEY, 
                 sender_id INT REFERENCES users(id), 
                 receiver_id INT REFERENCES users(id), 
                 amount NUMERIC(10, 2) NOT NULL,
                 payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                 """)
        log(f"{request_info}. executing query: {query}")
        cur.execute(query)
        conn.commit()
        cur.close()
        return True
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f"Error is : {e}")
        return False
    finally:
        release_db_connection(conn)



def alter_users_table(request_info):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query = """
        ALTER TABLE users ADD COLUMN
        balance NUMERIC(10, 2) DEFAULT 0.00
        """
        cur.execute(query)
        conn.commit()
        return True
    except psycopg2.Error as e:
        print(e)
        return False
    finally:
        if cur:
            cur.close()
        release_db_connection(conn)
