# 튜플 생성
t = ()      # 공튜플
t = (1,)    # 항목이 하나일 때는 1 이라는 정수로 보니까 콤마를 사용
t = (1, 2, 3)
print(t, type(t))

#
# sequence 지원 연산
#

# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])
print(t[::-1])

# 반복
print(t * 2)

# 연결
print(t + (4,))

# 길이
print(len(t))

# 확인
print(4 in t)
print(4 not in t)

# 튜플은 수정이 안된다 : 에러발생
# t[0] = 100

# 여러개 값의 대입
x, y, z = 10, 20, 30
print(x, y, z)

# swap
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

#
# 객체함수 : 많지않다(immutable이기 때문에)
#
t = (20, 30, 10, 20)
print(t.index(20))
print(t.index(20, 2))
print(t.count(20))

# 변환
t = (1, 2, 3, 3)
print(t)

s = set(t)      # 튜플 -> 세트로 변환
print(s, type(s))

l = list(t)     # 튜플 -> 리스트로 변환
print(l, type(l))

t = tuple(l)    # 리스트 -> 튜플로 변환
print(t, type(t))

