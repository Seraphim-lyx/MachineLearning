from openpyxl import load_workbook

import math


class lenearRegression(object):
    """docstring for LenearRegression"""

    theta = [0, 1, 2, -1, -2]

    def __init__(self):
        pass

    def loadData(self, file, sheet):
        """
        loading raw data
        """
        wb = load_workbook(filename=file)
        self.ws = wb[sheet]
        self.max_row = self.ws.max_row
        self.setFactor()

    def learning(self):
        """
        iterate each attributes for gradient descent
        """
        for j in range(len(self.theta)):
            self.theta[j] = self.batchGD(j, self.theta[j])

    def batchGD(self, j, theta):
        """
        """
        total = 0
        alpha = 1
        minValue = theta
        for row in self.ws.rows:
            row_ = self.reOrderValue(row)
            err = self.error(row_)
            total += err * row_[j]

        jtheta = (total / self.max_row) * alpha

        # print(self.theta[j])
        if minValue <= minValue - jtheta:
            return minValue
        else:
            self.theta[j] = minValue - jtheta
            return self.batchGD(j, self.theta[j])  # recursion for min value

    def error(self, row):
        """
        calculate the distance between
        computing result and real result
        """
        y = self.theta[0] * row[0] + \
            self.theta[1] * row[1] + \
            self.theta[2] * row[2] + \
            self.theta[3] * row[3] + \
            self.theta[4] * row[4]

        return y - row[5]

    def reOrderValue(self, row):
        r = []
        r.append(1)
        r.append(self.factorScaling(row[1].value))
        r.append(row[3].value)
        r.append(row[4].value)
        r.append(row[5].value)
        r.append(row[2].value)
        return r

    def factorScaling(self, num):
        """
        scaling range for large number
        """
        return (num - self.meanVal) / self.sd

    def setFactor(self):
        """
        Generate mean and stand deviation
        for number in large range
        """
        val = [row[1].value for row in self.ws.rows]
        self.meanVal = sum(val) / len(val)
        powTotal = 0

        for i in val:
            powTotal += pow(i - self.meanVal, 2)
        self.sd = math.sqrt(powTotal / len(val))

    def test(self):

        for row in self.ws.rows:
            y = self.theta[0] * 1 + \
                self.theta[1] * self.factorScaling(row[1].value) + \
                self.theta[2] * row[3].value + \
                self.theta[3] * row[4].value + \
                self.theta[4] * row[5].value
            print(row[2].value - y)


l = lenearRegression()
l.loadData('Data.xlsx', 'Sheet1')
l.learning()
# l.test()
print(l.theta)
# print(l.sd)
