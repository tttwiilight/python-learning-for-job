#循环综合练习2
# 猜数字游戏
# 1. 系统随机生成一个数字
# 2. 用户根据提示猜数字，并将数字输入系统
# 3. 猜错系统给提示，大了还是小了，继续猜
# 4. 猜对，系统退出，游戏结束
import random
random_number=random.randint(1,100)

while True:
    num=int(input("输入一个数字："))
    if num<random_number:
        print("数字猜小了哦(｡ì _ í｡)")
    elif num>random_number:
        print("数字猜大了呀( ̀⌄ ́)")
    else:
        print("猜对了!!!!!!!!!!!!!(⁎⁍̴̛ᴗ⁍̴̛⁎)")
        break
print(f"随机生成的数字是：{random_number}喔")
