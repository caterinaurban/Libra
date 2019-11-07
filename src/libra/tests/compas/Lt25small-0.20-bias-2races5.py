
assume(0 <= x02 <= 0)
assume(1 <= x03 <= 1)
assume(0 <= x04 <= 0)

x10 = (-0.397207)*x00 + (-0.145913)*x01 + (0.110853)*x02 + (0.160679)*x03 + (-0.123580)*x04 + (-0.156923)*x05 + (0.293566)*x06 + (-0.243087)*x07 + (-0.237544)*x08 + (0.510782)*x09 + (0.042993)*x010 + (0.830375)*x011 + (1.195180)*x012 + (0.404275)*x013 + (0.408630)*x014 + (0.184736)*x015 + (0.038388)*x016 + (0.089441)*x017 + (-0.015768)*x018 + (0.043839)
x11 = (-0.083994)*x00 + (0.285682)*x01 + (0.074497)*x02 + (0.071250)*x03 + (0.089330)*x04 + (-0.115988)*x05 + (-0.073639)*x06 + (0.090578)*x07 + (0.034041)*x08 + (0.557762)*x09 + (0.336280)*x010 + (-0.637275)*x011 + (-0.473577)*x012 + (0.086165)*x013 + (0.148602)*x014 + (-0.679893)*x015 + (0.154833)*x016 + (0.088009)*x017 + (0.215031)*x018 + (0.087368)
x12 = (0.038862)*x00 + (0.319652)*x01 + (-0.195015)*x02 + (-0.309571)*x03 + (0.092660)*x04 + (-0.262642)*x05 + (0.030449)*x06 + (0.033830)*x07 + (-0.161383)*x08 + (0.103255)*x09 + (0.036800)*x010 + (-0.294324)*x011 + (-0.842861)*x012 + (0.168553)*x013 + (-0.002685)*x014 + (0.030177)*x015 + (-0.308729)*x016 + (0.453632)*x017 + (0.345873)*x018 + (0.043137)
x13 = (0.051459)*x00 + (0.228564)*x01 + (-0.364895)*x02 + (0.235687)*x03 + (0.037179)*x04 + (-0.340880)*x05 + (-0.466867)*x06 + (-0.453113)*x07 + (-0.224888)*x08 + (0.186208)*x09 + (-0.214193)*x010 + (0.336517)*x011 + (-0.068446)*x012 + (-0.451618)*x013 + (0.240750)*x014 + (-0.416293)*x015 + (-0.529998)*x016 + (-0.376678)*x017 + (-0.457961)*x018 + (-0.077250)
x14 = (0.096152)*x00 + (0.082742)*x01 + (-0.128106)*x02 + (0.157967)*x03 + (-0.392852)*x04 + (0.178723)*x05 + (0.027984)*x06 + (0.445245)*x07 + (0.363309)*x08 + (0.065703)*x09 + (0.230768)*x010 + (0.800975)*x011 + (1.040272)*x012 + (0.203277)*x013 + (0.282850)*x014 + (0.000423)*x015 + (0.359719)*x016 + (-0.439659)*x017 + (-0.011914)*x018 + (-0.000224)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.934118)*x10 + (0.179427)*x11 + (-0.000497)*x12 + (-0.396169)*x13 + (-0.843549)*x14 + (-0.212161)
x21 = (0.503492)*x10 + (-0.395561)*x11 + (-0.042264)*x12 + (0.066923)*x13 + (1.017629)*x14 + (-0.028539)
x22 = (0.668853)*x10 + (-0.006175)*x11 + (0.062165)*x12 + (-0.475151)*x13 + (0.603742)*x14 + (-0.094200)
x23 = (0.340040)*x10 + (0.830391)*x11 + (0.424862)*x12 + (0.421286)*x13 + (-0.378350)*x14 + (0.195415)
x24 = (0.734315)*x10 + (0.070137)*x11 + (-0.651731)*x12 + (-0.323499)*x13 + (-0.070956)*x14 + (0.020809)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.668953)*x20 + (0.788622)*x21 + (0.320784)*x22 + (-0.677434)*x23 + (0.931207)*x24 + (0.015421)
x31 = (0.200628)*x20 + (0.261935)*x21 + (0.325025)*x22 + (-0.218214)*x23 + (0.865365)*x24 + (-0.141064)
x32 = (0.139416)*x20 + (0.330245)*x21 + (0.520689)*x22 + (0.223914)*x23 + (0.596812)*x24 + (0.059153)
x33 = (-0.076402)*x20 + (-0.029753)*x21 + (-0.758706)*x22 + (-0.467757)*x23 + (-0.559778)*x24 + (0.000000)
x34 = (-0.144281)*x20 + (-0.755330)*x21 + (-0.039102)*x22 + (-0.423301)*x23 + (-0.458272)*x24 + (0.000000)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.399974)*x30 + (0.004859)*x31 + (-0.778309)*x32 + (0.299154)*x33 + (-0.576981)*x34 + (-0.052562)
x41 = (-0.667349)*x30 + (0.575983)*x31 + (-0.516904)*x32 + (-0.012329)*x33 + (0.006994)*x34 + (0.000000)
x42 = (0.686960)*x30 + (0.606886)*x31 + (0.690692)*x32 + (0.183529)*x33 + (-0.564675)*x34 + (-0.156345)
x43 = (-0.791634)*x30 + (-0.408498)*x31 + (0.308565)*x32 + (-0.496434)*x33 + (-0.092526)*x34 + (0.190907)
x44 = (-0.106101)*x30 + (-0.824541)*x31 + (0.813710)*x32 + (0.541099)*x33 + (0.402443)*x34 + (0.186490)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.609843)*x40 + (0.535418)*x41 + (-0.953312)*x42 + (0.422475)*x43 + (-0.119728)*x44 + (0.116612)
x51 = (0.001064)*x40 + (-0.621891)*x41 + (-0.336780)*x42 + (-0.795359)*x43 + (0.091947)*x44 + (0.046596)
x52 = (-0.649387)*x40 + (-0.081481)*x41 + (0.523832)*x42 + (0.579698)*x43 + (-1.017171)*x44 + (-0.137404)
#

