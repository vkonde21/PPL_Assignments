#Amicable numbers
import math
#Optimized divisor function	
def divisor(i):
	l=[]
	o=int(math.sqrt(i) + 1)
	if(i==1):
		return l
	for k in range(1,o):
		if(i%k==0):
			l.append(k)
			d=int(i/k)
			if(d!=k and d!=i):
				l.append(d)
	return l

count=0
x=2
y=3
l1=[]
l2=[]
while(count<10):
	s1=sum(divisor(x))
	#x is first number and s1 is second number
	#here first condition is already satisfied that sum of divisors of first number is equal to the second number.
	#as per defn of amicable nos. s1 = second no. and s2 = first no.
	#Now we have to check whether sum of divisors of second number(s1) is equal to first number or not
	s2=sum(divisor(s1))
	if(s2==x and s1!=x):
		if(x not in l1 and x not in l2):
			print("(",x,",",s1,")")
			l1.append(x)
			l2.append(s1)
			count = count + 1
	x = x + 1
	
	

