import pickle
import operator
from collections import OrderedDict
from operator import itemgetter

word_dict ={}

print("LOADING...")
# w=open("b.txt","w",encoding="utf-8")
with open("word_dictionary_DouDic.txt", "rb") as fp:   # Unpickling
	word_dict = pickle.load(fp)
print("------OK------")

stop=1

while stop!=0:
	input_word=input()
	input_count=input()


	l=OrderedDict(sorted(word_dict[input_word].items(), key=itemgetter(1),reverse=True))
	count=1

	with open("result.txt",'w',encoding="utf-8") as w:
		for i in l:
			count+=1
			w.write(i+" "+str(l[i])+"\n")
			if count >int(input_count):
				break
	
# for key,value in word_dict['國文']:
# 	print(key)
# input_word=input()

