from matplotlib import pyplot
from openpyxl import load_workbook


wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
print(sheet['A'][1:])


def getvalue(x): return x.value


print(list(map(getvalue, sheet['A'][1:])))

list_x = list(map(getvalue, sheet['A'][1:]))

list_y = list(map(getvalue, sheet['B'][1:]))

pyplot.plot(list(map(getvalue, sheet['A'][1:])), list(map(getvalue, sheet['C'][1:])), label="Метка 1")
pyplot.plot(list(map(getvalue, sheet['A'][1:])), list(map(getvalue, sheet['D'][1:])), label="Метка 2")
pyplot.plot(list(map(getvalue, sheet['A'][1:])), list(map(getvalue, sheet['B'][1:])), label="Label 3")
pyplot.show()
