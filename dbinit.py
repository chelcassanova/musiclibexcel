import re
from random import randint
import sqlite3
import eyed3

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

    @staticmethod
    def create_table(conn):

        """
        Create a table using the create_table_sql statement
        :param conn: The Connection object that represents the database
        :return:
        """
        try:
            create_table_sql = """CREATE TABLE IF NOT EXISTS master (
                             id integer,
                             title text NOT NULL,
                             artist text NOT NULL,
                             album text NOT NULL,
                             playlist text DEFAULT \'Empty\');"""
            curse = conn.cursor()
            curse.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    @staticmethod
    def insert_song(conn, insert_sql, filepath):
        """
        Insert a song into the table
        :param conn: Database connection
        :param song: Song info
        :return:
        """

        # NOTE: The question marks beside VALUES are arguments
        sql = """INSERT INTO master (id, title, artist, album, playlist)
                VALUES(?,?,?,?,?)"""

        tag = eyed3.load(filepath)
        #playlistname = re.search()
        curse = conn.cursor()
        if tag is not None and tag.tag.title is not None and tag.tag.artist is not None and tag.tag.album is not None:
            curse.execute(insert_sql, (randint(1, 10000).__str__(), tag.tag.title, tag.tag.artist, tag.tag.album, "Empty"))
            conn.commit()

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
