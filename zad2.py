print("Zadanie 2")
print("\n")

x = int(input("Wprowadź liczbę x: "))
y = int(input("Wprowadź liczbę y: "))
z = int(input("Wprowadź liczbę z: "))

if x > y and x > z:
    if y > z:
        print(f"Porządek liczb od najmniejszej do najwiekszej: {z}, {y}, {x}")
    elif z > y:
        print(f"Porządek liczb od najmniejszej do najwiekszej: {y}, {z}, {x}")
elif y > x and y > z:
    if x > z:
        print(f"Porządek liczb od najmniejszej do najwiekszej: {z}, {x}, {y}")
    elif z > x:
        print(f"Porządek liczb od najmniejszej do najwiekszej: {x}, {z}, {y}")
elif z > x and z > y:
    if x > y:
        print(f"Porządek liczb od najmniejszej do najwiekszej: {y}, {x}, {z}")
    elif y > x:
        print(f"Porządek liczb od najmniejszej do najwiekszej: {x}, {y}, {z}")


