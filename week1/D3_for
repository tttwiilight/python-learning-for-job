#嵌套循环练习1
#根据输入的直角边长度，打印等腰直角三角形
a=int(input("输入等腰直角边边长："))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end="  ")
    print()

#嵌套练习2
#根据输入的数字，打印对应的数字金字塔
a=int(input("输入一个数字，获得数字金字塔："))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(f"{j}",end="  ")
    print()
#卡点：不明白怎么打不一样的数字

#嵌套练习3
#打印国际象棋棋盘
for i in range(1,9):
    for j in range(1,9):
        if j%2==1:
            print("●",end=" ")
        else:
            print("○",end=" ")
    print()
#卡点是要注意棋盘格是行列共同控制的每个格子
#订正：
for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
            print("●",end=" ")
        else:
            print("○",end=" ")
    print()
