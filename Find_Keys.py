from nltk import word_tokenize,Text,pos_tag

# find the noun from sentence

def Give_Noun (Sentence):
	tokens = word_tokenize(Sentence)
	text = Text(tokens)
	tags = pos_tag(text)           # returning words with there part of speech id 

	key = []
	l = len(tags)
	print tags
	i=0
	j=0
	while (l>0):
		if (tags[j][1]=='NN' or tags[j][1]=='NNP'):
			key.append(tags[j][0])
			i+=1
		l = l-1
		j+=1
		
	return key

#print Give_Noun ( 'what is the father of taylor swift?')