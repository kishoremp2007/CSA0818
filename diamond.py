row=int(input("Enter number of rows: "))
for i in range(1,row+1):
    print(" "*(row-i)+"*"*(2*i-1))
for i in range(row-1,0,-1):
    print(" "*(row-i)+"*"*(2*i-1))
         
