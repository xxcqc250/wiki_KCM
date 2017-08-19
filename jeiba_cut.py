# encoding=utf-8
import jieba


input_text=jieba.cut("我喜歡吃漢堡還有薯條，此外，我也很喜歡五月天的歌曲")
seg_list=[]
for sg in input_text:
	seg_list.append(sg)
print(seg_list)

# print(seg_list)
word_num=0 # 單詞編號 (index)
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

		# list增加1個元素
		obj_list.insert(len(obj_list),0)

# 轉成方陣array
for i in range(0,len(obj_list)):	
	wiki_counter_list.insert(len(wiki_counter_list),obj_list)

	
# 兩兩配對=========================

seg_index=1
for sg in seg_list:
	for oth_sg in range(seg_index,len(seg_list)):
		print(sg+" | "+seg_list[oth_sg])
	seg_index+=1


# print(word_dict)

# a=list([[1,2],[3,4]])
# # shape=a.shape
# # print(shape[0])
# a[0].insert(len(a[0]),5)
# a[1].insert(len(a[1]),6)

# print(a)



