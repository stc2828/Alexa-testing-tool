import pandas as pd
import nltk

length = []
for j in ["WebMD",  "TED talks", "fitbit", "uber", "kayak","Trainer Tips","campbell's kitchen","All recipes", "Bartender","Domino's Pizza","7 minute workout", "mayo clinic first aid","opening bell","this day in history", "Inspire me",  "Airport Security Line Wait Times"]:
	reader = pd.read_csv("responses_thirdtime.csv")
	row_index = -1

	for i in reader['name']:
		row_index = row_index + 1
		if i == j and reader['question'][row_index] == 'Alexa, stop':
			print(i)
			text = nltk.word_tokenize(reader['response'][row_index])
			print(len(text))
			length.append(len(text))

sum = 0 
for i in range(len(length)):
	#print(length[i])
	sum = sum + length[i]
	print(sum)

print(sum/16)

			


