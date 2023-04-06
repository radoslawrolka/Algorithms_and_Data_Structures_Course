"""
RADOSLAW ROLKA
Sprawdza 2 palindromy w jednym obiegu petli (main loop).

Dla parzystej dlugosci napisu ustawia srodki palindromu (mid_char[]) na obie wewnetrzne litery napisu.
Nieparzysty: sprawdza dlugosc palindromu dla srodkowej litery napisu, potem ustawia srodki na prawo i lewo (mid_char).

Sprawdzam czy moze istniec wiekszy palindrom, jesli nie to zwracam najwiekszy znaleziony (maks_len).
Dla każdego środka ustawiam ll,lp,pl,pp (Lewy srodek Lewa granica, Lewy srodek Prawa granica, ...)
    i sprawdzamy odpowiednie litery, przesuwamy granice, inkrementujemy dlugosc.
Po skonczonych obiegach petli (while) przesuwamy mid_chary blizej krancow napisu.
time complexity: O(n^2)
"""

from zad1testy import runtests

def ceasar(s):
    maks_len = 1
    length = 1
    n = len(s)

    if n % 2 == 0:
        mid_char = [n // 2, (n // 2) + 1]
    else:
        mid_char = n // 2
        for i in range(1, (n-1)//2 +1):
            if s[mid_char + i] != s[mid_char - i]:
                break
            else:
                length += 2
        if maks_len < length:
            maks_len = length
        mid_char = [mid_char - 1, mid_char + 1]

    for mid_char[1] in range(mid_char[1],n):
        if maks_len >= mid_char[0]*2+1:
            return maks_len

        else:
            ll = mid_char[0] - 1
            lp = ll + 2
            pl = mid_char[1] - 1
            pp = pl + 2

            length = 1
            while ll >= 0:
                if s[ll] != s[lp]:
                    break
                else:
                    ll -= 1
                    lp += 1
                    length += 2
            if maks_len < length:
                maks_len = length

            length = 1
            while pp < n:
                if s[pl] != s[pp]:
                    break
                else:
                    pl -= 1
                    pp += 1
                    length += 2
            if maks_len < length:
                maks_len = length
            mid_char[0] -= 1

    return maks_len

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
