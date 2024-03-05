import random
import json

def text2WordsPos():
    words, pos = list(), list()
    filePathNames = getFilePathNames()
    for filePathName in filePathNames:
        with open(filePathName, 'r', encoding='utf-8') as lineCharacterLabelData:
            for line in lineCharacterLabelData:
                if(len(line.split())) != 2:
                    words.append('。')
                    pos.append('O')
                else:
                    words.append(line.split()[0])
                    pos.append(line.split()[1])
    return words, pos

def listSplit(words, pos):
    lastIndex = 0
    splitedWords, splitedPos = list(), list()

    for index, character in enumerate(words):
        if character in ['，', '。']:
            splitedWords.append(words[lastIndex : index + 1])
            splitedPos.append(pos[lastIndex : index + 1])
            lastIndex = index + 1
    return splitedWords, splitedPos

def listShuffle(words, pos):
    shuffledWords, shufflePos = list(), list()
    wordIndices = [i for i in range(len(words))]
    random.shuffle(wordIndices)
    
    for index in wordIndices:
        shuffledWords.append(words[index])
        shufflePos.append(pos[index])

    return shuffledWords, shufflePos
            
def getFilePathNames():
    filePathNames = list()
    processedFilePath = './datasets/labeledData/Chapter1/'
    #fileNames.extend(['C1-5.txt'])
    for index in range(93):
        filePathNames.extend([processedFilePath + f"C1-{index}.txt"])
    return filePathNames

def encapsulate(words, pos, mode):
    jsonLine = dict()
    outputPath = './datasets/'
    fileName = mode + '.json'

    with open(outputPath + fileName, 'w', encoding='utf-8') as outputFile:
        for index in range(len(words)):
            jsonLine = {
                "WORD" : words[index],
                "POS"  : pos[index]
            }
            outputFile.write(json.dumps(jsonLine, ensure_ascii=False) + '\n')

def encapsulateAll(shuffledWords, shuffledPos):
    encapsulate(shuffledWords, shuffledPos, 'all')
    encapsulate(shuffledWords[:606], shuffledPos[:606], 'train')
    encapsulate(shuffledWords[606:], shuffledPos[606:], 'test')


def main():
    words, pos = text2WordsPos()
    splitedWords, splitedPos = listSplit(words, pos)
    shuffledWords, shuffledPos = listShuffle(splitedWords, splitedPos)
    encapsulateAll(shuffledWords, shuffledPos)


if __name__ == "__main__":
    main()