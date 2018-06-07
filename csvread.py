import csv
import pandas as pd
import nltk


datas = ['name','response']
with open('possiblecommands.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(datas)
	for j in ["WebMD", "anypod", "TED talks", "fitbit", "uber", "kayak","Trainer Tips","campbell's kitchen","All recipes", "Bartender","Starbucks","Domino's Pizza","7 minute workout", "mayo clinic first aid","opening bell","this day in history", "Inspire me", "stop breathe think", "Airport Security Line Wait Times"]:
		reader = pd.read_csv("responses_secondtime.csv")
		row_index = -1
		for i in reader['name']:
			row_index = row_index + 1
			if i == j and reader['question'][row_index] == 'Alexa, help':
				text=reader['response'][row_index]	
		if(len(text)==0):
			break
		else:
			text = nltk.word_tokenize(text)
			print(text)
			index = []
			count = 0
			for i in text:
				if(i == "ask" or i == "like" or i == "say" or i == "Try" or i == "try"):
					index.append(count)
				count = count + 1
	#print(index)	

			index_or = []
			count = 0
			for i in text:
				if(i == "or" or i == "and"):
					index_or.append(count)
				count = count + 1
	#print(index_or)	
	
	

			subtexts = []
	#subtexts.append(text[index[0]+1:index_or[0]])
	#print(str(subtexts))
			for jj in range(len(index)):
		#print(j, subtexts)	
				if(len(index_or)!=0):
					if(index[jj]<index_or[0]):
						subtexts.append(" ".join(text[index[jj]+1:index_or[0]]))
					if(index[jj]>index_or[0] and index[jj]<index_or[-1]):
						for i in range(len(index_or)):
							dis = index_or[i]-index[jj]
							if(dis > 0):
								break
						subtexts.append(" ".join(text[index[jj]+1:index[jj]+dis]))
					elif(index[jj]>index_or[-1]):
						subtexts.append(" ".join(text[index[jj]+1:-1]))
				else:
					subtexts.append(" ".join(text[index[jj]+1:-1]))	

			for k in range(len(index_or)):
				if(k+1 <= len(index_or) -1):
					subtexts.append(" ".join(text[index_or[k]+1:index_or[k+1]]))	
	

			for t in subtexts:
				row = []
				row.append(j)
				row.append(t)
				print(t)
				writer.writerow(row)
			