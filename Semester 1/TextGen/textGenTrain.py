import pandas as pd
import keyboard

data = {} #Defined before on_key so method has access to it

def on_key(event):
    rows = []
    for dict in data:
        rows.append(data[dict])

    rows = sorted(rows, key=lambda x: x["count"], reverse=True)

    dataFrame = pd.DataFrame(rows)

    dataFrame.to_csv("AI\Semester 1\TextGen\wordPairs.csv", index=False)

keyboard.on_press(on_key)

dataFile = pd.read_csv('Semester 1\TextGen\essayData.csv')

essayList = dataFile.iloc[:, 1]



for essay in essayList:
    essay = essay.split()

    for i in range(len(essay)-1):
        wordOne = essay[i].lower().strip('!><?,.@#$%^&*()~`"\'\"')
        wordTwo = essay[i+1].lower().strip('!><?,.@#$%^&*()~`"\'\"')

        dataSetLookUp = wordOne+"|"+wordTwo

        print(dataSetLookUp)

        if dataSetLookUp in data:
            data[dataSetLookUp]["count"] += 1
        
        else:
            data[dataSetLookUp] = {"word1": wordOne, "word2": wordTwo, "count": 1}
            

rows = []
for dict in data:
    rows.append(data[dict])

rows = sorted(rows, key=lambda x: x["count"], reverse=True)

dataFrame = pd.DataFrame(rows)

dataFrame.to_csv("Semester 1\TextGen\wordPairs.csv", index=False)