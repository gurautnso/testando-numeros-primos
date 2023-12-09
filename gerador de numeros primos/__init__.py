breakpoint()
try:
    a = open('numbers.txt', 'rt')
    a.close()
except (FileExistsError, FileNotFoundError):
    pasta = False
finally:
    pasta = True
if pasta is False:
    a = open('numbers.txt', 'wt+')
    a.close()
if pasta is True:
    a = open('numbers.txt', 'rt')
    for c in a:
        nums = c.split(';')
    n = nums[-1]
    nums = ''
else:
    n = int(input('Digite um numero:'))
nl = 51
ne = 2
primos = 0
if n > 114:
    nl = 38
    ne = 3
    if n > 1_021:
        nl = 31
        ne = 4
        if n > 10_016:
            nl = 26
            ne = 5
            if n > 100_017:
                nl = 22
                ne = 6
print(f'{"1":>{ne}}', end=' ')
<<<<<<< HEAD
for c1 in range(n, n+1):
=======
for c1 in range(2, n+1):
    if n > 38:
        if c1 % nl == 0:
            print()
<<<<<<< HEAD
>>>>>>> parent of e0515c0 (save003)
=======
>>>>>>> parent of e0515c0 (save003)
    for c2 in range(2, c1+1):
        if c1/2 < c2:
            a = open('numbers.txt', 'at')
            a.write(f'\033[1:31m{c1:>{ne}}\033[m;')
            a.close()
            primos += 1
            break
        if c1 % c2 == 0:
            a = open('numbers.txt', 'at')
            a.write(f'{c1:>{ne}}')
            a.close()
            break
<<<<<<< HEAD
<<<<<<< HEAD
    if c1 % nl == 0:
        a = open('numbers.txt', 'at')
        a.write(f'\n')
        a.close()
a = open('numbers.txt', 'at')
a.write(f'\nTotal de primos:{primos}')
a.close()
=======
=======
>>>>>>> parent of e0515c0 (save003)
print(f'\nTotal de primos:{primos}')
>>>>>>> parent of e0515c0 (save003)
