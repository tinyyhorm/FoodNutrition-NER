import random
import json

def text2WordsPos():
    words, pos = list(), list()
    filePathNames = getFilePathNames()
    for filePathName in filePathNames:
        with open(filePathName, 'r', encoding='utf-8') as lineCharacterLabelData:
            for line in lineCharacterLabelData:
                line = filterLine(line)
                if(len(line.split())) != 2:
                    words.append('。')
                    pos.append('O')
                else:
                    words.append(line.split()[0])
                    pos.append(line.split()[1])
    return words, pos

def filterLine(line):
    line = line.replace('Non-Nutrient', 'NotNutrient')
    return line

def listSplit(words, pos):
    lastIndex = 0
    lenIndex = 0
    splitedWords, splitedPos = list(), list()

    for index, character in enumerate(words):
        lenIndex += 1
        if character in ['，', '。'] or (lenIndex >= 16 and pos[index] == 'O'):
            splitedWords.append(words[lastIndex : index + 1])
            splitedPos.append(pos[lastIndex : index + 1])
            lastIndex = index + 1
            lenIndex = 0
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
    processedFilePath = './datasets/ChatGPT Data/'
    #fileNames.extend(['C1-5.txt'])
    for index in range(93):
        filePathNames.extend([processedFilePath + f"C1-{index}.txt"])
    return filePathNames

def encapsulate(words, pos, mode):
    jsonLine = dict()
    outputPath = './datasets/Human Review Data/'
    fileName = mode + '+r.json'

    with open(outputPath + fileName, 'w', encoding='utf-8') as outputFile:
        for index in range(len(words)):
            jsonLine = {
                "WORD" : words[index],
                "POS"  : pos[index]
            }
            outputFile.write(json.dumps(jsonLine, ensure_ascii=False) + '\n')

def encapsulateAll(shuffledWords, shuffledPos, proportion=0.8):
    splitIndex = int(len(shuffledWords) * proportion)

    encapsulate(shuffledWords, shuffledPos, 'all')
    encapsulate(shuffledWords[:splitIndex], shuffledPos[:splitIndex], 'train')
    encapsulate(shuffledWords[splitIndex:], shuffledPos[splitIndex:], 'test')


def main():
    words, pos = text2WordsPos()
    splitedWords, splitedPos = listSplit(words, pos)
    shuffledWords, shuffledPos = listShuffle(splitedWords, splitedPos)
    encapsulateAll(shuffledWords, shuffledPos, 0.8)


if __name__ == "__main__":
    main()