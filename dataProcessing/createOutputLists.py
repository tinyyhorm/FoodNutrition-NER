import json

def createJsonOutputs(sourceFile):
    outputText = ''

    with open(sourceFile, "r", encoding='utf-8') as sourceDate:
        for text in sourceDate:
            outputData = {
                "Text" : text,
                "Output" : ""
            }
            outputText += json.dumps(outputData, ensure_ascii=False) + "\n"
    
    with open("/Users/tiny-mac/Developer/Datasets/FoodNutrition/outputs/Chapter1-Outputs.txt", 'w', encoding='utf-8') as outputs:
        outputs.write(outputText)
        
# createJsonOutputs("/Users/tiny-mac/Developer/Datasets/FoodNutrition/datasets/Chapter1.txt")

def createListOutputs(sourceFile):
    with open(sourceFile, "r", encoding='utf-8') as sourceDate:
        for line, text in enumerate(sourceDate):
            filePath = '/Users/tiny-mac/Developer/Datasets/FoodNutrition/outputs/'
            with open(filePath + 'C1-'+ str(line)+'.txt', 'w', encoding='utf-8') as outputLineFile:
                outputLine = "Text:" + text + "Output:\n"
                outputLineFile.write(outputLine)

createListOutputs("/Users/tiny-mac/Developer/Datasets/FoodNutrition/datasets/Chapter1.txt")

            

    
