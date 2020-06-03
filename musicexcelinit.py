import os
from openpyxl import *
from tkinter import filedialog, Tk

class MusicExcelInit:
    musicpath = ""
    def __init__(self, file):
        # Load the file and print the sheet names
        self.file = load_workbook('musiclibrary.xlsx')
        self.folders = []
        self.sheets = self.file.get_sheet_names()

        # Delete the current sheets in the workbook (except for one, which will be removed at the end)
        for x in range(1, len(self.sheets)):
            sheet = self.file.get_sheet_by_name(self.sheets[x])
            self.file.remove_sheet(sheet)

    def getdirs(self):
        """Ask for the relevant library while hiding the Tk main window"""
        Tk().withdraw()
        self.musicpath = filedialog.askdirectory(title="Choose the music library...")

        # Try to make a list of the items in the chosen directory and throw an
        # exception if the user cancels
        try:
            self.direc = (os.listdir(self.musicpath))
        except FileNotFoundError:
            print("No directory was selected, please try again.")
            quit()

        # Create a list for folders in the directory and check the directory to compare files and folders
        for item in self.direc:
            extension = item[len(item) - 4:len(item)]
            if extension[0] != '.':
                self.folders.append(item)

    def createsheets(self):
        # Create the sheets for the respective folders
        for folder in self.folders:
            self.file.create_sheet(folder)

        # Delete the first sheet in the workbook since it'll either be a default sheet or a duplicate sheet
        sheets = self.file.get_sheet_names()
        first_sheet = self.file.get_sheet_by_name(sheets[0])
        self.file.remove_sheet(first_sheet)
        # print(self.file.get_sheet_names())
        self.file.save('musiclibrary.xlsx')

    def givedirec(self):
        """Return the directory of the music library"""
        # Tk().withdraw()
        # self.musicpath = filedialog.askdirectory(title="Choose the music library...")
        return self.musicpath

    def __str__(self):
        return "python is very neat"
