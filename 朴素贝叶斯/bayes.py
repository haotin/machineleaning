from numpy import *

#词表到向量的转化函数
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]  #1代表no文字  0代表正常文字
    return postingList,classVec
#返回不重复set列表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet =vocabSet| set(document)#创建两个集合的并集
    return list(vocabSet)


def setOfWord2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]= 1
        else:print ("the word:%s is not in my Vocabulary!"%word)
    return returnVec


'''
postingList,classVec = loadDataSet()
vocabSet = createVocabList(postingList)
data=setOfWord2Vec(vocabSet,postingList[0])
print (data)
'''
#朴素贝叶斯分类器训练函数
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] ==1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom  #change to log()
    p0Vect = p0Num/p1Denom  #change to log()
    return p0Vect,p1Vect,pAbusive

