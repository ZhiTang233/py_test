str1 = 'good good study'
# 1. 将str1 中的g改为G
str2 = str1.replace('g', 'G')
print('str1:', str1)
print('str2:', str2)

# 2. 将str1中的第一个good 改为 GOOD
str3 = str1.replace('good', 'GOOD', 1)
print('str3:', str3)
