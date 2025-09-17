import pandas

df = pandas.read_csv('titanicPassengers.csv')

numColumn = df.iloc[:, 2]

nameColumn = df.iloc[:, 3]

for i in range(len(numColumn)):
    print(nameColumn[i], numColumn[i])