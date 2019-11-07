
x10 = (0.157593)*x00 + (0.236645)*x01 + (0.185374)*x02 + (-0.596501)*x03 + (-0.512773)*x04 + (-0.025578)*x05 + (0.165489)*x06 + (-0.484678)*x07 + (-0.551736)*x08 + (-0.362384)*x09 + (0.663246)*x010 + (-0.006900)*x011 + (-0.028441)*x012 + (0.055104)*x013 + (0.264894)*x014 + (-0.360712)*x015 + (0.292266)*x016 + (-0.121288)
x11 = (-0.178243)*x00 + (0.486946)*x01 + (0.122814)*x02 + (0.391992)*x03 + (-0.192112)*x04 + (-0.076856)*x05 + (0.366068)*x06 + (0.446779)*x07 + (-0.131193)*x08 + (-0.301305)*x09 + (0.374589)*x010 + (-0.244303)*x011 + (-0.574643)*x012 + (-0.302390)*x013 + (0.421531)*x014 + (0.015019)*x015 + (-0.436241)*x016 + (0.061408)
x12 = (0.535902)*x00 + (0.325233)*x01 + (-0.352199)*x02 + (0.248009)*x03 + (-0.136245)*x04 + (0.588995)*x05 + (-0.160838)*x06 + (0.422495)*x07 + (-0.048060)*x08 + (-0.433152)*x09 + (-0.421735)*x010 + (0.063302)*x011 + (0.298962)*x012 + (-0.321983)*x013 + (-0.241923)*x014 + (-0.036611)*x015 + (0.094411)*x016 + (0.126735)
x13 = (0.110861)*x00 + (0.272140)*x01 + (-0.014017)*x02 + (0.245097)*x03 + (0.099818)*x04 + (0.179300)*x05 + (0.110500)*x06 + (0.309219)*x07 + (-0.375683)*x08 + (-0.269411)*x09 + (-0.490802)*x010 + (0.239484)*x011 + (-0.218214)*x012 + (0.650013)*x013 + (-0.579994)*x014 + (-0.129889)*x015 + (0.640769)*x016 + (0.134337)
x14 = (0.255349)*x00 + (0.176963)*x01 + (-0.123244)*x02 + (-0.062008)*x03 + (0.526269)*x04 + (-0.168117)*x05 + (-0.558041)*x06 + (0.061898)*x07 + (0.029842)*x08 + (0.186025)*x09 + (0.087675)*x010 + (0.403058)*x011 + (-0.436228)*x012 + (0.084945)*x013 + (0.533352)*x014 + (0.126009)*x015 + (-0.634548)*x016 + (0.131870)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.075071)*x10 + (0.528846)*x11 + (0.020280)*x12 + (0.793983)*x13 + (-0.414260)*x14 + (-0.053342)
x21 = (-0.656928)*x10 + (0.816820)*x11 + (0.743793)*x12 + (-0.857726)*x13 + (0.876382)*x14 + (0.141775)
x22 = (0.368499)*x10 + (-0.313819)*x11 + (-0.219868)*x12 + (-0.662153)*x13 + (0.709524)*x14 + (-0.006075)
x23 = (-0.418032)*x10 + (0.033683)*x11 + (-0.085484)*x12 + (0.053008)*x13 + (-0.525632)*x14 + (-0.069793)
x24 = (-0.199065)*x10 + (-0.340303)*x11 + (0.739333)*x12 + (-0.763548)*x13 + (0.442972)*x14 + (0.114641)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.449126)*x20 + (0.482969)*x21 + (0.435857)*x22 + (0.204978)*x23 + (-0.116722)*x24 + (0.185078)
x31 = (-0.622335)*x20 + (0.580883)*x21 + (0.047210)*x22 + (0.628914)*x23 + (0.513933)*x24 + (0.145212)
x32 = (-0.772979)*x20 + (0.484032)*x21 + (-0.741137)*x22 + (-0.539308)*x23 + (-0.323593)*x24 + (-0.143395)
x33 = (0.111130)*x20 + (0.701030)*x21 + (-0.052697)*x22 + (0.219331)*x23 + (-0.552933)*x24 + (-0.127253)
x34 = (0.039527)*x20 + (-0.137439)*x21 + (-0.367580)*x22 + (-0.313854)*x23 + (-0.696947)*x24 + (-0.063516)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.201921)*x30 + (0.954842)*x31 + (0.004158)*x32 + (0.173293)*x33 + (0.012150)*x34 + (-0.126619)
x41 = (-0.362095)*x30 + (-0.610030)*x31 + (-0.562888)*x32 + (0.091703)*x33 + (-0.681849)*x34 + (0.000000)
x42 = (-0.586725)*x30 + (-0.595368)*x31 + (-0.536360)*x32 + (-0.366936)*x33 + (0.140904)*x34 + (0.000000)
x43 = (-0.509213)*x30 + (0.617978)*x31 + (-0.153870)*x32 + (0.775374)*x33 + (0.204982)*x34 + (0.098638)
x44 = (0.478924)*x30 + (-0.586422)*x31 + (-0.091437)*x32 + (-0.513276)*x33 + (-0.498230)*x34 + (0.257744)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (1.025335)*x40 + (-0.779643)*x41 + (-0.026682)*x42 + (0.195680)*x43 + (-0.916480)*x44 + (-0.192282)
x51 = (-0.507041)*x40 + (0.024417)*x41 + (-0.767249)*x42 + (-0.351355)*x43 + (-0.040428)*x44 + (0.192282)
