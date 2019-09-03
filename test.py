from openpyxl import load_workbook
from libs.add_excel import add_to_excel
import pandas as pd

if __name__ == '__main__':
    file_home = '/Users/xiahualou/PycharmProjects/logExtract/template.xlsx'
    wb = load_workbook(filename=file_home)
    ws = wb['rabbitmq']
    add_to_excel(ws, "T")
    add_to_excel(ws, "L", True)
    wb.save("copy.xlsx")
