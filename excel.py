# open py excel

import openpyxl

book = openpyxl.load_workbook("C:\\Users\\chara\\OneDrive\\Desktop\\book1.xlsx")
sheet = book.active
cell = sheet.cell(row=4,column=4)
print(cell.value)

#writing data to excel

sheet['B8']="hey iam charan"
book.save("C:\\Users\\chara\\OneDrive\\Desktop\\book1.xlsx")
book.close()