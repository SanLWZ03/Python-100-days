# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习1：实现计算求最大公约数和最小公倍数的函数。

# def gcd(x,y):
#     count=0
#     if x==y:
#         return x
#     else:
#         while x%2==0 and y%2==0:
#             x/=2
#             y/=2
#             count+=1
#         while x-y!=0:
#             if x>y:
#                 x-=y
#             elif y>x:
#                 y-=x
#         return (2*count*x)
# def lcm(x,y):
#     return x*y/gcd(x,y)
# print(gcd(10,20))
# print(lcm(12,20))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习2：实现判断一个数是不是回文数的函数。
# eg.  12321  7846487

def Palindrome(x):
    temp = x
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == x
# num = int(input('请输入要判断的数:'))
# if Palindrome(num):
#     print('%d 是回文数'%num)
# else:
#     print('%d 不是回文数'%num)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习3：实现判断一个数是不是素数的函数。

def is_Prime_Number(x):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    return count==2
# while True:
#     num = int(input('请输入要判断的数:'))
#     if num<=1:
#         print('请输入大于1的数！')
#     else:
#         break
# if(is_Prime_Number(num)):
#     print('%d 是素数'%num)
# else:
#     print('%d 不是素数'%num)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习4：写一个程序判断输入的正整数是不是回文素数。

while True:
    num = int(input('请输入要判断的数:'))
    if num<=1:
        print('请输入大于1的数！')
    else:
        break
if(is_Prime_Number(num) and Palindrome(num)):
    print('%d 是回文素数'%num)
else:
    print('%d 不是回文素数'%num)
