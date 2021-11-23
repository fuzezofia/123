import random
from DBUtils import update
from DBUtils import select


# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"

def welcome():
    print("---------------------------------------")
    print("-     中国工商银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    # 判断是否已满
    sql = "select count(*) from user"
    param = []
    data = select(sql,param,mode="one")# (4,)
    if data[0] > 100:
        return 3

    sql1 = "select * from user where username  = %s"
    param1 = [username]
    data1 = select(sql1,param1,mode= "all")# () 

    # 判断是否开过户
    if len(data1) > 0:
        return 2

    # 正常开户
    sql2 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,money,"2021-11-22",bank_name]
    update(sql2,param2)
    return 1

# 开户的输入数据
def  addUser():
    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")
    door  = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000,99999999)

    status = bank_addUser(account,username,password,country,province,street,door,money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status  == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username,account,password,country,province,street,door,money,bank_name))
        print(bank)


#存钱
def bank_cun():
    account = input('请输入账号')
    addmoney = int(input('请输入存款金额'))
    addcun = cun_money(account,addmoney)
    if addcun  == 1:
        print("嘻嘻，存款成功")
        info = '''
            ------------个人信息查询结果-------------
            账号：%s
            存入金额：%s
            ---------------------------------------
        '''
        print(info % (account,addmoney))



def cun_money(account,addmoney):
    sql4 = 'select * from user where account = %s'
    param4 = [account]
    abc = select(sql4, param4,mode='all')
    if len(abc) > 0:
        sql3 = 'update user set money = money  + %s'
        param3 = [addmoney]
        update(sql3,param3)
        return 1
    else:
        print('失败')
        return 2


# 取钱
def bank_qumoney():
    account = input("请输入账号:")
    password = input('请输入密码：')
    money = int(input("请输入取款金额:"))
    add = add_money(account,money,password)
    if add == 3:
        print("对不起，钱不够")
    elif add == 2:
        print("密码不对")
    elif add == 1:
        print('账户不存在')
    elif add == 0:
        print("取钱成功")
        print("下面是您的账户信息:")
        info = '''
            --------------账户信息--------------
            用户名：%s
            取出金额: %s 元
            ----------------------------------
            '''
        print(info % (username, money))

def add_money(account,money,password):
    sql5 = 'select * from user where account  = %s'
    param5 = [account]
    a = select(sql5, param5,mode='all')
    sql1='select password from user where account = %s and password = %s'
    param1 = [account,password]
    b=select(sql1, param1)
    sql2="select money from user where account=%s and money >=%s"
    param2=[account,money]
    c=select(sql2, param2)
    if len(a)==0:
        return 1
    else:
        if len(b) == 0 :
            return 2
        else:
            if len(c)==0:
                return 3
            else:
                sql3 = 'update user set money = money  - %s where account = %s'
                param3 = [money,account]      
                update(sql3,param3)


#查询
def bank_cha(account,password):
    sql1='select * from user where account = %s and password = %s'
    param1 = [account,password]
    b=select(sql1, param1)
    if  len(b) > 0 :
        return 1

def bank_chaxin():
    account = input('请输入账号：')
    password = input('请输入密码：')
    addcha = bank_cha(account,password)
    if addcha == 1:
        print("嘻嘻，查询成功")
        sql='select * from user where account=%s'
        param=[account]
        a=select(sql, param)
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (a[0][1],
        a[0][0],
        a[0][2],
        a[0][3],
        a[0][4],
        a[0][5],
        a[0][6],
        a[0][7],
        a[0][9]
        ))

#转账
def transfer_process(account1,password,account2,money):
    sql5 = 'select * from user where account  = %s'
    param5 = [account1]
    a = select(sql5, param5,mode='all')

    sql6 = 'select * from user where account  = %s'
    param6 = [account2]
    b = select(sql6, param6,mode='all')
    if len(a)==0 or len(b)==0:
        return 1
    else:
        sql1='select password from user where account = %s and password = %s'
        param1=[account2,password]
        d=select(sql1, param1,mode='all')
        if len(d)==0:
            return 2
        else:
            sql='select money from user where account = %s and money > %s'
            param=[account1,money]
            c=select(sql, param,mode='all')
            if len(c)==0:
                return 3
            else:
                sql2='update user set money = money  + %s where account=%s'
                param2=[money,account2]
                update(sql2, param2)
                sql3='update user set money = money  - %s where account=%s'
                param3=[money,account1]
                update(sql3, param3)
def transfer():
    account1 = input("请输入转出账户账号:")
    password = input("请输入转出账户密码：")
    account2 = input("请输入转入账户账号:")
    money = input("请输入转账金额:")
    transfer = transfer_process(account1, password, account2, money)
    if transfer == 1:
        print("账号输入错误")
    elif transfer == 2:
        print("密码输入错误")
    elif transfer == 3:
        print("余额不足")
    else:
        print("转账成功，下面是您的转账信息:")
        info = '''
        --------------转账信息--------------
        转出账户账号: %s
        转入账户账号: %s
        转 账 金 额: %s 元
        ----------------------------------
        '''
        print(info % ( account1, account2, money))

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        bank_cun()
    elif chose == "3":
        bank_qumoney()
    elif chose == "4":
        transfer()
    elif chose == "5":
        bank_chaxin()
    elif chose == "6":
        pass



































































