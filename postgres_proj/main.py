# create a new python project
# create a new venv: .venv
# activate the venv:

# mac: source .venv/bin/activate
# windows: .venv\Scripts\activate

# pip install psycopg2

# pip install psycopg2-binary

# https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries


# BEST PRACTICES FOR USING PSYCOPG2:
# TODO: always close cursor and connection
# with psycopg2.connect(DSN) as conn:
#     with conn.cursor() as curs:
#         curs.execute(SQL)
# TODO: use connection pool
# TODO: handle exceptions
# TODO: use parameterized queries

import psycopg2
from psycopg2 import pool

import logging

import datetime


logging.basicConfig(filename='db_logs.log', level=logging.INFO)


if __name__ == '__main__':
    try:
        # simple connection
        # conn = psycopg2.connect(
        #     dbname="test1db",
        #     user="omermunk",
        #     password="1234",
        #     host="localhost",
        #     port="5432"
        # )

        connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname="test1db",
            user="omermunk",
            password="1234",
            host="localhost",
            port="5432"
        )

        conn = connection_pool.getconn()


        print("Connected to the database")
        cur = conn.cursor()

        # this is how to make a query and fetch all the results
        name_to_search = input("Hi, I am so naive, enter the name you want me to search")
        # cur.execute(f"SELECT * FROM clients where cname = '{name_to_search}';")
        query = f"SELECT * FROM clients where cname = %s"
        params = (name_to_search,)
        cur.execute(query,params )
        rows = cur.fetchall()
        for row in rows:
            print(row)

        logging.info(f"{datetime.datetime.now()} query exectued: {query}, params: {params}")


        # insert new client
        # example: ('234567890', 'Yossi', 'Hanasi 59', '011-111111', datetime.date(1975, 1, 1), 1)
        cur.execute("INSERT INTO clients (cid, cname, Aaddress, phonenum, birthdate, tlicence) VALUES (%s, %s, %s, %s, %s, %s);",
                    ('234567855', 'Benny', 'Beit Hamikdash', '011-111111', '1975-01-01', 1))

        print("before commit")
        conn.commit()
        print("after commit")

        cur.close()

        connection_pool.putconn(conn)


    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database"
              "or execute the query")
        print(e)
        logging.error(f"{datetime.datetime.now()} SQL Error: {e}")
    except Exception as e:
        print(e)
        logging.error(f"{datetime.datetime.now()} Python Error: {e}")

    finally:
        if cur:
            print("Closing cursor")
            cur.close()
        if conn:
            print("Closing connection")
            conn.close()
        if connection_pool:
            connection_pool.closeall()
