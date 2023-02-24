import sys

if len(sys.argv) < 2:
    sys.exit()
n = str(sys.argv[-1])
try:
    assert len(sys.argv) == 2, "Only one argument is allowed"
    assert bool(n.isnumeric()), "Argument is not a number"

    if int(n) % 2 == 0:
        print("Odd number")
    else:
        print("Even number")

except AssertionError as msg:
    print(msg)
