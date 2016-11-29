import urllib, json, dictionary

def fetch_P_url(prop_str):
	a = "https://www.wikidata.org/w/api.php?action=wbsearchentities&search="
	c = "&language=en&type=property&format=json"
	word_arr = prop_str.split()
	l = len(word_arr)
	b = ""
	for i in range (0,l-1):
		b = b + word_arr[i] + "%20"
	b = b + word_arr[l-1]
	return (a+b+c)

def no_of_P_id (P_val):
	#processing JSON doc
	data = fetch_data(P_val)
	return(len(data['search']))

def fetch_data (P_val):
	P_url = fetch_P_url(P_val)
	response = urllib.urlopen(P_url)
	data = json.loads(response.read())
	return data

def search (arr, str):
	str = str.lower()
	l = len(arr)
	for i in range (0,l):
		if (arr[i]['label'].lower() == str):
			return i
	return (-1)

def use_dictionary (P_val):
	syn_list = dictionary.fetch_syn (P_val)
	for syn in syn_list:
		if (no_of_P_id(syn) == 0):
			syn_list.remove(syn)
	l = len(syn_list)
	if (l==0):
		return ('P$#')
	print('Did you mean?\n')
	for syn in syn_list:
		print (syn)
	while (1):
		str = raw_input('Enter option:\n')
		k = search (syn_list, str)
		if (k != -1):
			break
		print ('Invalid choice')
	D = fetch_data(P_val)
	P_id = work_P(no_of_P_id(str), D, str)
	return P_id
	

def work_P (no_of_results, data, P_val): #I need the P_val in this function
	if (no_of_results == 0):
		return(use_dictionary(P_val)); #returns a list of synonyms found in the dictionary
	if (no_of_results == 1):
		return (data['search'][0]['id'])
	print('Did you mean?\n')
	for i in range (0, no_of_results):
		print (data['search'][i]['label'])
	while (1):
		str = raw_input('Enter option:\n')
		k = search (data['search'], str)
		if (k != -1):
			break
		print ('Invalid choice')
	return (data['search'][k]['id'])

def final_f (P_val):
	x = no_of_P_id(P_val)
	D = fetch_data(P_val)
	return (work_P(x,D,P_val))
