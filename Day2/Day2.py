# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a)) # <class 'int'>
# print(type(b)) # <class 'float'>
# print(type(c)) # <class 'complex'>
# print(type(d)) # <class 'str'>
# print(type(e)) # <class 'bool'>
# a=input('a = ')
# b = int(a)  # 会报错  invalid literal for int() with base 10: 
# print(a)
# print(b)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习一  华氏温度转换为摄氏温度  C = 5×(F- 32)/9

# f = float(input('请输入华氏温度：')) #不加int()类型为 str
# c = 5*(f - 32)/9                 #转换
# print('%f华氏度对应的摄氏温度为：%f' % (f,c))  #输出


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习二：输入圆的半径计算计算周长和面积

# import math
# PI = math.pi            # 圆周率
# r = float(input('请输入圆的半径：'))
# c = 2*r*PI              #周长
# s = PI*r**2             #面积   （r**2 平方）
# print('圆的周长为：%f，面积为：%f'%(c,s))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习三：输入年份判断是不是闰年 

year = int(input('请输入年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    print('%d年 是闰年！' % (year))
else:
    print('%d年 不是闰年！' % (year))