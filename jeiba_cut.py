# encoding=utf-8
import jieba
import pickle

word_num=0 # 單詞編號 (index)/計算有多少個新的詞
word_dict={} # 單詞字典 {key:index}
wiki_counter_list=[]
obj_list=[] # 增加一列的model

# 讀取檔案==================
f=open("wiki_00",encoding="utf8")
# f=open("b.txt",encoding="utf8")
lines=f.readlines()

for i in lines:
	x=i.find('doc') # 把doc的tag去除(沒有doc tag會回傳-1)

	if(i!="\n" and x==-1):
		Str=i.replace('。','，')
		Str=i.replace('\n','')
		Str=Str.split('，')

		for j in Str:
			input_text=jieba.cut(j)
			seg_list=[]
			for sg in input_text:
				seg_list.append(sg)

			# 判斷Dictionary有沒有這個單詞
			for sg in seg_list:
				if(sg not in word_dict):
					# Dictionary裡面沒有這個單詞
					# 新加入到Dict
					word_dict[sg]=word_num
					word_num+=1

					# array增加1列1行
					obj_list=[0]*word_num
					for i in range(len(wiki_counter_list)):
						wiki_counter_list[i].insert(len(wiki_counter_list),0)
					wiki_counter_list.insert(len(wiki_counter_list),obj_list)


				
			# 兩兩配對=========================
			seg_index=1
			for word1 in seg_list:
				for word2 in range(seg_index,len(seg_list)):
					# print(word1+" | "+seg_list[word2]+"====="+str(word_dict[word1])+" | "+str(word_dict[seg_list[word2]]))
					if word1==word2:
						continue
					wiki_counter_list[word_dict[word1]][word_dict[seg_list[word2]]]+=1
					wiki_counter_list[word_dict[seg_list[word2]]][word_dict[word1]]+=1

				seg_index+=1

# 將計算結果存入檔案==============================
with open("wiki_counter_list.txt", "wb") as fp:   #Pickling
	pickle.dump(wiki_counter_list, fp)

with open("word_dictionary.txt", "wb") as fp2:   #Pickling
	pickle.dump(word_dict, fp2)	

with open("word_count.txt","wb") as fp:
	pickle.dump(word_num,fp)



key_list=[]  
value_list=[]  

for key,value in word_dict.items():  
    key_list.append(key)  
    value_list.append(value)
with open("key_list.txt","wb") as fp:
	pickle.dump(key_list,fp)
with open("value_list.txt","wb") as fp:
	pickle.dump(value_list,fp)

# print(word_dict)
# for i in range(len(wiki_counter_list)):
# 	print(wiki_counter_list[i])