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

#
def setOfWord2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]= 1
        else:print ("the word:%s is not in my Vocabulary!"%word)
    return returnVec



postingList,classVec = loadDataSet()
vocabSet = createVocabList(postingList)
data=setOfWord2Vec(vocabSet,postingList[0])
print (data)