# missing page numbers

def isinlist(x,lst):
	lst = set(lst) 
	if x in lst :  
		return 1
	else:
		return 0

n=int(input("Enter the number of pages= "))
print("Enter page number list= ")	
string=input()
l=list((string.split(" ")))
for i in range(len(l)):
	l[i] = int(l[i])
print(l)
print("Missing page numbers are:")
for count in range(1,n+1):
	if isinlist(count,l)!=1:
		print(count)
	
