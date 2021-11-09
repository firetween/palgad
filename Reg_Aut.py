from random import *
login=['']
password=['']


while 1:
    print('Registreerimine, autoriseerimine või välja')
    v=input('Sinu valik: ')
    if v=='r':
        v=input('Auto või ise?')
        login()
        if v=='a':
            autoreg()
        else:
            ise_reg()
        reg(login,password)
    elif v=='a':
        avtor(login,password)
    else:
        break

