import pandas as pd
import keyboard
import spacy

nlp = spacy.load("en_core_web_sm")

data = {} #Defined before on_key so method has access to it

df = pd.read_csv("wordPairs.csv")

data = df.to_dict() #Defined before on_key so method has access to it

def on_key(event):
    rows = []
    for dict in data:
        rows.append(data[dict])

    rows = sorted(rows, key=lambda x: x["count"], reverse=True)

    dataFrame = pd.DataFrame(rows)

    dataFrame.to_csv("AI\Semester 1\TextGen\wordPairs.csv", index=False)

keyboard.on_press(on_key)

dataFile = pd.read_csv('Semester 1\TextGen\essayData.csv') #Change for new data

essayList = dataFile.iloc[:, 1] #Change for new data

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
            data[dataSetLookUp] = {"word1": wordOne, "word2": wordTwo, "count": 1, "type1": nlp(wordOne).tag_, "type2": nlp(wordTwo).tag_}
            

rows = []
for dict in data:
    rows.append(data[dict])

rows = sorted(rows, key=lambda x: x["count"], reverse=True)

dataFrame = pd.DataFrame(rows)

dataFrame.to_csv("Semester 1\TextGen\wordPairs.csv", index=False)