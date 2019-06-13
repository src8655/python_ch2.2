# 한 줄 문자열 정의
s = ''
str1 = 'Hello World'
print(type(s), type(str1))
print(isinstance(str1, str))

# 여러줄 문자열
str2 = '''ABC
123
가나다라
'''
print(str2)

# escape
print("Hello\nWorld\nI Say \"Hello World\"")
print('Hello\nWorld\nI Say "Hello World"')

#
# 문자열 연산
#

# 인덱싱
str1 = 'First String'
str2 = 'Second String'

# 1. 인덱싱
print(str1[0], str1[1], str2[2])
print(str1[-1], str1[-2], str1[-3])

# 2. 슬라이싱
# s[start:stop:step]
str3 = str2[2:5]
print(str3)
print(str2[2:len(str2)])
print(str2[2:])

s = 'Python'
print(s[-1])        # 마지막 문자
print(s[-2:])       # 마지막 2개 문자
print(s[:-2])       # 마지막 2개 문자를 제외한 전체 문자열

print(s[::-1])      # reverse
print(s[1::-1])     # 1번째, 2번째 문자 == s[1:0:-1]
print(s[:-3:-1])    # 마지막 2개 문자
print(s[-3::-1])    # 마지막 2개 문자 제외한 전체 문자열

# 연결(+)
print(str1 + ' ' + str2)
str3 = '1st' + ' ' + '2nd'
str3 = '1st' ' ' '2nd'
print(str3)

# 문자열 객체 연결은 문자열끼리만 할 수 있다.
name = '둘리'
age = 10
# print(name + age) # 비정상 종료 됨

# 반복
print(str1 * 3)

# len() 함수
print(len(str1))

# in, not in 연산
print('F' in str1)
print('S' not in str1)

# str 객체는 Immutable이다
# str1[0] = 'f' # 비정상 종료 됨

# 서식(formatting) = format 함수
print('name:' + name + ', age:' + str(age))
print('name:' + format(name, 's') + ', age:' + format(age, 'd'))

# 서식 : 튜플을 사용한 방식
f = 'name: %s, age: %d'
print(f % (name, age))
print(f % ('또치', 20))

# 서식 : 딕셔너리를 사용한 방식
f = 'name: %(n)s, age: %(a)d'
print(f % {'n':'둘리', 'a':10})
print(f % {'n':'또치', 'a':20})

#
# 객체함수
#

# 1. 대소문자 관련
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 2. 검색
s = 'I Like Python, I Like Java Also'
print(s.count('Like'))
print(s.find('Like'))
print(s.find('Like', 5))
print(s.find('JavaScript'))     # -1을 출력
print(s.rfind('Like'))

# 발견하지 못하면 예외발생
print(s.index('Like'))
# print(s.index('JavaScript'))    # 익셉션 : 비정상 종료 됨
print(s.rindex('Like'))
print(s.startswith('I Like'))
print(s.startswith('Like', 17))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))    # 0~25 => I Like Python, I Like Java

# 편집과 치환
s = '   spam and ham    '
print('------' + s.strip() + '------')
print('------' + s.rstrip() + '------')
print('------' + s.lstrip() + '------')

s = '<><abc><><defg><><>'
print('------' + s.strip('<>') + '------')  # 끝에있는 것만 사라짐
print('------' + s.strip('><') + '------')  # 윗줄과 결과가 같다 => 문자 하나 별로 비교해 지운다

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 분리 & 결합
s = 'spam and ham'
l = s.split(' and ')
print(l, type(l))

s2 = ':'.join(l)
print(s2, type(s2))

s3 = 'one:two:three:four:five'
print(s3.split(':'))
print(s3.split(':', 2))
print(s3.rsplit(':', 2))

lines = '''1st line
2nd line
3rd line
4th line
'''
print(lines.split('\n'))
print(lines .splitlines())  # 맨 끝에 하나만 없앤다

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcd'.isdigit())

print('abcd'.islower())
print('ABCD'.isupper())

print('     '.isspace())
print('\r\n'.isspace())
print('\t'.isspace())

# '0' 채우기
print('20'.zfill(5))
print('1234'.zfill(5))

# 서식: 객체함수
print('name:{}, age:{}'.format('둘리', 10))
print('name:{0}, age:{1}'.format('둘리', 10))
print('name:{1}, age:{0}'.format(10, '둘리'))
print('{:3}의 제곱근은 {:.7}'.format(2, 2**0.5))
print('name:{n}, age:{a}'.format_map({'a':20, 'n':'둘리'}))
