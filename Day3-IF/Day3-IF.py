# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习1：英制单位英寸与公制单位厘米互换。   1英寸=2.54厘米。

# length = float(input('请输入长度：'))
# unit = input('请输入单位"in" 或 "cm"("in"代表英寸，"cm"代表厘米): ')
# if unit=="in":
#     transLength = length*2.54 #转为cm
#     print('%f英寸 等于 %f厘米'%(length,transLength))
# else:
#     transLength = length/2.54 #转为in
#     print('%f厘米 等于 %f英寸'%(length,transLength))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习2：百分制成绩转换为等级制成绩。
# 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
#       70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

# grade = int(input('请输入你的成绩（0~100）：'))
# if grade >= 90:
#     print('你的等级为：A')
# elif grade >= 80 and grade < 90:
#     print('你的等级为：B')
# elif grade >= 70 and grade < 80:
#     print('你的等级为：C')
# elif grade >= 60 and grade < 70:
#     print('你的等级为：D')
# else:
#     print('你的等级为：E')

# grade = int(input('请输入你的成绩（0~100）：')) #优化后
# if grade >= 90:
#     level = 'A'
# elif grade >= 80:
#     level = 'B'
# elif grade >= 70:
#     level = 'C'
# elif grade >= 60:
#     level = 'D'
# else:
#     level = 'E'
# print('你的等级为：%s'% (level))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 练习3：输入三条边长，如果能构成三角形就计算周长和面积。   两边之和大于第三边

a = int(input('请输入第一条边长：'))
b = int(input('请输入第二条边长：'))
c = int(input('请输入第三条边长：'))
if a+b>c and a+c>b and b+c>a:
    circumference = a+b+c                              #周长
    p=circumference/2
    acreage = (p * (p - a) * (p - b) * (p - c)) ** 0.5 #面积   海伦公式
    print('%d、%d、%d三条边能构成三角形，该三角形周长为：%d,面积为：%d'%(a,b,c,circumference,acreage))
else:
    print('%d、%d、%d三条边不能构成三角形'%(a,b,c))