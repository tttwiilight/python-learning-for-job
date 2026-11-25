#循环综合练习1
#根据输入的用户名密码执行登录操作，具体要求如下：
# 1.正确的用户名和密码是admin/666888、zhangsan/123456、taoge/888666
# 2.输入用户名和密码，直到登录成功，程序运行结束；登录失败，继续输入用户名和密码
# 3.输入的用户名和密码不能是空的
# 4.登录成功：输出“登录成功”
# 5.登录失败，输出“密码错误”
while True:
    account=input("输入用户名：")
    password=input("输入密码：")
    if account=="" or password=="":
       print("输入错误，请重新输入！")
       continue
    if account=="admin" and password=="666888":
        print("登录成功!")
        break
    elif account=="zhangsan" and password=="123456":
        print("登录成功!")
        break
    elif account=="taoge" and password=="888666":
        print("登录成功!")
        break
    else:
        print("登录失败,请重新输入！")
