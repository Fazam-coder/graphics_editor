import sqlite3

from const import NAME_DB, ID, IS_DELETED, LOG, ACTIONS, ACTION

con = sqlite3.connect(NAME_DB)
cur = con.cursor()


def add_object(table_name, id, object, sx, sy, ex, ey, color, thickness):
    update_is_deleted(id)
    delete_is_deleted()
    red = color.red()
    green = color.green()
    blue = color.blue()
    query = f"""INSERT INTO {table_name} 
    VALUES ({id}, {object}, {sx}, {sy}, {ex}, {ey}, {red}, {green}, {blue}, {thickness}, 'False')"""
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
    query = f'UPDATE {LOG} SET {IS_DELETED} = True WHERE {ID} >= {id}'
    cur.execute(query)
    con.commit()


def delete_is_deleted():
    query = f'DELETE FROM {LOG} WHERE {IS_DELETED} = True'
    cur.execute(query)
    con.commit()


def select_all():
    query = f"SELECT * FROM {LOG}"
    return cur.execute(query).fetchall()


def select_action(id):
    query = f"SELECT {ACTION} FROM {ACTIONS} WHERE {ID} = {id}"
    return cur.execute(query).fetchone()[0]