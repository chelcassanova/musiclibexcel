import sqlite3

# Python's SQLite needs to first have a connection that represents the database
class MusicDBInit:
    def __init__(self, db_filename):
        """
        Create a database connection
        :param db_filename: Database name
        :return:
        """
        conn = None
        try:
            self.conn = sqlite3.connect(db_filename)
            # return conn
        except sqlite3.Error as error:
            print(error)

    def create_table(self, conn, create_table_sql):

        """
        Create a table using the create_table_sql statement
        :param conn: The Connection object that represents the database
        :param create_table_sql: A CREATE TABLE statement
        :return:
        """
        try:
            curse = conn.cursor()
            curse.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def insert_song(self, conn, song):
        """
        Insert a song into the table
        :param conn: Database connection
        :param song: Song info
        :return:
        """

        # NOTE: The question marks beside VALUES are arguments
        sql = """INSERT INTO master (id, title, artist, playlist)
                VALUES(?,?,?,?)"""

        curse = conn.cursor()
        curse.execute(sql, song)
        return curse.lastrowid

#
# def main():
#     conn = MusicDBInit(r"music_database.db")
#     sql_create_master_db = """CREATE TABLE IF NOT EXISTS master (
#                             id integer PRIMARY KEY,
#                             title text NOT NULL,
#                             artist text NOT NULL,
#                             playlist text DEFAULT \'Empty\');"""
#
#     if conn:
#         create_table(conn, sql_create_master_db)
#     else:
#         print("Error: Couldn't create the database")
