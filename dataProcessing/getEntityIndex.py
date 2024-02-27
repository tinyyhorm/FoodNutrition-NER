def getIndex(text, entities):
    for entity in entities:
        index_s = text.find(entity[-1])
        if index_s != -1:
            index_e = index_s + len(entity) - 1
            print(entity, index_s, index_e)


def getEntities(outputsFile):
    with open(outputsFile, 'r', encoding='utf-8') as outputs:
        entities = []
        text = ""
        entityType = ""

        for output in outputs:
            output = output.strip().replace('\n', '')
            if output[:4] == "Text":
                text = output[5:]
                print(text)
            if output[:2] in ["食品", "食物", "人群", "器官", "疾病"] :
                entityType = output[:2]
            elif output[:3] == "营养素":
                entityType = output[:3]
            elif output[:4] == "非营养素":
                entityType = output[:4]
            elif entityType != "":
                entities.append([entityType, output])
        
        getIndex(text, entities)
            
# test = "Text:营养(nutrition)，原意指“谋求养生”。根据《中国营养科学全书》中的定义，营养指机体通过摄取食物，经过体内消化、吸收和代谢，利用食物中对身体有益的物质作构建机体组织器官、满足生理功能和体力活动需要的过程。"
# getIndex(test, ["营养", "nutritiin"])

for index in range(93):
    getEntities(f"/Users/tiny-mac/Developer/Datasets/FoodNutrition/outputs/C1-{index}.txt")
#getEntities("/Users/tiny-mac/Developer/Datasets/FoodNutrition/outputs/C1-3.txt")

