import sys

l = sys.argv[-1]
st = ""
out = ""

if len(sys.argv) < 2:
    sys.exit()
for i in sys.argv:
    if i != "exec.py":
        if i != l:
            st += i + ' '
        else:
            st += i

for x in reversed(st):
    if x.isupper():
        out += x.lower()
    if x.islower():
        out += x.upper()
    if x == ' ':
        out += ' '
print(out)
