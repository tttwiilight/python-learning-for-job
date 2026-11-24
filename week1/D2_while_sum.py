#while循环练习
#计算1-100之间所有的偶数累加之和
total=0
i=1
while i<=100:
    if i%2==0:
        total+=i
    i+=1

print(f"循环结束，累加之和为{total}")
#卡点为tatal的设置想不到
