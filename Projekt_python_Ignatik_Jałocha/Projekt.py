import tkinter, sys, math
def wyjdz():
    sys.exit()

def szyfruj1():
    z = e.get()
    z = z.replace(" ", "")  #Pomija spacje w tekście do zaszyfrowania
    klucz = s.get()
    # klucz = ord(klucz) - 48 Jesli trzeba bedzie wpisywac recznie
    n = z.upper()
    zaszyfrowany = ''
    for ch in n:
        if ord('A') <= ord(ch) <= ord('Z'): #Zamienia litery na wartości i sprawdza czy znajdują się pomiędzy A i Z
            kod = ord(ch) + klucz           # Dodaje do wartości danej litery wartość klucza co skutkuje, nową literą
        if kod > ord('Z'):                  #Jeśli litery wyjdą poza zakres alfabetu to liczenie kontynuuje się od początku
            kod -= 26
        zaszyfrowany += chr(kod)
    l.config(text=zaszyfrowany)

def deszyfruj1():
    z = e.get()
    klucz1 = s.get()
    # klucz = ord(klucz) - 48
    f = z.upper()
    odszyfrowany = ''
    for ch in f:
        if ord('A') <= ord(ch) <= ord('Z'): #Zamienia litery na wartości i sprawdza czy znajdują się pomiędzy A i Z
            kod = ord(ch) - klucz1          #Odejmuje od wartości danej litery wartość klucza co skutkuje, nową literą
        if kod < ord('A'):                  #Jeśli wartość litery będzie mniejsza od wartości 'A' odejmuje od 'Z'
            kod += 26
        odszyfrowany += chr(kod)
    l.config(text=odszyfrowany)

klucz2 = ["BACDFEHGJILKNMORSTPWUVYXZ", "ZXYVUWPTSROMNKLIJGHEFDCAB"]
def szyfruj2():
    g = e.get()
    z = g.upper()
    z = z.replace(" ", "")  #Pomija spacje w tekście do zaszyfrowania
    zaszyfrowany = ""
    if len(z) % 2 != 0:     #Sprawdza czy tekst ma parzystą długość, jeśli nie to dopisuje do niego X
        z += "X"
    p = 0
    while p < len(z):
        a1 = z[p]           #Przypisanie do a1 danej literki z tekstu wpisywanego przez użytkownika
        if p + 1 < len(z):
            a2 = z[p + 1]   #Przypisanie do a2 danej literki  tekstu wpisywanego przez użytkownika
            p += 2
        g1 = a1
        g2 = a2
        idx1 = klucz2[0].find(a1)   #Przypisanie do idx1 pozycji w pierwszym kwadracie na jakiej znajduje się literka z a1
        idx2 = klucz2[1].find(a2)   #Przypisanie do idx2 pozycji w drugim kwadracie na jakiej znajduje się literka z a2

        if math.floor(idx1/5) != math.floor(idx2/5):
            g1 = klucz2[0][((5 * math.floor(idx2/5)) + idx1 % 5)]   #Przypisanie do g1 litery z pierwszego kwadratu znajdujacej sie na miejscu wyniku dzialania
            g2 = klucz2[1][((5 * math.floor(idx1/5)) + idx2 % 5)]   #Przypisanie do g2 litery z pierwszego kwadratu znajdujacej sie na miejscu wyniku dzialania

        zaszyfrowany = zaszyfrowany + g1
        zaszyfrowany = zaszyfrowany + g2

    l.config(text=zaszyfrowany)

def deszyfruj2():       #Tak samo jak w szyfruj2(), z drobnym wyjątkiem na końcu
    f = e.get()
    z = f.upper()
    zaszyfrowany = ""
    if len(z) % 2 != 0:
        z += "X"
    p = 0
    while p < len(z):
        a1 = z[p]
        if p + 1 < len(z):
            a2 = z[p + 1]
            p += 2
        g1 = a1
        g2 = a2

        idx1 = klucz2[0].find(a1)
        idx2 = klucz2[1].find(a2)
        if idx2 == -1:
            idx2 = -idx2
        if math.floor(idx1/5) != math.floor(idx2/5):
            g1 = klucz2[0][((5 * math.floor(idx2/5)) + idx1 % 5)]
            g2 = klucz2[1][((5 * math.floor(idx1/5)) + idx2 % 5)]

        zaszyfrowany = zaszyfrowany + g1
        zaszyfrowany = zaszyfrowany + g2
        if zaszyfrowany[-1] is 'X':                 #Usuwanie X znajdującego się na końcu rozszyfrowanego tekstu
            zaszyfrowany = zaszyfrowany[:-1]
    l.config(text=zaszyfrowany)

def szyfruj3():
    tekst1 = e.get()
    klucz3 = s1.get()
    tekst = tekst1.upper()
    zaszyfrowany = ""
    tabelaplotek = [None]*klucz3        #Tworzy tablice klucz3-elementową wypełnioną None
    a = 0
    i = len(tekst)
    while a < klucz3:                   #Zastępuje w tablicy None i-elementową tablicą
        tabelaplotek[a] = [None] * i
        a += 1
    r = 0
    kierunek = 1
    a = 0
    for c in range(len(tekst1)):
        tabelaplotek[r][a] = tekst[c]   #Przypisuje daną literę z tekstu do odpowiedniego miejsca w odpowiedniej tablicy w tabelaplotek
        if (r == klucz3 - 1) & (kierunek == 1) | (r == 0) & (kierunek == -1):  #Weryfikacja do której tabeli przypisać literę
            kierunek = -kierunek
            a += 1
        r += kierunek
    for x in range(klucz3):
        poz = 0
        while poz < len(tekst):
            if tabelaplotek[x][poz] is None:        #Usuwa None
                tabelaplotek[x][poz] = ''
            zaszyfrowany = zaszyfrowany + tabelaplotek[x][poz]  #Zapisuje do zaszyfrowany litery z tabelaplotek
            poz += 1
    l.config(text=zaszyfrowany)

def deszyfruj33(): # Kod pomocniczy do deszyfracji kodu płotkowego. Szyfruje wiadomość kodem płotkowym o kluczu wybieranym przez użytkownika
    tekst = e.get()
    klucz = s1.get()

    tabelaplotek = [None]*klucz
    a = 0
    i = len(tekst)
    while a < klucz:
        tabelaplotek[a] = [None]*i
        a += 1
    r = 0
    kierunek = 1
    a = 0
    for c in range(len(tekst)):
        tabelaplotek[r][a] = [ c , tekst[c] ]
        if(r == klucz - 1) & (kierunek == 1) | ( r == 0) & (kierunek == -1):
            kierunek = -kierunek
            a += 1
        r += kierunek

    asd = 0
    tabliczka = [None]*i
    s = 0
    for x in range(klucz):
        for y in range(i):
            if tabelaplotek[x][y] is None:
                asd += 1
            else:
                tabliczka[s] = tabelaplotek[x][y]
                s += 1



    return tabliczka
def deszyfruj3():
    tekst = e.get()
    zaszyfrowany3 = ''
    tabliczkatekstu = [None]*len(tekst)         #Tworzy nam tabele wypełnioną None z ilością elementów rownej długości szyfrowanego tektu
    for x in range(len(tekst)):                 #Tworzy nam liczbe tablic dwuelementowych równą długości szyfrowanego tekstu w tablicy
        tabliczkatekstu[x] = [None]*2
        tabliczkatekstu[x] = [ x , tekst[x] ]   #Nadawanie indeksu literom

    tabliczkaiksu = deszyfruj33()               #Przypisanie wpisanego tekstu zaszyfrowanego do tabliczkaiksu, również posiadającego indeksy przypisane dla każdej litery
    i = len(tekst)
    tabliczkaczekoladek = [None]*i



    for x in range(i):
        for y in range(i):
            if tabliczkatekstu[x][0] == tabliczkaiksu[y][0]:    #Sprawdza czy indeks litery w tabliczkatekstu jest rowny indeksowi litery w tabliczkaiksu
                tabliczkaczekoladek[x] = tabliczkatekstu[y][1]  #Jeśli tak to przypisyje do miejsca x tą literę
    for x in range(i):
        zaszyfrowany3 += tabliczkaczekoladek[x]
    l.config(text = zaszyfrowany3)


main = tkinter.Tk()
l = tkinter.Label(main, text="Wprowadz tekst")
l1 = tkinter.Label(main, text="Wprowadz klucz dla przestawieniowego:")
l2 = tkinter.Label(main, text="Wprowadz klucz dla plotkowego:")
l3 = tkinter.Label(main, text = "Szyfr Dwukwadratowy:")
e = tkinter.Entry(main, justify="center")
s = tkinter.Scale(main, orient="horizontal", from_=0, to=25)
s1 = tkinter.Scale(main, orient="horizontal", from_=2, to=7)
b = tkinter.Button(main, text="Zakończ", command=wyjdz)
b1 = tkinter.Button(main, text="Szyfrowanie Podstawieniowy", command=szyfruj1)
b2 = tkinter.Button(main, text="Deszyfracja Podstawieniowy", command=deszyfruj1)
b3 = tkinter.Button(main, text="Szyfrowanie Dwukwadratowy", command=szyfruj2)
b4 = tkinter.Button(main, text="Deszyfracja Dwukwadratowy", command=deszyfruj2)
b5 = tkinter.Button(main, text="Szyfrowanie Plotkowy", command=szyfruj3)
b6 = tkinter.Button(main, text="Deszyfrowanie Plotkowy", command=deszyfruj3)

l.pack()
e.pack()
l1.pack()
s.pack()
b1.pack()
b2.pack()
l2.pack()
s1.pack()
b5.pack()
b6.pack()
l3.pack()
b3.pack()
b4.pack()
b.pack(side = "bottom")

main.mainloop()
