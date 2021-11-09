import random
log_list=['A','B','C'] #login
pass_list=[''] #password


def login(l:list, p:list):
    n=input('Sisesta oma kasutaja nimi autoriseerimiseks: ')
    #t=login(n,l) 
    print(l)
    while n not in l:
        print('Here')
        n=input('Sisesta veel kord oma nimi: ')
    #while t!=True:
    #    print(t)
    #    n=input('Sisesta veel kord oma nimi: ')
    else:
        pass

#def login(l: list):
#    """Sisestatud nimi otsing

#    Tagastab olemasolek järjendis bool formaadis

#    :param str n:otsitav nimi
#    :rtype: bool

#    """
#    n=(input('Sisesta oma nimi: '))
#    t=0
#    if n in log_list:
#        t=true
#    return t


def ise_reg():
    pass


def auto_reg():
    """Salasõna genireerimine

    Tagastab salasõna str formaadis

    :rtype: str

    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    pas = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(pas)
    return pas


def avtor(l:list, p:list):
    n=input('Sisesta oma kasutaja nimi autoriseerimiseks: ')
    t=login(n,l)
    while t!=True:
        n=input('Sisesta veel kord oma nimi: ')
    else:
        pass


def reg(v: str, l: list, p: list):
    """Registreerimine

    Tagastab logini ja salasõnade listid

    :param str v: kasutaja parooli loomise viis
    :rtype: list, list

    """
    t=login(input('Sisesta oma kasutaja nimi: '))
    while t==True:
        t=login(input('Sisesta veel kord oma kasutaja nimi, andmebaasis on selline nimi:'))
    if v=='a':
        pas=auto_reg()
    else:
        ise_reg()
    return l,p

while 1:
    print('Registreerimine, autoriseerimine, registreerimine või välja: "a", "r" või "v"')
    v=input('Sinu valik: ')
    if v=='a':
        t=login(log_list, pass_list)
        #reg(input('Auto või ise?'))
    elif v=='r':
        t=avtor(log_list, pas_list)#True, False
        if t:
            print('Tere tulemast')
        else: v=input('Kas tahad registreerida?')
        if v=='jah':
            print('Registreerimine')
        else:
            pass
    elif v=='v':
        print('Head aega!')
        break
    else:
        break

