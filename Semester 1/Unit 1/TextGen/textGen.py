import pandas as pd
import keyboard, random
import spacy #VB = verb, NN = noun, JJ adjective, DT = determiner, PR = pronoun, 

#Refer to chatGPT for sentence rules
#[Determiner] + [Adjective(s)] + Noun (subject) + Verb (+ Object) (+ Adverbs) = Basic sentence

tags = [
    "CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNS","NNP","NNPS",
    "PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","SYM","TO","UH","VB","VBD","VBG",
    "VBN","VBP","VBZ","WDT","WP","WP$","WRB"
]

def getRandomWord(dataset, type):
    possRows = dataSet[dataSet["type1"] in type].head(10)

    return random.choice(possRows)["word1"]

dataSet = pd.read_csv("wordPairs.csv")

prevWord = "yes"
print(prevWord, end="")

def on_key(event):
    prevWord = getRandomWord(dataSet, [tag for tag in tags if tag.startswith("DT")])


   # global prevWord
    #possWords = []
    #for i in range(dataSet.shape[0]):
        #if len(possWords) > 10:
            #break
            
        #row = dataSet.iloc[i].to_dict()

        #if row["word1"] == prevWord:
            #possWords.append(row["word2"])

    #prevWord = random.choice(possWords)
    #print(" "+prevWord, end="")

keyboard.on_press(on_key)

x = 0
while True:
    x += 1