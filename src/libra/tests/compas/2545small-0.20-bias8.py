
assume(0 <= x02 <= 0)
assume(1 <= x03 <= 1)
assume(0 <= x04 <= 0)

x10 = (0.138064)*x00 + (-0.378498)*x01 + (-0.184449)*x02 + (0.293368)*x03 + (0.264379)*x04 + (0.433180)*x05 + (-0.047378)*x06 + (0.109041)*x07 + (-0.112848)*x08 + (0.390092)*x09 + (-0.056348)*x010 + (0.489994)*x011 + (0.847275)*x012 + (0.744563)*x013 + (0.557355)*x014 + (0.444983)*x015 + (0.284937)*x016 + (-0.285862)*x017 + (0.218727)*x018 + (0.571243)*x019 + (-0.476773)*x020 + (-0.140004)
x11 = (-0.205018)*x00 + (0.331159)*x01 + (-0.275100)*x02 + (0.358566)*x03 + (0.072397)*x04 + (-0.047348)*x05 + (-0.211196)*x06 + (-0.317420)*x07 + (0.000498)*x08 + (0.297431)*x09 + (-0.043869)*x010 + (-0.129103)*x011 + (-0.969627)*x012 + (-0.425467)*x013 + (-0.294324)*x014 + (-0.340629)*x015 + (0.043196)*x016 + (-0.322501)*x017 + (-0.201942)*x018 + (-0.291114)*x019 + (-0.121873)*x020 + (-0.092893)
x12 = (-0.098847)*x00 + (-0.216976)*x01 + (0.008179)*x02 + (0.251066)*x03 + (0.332529)*x04 + (-0.076351)*x05 + (-0.137823)*x06 + (-0.045823)*x07 + (-0.156696)*x08 + (0.212572)*x09 + (-0.161476)*x010 + (0.752137)*x011 + (1.194942)*x012 + (0.593858)*x013 + (1.426756)*x014 + (0.035098)*x015 + (0.058403)*x016 + (-0.037594)*x017 + (-0.283804)*x018 + (0.254335)*x019 + (0.161285)*x020 + (-0.044362)
x13 = (-0.046452)*x00 + (0.100236)*x01 + (-0.083033)*x02 + (-0.190385)*x03 + (0.596951)*x04 + (-0.070336)*x05 + (0.399809)*x06 + (0.116503)*x07 + (0.279374)*x08 + (-0.129119)*x09 + (0.163549)*x010 + (1.111438)*x011 + (0.843255)*x012 + (-0.089571)*x013 + (0.726520)*x014 + (0.045090)*x015 + (-0.257235)*x016 + (0.131075)*x017 + (0.432368)*x018 + (-0.007647)*x019 + (0.068528)*x020 + (0.010713)
x14 = (-0.437189)*x00 + (-0.195166)*x01 + (-0.627075)*x02 + (0.407070)*x03 + (0.032950)*x04 + (-0.174275)*x05 + (0.001047)*x06 + (-0.261204)*x07 + (0.241718)*x08 + (-0.330437)*x09 + (0.402621)*x010 + (0.726707)*x011 + (0.385319)*x012 + (0.591372)*x013 + (1.336387)*x014 + (-0.009820)*x015 + (0.148682)*x016 + (-0.146558)*x017 + (0.086200)*x018 + (-0.159102)*x019 + (0.369133)*x020 + (0.032777)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.014396)*x10 + (-0.499369)*x11 + (0.773083)*x12 + (0.742831)*x13 + (0.624916)*x14 + (-0.137204)
x21 = (-0.503752)*x10 + (0.115948)*x11 + (-0.346230)*x12 + (0.040722)*x13 + (0.225993)*x14 + (-0.047205)
x22 = (-0.279971)*x10 + (-0.234102)*x11 + (-0.407847)*x12 + (0.707668)*x13 + (0.779736)*x14 + (0.155678)
x23 = (0.246195)*x10 + (0.610985)*x11 + (-0.214239)*x12 + (-0.073958)*x13 + (0.173390)*x14 + (-0.023663)
x24 = (0.434489)*x10 + (0.095677)*x11 + (0.955545)*x12 + (-0.306705)*x13 + (0.064124)*x14 + (-0.035417)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.654608)*x20 + (-0.609272)*x21 + (0.462117)*x22 + (-0.682225)*x23 + (0.841486)*x24 + (-0.097136)
x31 = (-0.040438)*x20 + (-0.300288)*x21 + (0.270759)*x22 + (0.197029)*x23 + (-0.404236)*x24 + (-0.023783)
x32 = (-0.707897)*x20 + (-0.074914)*x21 + (0.774939)*x22 + (-0.606209)*x23 + (0.207495)*x24 + (0.213673)
x33 = (0.287927)*x20 + (0.398596)*x21 + (-0.069526)*x22 + (-0.523469)*x23 + (0.369304)*x24 + (-0.107714)
x34 = (0.512210)*x20 + (-0.704431)*x21 + (-0.272712)*x22 + (0.477692)*x23 + (0.139188)*x24 + (-0.130367)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.430147)*x30 + (-0.677030)*x31 + (-0.264002)*x32 + (0.367220)*x33 + (-0.279728)*x34 + (0.002981)
x41 = (0.559041)*x30 + (0.300432)*x31 + (-0.846471)*x32 + (0.103987)*x33 + (0.799172)*x34 + (-0.106278)
x42 = (0.042163)*x30 + (-0.569451)*x31 + (0.618458)*x32 + (-0.116338)*x33 + (-0.510848)*x34 + (0.226057)
x43 = (-0.062255)*x30 + (0.249953)*x31 + (-0.168298)*x32 + (-0.069116)*x33 + (-0.445927)*x34 + (-0.002254)
x44 = (0.629399)*x30 + (-0.655331)*x31 + (-0.035983)*x32 + (0.164774)*x33 + (0.195038)*x34 + (-0.059102)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-1.068852)*x40 + (-0.194898)*x41 + (0.233304)*x42 + (0.678809)*x43 + (-0.914466)*x44 + (0.162445)
x51 = (0.354059)*x40 + (-0.737138)*x41 + (-0.106193)*x42 + (0.505312)*x43 + (0.598799)*x44 + (-0.035148)
x52 = (-0.332474)*x40 + (0.409509)*x41 + (-0.945594)*x42 + (-0.550976)*x43 + (0.891130)*x44 + (-0.062060)
#
