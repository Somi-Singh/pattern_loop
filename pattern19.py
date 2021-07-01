k=1
i=5
while i>=1:
    j=1
    while j<=i:
        print(chr(k+64),end="")
        j+=1
        k+=1
    print()
    i-=1