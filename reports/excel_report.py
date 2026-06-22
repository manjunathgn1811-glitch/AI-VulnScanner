from openpyxl import Workbook


def generate_excel(target, risk):

    wb = Workbook()

    ws = wb.active

    ws.title = "Assessment"

    ws.append(["Target", "Risk"])

    ws.append([target, risk])

    path = "exports/report.xlsx"

    wb.save(path)

    return path