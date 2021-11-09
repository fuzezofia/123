import random
Ran = random.randint(0, 150)
i = 0
d = 5000
while i < 10and d>0:
    num = input("请输入一个数字")
    num = int(num)
    i=i+1
    if num == Ran:
        print("恭喜你，猜中，本次猜的数字为", num)
        i = i + 10
        d = d + 3000
    elif num < Ran:
        print("小了")
        d = d - 1000
    else:
        print("大了")
        d = d - 1000
if d > 0:
    print("你的金币为", d)
else:
    print("你的金币已空")
