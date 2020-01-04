# while循环
# 数字猜谜游戏
# number = 7
# guess = -1
# print("猜出那个数！")
# while guess != number:
#     guess = int(input("它是？"))
#     if guess == number:
#         print("Yes!")
#     elif guess < number:
#         print("猜大点")
#     elif guess > number:
#         print("猜小点")

# for遍历
# languages = ['c', 'c++', 'perl', 'python']
# for x in languages:
#     print(x)

# 可以用range()函数来创建一个列表
# print(list(range(5)))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
print(parrot(1000))
print(parrot(voltage=1000))
