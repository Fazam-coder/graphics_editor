import sqlite3

from const import NAME_DB, ID, IS_DELETED, LOG

con = sqlite3.connect(NAME_DB)
cur = con.cursor()


def add_object(table_name, id, object):
    query = f"INSERT INTO {table_name} VALUES ({id}, {object}, 'False')"
    cur.execute(query)
    con.commit()


def select_id(table_name, field, object):
    query = f"""SELECT {ID} FROM {table_name}
                WHERE {field} = ?"""
    return cur.execute(query, (object, )).fetchone()[0]


def delete_all(table_name):
    query = f'DELETE FROM {table_name}'
    cur.execute(query)
    con.commit()


def update_is_deleted(id):
    query = f'UPDATE {LOG} SET {IS_DELETED} = True WHERE {ID} = {id}'
    cur.execute(query)
    con.commit()