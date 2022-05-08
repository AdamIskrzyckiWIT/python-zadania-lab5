import statistics

oceny = []


for x in range(5):
    x = int(input("Wprowadz ocene: "))
    oceny.append(x)

print("Srednia ocen: ", statistics.mean(oceny))
print("Mediana ocen: ", statistics.median(oceny))
print("Odchylenie standardowe ocen: ", statistics.stdev(oceny))