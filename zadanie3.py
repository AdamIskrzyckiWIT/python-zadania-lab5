import random

liczby_urzytkownika = []
losy = []

def trafione(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

for x in range(6):
    x = int(input("Wprowadz liczbe od 1 do 49: "))
    if(x >= 1 and x <= 49):
        liczby_urzytkownika.append(x)
    else:
        print("Liczba wychodzi poza zakres")
        liczby_urzytkownika = []
        break

for y in range(6):
    y = random.randint(1, 49)
    losy.append(y)

print("Twoje typy: ", liczby_urzytkownika)
print("Losy lotto: ", losy)

wynik = trafione(liczby_urzytkownika, losy)

print("Trafione liczby: ", wynik)
print("Trafiles ", len(wynik), " liczb")