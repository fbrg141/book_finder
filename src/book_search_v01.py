from tkinter import * from tkinter import scrolledtext
from tkinter import messagebox
import xlsxwriter
import os
import xlrd
import pickle

cwd = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.split(cwd)[0]
logRsrc = os.path.join(par_dir, "resource/log.txt")
mapRsrc = os.path.join(par_dir, "resource/map.pickle")
invRsrc = os.path.join(par_dir, "resource/inv__db.xlsx")


def loadMap():
    with open(mapRsrc, "rb") as handle:
        map = pickle.load(handle)
        print(map)

def updateMap():
    map ={}
    for sh in  xlrd.open_workbook(invRsrc).sheets():
        for row in range(sh.nrows):
            myCell1= sh.cell(row, 0)
            myCell2= sh.cell(row, 1)
            inv_num = myCell1.value
            name_str = myCell2.value
            map[inv_num] = name_str
    with open(mapRsrc, "wb") as handle:
        pickle.dump(map, handle, protocol=5)

def startCheck():
    updTime = str(os.stat(invRsrc)[8])
    with open(logRsrc, 'r+') as log:
        lines = log.read().splitlines()
        if lines ==  []:
            log.write('This file is used for storing log data of' \
                      'inv__db.xlsx file.\n')
            log.write(updTime)
            updateMap()
        elif lines[-1] != updTime:
            log.write("\n")
            log.write(updTime)
            updateMap()

def find(value, map):
    rValue = ""
    print(map)
    for str1, str2 in map.items():
        if str(str2).find(value) != -1:
            rValue += str(int(str1)) + "   |   " + str2 + "\n"
    if rValue == "":
        rValue = "Knjiga nije pronadjena."
    return rValue

def main():

    startCheck()
    with open(mapRsrc, "rb") as handle:
        map =pickle.load(handle)
    def clicked():
        value  = ent.get()
        if len(value) < 4:
            messagebox.showwarning("Greska", 'Unesite najmanje 4' \
                               'karaktera za pretragu')
            ent.delete(0, END)
        else:
            if txt.get(1.0, END) != "":
                txt.delete(1.0, END)
            outString = find(value, map)
            txt.insert(END, outString)


    window = Tk()
    window.title("Pretraga")
    window.geometry('750x500')
    btn = Button(window, text = "Pretraga", command = clicked)
    btn.grid(column=1, row=0)
    txt = Text(window)
    txt.grid(column=0, row=2)
    ent = Entry(window, width=40)
    ent.grid(column=0, row=0)
    window.mainloop()

main()

