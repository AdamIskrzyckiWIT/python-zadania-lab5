liczba1 = int(input('Wprowadz pierwsza liczbe  : '))
liczba2 = int(input('Wprowadz druga liczbe : '))
liczba3 = int(input('Wprowadz trzecia liczbe  : '))

min = 0

if liczba1 < liczba2 and liczba1 < liczba3 :
    min = liczba1
elif liczba2 < liczba3 :
    min = liczba2
else :
    min = liczba3

print(min, " jest najmniejsza liczba sposrod wprowadzonych")