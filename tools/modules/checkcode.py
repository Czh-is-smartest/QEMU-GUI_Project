import random as r


def code(x=1):
    checkcode = ''
    for j in range(x):
        for i in range(4):
            index = r.randrange(0, 4)
            if index != i and index + 1 != i:
                checkcode += chr(r.randint(97, 122))
            elif index + 1 == i:
                checkcode += chr(r.randint(65, 90))
            else:
                checkcode += str(r.randint(1, 9))
    return checkcode


if __name__ == '__main__':
    print('验证码：' + str(code(11)))
