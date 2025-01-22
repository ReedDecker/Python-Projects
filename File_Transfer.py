import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import sys
import time
from datetime import datetime, timedelta

class ParentWindow(Frame):
    # Creates function to select source directory.
    def sourceDir(self):
                selectsourceDir = tkinter.filedialog.askdirectory()
                self.source_dir.delete(0, END)
                self.source_dir.insert(0, selectsourceDir)
    # Creates function to select destination directory.
    def destDir(self):

                selectDestDir = tkinter.filedialog.askdirectory()
                self.destination_dir.delete(0, END)
                self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
                # Gets source directory
                source = self.source_dir.get()
                # Gets destination directory
                destination = self.destination_dir.get()
                # Gets a list of files in the source directory
                source_files = os.listdir(source)
                # Runs through each file in the source directory

                for i in source_files:

                    # moves each file from the source to the destination
                    shutil.move(source + "/" + i, destination)

                    path = '/Users/reeddecker/Desktop/Customer_Source'

                    # Both the variables would contain time
                    # elapsed since EPOCH in float
                    ti_c = os.path.getctime(path)
                    ti_m = os.path.getmtime(path)

                    # Converting the time in seconds to a timestamp
                    c_ti = time.ctime(ti_c)
                    m_ti = time.ctime(ti_m)

                    print(f"The file located at the path {path} \
                    was created at {c_ti} and was "
                    f"last modified at {m_ti}")


    def exit_program(self):
        root.destroy()
                
    def __init__(self, master):
            Frame.__init__ (self)
            self.master.title("File Transfer")
            self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
            self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
            self.source_dir = Entry(width=75)
            self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))
            self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
            self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
            self.destination_dir = Entry(width=75)
            self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
            self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
            self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
            self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
            self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

