
# < 25
assume(0 <= x02 <= 0)
assume(0 <= x03 <= 0)
assume(1 <= x04 <= 1)

x10 = (-0.470760)*x00 + (-0.358559)*x01 + (-0.049409)*x02 + (0.414751)*x03 + (-0.093150)*x04 + (-0.357850)*x05 + (0.467858)*x06 + (0.080497)*x07 + (0.444068)*x08 + (-0.036669)*x09 + (0.030664)*x010 + (-0.409431)*x011 + (-0.610014)*x012 + (-0.150868)*x013 + (0.317468)*x014 + (-0.111446)*x015 + (-0.105528)*x016 + (-0.101167)*x017 + (0.026970)*x018 + (0.064046)
x11 = (-0.366529)*x00 + (0.001753)*x01 + (-0.218099)*x02 + (-0.499027)*x03 + (-0.331554)*x04 + (0.205672)*x05 + (0.226759)*x06 + (-0.276796)*x07 + (0.312428)*x08 + (0.347502)*x09 + (0.274081)*x010 + (0.170480)*x011 + (-0.484554)*x012 + (-0.358572)*x013 + (0.061862)*x014 + (-0.151716)*x015 + (-0.308328)*x016 + (0.522436)*x017 + (-0.145417)*x018 + (0.031645)
x12 = (-0.040002)*x00 + (-0.225343)*x01 + (-0.542850)*x02 + (0.706706)*x03 + (-0.108545)*x04 + (0.039585)*x05 + (-0.043858)*x06 + (-0.107190)*x07 + (-0.049420)*x08 + (0.127655)*x09 + (-0.011019)*x010 + (0.100978)*x011 + (0.510507)*x012 + (-0.160815)*x013 + (-0.057108)*x014 + (-0.024163)*x015 + (-0.190110)*x016 + (-0.037145)*x017 + (-0.467548)*x018 + (-0.002709)
x13 = (0.190414)*x00 + (0.267345)*x01 + (-0.280562)*x02 + (-0.247394)*x03 + (-0.119264)*x04 + (-0.020809)*x05 + (-0.039222)*x06 + (0.016915)*x07 + (-0.030399)*x08 + (-0.006685)*x09 + (-0.045277)*x010 + (1.128474)*x011 + (1.307848)*x012 + (-0.031350)*x013 + (-0.024144)*x014 + (0.133774)*x015 + (0.136913)*x016 + (-0.133948)*x017 + (-0.081433)*x018 + (0.065475)
x14 = (-0.358189)*x00 + (0.561786)*x01 + (-0.203292)*x02 + (-0.414769)*x03 + (0.005510)*x04 + (0.210954)*x05 + (0.043228)*x06 + (-0.014654)*x07 + (0.288810)*x08 + (0.001834)*x09 + (0.094690)*x010 + (-0.126204)*x011 + (-0.317855)*x012 + (-0.302992)*x013 + (-0.058535)*x014 + (0.393600)*x015 + (-0.137937)*x016 + (-0.451532)*x017 + (0.441788)*x018 + (-0.032890)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.449514)*x10 + (-0.106890)*x11 + (0.126375)*x12 + (0.830680)*x13 + (0.750941)*x14 + (-0.037031)
x21 = (-0.281391)*x10 + (-0.283939)*x11 + (-0.616972)*x12 + (0.906931)*x13 + (0.509038)*x14 + (0.051329)
x22 = (-0.038791)*x10 + (0.470249)*x11 + (0.673924)*x12 + (-0.232143)*x13 + (0.575127)*x14 + (0.115721)
x23 = (-0.086044)*x10 + (0.698190)*x11 + (-0.083180)*x12 + (-0.620362)*x13 + (0.375750)*x14 + (0.266500)
x24 = (0.886903)*x10 + (0.220473)*x11 + (-0.486237)*x12 + (-0.231054)*x13 + (0.811508)*x14 + (0.109258)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.519631)*x20 + (0.160165)*x21 + (0.585281)*x22 + (-0.256674)*x23 + (0.242441)*x24 + (-0.295138)
x31 = (1.249562)*x20 + (0.899762)*x21 + (0.359568)*x22 + (-0.477831)*x23 + (-0.190654)*x24 + (0.008181)
x32 = (0.024192)*x20 + (0.165804)*x21 + (0.830011)*x22 + (0.133677)*x23 + (0.559106)*x24 + (-0.002830)
x33 = (-0.130334)*x20 + (0.544731)*x21 + (-0.391701)*x22 + (-1.050590)*x23 + (-0.812499)*x24 + (0.131997)
x34 = (0.894867)*x20 + (0.522048)*x21 + (-0.807415)*x22 + (-0.104730)*x23 + (-0.105270)*x24 + (0.103486)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.557159)*x30 + (0.665260)*x31 + (0.464953)*x32 + (0.809619)*x33 + (0.820271)*x34 + (-0.126773)
x41 = (-0.031022)*x30 + (-0.686312)*x31 + (-0.108893)*x32 + (0.432172)*x33 + (0.514206)*x34 + (-0.036392)
x42 = (-0.715163)*x30 + (0.345473)*x31 + (-0.434505)*x32 + (0.883509)*x33 + (0.815836)*x34 + (0.053564)
x43 = (-0.132306)*x30 + (-0.229766)*x31 + (-0.552404)*x32 + (0.800576)*x33 + (0.689375)*x34 + (0.011838)
x44 = (0.218625)*x30 + (0.978628)*x31 + (0.220117)*x32 + (0.106321)*x33 + (0.454545)*x34 + (-0.116137)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.311013)*x40 + (-0.354002)*x41 + (-1.324724)*x42 + (0.162118)*x43 + (-0.624265)*x44 + (0.280001)
x51 = (0.441388)*x40 + (-0.145031)*x41 + (-0.630431)*x42 + (-0.480091)*x43 + (-0.091946)*x44 + (-0.071888)
x52 = (-0.012343)*x40 + (0.257321)*x41 + (0.940569)*x42 + (0.529530)*x43 + (-0.331926)*x44 + (-0.210149)
#
