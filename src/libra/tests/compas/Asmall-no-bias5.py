
assume(0 <= x05 <= 0)
assume(0 <= x06 <= 0)
assume(1 <= x07 <= 1)
assume(0 <= x08 <= 0)
assume(0 <= x09 <= 0)
assume(0 <= x010 <= 0)

x10 = (0.323891)*x00 + (0.091306)*x01 + (-0.077396)*x02 + (0.358384)*x03 + (0.132141)*x04 + (0.013925)*x05 + (0.227707)*x06 + (0.390730)*x07 + (0.432650)*x08 + (0.032908)*x09 + (0.139577)*x010 + (-0.537310)*x011 + (-0.159489)*x012 + (-0.317645)*x013 + (-0.806102)*x014 + (0.527823)*x015 + (0.447673)*x016 + (0.256064)*x017 + (0.149170)*x018 + (-0.381021)*x019 + (0.327911)*x020 + (0.154659)
x11 = (0.176459)*x00 + (-0.165086)*x01 + (0.092829)*x02 + (0.100098)*x03 + (-0.190791)*x04 + (-0.007449)*x05 + (0.024295)*x06 + (0.084827)*x07 + (0.109308)*x08 + (-0.104394)*x09 + (-0.080038)*x010 + (1.327890)*x011 + (0.652379)*x012 + (0.390027)*x013 + (0.641234)*x014 + (-0.040156)*x015 + (0.038185)*x016 + (0.382665)*x017 + (0.249094)*x018 + (-0.224420)*x019 + (0.023568)*x020 + (0.026134)
x12 = (-0.339241)*x00 + (-0.344808)*x01 + (0.425420)*x02 + (-0.267787)*x03 + (-0.033548)*x04 + (0.324392)*x05 + (-0.411670)*x06 + (0.151770)*x07 + (0.280981)*x08 + (0.323667)*x09 + (-0.435102)*x010 + (-0.053766)*x011 + (-0.211666)*x012 + (0.383416)*x013 + (-0.527476)*x014 + (-0.412129)*x015 + (-0.245953)*x016 + (0.228506)*x017 + (-0.377797)*x018 + (-0.288403)*x019 + (-0.040542)*x020 + (-0.010928)
x13 = (0.077485)*x00 + (-0.376351)*x01 + (-0.335012)*x02 + (-0.414225)*x03 + (-0.215798)*x04 + (0.330827)*x05 + (0.210303)*x06 + (0.173386)*x07 + (0.157742)*x08 + (0.162222)*x09 + (0.092763)*x010 + (-0.537909)*x011 + (-0.360104)*x012 + (-0.304370)*x013 + (-0.565195)*x014 + (-0.003239)*x015 + (0.261317)*x016 + (0.239332)*x017 + (0.093147)*x018 + (0.143702)*x019 + (-0.252295)*x020 + (0.157406)
x14 = (-0.300364)*x00 + (0.260875)*x01 + (-0.316237)*x02 + (-0.214418)*x03 + (0.302359)*x04 + (0.357646)*x05 + (0.009495)*x06 + (0.189717)*x07 + (0.372690)*x08 + (0.105958)*x09 + (0.230918)*x010 + (-1.163440)*x011 + (-0.685140)*x012 + (-0.918066)*x013 + (-0.328390)*x014 + (0.631145)*x015 + (-0.469071)*x016 + (0.046816)*x017 + (0.031248)*x018 + (-0.049371)*x019 + (-0.195057)*x020 + (0.064683)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.732505)*x10 + (-0.231621)*x11 + (-0.538281)*x12 + (-0.409254)*x13 + (-0.254417)*x14 + (0.103560)
x21 = (-0.321781)*x10 + (0.476195)*x11 + (-0.443531)*x12 + (0.260987)*x13 + (0.723012)*x14 + (0.207746)
x22 = (0.715789)*x10 + (-0.520308)*x11 + (-0.105813)*x12 + (0.628813)*x13 + (0.694349)*x14 + (0.082193)
x23 = (0.327038)*x10 + (-0.718150)*x11 + (0.112969)*x12 + (0.530144)*x13 + (0.022654)*x14 + (0.061822)
x24 = (0.559376)*x10 + (-0.887492)*x11 + (-0.200992)*x12 + (0.538955)*x13 + (0.405560)*x14 + (-0.018115)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.254463)*x20 + (0.389518)*x21 + (0.099063)*x22 + (-0.336945)*x23 + (0.154970)*x24 + (0.264424)
x31 = (-0.126180)*x20 + (0.653500)*x21 + (0.377287)*x22 + (-0.690697)*x23 + (0.541066)*x24 + (0.019744)
x32 = (0.128225)*x20 + (0.724182)*x21 + (0.087769)*x22 + (-0.782224)*x23 + (-0.419693)*x24 + (0.272709)
x33 = (-0.301202)*x20 + (0.409075)*x21 + (0.204352)*x22 + (0.780776)*x23 + (-0.069425)*x24 + (-0.033660)
x34 = (-0.538901)*x20 + (-0.517338)*x21 + (0.909836)*x22 + (0.781455)*x23 + (0.871122)*x24 + (-0.005879)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.760774)*x30 + (0.192112)*x31 + (0.966230)*x32 + (-0.450455)*x33 + (-0.862274)*x34 + (0.250745)
x41 = (-0.730986)*x30 + (0.558674)*x31 + (-0.502849)*x32 + (0.684921)*x33 + (-0.507161)*x34 + (0.003399)
x42 = (0.370752)*x30 + (0.474518)*x31 + (-0.811753)*x32 + (-0.193090)*x33 + (-0.752173)*x34 + (-0.058003)
x43 = (0.635165)*x30 + (0.581338)*x31 + (-0.694535)*x32 + (-0.675710)*x33 + (0.903309)*x34 + (-0.199483)
x44 = (-0.566599)*x30 + (-0.495759)*x31 + (0.363009)*x32 + (-0.510603)*x33 + (0.186449)*x34 + (0.000000)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-1.349761)*x40 + (0.373436)*x41 + (0.457879)*x42 + (0.397299)*x43 + (0.697749)*x44 + (-0.405481)
x51 = (-0.269819)*x40 + (0.284783)*x41 + (0.422280)*x42 + (0.053073)*x43 + (-0.523343)*x44 + (0.125340)
x52 = (0.870655)*x40 + (0.395018)*x41 + (-0.142696)*x42 + (-0.356536)*x43 + (0.820029)*x44 + (0.261223)
#

