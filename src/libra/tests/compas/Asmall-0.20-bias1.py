
assume(0 <= x05 <= 0)
assume(1 <= x06 <= 1)
assume(0 <= x07 <= 0)
assume(0 <= x08 <= 0)
assume(0 <= x09 <= 0)
assume(0 <= x010 <= 0)

x10 = (-0.355956)*x00 + (0.216933)*x01 + (0.112088)*x02 + (-0.460043)*x03 + (0.654527)*x04 + (-0.243296)*x05 + (-0.045194)*x06 + (-0.031787)*x07 + (-0.047311)*x08 + (0.042302)*x09 + (-0.101165)*x010 + (0.869257)*x011 + (0.451634)*x012 + (0.649568)*x013 + (0.590028)*x014 + (-0.343705)*x015 + (-0.355326)*x016 + (-0.162596)*x017 + (0.383471)*x018 + (-0.624940)*x019 + (-0.336952)*x020 + (0.042682)
x11 = (-0.195489)*x00 + (-0.116636)*x01 + (-0.251223)*x02 + (-0.082118)*x03 + (0.130152)*x04 + (-0.006075)*x05 + (0.126670)*x06 + (0.138712)*x07 + (0.118670)*x08 + (0.130709)*x09 + (-0.012899)*x010 + (1.233142)*x011 + (0.787831)*x012 + (0.566189)*x013 + (1.363199)*x014 + (-0.085944)*x015 + (0.232115)*x016 + (0.347649)*x017 + (0.403357)*x018 + (0.101364)*x019 + (-0.172370)*x020 + (-0.006119)
x12 = (-0.368952)*x00 + (0.247015)*x01 + (0.426636)*x02 + (0.250657)*x03 + (-0.195093)*x04 + (0.135477)*x05 + (-0.227534)*x06 + (-0.185492)*x07 + (-0.049107)*x08 + (-0.141049)*x09 + (0.272078)*x010 + (0.600144)*x011 + (0.154969)*x012 + (0.611799)*x013 + (0.862072)*x014 + (0.492020)*x015 + (-0.565739)*x016 + (-0.023279)*x017 + (-0.015682)*x018 + (0.147198)*x019 + (0.375516)*x020 + (-0.056348)
x13 = (0.338760)*x00 + (-0.006371)*x01 + (-0.401718)*x02 + (-0.101439)*x03 + (0.270171)*x04 + (-0.116166)*x05 + (0.048079)*x06 + (0.056848)*x07 + (-0.059160)*x08 + (0.264040)*x09 + (0.004125)*x010 + (0.401628)*x011 + (1.132328)*x012 + (0.135306)*x013 + (1.151789)*x014 + (0.053593)*x015 + (-0.210714)*x016 + (-0.109107)*x017 + (-0.384718)*x018 + (0.096069)*x019 + (0.005842)*x020 + (0.077009)
x14 = (-0.025816)*x00 + (-0.619220)*x01 + (-0.766920)*x02 + (0.305489)*x03 + (0.026792)*x04 + (0.227693)*x05 + (-0.054647)*x06 + (-0.191165)*x07 + (0.007729)*x08 + (0.019968)*x09 + (0.072121)*x010 + (1.135635)*x011 + (0.317284)*x012 + (0.453971)*x013 + (0.542603)*x014 + (0.013059)*x015 + (0.070702)*x016 + (-0.177007)*x017 + (-0.001652)*x018 + (-0.147550)*x019 + (0.137226)*x020 + (0.006623)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.694720)*x10 + (-0.205408)*x11 + (0.218375)*x12 + (-0.241138)*x13 + (-0.120393)*x14 + (0.011599)
x21 = (-0.100593)*x10 + (-0.883859)*x11 + (0.398013)*x12 + (-0.477481)*x13 + (0.255895)*x14 + (0.079328)
x22 = (0.251477)*x10 + (1.273862)*x11 + (0.175170)*x12 + (0.396568)*x13 + (0.470136)*x14 + (-0.051357)
x23 = (-0.151485)*x10 + (0.695660)*x11 + (-0.183999)*x12 + (-0.076950)*x13 + (0.136183)*x14 + (0.043945)
x24 = (0.654459)*x10 + (0.406620)*x11 + (0.452550)*x12 + (0.829865)*x13 + (0.612920)*x14 + (-0.116101)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.711497)*x20 + (-0.432482)*x21 + (0.966334)*x22 + (0.753473)*x23 + (0.740216)*x24 + (-0.132851)
x31 = (0.413832)*x20 + (-0.201690)*x21 + (0.503837)*x22 + (0.179045)*x23 + (-0.792083)*x24 + (0.234355)
x32 = (0.256189)*x20 + (-0.562018)*x21 + (-0.354947)*x22 + (-0.611116)*x23 + (-0.193065)*x24 + (0.008931)
x33 = (-0.455582)*x20 + (0.200013)*x21 + (0.220821)*x22 + (0.397729)*x23 + (0.621966)*x24 + (0.328245)
x34 = (-0.222782)*x20 + (0.644218)*x21 + (0.333086)*x22 + (0.472805)*x23 + (0.230488)*x24 + (-0.178632)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (-0.453361)*x30 + (-0.009512)*x31 + (-0.601432)*x32 + (-0.489257)*x33 + (-0.428510)*x34 + (0.000000)
x41 = (0.909430)*x30 + (-0.659828)*x31 + (-0.466567)*x32 + (0.170068)*x33 + (0.285704)*x34 + (-0.070840)
x42 = (-0.383931)*x30 + (0.629203)*x31 + (-0.428382)*x32 + (0.490679)*x33 + (-0.386088)*x34 + (0.270557)
x43 = (-0.574889)*x30 + (0.631092)*x31 + (0.365983)*x32 + (-0.151396)*x33 + (0.031147)*x34 + (0.054654)
x44 = (0.362158)*x30 + (0.518451)*x31 + (-0.309166)*x32 + (0.294148)*x33 + (-0.105310)*x34 + (0.010475)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (0.128797)*x40 + (-0.149885)*x41 + (1.094327)*x42 + (0.013614)*x43 + (-0.565491)*x44 + (0.083942)
x51 = (0.074643)*x40 + (0.011725)*x41 + (-0.546777)*x42 + (0.139518)*x43 + (0.579085)*x44 + (0.042068)
x52 = (-0.203598)*x40 + (0.994308)*x41 + (-1.143330)*x42 + (-0.965087)*x43 + (-0.283773)*x44 + (-0.085971)
#

