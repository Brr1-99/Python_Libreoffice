from openpyxl import Workbook, load_workbook

wb = load_workbook('Prueba.ods')
ws = wb.active

wb.save('Prueba.ods')
