def division(x, y):
	try:
		result = x/y
		print("Result is: ", result)
	except TypeError:
          print("You divided values of incompatible types")
	except ZeroDivisionError:
		print("division by zero not allowed")

while(True):
	print('\n\n1.File handling')
	print("2.Get nth element of a list")
	print("3.Perform division")
	print("4.Exit")
	choice = int(input("Enter your choice: "))
	if(choice == 1):
	#IO Error
		try:
			testfile = input("Enter filename: ")
			fh = open(testfile)
			fh.close()
			file = open(testfile, 'w')
		except FileNotFoundError:
			print("No such file in directory")
		except IOError:
			print("File can be read only")
		else:
			print("File written successfully")
	
	
	#Index Error
	elif(choice == 2):
		l = ["PPL", "Assignments", "Project"] 
		try:  
			print("List is:",l)
			i = int(input("Enter index: "))
			print(l[i])	
		except IndexError: 
			print("An error occurred")

	#Zero division error
	elif(choice == 3):
		try:
			a = int(input("Enter a: "))
			b = int(input("Enter b: "))
		except ValueError:
			print("Invalid inputs")

		else:
			division(a, b)
	else:
		break


		

	
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

