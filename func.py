# -*- coding utf-8 -*-
def sum8(a, b):
    des = 0
    sum = []
    intsum = ''
    if int(a) >= int(b):
        l1, l2 = list(a), list(b)
    else:
        l1, l2 = list(b), list(a)

    while l1:
        x, y = int(l1.pop()), int(l2.pop()) if l2 else 0
        unit = x + y
        unit = unit + des
        # print(unit + des)
        des = 0
        if int(unit) >= 8:
            des = 1
            unit = int(unit) - 8  #  не нужен int ?
        sum.append(unit)
    else:
        sum.append(des) if des == 1 else sum

    for i in sum[::-1]:
        intsum += str(i)

    # print(int(intsum))
    return int(intsum)


def dif8(a,b):
    des = 0
    dif = []
    intdif = ''
    if int(a) >= int(b):
        l1, l2 = list(a), list(b)
        znak = 1
    else:
        l1, l2 = list(b), list(a)
        znak = -1
    while l1:
        x = int(l1.pop()) - des
        y = int(l2.pop()) if l2 else 0
        if x < y:
            x += 8
            des = 1
        else:
            des = 0
        unit = x - y
        dif.append(unit)

    for i in dif[::-1]:
        intdif += str(i)

    # print(int(intdif) * znak)
    return int(intdif) * znak

def decimalconv(a):
    res = 0
    a = list(enumerate(list(str(a)[::-1])))
    for x,y in a:
        res += (int(y)) * (8 ** x)
    # print(res)
    return res

def

if __name__ == '__main__':

    # print('\nASSERT sum8():')
    assert sum8('123','456') == 601
    assert sum8('55511', '1257') == 56770
    assert sum8('2233', '455454545') == 455457000
    assert sum8('4752', '4752') == 11724
    assert sum8('10000', '777') == 10777

    # print('\nASSERT dif8():')
    assert dif8('456','123') == 333
    assert dif8('4567','123') == 4444
    assert dif8('4511','123') == 4366
    assert dif8('4501','123') == 4356
    assert dif8('4001','123') == 3656
    assert dif8('123','4001') == -3656
    assert dif8('437','4562') == -4123
    assert dif8('4752', '4752') == 0
    assert dif8('4752', '4751') == 1
    assert dif8('10000', '777') == 7001
    assert dif8('100', '7') == 71

    # print('\nASSERT decimalconv():')
    assert decimalconv(15) == 13

    print('TEST COMPLETE!')