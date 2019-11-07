
assume(1 <= x02 <= 1)
assume(0 <= x03 <= 0)
assume(0 <= x04 <= 0)

x10 = (0.067645)*x00 + (0.047427)*x01 + (0.488096)*x02 + (0.380296)*x03 + (0.002629)*x04 + (-0.037194)*x05 + (-0.189885)*x06 + (0.064303)*x07 + (-0.174688)*x08 + (-0.036535)*x09 + (-0.100094)*x010 + (0.926369)*x011 + (0.777298)*x012 + (0.192888)*x013 + (1.438129)*x014 + (-0.222217)*x015 + (-0.396806)*x016 + (0.099297)*x017 + (0.288982)*x018 + (0.050006)*x019 + (0.000424)*x020 + (-0.003280)
x11 = (-0.228150)*x00 + (-0.221464)*x01 + (0.255311)*x02 + (0.155469)*x03 + (0.227599)*x04 + (-0.344375)*x05 + (0.523714)*x06 + (-0.143195)*x07 + (0.396874)*x08 + (0.311428)*x09 + (-0.306958)*x010 + (0.507012)*x011 + (0.371498)*x012 + (0.641924)*x013 + (0.646119)*x014 + (0.068395)*x015 + (0.245969)*x016 + (0.481350)*x017 + (-0.359492)*x018 + (-0.027720)*x019 + (-0.149265)*x020 + (0.055322)
x12 = (-0.150164)*x00 + (0.098088)*x01 + (-0.475499)*x02 + (-0.469948)*x03 + (-0.249990)*x04 + (-0.393461)*x05 + (-0.087707)*x06 + (-0.147115)*x07 + (0.090003)*x08 + (-0.284632)*x09 + (0.132192)*x010 + (-0.392097)*x011 + (-0.217768)*x012 + (0.413742)*x013 + (-0.310028)*x014 + (0.188430)*x015 + (-0.289035)*x016 + (-0.388667)*x017 + (-0.202139)*x018 + (-0.233981)*x019 + (-0.016571)*x020 + (-0.003162)
x13 = (-0.493542)*x00 + (0.425212)*x01 + (0.014730)*x02 + (-0.347885)*x03 + (-0.469807)*x04 + (0.004323)*x05 + (-0.215350)*x06 + (0.218110)*x07 + (-0.049415)*x08 + (-0.068929)*x09 + (0.306795)*x010 + (-0.029244)*x011 + (0.654220)*x012 + (0.506825)*x013 + (0.457985)*x014 + (-0.051677)*x015 + (0.479721)*x016 + (-0.266643)*x017 + (-0.570410)*x018 + (-0.094578)*x019 + (-0.302015)*x020 + (0.027902)
x14 = (0.058050)*x00 + (0.141346)*x01 + (0.250553)*x02 + (-0.414512)*x03 + (-0.315237)*x04 + (-0.174436)*x05 + (-0.087730)*x06 + (-0.070885)*x07 + (-0.113779)*x08 + (0.066812)*x09 + (0.087703)*x010 + (0.369693)*x011 + (0.313409)*x012 + (-0.250769)*x013 + (0.451858)*x014 + (-0.198779)*x015 + (0.089209)*x016 + (-0.104475)*x017 + (0.346870)*x018 + (-0.058760)*x019 + (-0.474193)*x020 + (-0.119943)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.931654)*x10 + (0.515872)*x11 + (-0.657944)*x12 + (0.697575)*x13 + (0.715227)*x14 + (-0.087194)
x21 = (-0.534720)*x10 + (0.371727)*x11 + (-0.343300)*x12 + (0.113253)*x13 + (0.043669)*x14 + (0.027085)
x22 = (0.304061)*x10 + (0.578750)*x11 + (0.724160)*x12 + (0.595915)*x13 + (-0.029822)*x14 + (0.071251)
x23 = (0.382299)*x10 + (0.637420)*x11 + (0.580523)*x12 + (0.246689)*x13 + (-0.790696)*x14 + (-0.041871)
x24 = (-0.783686)*x10 + (0.543789)*x11 + (-0.571083)*x12 + (0.680904)*x13 + (0.322255)*x14 + (0.068534)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.979442)*x20 + (-0.089479)*x21 + (-0.318695)*x22 + (0.541829)*x23 + (-0.847272)*x24 + (-0.077820)
x31 = (0.119297)*x20 + (0.451308)*x21 + (0.170085)*x22 + (-1.009497)*x23 + (-0.119790)*x24 + (0.052727)
x32 = (-0.611682)*x20 + (-0.188962)*x21 + (-0.077822)*x22 + (0.251464)*x23 + (0.517077)*x24 + (0.014993)
x33 = (0.566087)*x20 + (-0.204708)*x21 + (-0.560570)*x22 + (0.741649)*x23 + (-0.063993)*x24 + (-0.077541)
x34 = (0.734353)*x20 + (0.098987)*x21 + (-0.377523)*x22 + (-0.454653)*x23 + (0.393677)*x24 + (-0.068518)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.578778)*x30 + (-0.561913)*x31 + (0.213046)*x32 + (0.123183)*x33 + (0.590512)*x34 + (-0.132811)
x41 = (-0.482475)*x30 + (-0.558538)*x31 + (0.567552)*x32 + (-0.470285)*x33 + (-0.548713)*x34 + (-0.067097)
x42 = (-0.705026)*x30 + (0.687502)*x31 + (-0.703110)*x32 + (-0.273217)*x33 + (0.162463)*x34 + (-0.058247)
x43 = (0.911621)*x30 + (-0.872245)*x31 + (-0.901320)*x32 + (0.614705)*x33 + (0.810958)*x34 + (-0.066159)
x44 = (0.843578)*x30 + (0.030796)*x31 + (-0.286510)*x32 + (-0.302388)*x33 + (0.227978)*x34 + (-0.114388)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.839313)*x40 + (-0.643212)*x41 + (0.399083)*x42 + (-1.019810)*x43 + (-0.161540)*x44 + (0.220299)
x51 = (-0.345288)*x40 + (0.756150)*x41 + (-0.086331)*x42 + (0.003072)*x43 + (0.247469)*x44 + (0.022250)
x52 = (0.952657)*x40 + (0.747880)*x41 + (-0.368216)*x42 + (0.422448)*x43 + (0.490377)*x44 + (-0.218073)
#

