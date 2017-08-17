# encoding=utf-8
import jieba


seg_list=jieba.cut("我喜歡吃漢堡還有薯條，此外，我也很喜歡五月天的歌曲")
# for sg in seg_list:
# 	if(sg!="，"):
# 		print(sg)
word_num=0
word_dict={}

# 判斷Dictionary有沒有這個單詞
for sg in seg_list:
	if(sg not in word_dict):
		# Dictionary裡面沒有這個單詞
		word_dict[sg]=word_num
		word_num+=1
		
	
# 兩兩配對
seg_index=1
for oth_sg in range(seg_index,len(seg_list)):


# print(word_dict)

a=list([[1,2],[3,4]])
# shape=a.shape
# print(shape[0])
a[0].insert(len(a[0]),5)
a[1].insert(len(a[1]),6)

# print(a)



