import random
Ran = random.randint(1,3)
if Ran == 1:
    print("恭喜你抽到辣条三折优惠卷")
else:
    print("恭喜你抽到lenovo电脑九折优惠卷")
shop = [
    ["牙膏",21.5],
    ["lenovo",4500],
    ["Mac pro",12000],
    ["Iphone 18 max Pro",56000],
    ["海尔洗衣机",2500],
    ["辣条",3],
    ["洗衣粉",25],
    ["利群",160],
    ["红塔山",130]
]

mycart = []
out = [
    ["牙膏",21.5,0],
    ["lenovo",4500,0],
    ["Mac pro",12000,0],
    ["Iphone 18 max Pro",56000,0],
    ["海尔洗衣机", 2500,0],
    ["辣条",3,0],
    ["洗衣粉",25,0],
    ["利群",160,0],
    ["红塔山",130,0]
]
if Ran == 1:
    shop[5][1]=0.9
    out[5][1]=0.9
else:
    shop[1][1]=4050
    out[1][1]=4050

salary = input("请输入您的钱包余额：")
sal = salary = int(salary)


while True:
    for key,value in enumerate(shop):
        print(key,value)

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
                    out[chose][2]=out[chose][2]+1
                print(shop[chose][0],"添加购物车成功！余额还剩:￥",salary)
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("指令不存在请重新输入")


print("-----------------欢迎下次光临小商店------------------")
print("--------------以下是您的购物小条，请拿好：-------------")
print("--------------------------------------------------")
for key,value in enumerate(out):
    if out[key][2]>0:
        print(out[key][0],out[key][1],"×",out[key][2])
print("-------------------------------------------------")
print("您本次还剩余额为：￥",salary,"，本次消费：￥",(sal - salary))











