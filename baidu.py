
import xlrd

# 工作簿对象
wb = xlrd.open_workbook(filename=r"D:\测试开发技术\py\day8\百度合作单位-人员管理-二期.xls")
st = wb.sheet_by_index(0)
rows = st.nrows
cols =  st.ncols
#男女
a = 0
b = 0
#年龄
c = 0
#工资
d = 0
e = 0
#手机号
f = 0
g = 0
h = 0
#地区
i = 0
k = 0
l = 0
m = 0
#公司
n = 0
for j  in range(1,rows):
    data = st.row_values(j)
    if data[8] == "男":
        a = a + 1
    elif data[8] =='女' :
        b = b + 1 
    if data[7] > 45 :
        c = c + 1
    if data[11] > 8000:
        d = d + 1
    elif data[11] < 3000:
        e = e + 1
    if data[5] .startswith('14' or '17'):
        f = f + 1
    elif data[5].startswith('13'):
        g = g + 1
    elif data[5].startswith('15'):
        h = h + 1
    if data[9] .startswith('黑龙江'):
        i = i + 1
    elif data[9].startswith('北京'):
        k = k + 1
    elif data[9].startswith('福建'):
        l = h + 1
    elif data[9].startswith('四川'):
        m = m + 1
    if data[13] .endswith('传媒有限公司'):
        n = n + 1

print("男生人数为：",a)
print('女生人数为：',b)
print('45岁以上的人数为：',c)
print('工资8000以上的人数为：',d)
print('工资3000以下的人数为：',e)
print('电话号码为电信的人数为：',f)
print('电话号码为移动的人数为：',g)
print('电话号码为联通的人数为：',h)
print('居住地为黑龙江的人数为',i)
print('居住地为北京的人数为',k)
print('居住地为福建的人数为',l)
print('居住地为四川的人数为',m)
print('去传媒有限公司的人数为',n)




























