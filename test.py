
f=open("wiki_00",encoding="utf8")
w=open("a.txt",'w',encoding="utf8")

line=f.readlines()
for i in line:
	x=i.find('doc')
	if(i!="\n" and x==-1):
		print(len(i))
		for j in range(len(i)):
			w.write(i[j])	
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