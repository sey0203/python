import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

with open("excel.txt", "r", encoding="utf-8") as f:
  txt_data = f.readlines()

row_num = 1
for txt in txt_data:
  sheet.cell(row=row_num, column=1, value=txt)

  row_num += 1

workbook.save("sample.xlsx")