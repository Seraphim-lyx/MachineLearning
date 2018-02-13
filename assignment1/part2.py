from openpyxl import load_workbook

import math
import random


class lenearRegression(object):
    """docstring for LenearRegression"""

    def __init__(self):
        self.theta = [0, 1, 2, -1, -2]
        self.mean = [0, 0, 0, 0]
        self.sd = [0, 0, 0, 0]
        self.trainSet = []
        self.testSet = []

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
        minCF = self.costFunction(self.theta)
        for j in range(len(self.theta)):
            self.theta[j] = self.batchGD(j, [0, 1, 2, -1, -2], minCF)

    def batchGD(self, j, thetaList, minCF):
        """
        """
        th = thetaList[j]
        total = 0
        alpha = 1
        for row in self.ws.rows:
            row_ = self.reOrderValue(row)
            err = self.error(row_, thetaList)
            total += err * row_[j]
        # print(total)
        thetaList[j] = thetaList[j] - (total / self.max_row) * alpha

        cf = self.costFunction(thetaList)

        # print(j, minCF, cf)
        if minCF <= cf:
            return th
        else:
            # recursion for min value
            return self.batchGD(j, thetaList, cf)

    def costFunction(self, tl):
        total = 0
        for row in self.ws.rows:
            row_ = self.reOrderValue(row)
            err = self.error(row_, tl)
            total += pow(err, 2)
        return total / (2 * self.max_row)

    def error(self, row, t):
        """
        calculate the distance between
        computing result and real result
        """
        y = t[0] * row[0] + \
            t[1] * row[1] + \
            t[2] * row[2] + \
            t[3] * row[3] + \
            t[4] * row[4]
        # print(y - row[5])
        return y - row[5]

    def reOrderValue(self, row):
        r = []
        r.append(1)
        r.append(self.factorScaling(row[1].value, 0))
        r.append(self.factorScaling(row[3].value, 1))
        r.append(self.factorScaling(row[4].value, 2))
        r.append(self.factorScaling(row[5].value, 3))
        r.append(row[2].value)
        return r

    def factorScaling(self, num, k):
        """
        scaling range for large number
        """
        return (num - self.mean[k]) / self.sd[k]

    def setFactor(self):
        """
        Generate mean and stand deviation
        for number in large range
        """
        val = []
        val.append([row[1].value for row in self.ws.rows])
        val.append([row[3].value for row in self.ws.rows])
        val.append([row[4].value for row in self.ws.rows])
        val.append([row[5].value for row in self.ws.rows])

        for i in range(len(val)):
            self.mean[i] = sum(val[i]) / len(val[i])

        for v in range(len(val)):
            powTotal = 0
            for i in val[v]:
                powTotal += pow(i - self.mean[v], 2)
                self.sd[v] = math.sqrt(powTotal / len(val[v]))

    def test(self):
        # print(self.theta)
        total = 0
        for row in self.ws.rows:
            y = self.theta[0] * 1 + \
                self.theta[1] * self.factorScaling(row[1].value, 0) + \
                self.theta[2] * self.factorScaling(row[3].value, 1) + \
                self.theta[3] * self.factorScaling(row[4].value, 2) + \
                self.theta[4] * self.factorScaling(row[5].value, 3)
            total += abs(y - row[2].value)
        print(total/self.max_row)


l = lenearRegression()
l.loadData('data.xlsx', 'Sheet1')
l.learning()
l.test()
# print(l.mean)
print(l.sd)
