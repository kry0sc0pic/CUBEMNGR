# All module imports
import shutil
from os import mkdir
from subprocess import call
from tkinter import Label, filedialog, Button, Tk, Entry, Listbox
import datetime as dt

# Get the date and time
t1 = dt.datetime.now()
t1 = str(t1)
date, ttime = t1.split(' ')
time, _ = ttime.split('.')
times = []


FILEPATH = ""  # Intialize a variable to hold the path to the Scramble file.


# Function to ask user for the scramble file path and display it on the UI
def selectFile():
    FILEPATH = filedialog.askopenfilename(
        title="Select Scramble PDF", initialdir="")  # Add your preferred starting directory in the initialdir field
    filepath["text"] = FILEPATH

# Function to add a time entry to the listbox on the UI


def addTimeToList():
    string = f"{SrNoEnt.get()}) {minEnt.get()}:{secEnt.get()}.{msecEnt.get()}"
    timings.insert("end", string)
    times.append(f"{minEnt.get()}:{secEnt.get()}.{msecEnt.get()}")

# Function to export the solve times and other details to a .txt file inside a new folder


def exportResults():
    timeList = time.split(':')
    h = int(timeList[0]) - 12
    m = int(timeList[1])
    s = int(timeList[2])
    path = f"Results for {date} - {h}-{m}-{s}"
    mkdir(path)
    with open(f"{path}/results.txt", "a") as file:
        file.write(f"Date: {date}\n")
        file.write(f"Time: {h}:{m}:{s}\n")
        t3 = 0
        for x in times:
            t3 += 1
            file.write(f"Attempt {t3}: {x}\n")
        shutil.copy(FILEPATH, path)


# Create the Application window and create a title label
window = Tk()
window.title("Cube Manager")
title = Label(window, text="Cube Manager")
title.grid(row=0, column=0, columnspan=4)


# Code to create buttons and entry boxes to enter the solve times
SrNo = Label(window, text="Attempt Number")
minlab = Label(window, text="min")
seclab = Label(window, text="sec")
mseclab = Label(window, text="msec")
SrNoEnt = Entry(window)
minEnt = Entry(window)
secEnt = Entry(window)
msecEnt = Entry(window)
timings = Listbox(window)
addTime = Button(window, text="Add time", command=addTimeToList)
SrNo.grid(column=0, row=3)
minlab.grid(column=1, row=3)
seclab.grid(column=2, row=3)
mseclab.grid(column=3, row=3)
SrNoEnt.grid(column=0, row=4)
minEnt.grid(column=1, row=4)
secEnt.grid(column=2, row=4)
msecEnt.grid(column=3, row=4)
timings.grid(column=0, row=5, columnspan=4)
addTime.grid(column=0, row=6, columnspan=4)

# Create Button and Label to select scramble file
selectScramPDF = Button(
    window, text="Select Scramble File ", command=selectFile)
filepath = Label(text="")
selectScramPDF.grid(column=0, row=8, columnspan=1)
filepath.grid(column=2, row=8, columnspan=3)

# Create button to export the results
exportButton = Button(window, text="Export Results", command=exportResults)
exportButton.grid(row=9, column=1, columnspan=3)
window.mainloop()
