a=int(input("lvl"))
for i in range(a):
	if (i==0):
		print("@"*1)
	elif(i==1):
		print("@ "*2)
	else:
		print("@"," "*(i-2),"@")
for i in range(a,-1,-1):
	if (i==0):
		print("@"*1)
	elif(i==1):
		print("@ "*2)
	else:
		print("@"," "*(i-2),"@")