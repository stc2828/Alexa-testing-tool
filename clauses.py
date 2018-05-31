from nltk import Tree
from stat_parser import Parser
parser = Parser()

parse_str = parser.parse("Mayo Clinic first had provided self care instructions for dozens of everyday situations you can ask how do I treat my baby's fever or tell me about spider bites or help for upper and follow the prompts to learn more about that you can also say")
#parse_str = "(ROOT (S (SBAR (IN Though) (S (NP (PRP he)) (VP (VBD was) (ADJP (RB very) (JJ rich))))) (, ,) (NP (PRP he)) (VP (VBD was) (ADVP (RB still)) (ADJP (RB very) (JJ unhappy))) (. .)))"

t = Tree.fromstring(str(parse_str))

subtexts = []
for subtree in t.subtrees():
    if subtree.label()=="SBAR+S" or subtree.label()=="CC":
        print (subtree.leaves())
        subtexts.append(' '.join(subtree.leaves()))
#print (subtexts)


for i in reversed(range(len(subtexts)-1)):
    subtexts[i] = subtexts[i][0:subtexts[i].index(subtexts[i+1])]

for text in subtexts:
    print(text)

# ADDED IN EDIT - Not sure for generalized cases
#leftover = presubtexts[0][presubtexts[0].index(presubtexts[1])+len(presubtexts[1]):]
#print(leftover)
