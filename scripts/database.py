import sqlite3
from sqlite3 import Error

def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_microclimate_data(conn, data):
    sql = """INSERT INTO microclimate_data(
                 id, lat, lon, is_green_space,
                 temperature, humidity, air_quality_index)
             VALUES(?, ?, ?, ?, ?, ?, ?)"""
    cursor = conn.cursor()
    cursor.executemany(sql, data)
    conn.commit()


def main():
    database_file = "data/microclimate_data.db"

    create_table_sql = """CREATE TABLE IF NOT EXISTS microclimate_data (
                              id INTEGER PRIMARY KEY,
                              lat REAL NOT NULL,
                              lon REAL NOT NULL,
                              is_green_space INTEGER NOT NULL,
                              temperature REAL,
                              humidity REAL,
                              air_quality_index REAL
                          );"""

    conn = create_connection(database_file)

    if conn is not None:
        create_table(conn, create_table_sql)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == "__main__":
    main()
