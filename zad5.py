print("Zadanie 5")
print("\n")

print("A)")

zawartosc_pliku = open("notowania_gieldowe.txt", "r").read()
print(zawartosc_pliku)

print("\nB)")

with open("notowania_gieldowe.txt", "a") as file:
    file.write("\nALR, 113")

with open("notowania_gieldowe.txt", "r") as file:
    zawartosc_po_dopisaniu = file.read()
    print(zawartosc_po_dopisaniu)