n = int(input("Ile liczb chcesz wpisac? : "))
liczby = []

for x in range(n):
    x = int(input("Wprowadz liczbe: "))
    liczby.append(x)

for liczba in liczby:
    print("Element:", liczba, "Index: ", liczby.index(liczba))