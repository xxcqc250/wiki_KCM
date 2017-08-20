import pickle

with open("wiki_counter_list.txt", "rb") as fp:   # Unpickling
	counter_list = pickle.load(fp)
with open("word_dictionary.txt", "rb") as fp:   # Unpickling
	word_num = pickle.load(fp)

word=input()
count=input()

print(word_num[word])

# w=open("a.txt",'w',encoding="utf8")
# w.write(str(word_num))