import random


def levo():
    s_levo = []
    for i in range(3, 21):  # 21
        s_levo.append(i)
    c_levo = random.choice(s_levo)
    return c_levo


result_0 = []
# print(result,type(result))
l = levo()
print('число слева: ',l)
# l=20
for i in range(1, 21):  # 21
    if i == l:
        break
    for j in range(2, 20):  # 20
        # r = i + j
        if j == l or j <= i:
            continue
        # elif i>j:
        #    continue
        elif l / (i + j) == l // (i + j):
            # else:
            #    r=i+j
            #    print(i, j, r, l/r, l//r)
            # if l/r == l//r:
            result_0.append(f'{str(i)}{str(j)}')
            result = ''.join(result_0)
print('пароль: '+result)
