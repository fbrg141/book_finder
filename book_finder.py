import xlsxwriter
import os
import xlrd
import pandas
map={}

for sh in  xlrd.open_workbook("inv__db.xlsx").sheets():
    for row in range(sh.nrows):
        myCell1= sh.cell(row, 0)
        myCell2= sh.cell(row, 1)
        inv_num = myCell1.value
        name_str = myCell2.value
        map[inv_num] = name_str

x=input()
if len(x) < 3:
    print("Alo pope, sta radis to")
for str1, str2 in map.items():
    if str(str2).find(x)  != -1:
        print(int(str1), str2)


# cuvanje mape
# gui
# podeli polja za pisca nazi i godinu
