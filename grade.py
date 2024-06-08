while True:
	m =str(input("enter score:----"))
	print(type(m))
	if(m  >= str(0.0) and m<= str(1.0)):
		if(m>=str(0.9)):
			print("A")
		elif(m>=str(0.8)):
			print("B")
		elif(m>= str(0.7)):
			print("c")
		elif(m>=str(0.6)):
			print("d")
		elif(m<str(0.6)):
			print("f")
	else:
		print("Wrong input")
