from random import random

def gen(n):
    st = ''
    for i in range(n):
        z = random()
        if z < .5:
            st += 'a'
        else:
            st += 'b'
    print(st)

def genMorse(n):
    st = ''
    for i in range(n):
        z = random()
        if z < .5:
            st += '.-'
        else:
            st += '-...'
        st += '/'
    print(st)

while True:
    num = int(input('Number? '))
    gen(num)
    # genMorse(num)
