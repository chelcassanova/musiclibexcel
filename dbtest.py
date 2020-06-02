import sqlite3

# Python's SQLite needs to first have a connection that represents the database
def create_connection(db_filename):
    conn = None

    try:
        conn = sqlite3.connect(db_filename)
        print("file made")
    except sqlite3.Error as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_connection("music_database.db")