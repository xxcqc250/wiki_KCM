# encoding=utf-8
import jieba

# 讀取檔案==================
f=open("wiki_00",encoding="utf8")
lines=f.readlines()
for i in line:
	



input_text=jieba.cut("我喜歡吃漢堡還有我愛吃薯條")
seg_list=[]
for sg in input_text:
	if(sg!="，" and sg!="。"):
		seg_list.append(sg)
print(seg_list)

word_num=0 # 單詞編號 (index)/計算有多少個新的詞
word_dict={} # 單詞字典 {key:index}
wiki_counter_list=[]
obj_list=[] # 增加一列的model

# test_obj=[]
# test=[]

# 判斷Dictionary有沒有這個單詞
for sg in seg_list:
	if(sg not in word_dict):
		# Dictionary裡面沒有這個單詞
		# 新加入到Dict
		word_dict[sg]=word_num
		word_num+=1

		# array增加1列1行
		# for i in range(word_num):
		obj_list=[0]*word_num
		for i in range(len(wiki_counter_list)):
			wiki_counter_list[i].insert(len(wiki_counter_list),0)
		wiki_counter_list.insert(len(wiki_counter_list),obj_list)

			# obj_list.insert(len(obj_list),0)

# 轉成方陣array
# wiki_counter_list=[([0] * word_num) for i in range(word_num)]
# for i in range(0,len(obj_list)):	
# 	wiki_counter_list.insert(len(wiki_counter_list),obj_list)
	
# 兩兩配對=========================
seg_index=1
for word1 in seg_list:
	for word2 in range(seg_index,len(seg_list)):
		print(word1+" | "+seg_list[word2]+"====="+str(word_dict[word1])+" | "+str(word_dict[seg_list[word2]]))
		wiki_counter_list[word_dict[word1]][word_dict[seg_list[word2]]]+=1
		wiki_counter_list[word_dict[seg_list[word2]]][word_dict[word1]]+=1

	seg_index+=1

# print(wiki_counter_list)
for i in range(0,len(wiki_counter_list)):
	print(wiki_counter_list[i])


# print(word_dict)

# a=list([[1,2],[3,4]])
# # shape=a.shape
# # print(shape[0])
# a[0].insert(len(a[0]),5)
# a[1].insert(len(a[1]),6)

# print(a)



