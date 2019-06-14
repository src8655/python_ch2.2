
# 순서없는 set이라 매칭이 잘 안됨
# seq1 = {'foo', 'bar', 'baz'}
# seq2 = {'one', 'two', 'three'}

# 순서가 있는 튜플로 해야함
seq1 = ('foo', 'bar', 'baz', 'baz')
seq2 = ('one', 'two', 'three', 'three')

z = zip(seq1, seq2)
print(z, type(z))

for t in z:
    print(t)

