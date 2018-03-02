# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:36:48 2018

@author: lanlandetian
"""

import UserCF
import UserCF_IIF
import UserTimeCF
import ItemCF
import ItemCF_IUF
import ItemTimeCF
import random
import Evaluation
import LFM
import operator

import imp
imp.reload(UserCF)
imp.reload(UserTimeCF)
imp.reload(ItemCF)
imp.reload(ItemCF_IUF)
imp.reload(ItemTimeCF)
imp.reload(Evaluation)
imp.reload(LFM)


def readData():
    data = []
    fileName = 'u.data'
    fr = open(fileName, 'r')
    for line in fr.readlines():
        lineArr = line.strip().split()
        data.append([lineArr[0], lineArr[1], lineArr[2], lineArr[3]])
    return data


def SplitData(data, M, k, seed):
    test = []
    train = []
    M = 8
    random.seed(seed)
    for user, item, rating, time in data:
        if random.randint(0, M-1) == k:
            test.append([user, item, rating, time])
        else:
            train.append([user, item, rating, time])
    return train, test


# 将列表形式数据转换为dict形式
def transform(oriData):
    ret = dict()
    for user, item, rating, time in oriData:
        if user not in ret:
            ret[user] = dict()
        ret[user][item] = [rating, time]
    return ret


if __name__ == '__main__':
    data = readData()
    # print(data)
    numFlod = 5
    precision = 0
    recall = 0
    coverage = 0
    popularity = 0
    # for i in range(0, numFlod):
    [oriTrain, oriTest] = SplitData(data, numFlod, 1, 0)
    train = transform(oriTrain)
    test = transform(oriTest)

    # print(test)
#        W = UserCF.UserSimilarity(train)
 #       rank = UserCF.Recommend('1',train,W)
  #      result = UserCF.Recommendation(test.keys(), train, W)

    # W = UserCF_IIF.UserSimilarity(train)
    # rank = UserCF_IIF.Recommend('1', train, W)
    # print(sorted(rank.items(), key=operator.itemgetter(1), reverse=True))
    # result = UserCF_IIF.Recommendation(test.keys(), train, W)
    # print({k: result[k] for k in list(result)[:2]})

#        W = ItemCF.ItemSimilarity(train)
 #       rank = ItemCF.Recommend('1',train,W)
  #      result =  ItemCF_IUF.Recommendation(test.keys(),train, W)

    # W = ItemTimeCF.ItemSimilarity(train)
    # rank = ItemTimeCF.Recommend('1', train, W)
    # print(sorted(rank.items(), key=operator.itemgetter(1), reverse=True))
    W = UserTimeCF.UserSimilarity(train)
    rank = UserTimeCF.Recommend('1', train, W)
    print(sorted(rank.items(), key=operator.itemgetter(1), reverse=True))
  #      result =  ItemCF_IUF.Recommendation(test.keys(),train, W)

    #     [P, Q] = LFM.LatentFactorModel(train, 100, 30, 0.02, 0.01)
    #     rank = LFM.Recommend('2', train, P, Q)
    #     result = LFM.Recommendation(test.keys(), train, P, Q)

    #     N = 30
    #     precision += Evaluation.Precision(train, test, result, N)
    #     recall += Evaluation.Recall(train, test, result, N)
    #     coverage += Evaluation.Coverage(train, test, result, N)
    #     popularity += Evaluation.Popularity(train, test, result, N)

    # precision /= numFlod
    # recall /= numFlod
    # coverage /= numFlod
    # popularity /= numFlod

    # print("%20s%20s%20s%20s" %
    #       ('precision', 'recall', 'coverage', 'popularity'))
    # print("%20s%%%20s%%%20s%%%20s" %
    #       (precision * 100, recall * 100, coverage * 100, popularity))
    # # 运行完标志
    # print('Done!')
