#FIRST 10  HARMONIC DIVISORS
from statistics import harmonic_mean

#a harmonic divisor number, is a positive integer whose divisors have a harmonic mean that is an integer.
def divisor(i):
	l=[]
	o=int(i/2)+1
	for k in range(1,o):
		if(i%k==0):
			l.append(k)
	l.append(i)		
	return l

count = 0
x = 1
while(count<10):
	l = divisor(x)
	s = harmonic_mean(l)
	if(s - int(s) == 0):
		print(x)
		count = count + 1
	x = x + 1
