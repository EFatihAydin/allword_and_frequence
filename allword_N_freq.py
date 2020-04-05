#import library
from functools import reduce
from collections import Counter

#clean: clean and lower text by turkish words
def clean(text):
	d = { "Ş":"ş", "İ":"i", "Ü":"ü", "Ç":"ç", "Ö":"ö", "Ğ":"ğ",  "I":"ı", "Î":"ı", "Û":"u", "Â":"a" , "â":"a" , "î":"ı" , "û":"u" }
	text = reduce( lambda x, y: x.replace( y,d[y] ),d,text )
	text = text.lower()
	text = text.strip()
	return text

#group_list: count items in list (list to dictionary) and convert to list(tupple in list)
def group_list(lst): 
    return list(zip(Counter(lst).keys(), Counter(lst).values()))

#read stopwords file
sw = open('stop_words.txt' , encoding = 'utf-8')

#convert lines to stopwords data
swliste = sw.readlines()
swliste = list(map(lambda x:x.strip(),swliste))

#variables
words = []
numbers = ["0","1","2","3","4","5","6","7","8","9"]

#read all data and search words in every line 
for line in open("data.txt"):
	text = clean(line)
	text = text.strip("\n")

	for word in text.split(" "):
		word = word.strip("\n")

		for i in range(len(numbers)):
			if numbers[i] in word:
				word = "Not Word"
				break

		if word == "Not Word":continue
		if word in swliste:continue

		words.append(word)

freq_word = group_list(words) 

print("Writing words file...")

with open("words.txt", "w") as file:
	for value in freq_word:
		lword = value[0]
		frekans = value[1]
		file.write(str(lword)+"|"+str(frekans)+"\n")
file.close()

print("Completed your file.")