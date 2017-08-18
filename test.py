test_obj=[]
test=[]
# test===============================
for i in range(0,5):
	test_obj.insert(len(test_obj),i)
	# print(test_obj)
	test.insert(len(test),test_obj)
	# print(test)
test_obj[3]="xxx"
print(test)