# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习1：输入一个正整数判断是不是素数。
#       素数指的是只能被1和自身整除的大于1的整数。

# number = int(input('请输入一个正整数:'))
# count = 0
# for i in range(1,number+1):
#     if number%i==0:
#         count+=1
# if count>2:
#     print('%d 不是素数'% number)
# elif count==2:
#     print('%d 是素数'% number)
# else:
#     print('%d 既不是素数也不是合数'% number)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
# 最大公约数  辗转相减法
# former = int(input('请输入第一个数:'))
# latter = int(input('请输入第二个数:'))
# currentFormer=former
# currentLatter=latter
# count = 0
# if former==latter:
#     print('%d和%d的最大公约数为%d、最小公倍数为%d'%(former,latter,former,former))
# else:
#     while currentFormer%2==0 and currentFormer%2==0:
#         currentFormer/=2
#         currentLatter/=2
#         count+=1
#     while currentFormer-currentLatter!=0:
#         if currentFormer>currentLatter:
#             currentFormer-=currentLatter
#         else:
#             currentLatter-=currentFormer
#     gcd=count*2*currentFormer           #Greatest Common Divisor(GCD)
#     lcm=former*latter/gcd               #Least Common Multiple  (a,b)x[a,b]=ab(a,b均为整数)。
#     print('%d和%d的最大公约数为：%d,最小公倍数为：%d'%(former,latter,gcd,lcm))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习3：打印如下所示的三角形图案。

# *
# **
# ***
# ****
# *****

#     *
#    **
#   ***
#  ****
# *****

#     *
#    ***
#   *****
#  *******
# *********

# triangle1 = int(input('请输入第一类三角形的层数:'))
# star = '*'
# for i in range(1,triangle1+1):
#     print(star)
#     star+='*'

# triangle2 = int(input('请输入第二类三角形的层数:'))
# spaceCounter = triangle2
# star = '*'
# space =' '
# for i in range(1,triangle2+1):
#     print(space*spaceCounter+star)
#     star+='*'
#     spaceCounter-=1

triangle3 = int(input('请输入第二类三角形的层数:'))
spaceCounter = triangle3
star = '*'
space =' '
for i in range(1,triangle3+1):
    print(space*spaceCounter+star)          #字符串能加 也能乘
    star+='**'                              #原答案使用双重循环 感觉不太好
    spaceCounter-=1

