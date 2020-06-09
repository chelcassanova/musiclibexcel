import os
import re
from random import randint
import sqlite3
from tkinter import filedialog, Tk
import eyed3
from dbinit import *

# Create the db file
# TODO: Consider making a function to print to stderr if needed

with MusicDBInit(r"music_database.db").conn as conn:
    MusicDBInit.create_table(conn)
    master = conn  # ??????


# Get the master music folder from the user
def getmasterfolder():
    # Hide the main Tk window that usually pops up
    Tk().withdraw()
    masterpath = filedialog.askdirectory(title="Select the root music folder...")

    return masterpath


# Get the subfolders in the root folder
def getsubfolders(masterpath):

    try:
        directories = os.listdir(masterpath)
        folders = []

        for item in directories:
            # Use regex to check for files, since we only wanna keep folders
            # Redundant on the surface since my own root folder only has subfolders
            extension = re.search("\.w+", item)

            if extension is None:  # extension is None if there was no file extension, so it was a folder
                folders.append(item)
                print(type(item))

        return folders
    except FileNotFoundError as e:
        print(e)  # TODO: make the message better


def insertsongs(rootfolder):
    for (dirpath, dirname, filelist) in os.walk(rootfolder):
        for file in filelist:
            extension = re.search("\.m+", file)

            if extension is not None:  # These are the mp3s
                # Load up the tag info with eyed3
                filepath = dirpath + "\\" + file
                print(filepath)
                tag = eyed3.load(filepath)
                if tag is not None and tag.tag is not None and tag.tag.title is not None:
                    insert = """INSERT INTO master (id, title, artist, playlist)
                                VALUES(?,?,?,?);"""
                    MusicDBInit.insert_song(master, insert, filepath)


def main():
    rootfolder = getmasterfolder()
    insertsongs(rootfolder)
    master.close()


if __name__ == "__main__":
    main()
