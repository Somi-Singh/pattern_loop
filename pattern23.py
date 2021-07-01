# spaces=3
# row=1
# while row<=4:
#     print(spaces*" ","* ",row)
#     row+=1
#     spaces-=1


space=3
row=1
while row<=4:
    col=1
    while col<=7:
        if row==1 and col==4:
            print("*",end="")
        elif row==2 and col==3 or col==5:
            print("*",end="")
        else:
            print(" ",end="")
        col+=1
    row+=1

