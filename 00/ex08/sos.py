import sys

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'Ñ':'--.--', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'}

text = str(sys.argv[1])
msg = []
for i in text:
    if i.islower():
        x = i.upper()
    else:
        x = i
    for letter, key in morse.items():
        if letter == x:
            msg.append(key)
count = 0
for m in msg:
    count += 1
    if count == len(msg):
        print(m)
    else:
        print(m, end=" / ")
