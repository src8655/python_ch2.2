
results = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = n * n
    results.append(result)

print(results)

# 더 간결하게 할 수 있다
results = [n*n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 리스트
strings = [s for s in ['a', 'as', 'bar', 'car', 'dove', 'python'] if len(s) <= 2]
print(strings)

# 1~100 사이의 수 중에서 짝수 리스트
evens = [n for n in range(1, 101) if n % 2 == 0]
print(evens)

# set comprehension, 중복x 위해서
strings = {s for s in ['a', 'as', 'bar', 'car', 'dove', 'as', 'python'] if len(s) <= 2}
print(strings)

# 문자열 길이를 set으로 저장하기
strings = {len(s) for s in ['a', 'as', 'bar', 'car', 'dove', 'as', 'python']}
print(strings)

# dict comprehension
d = {s: len(s) for s in ['a', 'as', 'bar', 'car', 'dove', 'as', 'python']}
print(d)

#
# 369
#
[n for n in range(1, 1000) if '3' in str(n) or '6' in str(n) or '9' in str(n)]