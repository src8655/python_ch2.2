# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

# 접근
print(d['basketball'])  # 없는 키일 때 에러나는 문제

# 변경가능
d['balleyball'] = 6
print(d)

# 반복(*), 연결(+) 지원하지 않는다(sequence형이 아니기 때문에)

# 길이
print(len(d))

# in, not in 가능 : 키만 가능
print('soccer' in d)
print('balleyball' in d)

#
# 다양한 dict 객체 생성 방법
#

# 1. literal
d = {}
print(type(d))

# 2. dict() 사용하는 방법1
d = dict()
print(d)

# 3. dict() 사용하는 방법2
d = dict(one=1, two=2, three=3)
print(d)

# 4. dict() 사용하는 방법3
d = dict([('one', 1), ('two', 2), ('three', 3)])
print(d)

# 5. dict() 사용하는 방법4 - zip를 사용하는 방법
keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)

# 다양한 key 타입
d = {}

d[True] = 'true'
d[10] = '10'
d['twenty'] = 20
d[(1, 2, 3)] = 6
# d[[1, 2, 3]] = 6      # 에러발생

print(d)

# keys 객체
keys = d.keys()
print(keys, type(keys))
for key in keys:
    print('{0}:{1}'.format(key, d[key]))

# values 객체
values = d.values()
print(values, type(values))

items = d.items()
print(items, type(items))

# 카피1
phone = {
    '둘리': '000-0000-0000',
    '마이콜': '111-1111-1111',
    '또치': '222-2222-2222'
}

p = phone
print(p)
print(phone)

p['도우넛'] = '333-3333-3333'
print(p)
print(phone)

# 카피2
phone = {
    '둘리': '000-0000-0000',
    '마이콜': '111-1111-1111',
    '또치': '222-2222-2222'
}
p = dict(phone)
print(p)
print(phone)

# get() 함수
# get을 사용하는 이유 : 없는 키를 사용 시 get은 오류를 뿜어내지 않는다.
# print(phone['도우넛'])
print(phone.get('도우넛'))

# setDefault
# get 차이점은 실제로 데이터를 저장한다
phone.setdefault('도우넛', '333-3333-3333')
print(phone)

# 삭제
print(phone.pop('둘리'))
print(phone)

# 튜플로 가져오기
item = phone.popitem()
print(item, type(item))
print(phone)

# 업데이트
phone.update({
    '도우넛': '333-3333-3333',
    '또치': '444-4444-4444'
})
print(phone)

# 모두 삭제하기
phone.clear()
print(phone)
