import random
log_list=['A','B','C'] #login
pass_list=[''] #password


def login(n: str, l: list):
    """Sisestatud nimi otsing

    Tagastab olemasolek järjendis bool formaadis

    :param str n:otsitav nimi
    :rtype: bool

    """
    if n in l:
        t=true
    return t


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


def avtor():
    return a



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
    print('Registreerimine, autoriseerimine või välja: a või v')
    v=input('Sinu valik: ')
    if v=='a':
        reg(input('Auto või ise?'))
    elif v=='a':
        t=avtor()#True, False
        if avtor(login,password):
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

