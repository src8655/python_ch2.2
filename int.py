# 10진
a = 23
print(a, type(a))
print(isinstance(a, int))
print(isinstance(a, float))

# 2진, 8진, 16진, 상수(literal)
b = 0b1101
c = 0o23
d = 0x23
print(b, c, d)

# 3.x int가 long이 합쳐졌다. (무한대 표현범위)
e = 2 ** 1024   # ** : pow 승수
print(e)
print(type(e))

# 변환변수
print(oct(38))
print(hex(38))
print(bin(38))