from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#分类器具体算法
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1))
    return sortedClassCount[0][0]

#样本从文件读取
def file2matrix(filename):
    fr = open(filename)
    arrayOLine = fr.readlines()
    numbersOfLines = len(arrayOLine)
    returnMat = zeros((numbersOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLine:
        line = line.strip()
        listFormLine = line.split('\t')
        returnMat[index,:] = listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))
        index += 1
    return returnMat,classLabelVector

#数据归一话处理
def autoNorm(dataSet):
    minVas = dataSet.min(0)
    maxVas = dataSet.max(0)
    ranges = maxVas - minVas
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet-tile(minVas,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet ,ranges,minVas

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normDataSet ,ranges,minVas = autoNorm(datingDataMat)
    m = normDataSet.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classfileResult = classify0(normDataSet[i,:], normDataSet[numTestVecs:m,:], datingLabels[numTestVecs:m],3)
        #print ('the class came back with: %d,the real is :%d' %(classfileResult,datingLabels[i]))
        if (classfileResult != datingLabels[i]): errorCount += 1
    #print ('the total error rate is :%f '%(errorCount/float(numTestVecs)))


def classfyPerson():
    resultList = ['not at all','in small doses', 'in large doses']
    percentTats = float(input('percentage of time spent playing video games?'))
    ffMiles = float(input('frequent flier milse earned per year?'))
    icecream = float(input('liters of ice cream consumed per year?'))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVas = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,icecream])
    classifierResult = classify0((inArr - minVas)/ranges, normMat,datingLabels,3)
    print ("you will probably like this person:", resultList[classifierResult-1])

#datingClassTest()
classfyPerson()


'''
#分类测试
group,labels=createDataSet()
print (classify0([0.2,0.1],group,labels,3))

#matplot测试
datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
datingDataMat = autoNorm(datingDataMat)
print (datingDataMat,datingLabels)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,0], 15*array(datingLabels),15*array(datingLabels))
plt.show()

'''