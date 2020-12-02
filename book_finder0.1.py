import xlsxwriter
import os
import xlrd
import pickle
map = {}
def loadMap():
    with open("map.pickle", "rb") as handle:
        map = pickle.load(handle)
        print(map)
        #problem je jer pravi mapu unutar  fje pa van fje stampa praznu mapu

def updateMap():
    print("Updating database...")
    for sh in  xlrd.open_workbook("inv__db.xlsx").sheets():
        for row in range(sh.nrows):
            myCell1= sh.cell(row, 0)
            myCell2= sh.cell(row, 1)
            inv_num = myCell1.value
            name_str = myCell2.value
            map[inv_num] = name_str
    with open("map.pickle", "wb") as handle:
        pickle.dump(map, handle, protocol=5)
    print("Done!")
# resi problem da sam kreira log.txt ako ga nema
def startCheck():
    updTime = str(os.stat("inv__db.xlsx")[8])
    with open("log.txt", 'r+') as log:
        lines = log.read().splitlines()
        if lines ==  []:
            log.write('This file is used for storing log data of' \
                      'inv__db.xlsx file.\n')
            log.write(updTime)
            log.close()
            updateMap()
            print(map)
        elif lines[-1] != updTime:
            print("Promena!")
            log.write("\n")
            log.write(updTime)
            log.close()
            updateMap()
            print(map)
        else:
            with open("map.pickle", "rb") as handle:
                map = pickle.load(handle)
            print(map)
            print("Database is not updated!")
def main():
    startCheck()


if __name__ ==  "__main__":
    main()
