"""
题目: 坐公交：假设坐公交需要买票上车，书写程序要求如下：
1. 如果有票则可以上车，否则不能上车
2. 上车后，如果有座位可以坐下，否则不能坐下。

思路:
1. 书写ticket是否和1相等，如果条件成立表示可以上车；否则不能上车；
2. 当`ticket == 1`条件成立的时候，书写判断能否坐下的if语句。
"""
# 方法1:
while True:
    ticket = int(input("请您出示车票:"))
    if ticket == 1:
        print('请上车!')
        seat = int(input('车上是否有剩余座位:'))
        if seat == 1:
            print('请入座!')
            break
        else:
            print('无座,请您扶好栏杆站好!')
            break
    else:
        print('请下车!')
        break

# 方法2
ticket = int(input("请您出示车票:"))
if ticket == 1:
    print('请上车!')
    seat = int(input('车上是否有剩余座位:'))
    if seat == 1:
        print('请入座!')
    else:
        print('无座,请您扶好栏杆站好!')
else:
    print('请下车!')

# 方法3
ticket = 1
seat = 1

if ticket == 1:
    print('有票，请上车')
    if seat == 1:
        print('有空座，坐下睡觉')
    else:
        print('没座位，站着睡')
else:
    print('没票，补票后才能上车')