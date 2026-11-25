#list练习
#用户输入10个数字，存储到一个列表里。
#将列表里的数字排序，输出最小值、最大值和平均值
#设一个列表
s=[]
#输入10个数字到列表里
for i in range(10):
    num=int(input("请输入数字："))
    s.append(num)

#排序
s.sort()
#输出
print("列表是：",s)
print(s[0])
print(s[-1])
print(sum(s)/len(s))

#list练习
#合并两个列表里的元素，并对合并的结果进行去重处理
number1=[19,23,54,64,875,20,109,232,123,54]
number2=[55,80,72,35,60,123,54,29,91]

number3=number1+number2
print(number3)

number_list=[]

for num in number3:
    if num not in number_list:
        number_list.append(num)

print(number_list)

# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

list4=list1+list2+list3
print(list4)
list5=[]
for i in list4:
    if i not in list5:
        list5.append(i)
list5.sort()

print(list5)


# 将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


s=[i**2 for i in list1 if i%3==0 or i%5==0]

print(s)

# 将如下列表中的正数提取出来，封装为一个新的列表
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

s=[i for i in list1 if i>0]

print(s)
