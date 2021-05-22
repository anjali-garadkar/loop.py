# oppogit trangal
rows=6
i=0
while i<=rows+1:
    j=0
    while j<=i:
        print(" ",end=" ")
        j=j+1
    k=i
    while k<=rows-i:
        print("*",end=" ")   
        k=k+1
    print()
    i=i+1     

