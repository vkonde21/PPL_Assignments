def geometric(a, r, n):  
    for i in range(0, n):  
        term = a * pow(r, i) 
        print(term, " ",end =" ") 
        
a = float(input("Enter the first term"))
b = float(input("Enter the common ratio"))
geometric(a,b,10)
print("\n")
