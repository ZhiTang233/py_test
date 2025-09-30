# 1.定义score变量记录考试分数
score = int(input('请输入你的分数'))
# 2. 如果分数是大于等于90 优
if score >= 90:
    print('优')
# 3. 如果分数是大于等于80 且 小于90 良
if (score >= 80) and score < 90:
    print('良')
# 4. 如果分数是大于等于70 且 小于80 中
if (score >= 70) and score < 80:
    print('中')
# 5. 如果分数是大于等于60 且 小于70 差
if (score >= 60) and score < 80:
    print('差')
# 6. 其他分数显示不及格
if score < 60:
    print('不及格')

