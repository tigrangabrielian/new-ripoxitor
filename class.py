s = 'aaaabbсaa'
r = ''
for i in s:
    if not len(r):
        r = i + '1'
    else:
        if i == r[-2]:
            r = '{}{}'.format(r[:-1], int(r[-1]) + 1)
        else:
            r = '{}{}{}'.format(r, i, '1')

print(r)
