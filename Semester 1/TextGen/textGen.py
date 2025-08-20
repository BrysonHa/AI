import pandas as pd
import keyboard, random

dataSet = pd.read_csv("Semester 1\TextGen\wordPairs.csv")

prevWord = "yes"
print(prevWord, end="")

def on_key(event):
    global prevWord
    possWords = []
    for i in range(dataSet.shape[0]):
        if len(possWords) > 10:
            break
            
        row = dataSet.iloc[i].to_dict()

        if row["word1"] == prevWord:
            possWords.append(row["word2"])

    prevWord = random.choice(possWords)
    print(" "+prevWord, end="")

keyboard.on_press(on_key)

x = 0
while True:
    x += 1