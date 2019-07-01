
x: float = float(input())
y0: float = float(input())
y1: float = float(input())

h1: float = -3*x - 1*y0 + 1*y1 + 1
h2: float = 2*y0 - 2*y1 - 1*x + 1
#
h1 = h1 if h1 >= 0 else 0
h2 = h2 if h2 >= 0 else 0

o1: float = (4*h1) + (-1*h2) + 4
o2: float = -2*h1 + 3*h2 + 4
#
# o1 = o1 if o1 >= 0 else 0
# o2 = o2 if o2 >= 0 else 0

print(o1, o2)
if o2 <= o1:
    raise ValueError
