n = int(input('Digite um numero:'))
nl = 51
ne = 2
primos = 0
if n > 114:
    nl = 38
    ne = 3
    if n > 1021:
        nl = 31
        ne = 4
        if n > 10016:
            nl = 26
            ne = 5
            if n > 100017:
                nl = 22
                ne = 6
print(f'{"1":>{ne}}', end=' ')
for c1 in range(2, n+1):
    if n > 38:
        if c1 % nl == 0:
            print()
    for c2 in range(2, c1+1):
        if c1/2 < c2:
            print(f'\033[1:31m{c1:>{ne}}\033[m', end=' ')
            primos += 1
            break
        if c1 % c2 == 0:
            print(f'{c1:>{ne}}', end=' ')
            break
print(f'\nTotal de primos:{primos}')
