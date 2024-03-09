import json
import pipeline2Model

def getWordPos():
    filePath = './datasets/Human Review Data/'
    word, pos = list(), list()

    for mode in ['train', 'test']:
        with open(filePath + mode + '.json', 'r', encoding='utf-8') as sourceFile:
            for line in sourceFile.readlines():
                sourceData = json.loads(line)
                word.append(sourceData["WORD"])
                pos.append(sourceData["POS"])

    return word, pos

def getSplitedWordDict():
    splitedWordDict = dict()
    dictPath = "./datasets/chaizi-jt.txt"

    with open(dictPath, 'r', encoding='utf-8') as dictFile:
        for dictLine in dictFile.readlines():
            word, splitedWord = dictLine[0], dictLine.split('\t')[-1]
            splitedWordDict[word] = splitedWord.strip().replace(' ', '')

    return splitedWordDict

def splitWord(originWord):
    splitedWord = list()
    splitedWordList = list()
    splitedWordDict = getSplitedWordDict()

    for wordList in originWord:
        for word in wordList:
            if word in list(splitedWordDict.keys()):
                splitedWordList.extend(splitedWordDict[word])
            else:
                splitedWordList.extend(word)
        splitedWord.append(wordList + splitedWordList)
        splitedWordList = []
    
    return splitedWord

def main():
    originWord, originPos = getWordPos()
    word = splitWord(originWord)
    pipeline2Model.encapsulateAll(word, originPos, )
    
if __name__ == "__main__":
    main()