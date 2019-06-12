# 객체의 대소의 비교
print(1 > 3)
print(2 > 4)

print(1 >= 3)
print(2 <= 4)

print(6 == 9)
print(6 != 9)

# 복합관계
a = 6
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 객체 비교
print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 2, 4] < [1, 3, 1])

# error
# tuple 을 list로
# print([1, 2, 4] < (1, 3, 1))
print([1, 2, 4] < list((1, 3, 1)))

# 동질성 비교, 동일성 비교
a = 10
b = 20
c = a
d = 10
print(a == b)
print(a is b)
print(a is c)
print(a == c)
print(a == d)
print(a is d)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)

# 논리의 계산 순서
print([] or 'logical')
print('logical' or 'operator')
print('' or 'operator')
print('' and 'operator')
print(None and 1)
print(None or [])
print('ok')


def f(msg=None):
    msg and print(msg)

f()
f('hello world')

# def f():
#     print('execution!!!!!')
#
# 1 + 2 > 10 and f()

