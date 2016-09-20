from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

# branch demo
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
    


'''
#分类测试
group,labels=createDataSet()
print (classify0([0.2,0.1],group,labels,3))

#matplot测试
datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
print (datingDataMat,datingLabels)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,0], 15*array(datingLabels),15*array(datingLabels))
plt.show()

'''
