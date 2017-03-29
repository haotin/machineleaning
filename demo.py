#knn
from numpy import *
import operator

dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]

print(dataSet[0])

print dataSet

'''
from math import  log
def creatdataSet():
    dataSet = [[1,1,'yes'],
           [1,1,'yes'],
           [1,0,'no'],
           [0,1,'no'],
           [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
dataSet,labels = creatdataSet()
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannon=0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannon -=prob * log(prob,2)
    print(shannon)
    return shannon
#calcShannonEnt(dataSet)

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
         if featVec[axis] == value:
             reduceFeatVec = featVec[:axis]
             reduceFeatVec.extend(featVec[axis+1:])
             retDataSet.append(reduceFeatVec)
    print(retDataSet)
    return retDataSet
splitDataSet(dataSet, 0, 1)

'''