
index = 0
for color in ['yellow', 'blue', 'black', 'white']:
    print('{0}:{1}'.format(index, color))
    index += 1

# 이럴 필요 없이
for index, color in enumerate(['yellow', 'blue', 'black', 'white']):
    print('{0}:{1}'.format(index, color))
    index += 1