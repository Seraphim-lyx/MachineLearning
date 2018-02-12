from openpyxl import load_workbook

wb = load_workbook(filename='data1.xlsx')

ws = wb['Sheet1']

# for row in ws.rows:
#     print(row[0].value)


class lenearRegression(object):
    """docstring for LenearRegression"""

    theta = [0, 1, 2, -1, -2]

    def __init__(self):
        pass

    def loadData(self, file, sheet):
        wb = load_workbook(filename=file)
        self.ws = wb[sheet]
        self.rows = self.ws.rows
        self.max_row = ws.max_row
        return ws

    def gradientDescent(self):

        for j in range(len(self.theta)):
            self.theta[j] = self.batchGD(j, self.theta[j])

    def batchGD(self, j, theta):
        total = 0
        alpha = 1
        minValue = theta
        for row in self.ws.rows:
            row_ = self.reOrderValue(row)
            err = self.error(row_)
            total += err * row_[j]
        # print(j)
        jtheta = (total / self.max_row) * alpha

        if minValue <= minValue - jtheta:
            return minValue
        else:
            self.theta[j] = minValue - jtheta
            return self.batchGD(j, self.theta[j])

    def error(self, row):

        y = self.theta[0] * row[0] + \
            self.theta[1] * row[1] + \
            self.theta[2] * row[2] + \
            self.theta[3] * row[3] + \
            self.theta[4] * row[4]

        return y - row[5]

    def reOrderValue(self, row):
        r = []
        r.append(1)
        r.append(row[1].value)
        r.append(row[3].value)
        r.append(row[4].value)
        r.append(row[5].value)
        r.append(row[2].value)
        return r


l = lenearRegression()
ws = l.loadData('data1.xlsx', 'Sheet1')
l.gradientDescent()
print(l.theta)
