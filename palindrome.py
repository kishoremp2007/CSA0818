num=int(input("Enter a number: "))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print("The given number is palindrome")
else:
    print("the given number is not palindrome")
    

row=int(input("Enter number of rows: "))
for i in range(1,row+1):
    print("*"*i)


row=int(input("Enter number of rows: "))
for i in range(row,0,-1):
        print("*"*i)


row=int(input("Enter number of rows: "))
for i in range(1,row+1):
    print(" "*(row-i)+"*"*(2*i-1))


row=int(input("Enter number of rows: "))
for i in range(row,0,-1):
    print(" "*(row-i)+"*"*(2*i-1))


row=int(input("Enter number of rows: "))
for i in range(1,row+1):
    print(" "*(row-i)+"*"*(2*i-1))
for i in range(row-1,0,-1):
    print(" "*(row-i)+"*"*(2*i-1))
         







