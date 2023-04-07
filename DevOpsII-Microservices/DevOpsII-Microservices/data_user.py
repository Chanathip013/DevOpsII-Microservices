import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_user.db")

def item():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT item, name, category
        FROM item 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'item': row[0],
            'name': row[1],
            'category': row[2]
            }
        data.append(record)
    
    conn.close()
    return data

def find_item(item):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT item, name, category
        FROM item
        WHERE item=?
    """
    val = (item,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'item': rows[0],
        'name': rows[1],
        'category': rows[2]
        }
    data.append(record)
    
    conn.close()
    return data

def item_add(item,name,category):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO item(item,name,category)
        VALUES(?,?,?)
    """
    val = (item,name,category)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"


def remove_item(item):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE from item
        WHERE item=?
    """
    val = (item,)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Item removed successfully"


def item_update(item,name,category):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE item(item,name,category)
        SET name=?, category=?
        WHERE item=?
    """
    val = (item,name,category)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Updated successfully"