import os
import re
import sqlite3
from tkinter import filedialog, Tk
import eyed3
from dbinit import *

# Create the db file
# TODO: Consider making a function to print to stderr if needed

with MusicDBInit(r"music_database.db").conn as conn:
    master = conn  # ??????


# Get the master music folder from the user
def getmasterfolder():
    # Hide the main Tk window that usually pops up
    Tk().withdraw()
    masterpath = filedialog.askdirectory(title="Select the root music folder...")

    return masterpath


# Get the subfolders in the root folder
def getsubfolders(masterpath):
    # with os.listdir(masterpath) as directories:
    #     # Check to see if there's any files amongst the folders
    #     folders = []
    #     for item in directories:
    #         print(item)
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
    subfolders = []
    for (dirpath, dirnames, filenames) in os.walk(root)
def main():
    rootfolder = getmasterfolder()
    getsubfolders(rootfolder)


if __name__ == "__main__":
    main()
