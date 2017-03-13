# -*- coding:UTF-8 -*-

# 2017.03.04 13:30
# n个人依次报数，第3号退出圈子

a = []
count = int(input("请输入人数："))
a = [i for i in range(1, count + 1)]
#a = [0, 1, 2, 3, 4, 5, 6]

flag = 1
i = 0

while len(a) > 1:
    #print(a)

    if flag == 3:
        #print('del %s' % a[i])
        a.remove(a[i])
        i -= 1
        flag = 1
    else:
        flag += 1

    if i >= len(a) - 1:
        i = 0
    else:
        i += 1

print(a)

exit()

# or

i = 0
k = 0
m = 0

while m < count - 1:
    if a[i] != 0:
        k += 1
    if k == 3:
        a[i] = 0
        k = 0
        m += 1
    i += 1
    if i == count:
        i = 0
    #print(a)
i = 0
while a[i] == 0:
    i += 1
print(a)

exit()

# or  使用余数
f = 0
def dele33(f, list):
    print(a)
    b = []
    for i in range(1, len(list)+1):
        if (i + f) % 3 == 0:
            b.append(a[i-1])
    f = (len(list) +f) % 3

    print('delete : %s ' % b)

    for c in b:
        a.remove(c)

    if len(a) <= 1:
        return

    dele33(f, a)


dele33(f, a)

exit()

# or

l = 0
def dele3(flag, n):
    b = []
    if n < 3:
        print(a[-1])
        return
    for i in range(0, n):
        if flag > 0 and flag % 3 == 0 and i != 0:
            b.append(a[i])
            flag = 0
        if flag > 3:
            flag %= 3
        if i != 0:
            flag += 1

    for j in range(len(b)):
        a.remove(b[j])

    l = flag
    print("a = ", a)
    return dele3(l, len(a))


dele3(l, len(a))


