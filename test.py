# -*- 
# import bz2

f=open("wiki_00",encoding="utf8")

w=open("a.txt",'w',encoding="utf8")

line=f.readlines()
for i in line:
	x=i.find('doc')
	if(i!="\n" and x==-1):
		w.write(i)
