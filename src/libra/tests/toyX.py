
x00 = float(input())
x01 = float(input())

x11 = -0.31*x01 + 0.99*x02 -0.63
x12 = -1.25*x01 - 0.64*x02 + 1.88
#
x10 = x10 if x10 >= 0 else 0
# if x10 > 0:
#     print('x10')
x11 = x11 if x11 >= 0 else 0
# if x11 > 0:
#     print('x11')

x21 = 0.40*x11 + 1.21*x12 + 0.00
x22 = 0.64*x11 + 0.69*x12 - 0.39
#
x20 = x20 if x20 >= 0 else 0
# if x20 > 0:
#     print('x20')
x21 = x21 if x21 >= 0 else 0
# if x21 > 0:
#     print('x21')

x31 = 0.26*x21 + 0.33*x22 + 0.45
x32 = 1.42*x21 + 0.40*x22 - 0.45
#
if x30 < x31:
    print('x31')
elif x31 < x30:
    print('x30')
