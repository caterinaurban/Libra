
x = float(input())
y = float(input())

if x < 0 or y < 0 or x > 1 or y > 1:
    raise ValueError

h1 = 0.1*x - 0.1*y + 0.1
h2 = -0.1*x + 0.5*y + 0.1
h3 = 0.1*x + 0.6*y + 0.1
h4 = 0.2*x - 0.1*y + 0.1
h5 = -0.1*x + 0.2*y + 0.1
h6 = 0.3*x + 0.3*y + 0.1
h7 = 0.4*x + 0.5*y + 0.1
h8 = -0.2*x - 0.5*y + 0.1
h9 = 0.1*x + 0.2*y + 0.1
#
h1 = h1 if h1 >= 0 else 0
h2 = h2 if h2 >= 0 else 0
h3 = h3 if h3 >= 0 else 0
h4 = h4 if h4 >= 0 else 0
h5 = h5 if h5 >= 0 else 0
h6 = h6 if h6 >= 0 else 0
h7 = h7 if h7 >= 0 else 0
h8 = h8 if h8 >= 0 else 0
h9 = h9 if h9 >= 0 else 0

o1 = 0.4*h1 - 0.1*h2 + 0.2*h3 + 0.3*h4 - 0.1*h5 - 0.2*h6 + 0.4*h7 + 0.3*h8 + 0.1*h9 + 0.4
o2 = -0.2*h1 + 0.3*h2 - 0.1*h3 + 0.2*h4 + 0.1*h5 + 0.3*h6 + 0.4*h7 + 0.2*h8 - 0.1*h9 + 0.4
#
o1 = o1 if o1 >= 0 else 0
o2 = o2 if o2 >= 0 else 0

if o2 <= o1:
    raise ValueError
