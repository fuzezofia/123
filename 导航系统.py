"""
    导航系统：
        1.字典数据。
        2.方法的使用。

        1.退出：输入q或者Q
任务1：
    将旅游导航系统结合商城系统，集成开发！
    需求：
        当最终到达景点后，询问是否去买纪念品？
            xxxxXXXXxxxxxxxxxxx
"""

citys = {
    "北京": {
        "昌平": {
            "十三陵": ["十三陵水库"],
            "八达岭": ["八达岭长城", "野生动物园"],
            "回龙观": ["五道口切糕", "甑糕", "呷哺呷哺", "海底捞"]
        },
        "海淀": {
            "高校": ["清华", "北大"],
            "景点": ["香山", "植物园"]
        },
        "朝阳": {
            "公园": ["玉渊潭公园", "朝阳南北塔"]
        },
        "延庆": {
            "景点": ["龙庆峡"]
        }
    },
    "上海": {
        "浦东新区": {
            "叶榭市": ["外滩公园", "外滩"]
        }
    }
}


def showCity(citys):
    print("---------欢迎来到Jason旅游导航系统！-------------")
    for i in citys:
        print(i)
    print("---------------------------------------")


#
while True:
    showCity(citys)
    chose = input("请输入您想去的一级城市：")
    if chose == 'q' or chose == 'Q':
        print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
        break  # 跳出循环
    if chose not in citys:
        print("温馨提示：当前城市没有项目！别瞎弄！")
    else:
        showCity(citys[chose])
        chose2 = input("请输入您想去的二级城市：")
        if chose2 == 'q' or chose2 == 'Q':
            print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
            break  # 跳出循环
        if chose2 not in citys[chose]:
            print("都跟你讲了没有这个城市项目，别瞎弄！")
        else:
            showCity(citys[chose][chose2])
            chose3 = input("请输入您想去的三级城市：")
            if chose3 == 'q' or chose3 == 'Q':
                print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
                break  # 跳出循环
            if chose3 not in citys[chose][chose2]:
                print("你故意找茬是不是？别瞎弄！")
            else:
                showCity(citys[chose][chose2][chose3])
                print("车已经达到！祝你玩的愉快！是否需要购买纪念品？")
        while True:
            x = input("请输入Y或N。")
            if x == "Y":
                import random

                Ran = random.randint(1, 3)
                if Ran == 1:
                    print("恭喜你抽到辣条三折优惠卷")
                else:
                    print("恭喜你抽到lenovo电脑九折优惠卷")
                shop = [
                    ["牙膏", 21.5],
                    ["lenovo", 4500],
                    ["Mac pro", 12000],
                    ["Iphone 18 max Pro", 56000],
                    ["海尔洗衣机", 2500],
                    ["辣条", 3],
                    ["洗衣粉", 25],
                    ["利群", 160],
                    ["红塔山", 130]
                ]

                mycart = []
                out = [
                    ["牙膏", 21.5, 0],
                    ["lenovo", 4500, 0],
                    ["Mac pro", 12000, 0],
                    ["Iphone 18 max Pro", 56000, 0],
                    ["海尔洗衣机", 2500, 0],
                    ["辣条", 3, 0],
                    ["洗衣粉", 25, 0],
                    ["利群", 160, 0],
                    ["红塔山", 130, 0]
                ]
                if Ran == 1:
                    shop[5][1] = 0.9
                    out[5][1] = 0.9
                else:
                    shop[1][1] = 4050
                    out[1][1] = 4050

                salary = input("请输入您的钱包余额：")
                sal = salary = int(salary)

                while True:
                    for key, value in enumerate(shop):
                        print(key, value)

                    chose = input("请输入您要买的商品编号：")
                    if chose.isdigit():
                        chose = int(chose)
                        if chose >= len(shop):
                            print("商品编号不存在")
                        else:
                            if salary < shop[chose][1]:
                                print("钱包余额不足")
                            else:
                                salary = salary - shop[chose][1]
                                mycart.append(shop[chose])
                                if shop[chose][0] == out[chose][0]:
                                    out[chose][2] = out[chose][2] + 1
                                print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    elif chose == "q" or chose == "Q":
                        print("欢迎下次光临！")
                        break
                    else:
                        print("指令不存在请重新输入")

                print("-----------------欢迎下次光临小商店------------------")
                print("--------------以下是您的购物小条，请拿好：-------------")
                print("--------------------------------------------------")
                for key, value in enumerate(out):
                    if out[key][2] > 0:
                        print(out[key][0], out[key][1], "×", out[key][2])
                print("-------------------------------------------------")
                print("您本次还剩余额为：￥", salary, "，本次消费：￥", (sal - salary))
                break
            elif x == "N":
                print("一路走好。")
                break
            else:
                print("指令不存在。")
        break
