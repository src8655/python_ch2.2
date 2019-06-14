seq = range(10)
print(seq, type(seq))
print(list(seq[5:]))
print(len(seq))

for i in seq:
    print(i, end=' ')
else:
    print()

for i in range(9, -1, -1):
    print(i, end=' ')
else:
    print()

print('ok')
