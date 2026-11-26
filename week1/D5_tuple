#字符串str
s="hello-python"
print(s[0])
#切片
print(s[:5])
#步长
print(s[0:5:2])
print(s[5:0:-2])  #反向截取要从后往前

s="hello-python!"
index=s.find('python')  #在字符串中查找第一次出现位置
print(index)

s.count('p')   #数这个子串出现了几次

ss=s.upper()#s中所有变大写
SS=s.lower()#s中所有变小写

xs=s.split('-')#按照指定字符分割，最后形成列表
print(xs)

s.strip()#去除字符串两端的空白字符或指定字符
s.strip('a')#去除字符串两端的空白字符或指定字符

st=s.replace('hello','bye') #将字符串中的子串替换为新的子串，形成一个新的字符串

s.startswith('h')  #检查字符串是否以子串开头，返回布尔值


#字符串案例
#输入一个字符串，判断字符串是否是回文
s=input("输入一句话：")

if s==s[::-1]:
    print("是回文")
else:
    print("不是回文")
#s[::-1] 是 Python 里"反转字符串"的标准写法

ss=input("输入一句英文：")
#将用户输入的10个字符串，反转后全部转为大写，记录在列表里，最后将列表内容全部遍历出来
l=[]
#1. 输入10个字符串
for i in range(10):
    ss=input(f"输入第{i+1}个字符串：")
    s=ss[::-1].upper()
    l.append(s)
#2. 每个字符串反转+大写
#3. 将处理后的字符串塞进列表
#4. 遍历列表
for item in l:
    print(item)

#tuple练习
#组包t=a，b，c，1，2，3  一定要加逗号
#解包ti=(1,2,3)  a,b,c=t1

#tuple案例
#1. 计算每个学生的总分、各科平均分，一起输出出来
#2. 统计语文成绩的最低分、最高分、平均分，输出
#3. 查找成绩优秀（平均分大于90）的学生，输出
student=(("s001","王林",85,92,78),
         ("s002","李沐婉",92,88,95),
         ("s003","十三",78,85,82),
         ("s004","曾牛",88,79,91),
         ("s005","周亦",95,96,89),
         ("s006","王卓",76,82,77),
         ("s007","红蝶",89,91,94))
print("学号\t\t姓名\t\t语文\t数学\t英语\t总分\t\t平均分")
for s in student:
    total=s[2]+s[3]+s[4]
    average=total/3
    print(f"{s[0]} \t{s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {average:.1f} \t")

chinese_scores=[s[2] for s in student]
print(chinese_scores)
print(f"语文成绩的最低分是：,{min(chinese_scores)},语文成绩的最高分是：,{max(chinese_scores)},语文成绩的平均是：,{sum(chinese_scores)/len(chinese_scores)}")

for s in student:
    total=s[2]+s[3]+s[4]
    average=total/3
    if average>90:
        print(f"学号是：{s[0]},姓名是{s[1]},平均分是：{average:.1f}")

#set案例

#求交集 set1.intersection()       s3=s1&s2
#存在s1，不存在于s2   s1.difference()       s3=s1-s2  集合推导式：s3={s for s in s1 if s not in s2}
#求并集 union   s1｜s2|s3
