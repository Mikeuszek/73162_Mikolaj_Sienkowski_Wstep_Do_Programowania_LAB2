print("Zadanie 1")
print("\n")

punkty = int(input("Wprowadź zdobytą liczbę punktów."))

if punkty >= 80:
    print("Egzamin zaliczony w terminie 0.")
elif punkty > 50 and punkty < 80:
    print("Możliwa poprawa egzaminu.")
else:
    print("Musisz poprwawić egzamin.")

