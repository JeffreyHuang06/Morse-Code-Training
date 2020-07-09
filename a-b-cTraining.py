from random import random

def gen(n):
    st = ''
    for i in range(n):
        z = random()
        if z < .3333:
            st += 'a'
        elif z < .6666:
            st += 'b'
        else:
            st += 'c'
    print(st)

def genMorse(n):
    st = ''
    for i in range(n):
        z = random()
        if z < .3333:
            st += '.-'
        elif z < .6666:
            st += '-...'
        else:
            st += '-.-.'
        st += ' / '
    print(st)

while True:
    num = int(input('Number? '))

    morse = False

    if not morse:
        gen(num)
    else:
        genMorse(num)
