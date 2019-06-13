# packing : tuple만 가능하다
t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking : tuple을 각 변수로 변환
a, b, c, d = t
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

# 에러 : 개수를 안맞추면 에러가 날 수 있음
# a, b, c = t
# a, b, c, d, e, f = t

# unpacking extended : 언패킹 확장
# 개수를 안맞춰도 되게 잔처리(*)
t = (1, 2, 3, 4, 5)
a, *b = t               # a에 하나만 받고 b에 나머지를 다 받는다
print(a, b)
print(type(a), type(b)) # 잔처리(*)는 list로 받는다

*a, b = t
print(a, b)             # b에 하나만 받고 나머지는 a에 다 받는다
print(type(a), type(b))

a, b, *c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)


# cf. 여러개 파라미터를 받는 함수
def mysum(*num):
    s = 0
    for i in num:
        s += i
    return s


print(mysum(1, 2))
print(mysum(1, 2, 3))
print(mysum(1, 2, 3, 4, 5, 6))

# c의 printf 만들어보기
# printf("name: %s, age: %d", "둘리", 10)
# 결과
# name: 둘리, age: 10
