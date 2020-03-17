import shutil
from os import mkdir
from subprocess import call
from tkinter import Label, filedialog, Button, Tk, Entry, Listbox
import datetime as dt
t1 = dt.datetime.now()
t1 = str(t1)
date , ttime = t1.split(' ')
time , _ = ttime.split('.')
times = []
PDFPath = ""


def selectPDF():
    PDFPath = filedialog.askopenfilename(title="Select Scramble PDF", initialdir="/home/cyberdude")
    pdfpath["text"] = PDFPath
#    print(pdfpath)

def addTimeF():
    string = f"{SrNoEnt.get()}) {minEnt.get()}:{secEnt.get()}.{msecEnt.get()}"
    timings.insert("end", string)
    times.append(f"{minEnt.get()}:{secEnt.get()}.{msecEnt.get()}")

def exportResults():
    timeList = time.split(':')
    h = int(timeList[0]) - 12
    m = int(timeList[1])
    s = int(timeList[2])
    path = f"Results for {date} - {h}-{m}-{s}"
    mkdir(path)
    with open(f"{path}/results.txt" , "a") as file:
        file.write(f"Date: {date}\n")
        file.write(f"Time: {h}:{m}:{s}\n")
        t3 = 0
        for x in times:
            t3 += 1
            file.write(f"Attempt {t3}: {x}\n")
        if(PDFPath):
            shutil.copy(PDFPath , path)
            

# Basic Stuff
window = Tk()
window.title("Cube Manager")
title = Label(window, text="Cube Manager")
title.grid(row=0, column=0, columnspan=4)


# TIME ENTERING CODE
SrNo = Label(window, text="Attempt Number")
minlab = Label(window, text="min")
seclab = Label(window, text="sec")
mseclab = Label(window, text="msec")
SrNoEnt = Entry(window)
minEnt = Entry(window)
secEnt = Entry(window)
msecEnt = Entry(window)
timings = Listbox(window)
addTime = Button(window, text="Add time", command=addTimeF)
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

# AVERAGES
'''
ao5Lab = Label(window, text="Average of 5: ")
ao5 = Label(window, text="")
ao5Lab.grid(column=0, row=7, columnspan=2)
ao5.grid(column=2, row=7, columnspan=2)
'''
# File Selection
selectScramPDF = Button(window, text="Select Scramble File ", command=selectPDF)
pdfpath = Label(text="")
selectScramPDF.grid(column=0, row=8, columnspan=1)
pdfpath.grid(column=2, row=8, columnspan=3)

#Export
exportButton = Button(window,text="Export Results" , command=exportResults)
exportButton.grid(row = 9 , column=1, columnspan=3)
window.mainloop()
