import nltk

#first set apart words
text = nltk.word_tokenize("Mayo Clinic first had provided self care instructions for dozens of everyday situations you can ask how do I treat my baby's fever or tell me about spider bites or help for upper and follow the prompts to learn more about that you can also say")
index = 0
marker_position = []
for i in text:
	if(i == "ask" or i == "like" or i == "or" or i == "say"):
		marker_position.append(index)
	index = index + 1

for j in marker_position:
	print(text[j])

#print(text)