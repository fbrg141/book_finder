import xlsxwriter
import os
import xlrd
import pandas
import pickle
import string
map={}

with open("log.txt", 'r+') as log:
    print(log.readline().strip())
    date = str(os.stat("inv__db.xlsx")[8]).strip()
    print(date)
    if log.readline().strip() != date:
        print("Updating database.")
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
        log.truncate(0)
        log.write(str(os.stat("inv__db.xlsx")[8]))
#x=input()
#if len(x) < 3:
#    print("Alo pope, sta radis to")
#for str1, str2 in map.items():
#    if str(str2).find(x)  != -1:
#        print(int(str1), str2)


# cuvanje mape
# gui
# podeli polja za pisca nazi i godinu
