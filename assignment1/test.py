from openpyxl import load_workbook

import math

theta = [-21.77230885416671, 1, -1324.5454118154291, -1, -2]

wb = load_workbook(filename='Data.xlsx')
ws = wb['Sheet1']

for row in ws.rows:

    y = theta[0] * 1 + \
        theta[1] * row[1].value + \
        theta[2] * row[3].value + \
        theta[3] * row[4].value + \
        theta[4] * row[5].value
    print(row[2].value - y)
