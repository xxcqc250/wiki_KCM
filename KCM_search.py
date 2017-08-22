import pickle
import operator
from collections import OrderedDict
from operator import itemgetter

word_dict ={}


w=open("b.txt","w",encoding="utf-8")
with open("word_dictionary_DouDic.txt", "rb") as fp:   # Unpickling
	word_dict = pickle.load(fp)

# word_dict['國文'] ={}
# word_dict['國文']['數學'] =8
# word_dict['國文']['英文'] =10
# word_dict['國文']['化學'] =9
# word_dict['數學'] ={}
# word_dict['數學']['國文']=4
# print(word_dict)
stop=1

while stop!=0:
	input_word=input("輸入關鍵字:")
	input_count=input("次數:")

	# word_dict['國文']=sorted(word_dict['國文'].items(),key=operator.itemgetter(0))
	# word_dict['國文']=sorted(word_dict['國文'].values())
	l=OrderedDict(sorted(word_dict[input_word].items(), key=itemgetter(1),reverse=True))
	# print(word_dict['國文'])
	count=1

	w=open("result.txt",'w',encoding="utf-8")

	for i in l:
		count+=1
		w.write(i+" "+str(l[i])+"\n")
		if count >int(input_count):
			# print('enough')
			break
	
# for key,value in word_dict['國文']:
# 	print(key)
# input_word=input()

