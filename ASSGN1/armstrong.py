# Program to check Armstrong numbers in a certain interval
lower = int(input())
upper = int(input())

#A positive integer of n digits is called an Armstrong number of order n(order is number of digits) if.

#abcd... = pow(a, n) + pow(b, n) + pow(c, n) + pow(d, n) + ....


for num in range(lower, upper + 1):
       # order of number
       order = len(str(num))
       sum1 = 0
       temp = num
       while temp > 0:
           digit = temp % 10
           sum1 += digit ** order
           temp //= 10
       if num == sum1:
           print(num)
