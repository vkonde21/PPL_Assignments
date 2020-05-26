#random output of a dice

import random 

name = 'y'
y='yes'
n='no'

while name!=n and name!='n':
	print ("output is : ") 
	print (random.choice([1,2,3,4,5,6]))
	name = input("Would you like to continue? (yes/no) :")
