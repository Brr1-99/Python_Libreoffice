from openpyxl import load_workbook

wb = load_workbook('Prueba.ods')
ws = wb.active

wb.save('Prueba.ods')


class sheet:
    def __init__(self, name):
        self.name = name
        self.column = []

    def add_column(self, name):
        self.column.append(name)
