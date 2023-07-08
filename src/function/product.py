import psycopg2
from src.sql.connection import connection
from tkinter import Listbox

name_db = connection.get_data().get('name_db')
user_db = connection.get_data().get('user_db')
pass_db = connection.get_data().get('pass_db')
host_db = connection.get_data().get('host_db')
port_db = connection.get_data().get('port_db')


def save_new_product(name, category, price):
    conn = psycopg2.connect(dbname=f'{name_db}',
                            user=f'{user_db}',
                            password=f'{pass_db}',
                            host=f'{host_db}',
                            port=f'{port_db}', )

    # The cursor object allows queries to be made.
    cursor = conn.cursor()

    query = '''INSERT INTO product (name, category,price) VALUES (%s,%s,%s)'''
    cursor.execute(query, (name, category, price))

    conn.commit()
    conn.close()


def get_products():
    conn = psycopg2.connect(dbname=f'{name_db}',
                            user=f'{user_db}',
                            password=f'{pass_db}',
                            host=f'{host_db}',
                            port=f'{port_db}', )

    cursor = conn.cursor()

    query = '''SELECT name,category,price FROM product'''

    cursor.execute(query)

    data = cursor.fetchall()

    return data


def get_product_by_id(search_id):
    conn = psycopg2.connect(dbname=f'{name_db}',
                            user=f'{user_db}',
                            password=f'{pass_db}',
                            host=f'{host_db}',
                            port=f'{port_db}', )

    cursor = conn.cursor()

    query = '''SELECT * FROM product WHERE id=%s'''

    cursor.execute(query, (search_id,))


    # Obtiene el primer dato
    data = cursor.fetchone()

    conn.commit()

    conn.close()

    return data

