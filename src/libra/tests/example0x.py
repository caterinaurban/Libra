
x: float = float(input())
y: float = float(input())

if x < 0 or y < 0 or x > 1 or y > 1:
    raise ValueError

h1: float = 1*x - 1*y + 1
h2: float = 2*y - 1*x + 1
#
h1 = h1 if h1 >= 0 else 0
h2 = h2 if h2 >= 0 else 0

o1: float = (4*h1) + (-1*h2) + 4
o2: float = -2*h1 + 3*h2 + 4
#
o1 = o1 if o1 >= 0 else 0
o2 = o2 if o2 >= 0 else 0

if o2 <= o1:
    raise ValueError
