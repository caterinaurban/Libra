
x10 = (0.120010)*x00 + (-0.210915)*x01 + (0.437321)*x02 + (0.299345)*x03 + (0.089359)*x04 + (0.194682)*x05 + (0.449298)*x06 + (-0.285014)*x07 + (-0.449121)*x08 + (-0.394697)*x09 + (-0.424955)*x010 + (-0.448823)*x011 + (0.184932)*x012 + (0.285736)*x013 + (-0.071013)*x014 + (0.220315)*x015 + (-0.005325)*x016 + (0.122110)
x11 = (0.569365)*x00 + (0.410888)*x01 + (0.550470)*x02 + (0.593067)*x03 + (0.428841)*x04 + (-0.087996)*x05 + (0.358768)*x06 + (-0.616333)*x07 + (0.497243)*x08 + (-0.233446)*x09 + (0.272595)*x010 + (0.461758)*x011 + (-0.382702)*x012 + (0.646831)*x013 + (-0.504206)*x014 + (-0.170210)*x015 + (-0.575128)*x016 + (0.084119)
x12 = (0.331312)*x00 + (0.314736)*x01 + (-0.136847)*x02 + (0.572520)*x03 + (-0.266501)*x04 + (0.029340)*x05 + (-0.249539)*x06 + (-0.206869)*x07 + (-0.098630)*x08 + (0.344382)*x09 + (-0.356531)*x010 + (-0.306077)*x011 + (-0.390057)*x012 + (0.268749)*x013 + (-0.175871)*x014 + (0.055666)*x015 + (-0.199283)*x016 + (0.144100)
x13 = (0.402232)*x00 + (0.329753)*x01 + (0.153645)*x02 + (0.049344)*x03 + (0.265511)*x04 + (0.296519)*x05 + (0.505491)*x06 + (-0.037335)*x07 + (-0.354209)*x08 + (-0.009207)*x09 + (0.121841)*x010 + (0.127492)*x011 + (-0.384199)*x012 + (0.273006)*x013 + (-0.353932)*x014 + (0.013832)*x015 + (-0.377260)*x016 + (0.079524)
x14 = (-0.258218)*x00 + (-0.311233)*x01 + (0.312514)*x02 + (0.055084)*x03 + (0.149094)*x04 + (-0.005186)*x05 + (-0.294914)*x06 + (-0.365502)*x07 + (-0.052105)*x08 + (-0.360127)*x09 + (0.021248)*x010 + (0.446062)*x011 + (-0.314253)*x012 + (0.199576)*x013 + (0.692981)*x014 + (-0.077855)*x015 + (0.321439)*x016 + (0.016058)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.175215)*x10 + (0.301239)*x11 + (0.207959)*x12 + (0.447346)*x13 + (-0.816918)*x14 + (0.175903)
x21 = (0.219725)*x10 + (0.050826)*x11 + (-0.531851)*x12 + (-0.490318)*x13 + (-0.638859)*x14 + (0.011992)
x22 = (-0.603124)*x10 + (-0.646166)*x11 + (0.664469)*x12 + (0.505370)*x13 + (-0.294295)*x14 + (0.104145)
x23 = (-0.011606)*x10 + (-0.524559)*x11 + (0.213669)*x12 + (-0.513770)*x13 + (0.658076)*x14 + (-0.071556)
x24 = (0.245964)*x10 + (-0.142743)*x11 + (0.062382)*x12 + (-0.534562)*x13 + (0.802320)*x14 + (0.151022)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.402692)*x20 + (-0.372616)*x21 + (-0.307213)*x22 + (0.090116)*x23 + (-0.481501)*x24 + (0.159232)
x31 = (0.035880)*x20 + (-0.729090)*x21 + (-0.050467)*x22 + (0.123857)*x23 + (-0.438653)*x24 + (-0.051499)
x32 = (-0.464839)*x20 + (0.142078)*x21 + (0.050218)*x22 + (0.559309)*x23 + (-0.439326)*x24 + (-0.018981)
x33 = (-0.023840)*x20 + (-0.521814)*x21 + (0.240908)*x22 + (-0.374859)*x23 + (0.427589)*x24 + (-0.000073)
x34 = (-0.451516)*x20 + (0.376970)*x21 + (0.705989)*x22 + (-0.468932)*x23 + (-0.406246)*x24 + (0.199479)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.864985)*x30 + (0.242374)*x31 + (0.106935)*x32 + (-0.876969)*x33 + (-0.262138)*x34 + (0.155277)
x41 = (0.948680)*x30 + (-0.277085)*x31 + (0.405650)*x32 + (-0.428234)*x33 + (-0.183116)*x34 + (0.078410)
x42 = (0.907741)*x30 + (-0.292498)*x31 + (0.591130)*x32 + (0.527924)*x33 + (-0.834145)*x34 + (-0.056411)
x43 = (-0.084699)*x30 + (-0.290910)*x31 + (0.371914)*x32 + (-0.348279)*x33 + (-0.763982)*x34 + (-0.004430)
x44 = (0.096438)*x30 + (-0.669723)*x31 + (-0.217408)*x32 + (-0.264177)*x33 + (-0.323028)*x34 + (-0.079694)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (0.085024)*x40 + (1.113030)*x41 + (0.747760)*x42 + (0.703709)*x43 + (-0.752932)*x44 + (-0.064831)
x51 = (-0.998544)*x40 + (0.360175)*x41 + (0.194910)*x42 + (0.307743)*x43 + (0.055578)*x44 + (0.064831)