def removeSpace(sourceFile):
    withoutSpacedFile = open(sourceFile+"withoutSpace", "w",encoding="utf8")
    with open(sourceFile, "r") as sourceDate:
        for line in sourceDate:
            withoutSpacedFile.writelines(line.replace(' ', ''))
    withoutSpacedFile.flush()
    withoutSpacedFile.close()
            
removeSpace("/Users/tiny-mac/Developer/Datasets/FoodNutrition/datasets/Chapter2.txt")