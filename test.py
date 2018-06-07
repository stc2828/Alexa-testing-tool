import pandas as pd

for j in ["WebMD", "anypod", "TED talks", "fitbit", "uber", "kayak","Trainer Tips","campbell's kitchen","All recipes", "Bartender","Starbucks","Domino's Pizza","Capital One","7 minute workout", "mayo clinic first aid","opening bell","this day in history", "Inspire me", "stop breathe think", "Airport Security Line Wait Times"]:
	#recognize possible commands
	reader = pd.read_csv("possiblecommands.csv")
	row_index = -1
	subtexts = []
	for i in reader['name']:
		row_index = row_index + 1
		if i == j:
			subtexts.append(reader['response'][row_index])

	for t in subtexts:
		print(t)
