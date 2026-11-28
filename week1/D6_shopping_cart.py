# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
 # 系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
 
 # 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，
 #             保存该商品信息到购物车。
 # 修改购物车：要求用户输入要修改的购物车商品名称，
 #             然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
 # 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
 # 查询购物车：将购物车中的商品信息展示出来，
 #             格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
 # 退出购物车

#1. 构建一个购物车dict
#2. 输出一个控制台
shopping_cart={"吧唧":{"price":35,"number":20},"立牌":{"price":88,"number":10}}
menu="""
###########请输入您的操作###########
#          1.添加购物车           #
#          2.修改购物车           #
#          3.删除购物车           #
#          4.查询购物车           #
#          5.退出购物车           #
#################################
"""

print("欢迎使用购物车管理系统(^ ^)")

while True:
    
    print(menu)
    
    
    act=input("请输入您要操作的序号（1-5）：")
    match act:
        case "1":               #3. 添加购物车
            name=input("请输入添加商品的名称：")
            if name in shopping_cart:
                print("该商品已在购物车中！")
                continue
            price=float(input("请输入添加商品的价格："))
            number=int(input("请输入添加商品的数量："))
            shopping_cart[name]={"price":price,"number":number}
            print("添加成功！")
        case "2":                #4. 修改购物车    
            name=input("请输入需要修改的商品的名称：")
            if name not in shopping_cart:
                print("该商品不在购物车中！")
                continue
            price=float(input("请输入需要修改的商品的价格："))
            number=int(input("请输入需要修改的商品的数量："))
            shopping_cart[name]={"price":price,"number":number}
            print("修改成功！")
        case "3":                #5. 删除购物车   
            name=input("请输入需要删除的商品的名称：")
            if name not in shopping_cart:
                print("该商品不在购物车中！")
                continue
            else:
                del shopping_cart[name]
                print("删除成功！")
        case "4":                #6. 查询购物车  
            for name in shopping_cart.keys():
                info=shopping_cart[name]
                print(f"商品名称是：{name},商品价格是：{info["price"]},商品数量是：{info["number"]}")
        case "5":                #7. 退出购物车
            print("退出成功,白白！")
            break
        case _:                #7. 退出购物车
            print("输入错误，请重新输入操作！")
