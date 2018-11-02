num = int(input('enter an integer: '))

for n in range(0, num*2):
    print(n)
    for i in range(0, n):
        print(i)

#Write a Python program using for loops that prints
#a pattern of *'s.  Given an input n for the number of *, 
# the program prints 2*n-1 rows.  

#The first row cotains one *, the second row two *, ..., 
#the n-th row contains n *, the nth+1 row contains n-1 *, 
#the nth+2 rows contains n-2 *, etc.
