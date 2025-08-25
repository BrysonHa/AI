import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

data = {} #Defined before on_key so method has access to it

#df = pd.read_csv("wordPairs.csv")

#data = df.to_dict() #Defined before on_key so method has access to it

dataFile = pd.read_csv('essayData.csv') #Change for new data

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
            if wordOne and wordTwo:
                data[dataSetLookUp] = {"word1": wordOne, "word2": wordTwo, "count": 1, "type1": nlp(wordOne)[0].tag_, "type2": nlp(wordTwo)[0].tag_}
            

rows = []
for dict in data:
    rows.append(data[dict])

rows = sorted(rows, key=lambda x: x["count"], reverse=True)

dataFrame = pd.DataFrame(rows)

dataFrame.to_csv("wordPairs.csv", index=False)