# encoding:utf-8


import jieba
import pickle
from opencc import OpenCC
import itertools



word_dic={}

# f=open("wiki_00",encoding="utf8")
# f=open("b.txt",encoding="utf8")
w=open("b_DouDic.txt",'w',encoding="utf-8")
# lines=f.readlines()

# 找到所有檔案
import os

for root, dirs, files in os.walk("extracted2"):
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

		# 將句子存入list
		for j in content:
			input_text=jieba.cut(j)
			seg_list=[]
			for sg in input_text:
				seg_list.append(sg)

			


			# 兩兩配對=========================
			for word1,word2 in itertools.combinations(seg_list, 2):
				if word1==word2: # 自己與自己不要算
					continue
				
				# word1不在dic中
				if word1 not in word_dic:
					word_dic[word1]={}
					word_dic[word1][word2]=1
				else:
					if word2 not in word_dic[word1]:
						word_dic[word1][word2]=1
					else:
						word_dic[word1][word2]+=1

				# word2不在dic中
				if word2 not in word_dic:
					word_dic[word2]={}
					word_dic[word2][word1]=1
				else:
					if word1 not in word_dic[word2]:
						word_dic[word2][word1]=1
					else:
						word_dic[word2][word1]+=1


with open("word_dictionary_DouDic.txt","wb") as fp:
	pickle.dump(word_dic,fp)
	fp.close()

# for i in word_dic:
# 	w.write(str(word_dic[i])+"\n")

w.write(str(word_dic))
w.close()