bank1 = set(["Grass", "Goat", "Tiger"])
#Initially grass, goat and tiger are on one side of the bank.They are to be taken on the other side.But only one of them bcan be taken at a time on ther side
bank2 = set([])
flag = 1  # flag = 1 for bank1
d1 = set(["Grass", "Goat"])
d2 = set(["Goat", "Tiger"])

while len(bank1) != 0:
	if flag == 1:
		x = bank1.pop()
        #pop method removes a random element from the set and returns the removed element.
		if(bank1 == d1 or bank1 == d2):
			bank1.add(x)
			flag = 1
		else:
			print("Man takes ", x, "from bank1 to bank2.")
			bank2.add(x)
			flag = 2
	else:
		if bank2 != d1 and bank2 != d2:
			flag = 1
			print("Man returns alone")
		else:
			x = bank2.pop()
			bank1.add(x)
			flag = 1
			print("Man takes ", x, "from bank2 to bank1.")

