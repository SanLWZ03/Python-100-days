# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 1寻找水仙花数。

# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
# 该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

# for i in range(100,1000):
#     hundreds = i//100         #百位  '//' 代表取整
#     tens = i%100//10          #十位
#     units = i%100%10         #个位
#     if (hundreds**3 + tens**3 + units**3) == i:
#         print('%d 是一个水仙花数'% i)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 2百钱百鸡问题。

# 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

# count = 0
# for x in range(0, 20):
#     for y in range(0, 33):                              #穷举法
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             count+=1
#             print('方案%d :公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (count,x, y, z))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 3 CRAPS赌博游戏。

# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续要骰子，直到分出胜负。
# import random
# money = 1000                  #玩家本金
# bank = 10000                  #庄家本金
# text = '糟糕！你破产了'        #输出文字
# while money>0:                #还有钱 可以继续玩
#     if bank<=0:                #庄家破产
#         text ='太厉害了，你把庄家赢破产了'
#         break
#     else:
#         count = 1
#         dice1 = random.randrange(1,7) #第一次扔出的骰子1
#         dice2 = random.randrange(1,7) #第一次扔出的骰子2
#         while True:
#                 bet = int(input('请输入下注金额：'))
#                 if 0 < bet <= money:  #赌注判断
#                     break
#                 else:
#                     print('不好意思你的钱不够了。')
#         if dice1+dice2==7 or dice1+dice2==11:
#             print('第%d轮%d 点！玩家胜利！'%(count,dice1+dice2))
#             money+=bet
#             bank-=bet
#             print('恭喜!你赢了%d元,现在账户总共有%d元'%(bet,money))
#         elif dice1+dice2==2 or dice1+dice2==3 or dice1+dice2==12:
#             print('第%d轮%d 点！庄家胜利！'%(count,dice1+dice2))
#             money-=bet
#             bank+=bet
#             print('糟糕!你输了%d元,现在账户总共有%d元'%(bet,money))
#         else:
#             print('第%d轮%d 点！继续！'%(count,dice1+dice2))
#             while True:
#                 count+=1
#                 currentDice1 = random.randrange(1,7) #继续仍骰子
#                 currentDice2 = random.randrange(1,7)
#                 if currentDice1+currentDice2==7:
#                     print('第%d轮%d 点！庄家胜利！'%(count,currentDice1+currentDice2))
#                     money-=bet
#                     bank+=bet
#                     print('糟糕!你输了%d元,现在账户总共有%d元'%(bet,money))
#                     break
#                 elif currentDice1+currentDice2==(dice1+dice2):
#                     print('第%d轮%d 点！玩家胜利！'%(count,currentDice1+currentDice2))
#                     money+=bet
#                     bank-=bet
#                     print('恭喜!你赢了%d元,现在账户总共有%d元'%(bet,money))
#                     break
# print(text)
# ps 玩了好久，除了把bank改到1000，全压的豪赌，从来没有把庄家赢破产的


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 4 生成斐波那契数列的前20个数。
# 斐波那契数列的特点是数列的前两个数都是1，
# 从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。

# former1=1
# former2=1
# print(former1)
# print(former2)
# for i in range(3,21):
#     current = former1+former2
#     print(current)
#     former1 = former2
#     former2 = current


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 5 找出10000以内的完美数。
# 完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

# for i in range(1,10001):
#     sum = 0
#     for j in range(1,i):
#         if i%j == 0:
#             sum += j
#     if sum == i:
#         print(i)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 6 输出100以内所有的素数。
# 素数指的是只能被1和自身整除的正整数（不包括1）。

# for i in range(2,101):
#     count = 0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:           #代表只有1和自身两个因数
#         print(i)
