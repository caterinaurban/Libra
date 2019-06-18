
# assume(0 <= x <= 1 and 0 <= y <= 1)

h1 = 1*x - 1*y + 1
h2 = 2*y - 1*x + 1
#
ReLU(h1)
ReLU(h2)

o1 = (4*h1) + (-1*h2) + 4
o2 = -2*h1 + 3*h2 + 4
#
ReLU(o1)
ReLU(o2)
