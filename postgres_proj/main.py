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

        # this is how to make a query and fetch all the results
        name_to_search = input("Hi, I am so naive, enter the name you want me to search")
        cur.execute(f"SELECT * FROM clients where cname = '{name_to_search}';")
        rows = cur.fetchall()
        for row in rows:
            print(row)


    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database"
              "or execute the query")
        print(e)
    except Exception as e:
        print(e)
    finally:
        if cur:
            print("Closing cursor")
            cur.close()
        if conn:
            print("Closing connection")
            conn.close()
