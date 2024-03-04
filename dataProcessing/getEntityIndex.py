def getEntities(outputsFile):
    with open(outputsFile, 'r', encoding='utf-8') as outputs:
        entities = []
        text = ""
        entityType = ""

        for output in outputs:
            output = output.strip().replace('\n', '')
            if output[:4] == "Text":
                text = output[5:]
            if output[:2] in ["食品", "食物", "人群", "器官", "疾病"] :
                entityType = output[:2]
            elif output[:3] == "营养素":
                entityType = output[:3]
            elif output[:4] == "非营养素":
                entityType = output[:4]
            elif entityType != "":
                entities.append([entityType, output])
        
        return text, entities

def getIndex(text, entities):
    textList = list(text)

    for entity in entities:
        index_s = text.find(entity[-1])
        if index_s != -1:
            index_e = index_s + len(entity[-1]) - 1
            labels = getLabel(entity, index_s, index_e)
            for index, label in enumerate(labels):
                # get unique entity
                if len(textList[index_s + index]) == 1:
                    textList[index_s + index] = textList[index_s + index] + ' ' + label

    return textList

def entityFilter(entityType):
    if entityType == '营养素':
        entityType = 'Nutrient'
    elif entityType in['食物', '食品']:
        entityType = 'Food'
    elif entityType == '非营养素':
        entityType = 'Non-nutrient'
    elif entityType == '人群':
        entityType = 'Group'
    elif entityType == '器官':
        entityType = 'Organ'
    elif entityType == '疾病':
        entityType = 'Disease'
    
    return entityType

def getLabel(entity, index_s, index_e):
    entityType = entityFilter(entity[0])
    labels = ['B-' + entityType]
    if len(entity[-1]) > 1:
        labels.extend(['I-' + entityType] * (index_e - index_s))
    return labels

def outputLabeledData(processedFilePath, labeledTexts, fileName):
    with open (processedFilePath + fileName, 'w', encoding='utf-8') as f:
        for labeledCharacter in labeledTexts:
            if len(labeledCharacter) == 1:
                labeledCharacter = labeledCharacter + ' ' + 'O'
            f.write(labeledCharacter + '\n')
            
def main():
    fileNames = list()
    originFilePath = './outputs/'
    processedFilePath = './datasets/labeledData/'

    #fileNames.extend(['C1-5.txt'])
    for index in range(93):
        fileNames.extend([f"C1-{index}.txt"])
    for fileName in fileNames:
        text, entities = getEntities(originFilePath + fileName)
        labeledText = getIndex(text, entities)
        outputLabeledData(processedFilePath, labeledText, fileName)

if __name__ == '__main__':
    main()