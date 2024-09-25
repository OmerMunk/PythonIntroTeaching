# create a new python project
# create a new venv: .venv
# activate the venv:

# mac: source .venv/bin/activate
# windows: .venv\Scripts\activate

# pip install psycopg2

# pip install psycopg2-binary

import psycopg2


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(
            dbname="test1db",
            user="omermunk",
            password="1234",
            host="localhost",
            port="5432"
        )
        print("Connected to the database")
        cur = conn.cursor()
        cur.execute("SELECT * FROM cars;")


        print(type(cur))
        rows = cur.fetchall()
        for row in rows:
            print(row)


    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    finally:
        if cur:
            print("Closing cursor")
            cur.close()
        if conn:
            print("Closing connection")
            conn.close()
