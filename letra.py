dobasok = [3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4, 5, 4]


print("2. feladat")
osszeg = 0
for szam in dobasok:
    osszeg += szam
    if osszeg % 10 == 0:
        osszeg -= 3
    elif osszeg > 45:
        print(osszeg)
        break
    print(osszeg, end=" ")
print("\n4. feladat")
if osszeg >= 45:
    print("A játékot befejezte")
