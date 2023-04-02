a = 26
for i in range(1, a + 1):
    print(' ' * (a - i) + '*' * (i != 1) + ' ' * (2 * i - 3) * (i < a) + '*' + '*' * (2 * i - 3) * (i == a))
print('----'*20, a)

for i in range(a, 0, -1):
    print(' ' * (a - i) + '*' * (i != 1) + ' ' * (2 * i - 3) * (i < a) + '*' + '*' * (2 * i - 3) * (i == a))
print('----' * 20, a)

for i in range(1, a + 1):
    print(' ' * (a - i) + '*' * (i != 1) + ' ' * (2 * i - 3) + '*')
for i in range(a - 1, 0, -1):
    print(' ' * (a - i) + '*' * (i != 1) + ' ' * (2 * i - 3) * (i < a) + '*' + '*' * (2 * i - 3) * (i == a))
print('----'*20, a)
lines = a
# 打印上半
for i in range(lines):
    print("-" * (lines * 2 - 2 - 2 * i), end="")
    my_list = []
    for j in range(i + 1):
        my_list.append(chr(96 + lines - j))
    for j in range(i):
        my_list.append(chr(ord(my_list[-1]) + 1))
    print('-'.join(my_list), end="")
    print("-" * (lines * 2 - 2 - 2 * i))
# 打印下半
for i in range(lines - 1):
    print("-" * (2 * (i + 1)), end="")
    # 换一种方式初始化list列表
    my_list = [chr(96 + lines - j) for j in range(lines - 1 - i)]
    for j in range(lines - 2 - i):
        my_list.append(chr(ord(my_list[-1]) + 1))
    print('-'.join(my_list), end="")
    print("-" * (2 * (i + 1)))


for i in range(1,7):
    print(" " * 3 * (6 - i) + " " * 44 + "* " * i * 2)

for i in range(1,3):
    print(" " * i + " " * 44 + "* " * 6 * 2)

for i in range(1,7):
    print(" " * 3 * (6 - i) + " " * 22 + "* " * i * 2 + " " * 6 + "* " * 6 * 2)

for i in range(1,3):
    print(" " * i + " " * 22 + "* " * 6 * 2 + " " * 6 + "* " * 6 * 2)

for i in range(1,7):
    print(" " * 3 * (6 - i) + "* " * i * 2 + " " * 6 + "* " * 6 * 2 + " " * 6 + "* " * 6 * 2)

for i in range(1,3):
    print(" " * i + "* " * 6 * 2 + " " * 6 + "* " * 6 * 2 + " " * 6 + "* " * 6 * 2)
