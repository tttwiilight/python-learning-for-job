# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：

# 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成后保存到系统中。
# 修改学生信息：要求输入要修改的学生姓名，
#             然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 列出所有学生：遍历所有学生信息并输出。
# 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，
#             以及语文、数学、英语最高分和最低分的学员姓名。
# 退出系统。

# 1.学生信息参考格式
# 2.操作类型
# 3.执行操作添加、修改、删除、查询
# 4.列出信息、输出
# 5.统计
# 6.退出
#结构：student_infor={"name":{"chinese":90,"math":95,"english":90}}
student_infor={}
menu1="""
###########请输入您的操作###########
#          1.添加学生信息          #
#          2.修改学生信息          #
#          3.删除学生信息          #
#          4.查询学生信息          #
#          5.列出所有学生          #
#          6.统计班级成绩          #
#          7.退出系统             #
##################################
"""

print("欢迎来到教务管理系统！")

while True:
    print(menu1)
    choice=input("输入您要执行的操作序号（1-7）：")
    
    match choice:
        case "1":
            name=input("输入学生姓名：")
            if name in student_infor:
                    print("此学生信息已存在")
                    continue
            chinese=float(input("输入学生的语文成绩："))
            math=float(input("输入学生的数学成绩："))
            english=float(input("输入学生的英语成绩："))
            student_infor[name]={"chinese":chinese,"math":math,"english":english}
            print("输入成功！")
            
        case "2":
            name=input("输入需要修改的学生姓名：")
            if name not in student_infor:
                    print("此学生信息不存在")
                    continue
            chinese=float(input("输入修改后的语文成绩："))
            math=float(input("输入修改后的数学成绩："))
            english=float(input("输入修改后的英语成绩："))
            student_infor[name]={"chinese":chinese,"math":math,"english":english}
            print("修改成功！")
            
        case "3":
            delete=input("输入需要删除的学生姓名")
            if delete not in student_infor:
                print("此学生不在系统当中，请重新输入！")
                continue
            del student_infor[delete]
            print("删除成功！")
            
        case "4":
            name=input("输入需要查询的学生姓名")
            
            if name not in student_infor.keys():
                print("此学生不在系统当中，请重新输入！")
                continue
            else:
                scores=student_infor[name]
                print(f"学生姓名：{name},学生语文成绩：{scores["chinese"]},学生数学成绩：{scores["math"]},学生英语成绩：{scores["english"]}")
        
        case "5":
            for n,s in student_infor.items():
                print(f"姓名：{n}\t\t语文分数：{s["chinese"]}\t数学分数：{s["math"]}\t英语分数：{s["english"]}\t")
        
        case "6":
            if not student_infor:
                print("暂无学生信息")
                continue
            chinese_score=[s["chinese"] for s in student_infor.values()]
            math_score=[s["math"] for s in student_infor.values()]
            english_score=[s["english"] for s in student_infor.values()]
            print("语文成绩的最高分是：",max(chinese_score),"数学成绩的最高分是：",max(math_score),"英语成绩的最高分是：",max(english_score))
            print("语文成绩的最低分是：",min(chinese_score),"数学成绩的最低分是：",min(math_score),"英语成绩的最低分是：",min(english_score))
            print("语文成绩的平均分是：",sum(chinese_score)/len(chinese_score),"数学成绩的平均分是：",sum(math_score)/len(math_score),"英语成绩的平均分是：",sum(english_score)/len(english_score))
            chinese_score=[(s["chinese"],name) for name,s in student_infor.items()]
            chinese_score.sort()
            print("语文成绩最高的是：",chinese_score[-1],"语文成绩最低的是：",chinese_score[0])
            math_score=[(s["math"],name) for name,s in student_infor.items()]
            math_score.sort()
            print("数学成绩最高的是：",math_score[-1],"数学成绩最低的是：",math_score[0])
            english_score=[(s["english"],name) for name,s in student_infor.items()]
            english_score.sort()
            print("英语成绩最高的是：",english_score[-1],"英语成绩最低的是：",english_score[0])

        case "7":
            print("退出成功！")
            break
        
        case _:
            print("输入错误，请重新输入：")
            continue
