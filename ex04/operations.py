import sys

if len(sys.argv) < 2:
    sys.exit()
n1 = str(sys.argv[1])
if len(sys.argv) == 2:
    print("Two arguments are required")
    sys.exit()
else:
    n2 = str(sys.argv[2])
try:
    assert len(sys.argv) <= 3, "Only one argument is allowed"
    assert bool(n1.isnumeric()), "Argument 1 is not a number"
    assert bool(n2.isnumeric()), "Argument 2 is not a number"

    print(f"Sum:        {int(n1) + int(n2)}")
    print(f"Difference: {int(n1) - int(n2)}")
    print(f"Product:    {int(n1) * int(n2)}")
    if int(n2) == 0:
        print(f"Quotient:   ERROR (division by zero)")
        print(f"Remainder:  ERROR (modulo by zero)")
    else:
        print(f"Quotient:   {int(n1) / int(n2)}")
        print(f"Remainder:  {int(n1) % int(n2)}")

except AssertionError as msg:
    print(msg)
