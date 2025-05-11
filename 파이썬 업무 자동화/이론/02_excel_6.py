from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

sheet.append([1,2,3,4,5,6,7,8])
sheet.append([1,2,3,4,5,6,7,8])
sheet.append([1,2,3,4,5,6,7,8])
sheet.append([1,2,3,4,5,6,7,8])
sheet.append([1,2,3,4,5,6,7,8])
sheet.append([1,2,3,4,5,6,7,8])

workbook.save("excel_6.xlsx")