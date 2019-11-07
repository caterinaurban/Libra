
x10 = (0.144953)*x00 + (-0.428523)*x01 + (-0.418981)*x02 + (0.437936)*x03 + (0.121803)*x04 + (-0.356561)*x05 + (0.161972)*x06 + (-0.580298)*x07 + (-0.033399)*x08 + (-0.141640)*x09 + (-0.064552)*x010 + (-0.605089)*x011 + (-0.566084)*x012 + (-1.050681)*x013 + (-0.639277)*x014 + (-0.234821)*x015 + (-0.029629)*x016 + (-0.101219)*x017 + (-0.240012)*x018 + (0.153013)*x019 + (0.392684)*x020 + (-0.410518)*x021 + (0.343544)*x022 + (-0.044566)
x11 = (-0.638158)*x00 + (0.221716)*x01 + (0.478821)*x02 + (0.188183)*x03 + (1.635316)*x04 + (-0.423541)*x05 + (0.236975)*x06 + (-0.027368)*x07 + (0.619365)*x08 + (0.211287)*x09 + (0.406912)*x010 + (0.288097)*x011 + (0.124936)*x012 + (0.280683)*x013 + (0.221912)*x014 + (-0.028685)*x015 + (0.805356)*x016 + (0.163041)*x017 + (0.147991)*x018 + (0.123505)*x019 + (0.092127)*x020 + (-0.225995)*x021 + (-0.144366)*x022 + (0.228042)
x12 = (-0.043025)*x00 + (-0.146112)*x01 + (-0.267273)*x02 + (-0.324436)*x03 + (-0.998508)*x04 + (0.655526)*x05 + (0.215172)*x06 + (0.348632)*x07 + (0.341307)*x08 + (0.158401)*x09 + (0.320320)*x010 + (-0.112612)*x011 + (-0.093910)*x012 + (-0.089480)*x013 + (-0.064932)*x014 + (-0.265108)*x015 + (-0.407537)*x016 + (-0.222874)*x017 + (-0.172996)*x018 + (-0.222506)*x019 + (0.386026)*x020 + (-0.202327)*x021 + (0.383468)*x022 + (0.028487)
x13 = (-0.430420)*x00 + (0.314237)*x01 + (-0.256430)*x02 + (0.051974)*x03 + (1.195296)*x04 + (-0.137437)*x05 + (0.816769)*x06 + (0.208371)*x07 + (0.216129)*x08 + (0.240039)*x09 + (0.211305)*x010 + (0.085394)*x011 + (0.261447)*x012 + (0.494193)*x013 + (0.491629)*x014 + (-0.138806)*x015 + (0.615150)*x016 + (-0.051661)*x017 + (0.084963)*x018 + (0.174011)*x019 + (0.425750)*x020 + (0.285212)*x021 + (-0.342524)*x022 + (0.162627)
x14 = (0.049517)*x00 + (-0.225173)*x01 + (0.010039)*x02 + (-0.166581)*x03 + (-0.437766)*x04 + (-0.157761)*x05 + (-0.404029)*x06 + (-0.001386)*x07 + (-0.295063)*x08 + (-0.064140)*x09 + (-0.300510)*x010 + (0.135185)*x011 + (0.109006)*x012 + (-0.369136)*x013 + (-0.026333)*x014 + (0.053700)*x015 + (-0.429596)*x016 + (-0.437067)*x017 + (0.252028)*x018 + (-0.145085)*x019 + (-0.023842)*x020 + (-0.385171)*x021 + (-0.384192)*x022 + (-0.134150)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.575131)*x10 + (0.135793)*x11 + (0.855388)*x12 + (0.269309)*x13 + (-0.607133)*x14 + (-0.136726)
x21 = (-0.362259)*x10 + (0.435308)*x11 + (-0.386291)*x12 + (0.600586)*x13 + (-0.383727)*x14 + (0.227265)
x22 = (-0.600433)*x10 + (-0.207109)*x11 + (-0.146004)*x12 + (-0.115758)*x13 + (-0.256109)*x14 + (0.137878)
x23 = (0.612507)*x10 + (0.173138)*x11 + (-0.114271)*x12 + (-0.473544)*x13 + (-0.303194)*x14 + (0.153799)
x24 = (-0.173095)*x10 + (0.878303)*x11 + (-0.531576)*x12 + (0.432427)*x13 + (-0.145774)*x14 + (0.286905)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.657258)*x20 + (-0.489422)*x21 + (-1.123975)*x22 + (0.163784)*x23 + (0.012077)*x24 + (-0.079836)
x31 = (-0.378799)*x20 + (0.288406)*x21 + (0.967551)*x22 + (0.680283)*x23 + (0.431589)*x24 + (0.228124)
x32 = (0.036767)*x20 + (0.749949)*x21 + (1.001255)*x22 + (-0.361723)*x23 + (0.936326)*x24 + (0.079167)
x33 = (-0.559546)*x20 + (-0.343103)*x21 + (0.120574)*x22 + (-0.440341)*x23 + (-0.280624)*x24 + (0.000000)
x34 = (0.726788)*x20 + (-0.544370)*x21 + (-1.394731)*x22 + (-0.544997)*x23 + (0.474231)*x24 + (-0.046119)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (-0.284295)*x30 + (0.295046)*x31 + (0.712608)*x32 + (-0.146999)*x33 + (-0.432389)*x34 + (0.113896)
x41 = (0.843113)*x30 + (-0.810720)*x31 + (-0.107567)*x32 + (-0.730876)*x33 + (1.096594)*x34 + (0.156262)
x42 = (-0.084475)*x30 + (0.858908)*x31 + (0.304893)*x32 + (0.169247)*x33 + (0.064982)*x34 + (-0.048449)
x43 = (-0.018899)*x30 + (0.116177)*x31 + (0.316160)*x32 + (0.503853)*x33 + (-0.614927)*x34 + (0.194069)
x44 = (-0.782099)*x30 + (0.208947)*x31 + (-0.148217)*x32 + (-0.510550)*x33 + (0.156607)*x34 + (-0.074829)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (0.901359)*x40 + (0.069585)*x41 + (0.199000)*x42 + (0.481443)*x43 + (-0.616673)*x44 + (-0.215674)
x51 = (0.030244)*x40 + (1.246210)*x41 + (-0.918131)*x42 + (-0.752502)*x43 + (0.538157)*x44 + (0.215675)
