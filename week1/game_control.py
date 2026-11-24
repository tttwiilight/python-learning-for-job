#match练习
act=input("输入动作指令")
match act:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"j"|"J":
        print("角色发动攻击")
    case "退出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("无效指令，请重新输入！")
#忘记兜底指令了
