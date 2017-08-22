# encoding:utf-8


import jieba
import pickle
from opencc import OpenCC



word_dic={}


# f=open("b.txt",encoding="utf8")
w=open("view.txt",'w',encoding="utf-8")



# 找到所有檔案
import os

for root, dirs, files in os.walk("D2"):
	# print (root)
	for file in files:
		print(os.path.join(root, file))
		# print(os.path.join(root, f))
		f=open(os.path.join(root, file),encoding="utf8")

		# read the content
		content=f.read()

		# 簡體繁體中文編碼
		opencc=OpenCC('s2t') 
		content=opencc.convert(content)

		# 把一些不必要的去除
		content=content.replace('。','，')
		content=content.replace('\n','')
		content=content.replace('、','，')

		# 切割句子
		content=content.split('，')

		# x=i.find('doc') # 把doc的tag去除(沒有doc tag會回傳-1)		
		# if(i!="\n" and x==-1):

		# 將句子存入list
		for j in content:

			# jieba斷句
			input_text=jieba.cut(j)
			seg_list=[]
			for sg in input_text:
				seg_list.append(sg)


			# 兩兩配對=========================
			seg_index=1 # 兩兩配對要用的
			for word1 in seg_list:
				for word2_num in range(seg_index,len(seg_list)):
					
					word2=seg_list[word2_num]
					
					if word1==word2: # 自己與自己不要算
						continue
					
					else: # key 排列一下
						keys=[]
						keys.append(word1)
						keys.append(word2)
						keys=sorted(keys)
						keys=tuple(keys)

					# key不在dict裡面要新增
					if(keys not in word_dic):
						word_dic[keys]=1
					else:
						word_dic[keys]+=1

				seg_index+=1
			
with open("word_dictionary.txt","wb") as fp:
	pickle.dump(word_dic,fp)

w.write(str(word_dic))
