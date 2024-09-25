import psycopg2
from ..db import get_db_connection, release_db_connection
from ..services.logger import log, log_error


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
        log(f"executing query: {query}, params: {params}")
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        users = cur.fetchall()
        return True, users
    except psycopg2.Error as e:
        log_error(f'Error: {e}')
        print(e)
        return False
    finally:
        if cur:
            cur.close()
        release_db_connection(conn)


def check_balance(sender_id, amount, cur):
    query = """
    SELECT balance FROM users WHERE id = %s
    """
    params = (sender_id,)
    cur.execute(query, params)
    sender_balance = cur.fetchone()[0]
    if sender_balance < amount:
        raise Exception(f"""not enough balance to pay amount. amount:
        {amount}, balance: {sender_balance}""")

def transfer_money(amount, cur, receiver_id, sender_id):
    update_sender_query = """
        UPDATE users SET balance = balance - %s WHERE id = %s
        """
    update_receiver_query = """
        UPDATE users SET balance = balance + %s WHERE id = %s
        """
    cur.execute(update_sender_query, (amount, sender_id,))
    cur.execute(update_receiver_query, (amount, receiver_id,))
    insert_payment_query = """
        INSERT INTO payments (sender_id, receiver_id, amount)
        VALUES (%s, %s, %s)
        """
    params = (sender_id, receiver_id, amount,)
    cur.execute(insert_payment_query, params)


def process_payment(sender_id, receiver_id, amount):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        check_balance(sender_id, amount, cur)

        transfer_money(amount, cur, receiver_id, sender_id)

        conn.commit()
        return True

    except psycopg2.Error as e:
        conn.rollback()
        return False
    finally:
        if cur:
            cur.close()
        release_db_connection(conn)


