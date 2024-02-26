import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)


def add_transaction(conn, transaction):
    sql = """ INSERT INTO transactions(type, amount, date, category_id, description)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return cur.lastrowid


def view_statement(conn):
    sql = """ select t.type, t.amount, t.date, c.category, t.description from transactions t join categories c on t.category_id = c.id; """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def view_categories(conn):
    sql = """ select c.id, c.category from categories c; """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def filter_statement(conn, filter):
    sql = """ select t.type, t.amount, t.date, t.description from transactions t where t.category_id = ?; """
    cur = conn.cursor()
    cur.execute(sql, filter)
    return cur.fetchall()


def set_budget(conn, transaction):
    sql = """ INSERT INTO budgets(category_id, amount)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return cur.lastrowid


def budget_viewer(conn):
    sql = """ select c.category, b.amount from budgets b join categories c on b.category_id = c.id; """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def generate_report(conn):
    sql = """select c.category, sum(t.amount), b.amount from transactions t  
            join categories c
            on t.category_id = c.id
            join budgets b
            on c.id = b.category_id
            where strftime("%m", date()) == strftime("%m", t.date)
            group by t.category_id;"""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()
