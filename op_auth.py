# 사칙연산
print(2 * 3)
print(2 / 3)
print(2 + 3)
print(2 - 3)
print(2 / 3.0)
print(2.0 / 3)
print(2.0 / 3.0)

# //(몫), **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# 몫, 나머지 동시에 값을 반환
result, last = divmod(2, 3)     # tuple을 리턴 => 자동으로 언패킹
print(result, last)

t = divmod(2, 3)
print(t, type(t))

# 연산자 우선순위
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

print(4 / 2 * 2)

# 보통 결합순서 왼 오
# 승수(**)는 결합순서 오 왼 => 2의 (3의 4승)승
print((2 ** 3) ** 4)
print(2 ** 3 ** 4)
print(2 ** (3 ** 4))
