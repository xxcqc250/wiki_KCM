# import pickle
# with open("word_dictionary_DouDic.txt","wb") as fp:
# 	pickle.dump("1",fp)
# 	fp.close()

# d={}
# d[('a','c')]=1
# d[('b','c')]=2
# for key in d:
#     l=[i for i, v in enumerate(d) if v[0] == 'b' or v[1] == 'b']
#     print(l)
# print(l)





# import jieba
# import pickle
# from opencc import OpenCC



# word_dic={}


# # f=open("b.txt",encoding="utf8")
# w=open("view.txt",'w',encoding="utf-8")



# 找到所有檔案
import os

for root, dirs, files in os.walk("data"):
	# print (root)
	for file in files:
		print(os.path.join(root, file))
		# print(os.path.join(root, f))
		# f=open(os.path.join(root, file),encoding="utf8")

		# content=f.read()
		# cc=OpenCC('s2t') 
		# content=cc.convert(content)
		# print(content)

		# lines=f.readlines()

		# 讀取每一行
		# for i in lines:
			# x=i.find('doc') # 把doc的tag去除(沒有doc tag會回傳-1)

			# 把一些不必要的去除
			# if(i!="\n" and x==-1):
				# 簡體繁體中文編碼
			# cc=OpenCC('s2t') 
			# i=cc.convert(i)

# 				Str=i.replace('。','，')
# 				Str=Str.replace('\n','')
# 				Str=Str.split('，')

# 				# 將句子存入list
# 				for j in Str:

# 					# jieba斷句
# 					input_text=jieba.cut(j)
# 					seg_list=[]
# 					for sg in input_text:
# 						seg_list.append(sg)


# 					# 兩兩配對=========================
# 					seg_index=1 # 兩兩配對要用的
# 					for word1 in seg_list:
# 						for word2_num in range(seg_index,len(seg_list)):
							
# 							word2=seg_list[word2_num]
							
# 							if word1==word2: # 自己與自己不要算
# 								continue
							
# 							else: # key 排列一下
# 								keys=[]
# 								keys.append(word1)
# 								keys.append(word2)
# 								keys=sorted(keys)
# 								keys=tuple(keys)

# 							# key不在dict裡面要新增
# 							if(keys not in word_dic):
# 								word_dic[keys]=1
# 							else:
# 								word_dic[keys]+=1

# 						seg_index+=1
			
# with open("word_dictionary.txt","wb") as fp:
# 	pickle.dump(word_dic,fp)

# w.write(str(word_dic))



















# import jieba
# import pickle
# from opencc import OpenCC # 下載安裝包

# # jieba斷句
# input_text=jieba.cut("我喜歡五月天的歌曲")
# for i in input_text:
# 	print(i)


# cc=OpenCC('s2t') 
# i=cc.convert("开放中文转换")
# print(i)



    # for line in bz_file:
    #     label, text = line.rstrip('\n').split('\t')
    #     text_words = text.split(',')
        # print(label)



# 找到所有檔案============================================
# import os

# for root, dirs, files in os.walk("data"):
# 	# print (root)
# 	for f in files:
# 		# print(f)
# 		print(os.path.join(root, f))


# import pickle
# from opencc import OpenCC

# cc=OpenCC('s2t')
# # cc.set_conversion('s2tw')
# st="开放中文转换"
# print(st)
# convert=cc.convert(st)
# print(convert)








# dic1={}
# dic1["a"]={}
# dic1["a"]["b"]=2
# print(dic1)



# a= [(1,2),(1,4),(2,5),(5,7)]
# s=[item for item in a if item[0]==2 or item[1]==2]



# dic={}
# k=[]
# k.append("嗨")
# k.append("你好")
# k=tuple(k)

# search=("嗨","你好")
# dic[k]=1
# if(search not in dic):
# 	print(dic)


# l=[[1,2,3,4],[5,6,7,8]]
# m=max(l[0])
# print(m)





# with open("key_list.txt", "rb") as fp:   # Unpickling
# 	key_list = pickle.load(fp)
# w=open("b.txt","w",encoding="utf-8")
# w.write(str(key_list))





# key_list=[]  
# value_list=[]  
# mydisc = {'key1':'123','key2':'234','key3':'345'}  
# for key,value in mydisc.items():  
#     key_list.append(key)  
#     value_list.append(value)  



  
# get_value = input("")  
# if get_value in value_list:  
#     get_value_index = value_list.index(get_value)  
#     print (key_list[get_value_index])
# else:  
#     print ("你要查的值%s不存在" %get_value ) 






# f=open("wiki_00",encoding="utf8")
# w=open("a.txt",'w',encoding="utf8")

# line=f.readlines()
# for i in line:
# 	x=i.find('doc')
# 	if(i!="\n" and x==-1):
# 		print(len(i))
# 		for j in range(len(i)):
# 			w.write(i[j])	
		# w.write(i)



# l=[0] * 5
# print(l)

# l=[0,1,2,3]
# l2=[]
# for i in range(5):
# 	l=[0,1,2,3]
# 	l2.insert(len(l2),l)

# l2[0][3]=9
# # l.append(0)
# for i in range(len(l2)):
# 	print(l2[i])