from postgres_proj.db import get_db_connection
import psycopg2

def normalize_db():
    source_conn = get_db_connection()
    target_conn = psycopg2.connect(
        dbname="normal_db",
        user="omermunk",
        password="1234",
        host="localhost",
        port="5432"
    )

    try :
        query1 = """
            CREATE TABLE customers (
                    customer_id SERIAL PRIMARY KEY,
                    customer_name VARCHAR(100),
                    address VARCHAR(255),
                    city VARCHAR(100)
            )
        """
        query2 = """
            CREATE TABLE phone_numbers (
                phone_id SERIAL PRIMARY KEY,
                customer_id INT REFERENCES customers(customer_id),
                phone_number VARCHAR(10)
            )
        """

        query3 = """
            CREATE TABLE products (
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(100),
                supplier_id INT REFERENCES suppliers(supplier_id),
                price NUMERIC(10, 2)
            )
        """


        query4 = """
            CREATE TABLE categories (
                category_id SERIAL PRIMARY KEY,
                category_name VARCHAR(100)
            )
        """


        query5 = """
            CREATE TABLE products_categories (
                product_id INT REFERENCES products(product_id),
                category_id INT REFERENCES categories(category_id),
                primary key (product_id, category_id)
            )
        """


        query6 = """
            CREATE TABLE suppliers (
                supplier_id SERIAL PRIMARY KEY,
                supplier_name VARCHAR(100)
            )
        """


        query7 = """
            CREATE TABLE orders (
                order_id SERIAL PRIMARY KEY,
                customer_id INT references customers(customer_id),
                order_date DATE
            )
        """

        query8 = """
            CREATE TABLE order_products (
                order_id INT REFERENCES orders(order_id),
                product_id INT REFERENCES products(product_id),
                quantity INT,
                primary key (order_id, product_id)
            )
        """

        # execute the queries
        cur = target_conn.cursor()
        cur.executemany([query1, query2, query3, query4, query5, query6, query7, query8])
        target_conn.commit()

        s_cur = source_conn.cursor()
        s_cur.execute("SELECT * FROM customers")
        while True:
            customer_row = s_cur.fetchone()
            if customer_row is None:
                break

            customer_name = customer_row[1]
            address = customer_row[3]
            city = customer_row[4]
            phone_numbers = customer_row[2].split(",")

            cur.execute("INSERT INTO customers (customer_name, address, city)"
                        " VALUES (%s, %s, %s) RETURNING customer_id",
                        (customer_name, address, city))
            customer_id = cur.fetchone()[0]

            for phone_number in phone_numbers:
                cur.execute("INSERT INTO phone_numbers (customer_id, phone_number)"
                            " VALUES (%s, %s)", (customer_id, phone_number))





    except Exception as e:
        pass
    finally:
        pass