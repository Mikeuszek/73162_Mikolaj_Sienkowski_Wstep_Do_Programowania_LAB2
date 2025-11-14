print("Zadanie 4")
print("\n")

print("A)")
gole =  int(input("Wprowadź liczbę goli strzelonych przez drużynę: "))
bonus = 0

if gole > 10:
    bonus = 10
elif gole > 5:
    bonus = 5

wynik = gole + bonus

print(f"Całkowity wynik wynosi: {wynik}")

print("\nB)")
gole2 =  int(input("Wprowadź liczbę goli strzelonych przez drużynę: "))
bonus2 = 0

if gole2 > 5:
    bonus2 = 5
    if gole2 > 10:
        bonus_calowity = bonus2 + 10
    else:
        bonus_calowity = bonus2

wynik2 = gole2 + bonus_calowity
print(f"Całkowity wynik wynosi: {wynik2}")