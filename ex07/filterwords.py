import sys

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()

cadena = str(sys.argv[1])
number = int(sys.argv[2])

cadena2 = cadena.split(" ")
cadena3 = []
for i in cadena2:
    if len(i) >= number:
        cadena3.append(i)
print(cadena3)

