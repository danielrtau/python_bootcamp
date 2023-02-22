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
        if i.find(',') != -1 or i.find('.') != -1:
            y = i[0:-1]
            cadena3.append(y)
        else:
            cadena3.append(i)
print(cadena3)

