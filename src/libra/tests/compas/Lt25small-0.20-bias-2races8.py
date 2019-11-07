
assume(1 <= x02 <= 1)
assume(0 <= x03 <= 0)
assume(0 <= x04 <= 0)

x10 = (-0.259263)*x00 + (0.046586)*x01 + (0.077184)*x02 + (0.194010)*x03 + (0.430923)*x04 + (0.033796)*x05 + (0.396568)*x06 + (0.234588)*x07 + (0.034654)*x08 + (0.020779)*x09 + (0.065468)*x010 + (-1.475205)*x011 + (-0.697139)*x012 + (-0.126862)*x013 + (-0.839113)*x014 + (0.246961)*x015 + (0.344880)*x016 + (-0.080569)*x017 + (0.209526)*x018 + (-0.176217)*x019 + (0.113722)*x020 + (0.123102)
x11 = (0.197292)*x00 + (0.002530)*x01 + (0.044482)*x02 + (0.101824)*x03 + (-0.157565)*x04 + (0.364972)*x05 + (0.065887)*x06 + (-0.093992)*x07 + (0.144329)*x08 + (-0.061584)*x09 + (0.274135)*x010 + (-0.867660)*x011 + (-0.155209)*x012 + (-0.653003)*x013 + (-1.028689)*x014 + (-0.140281)*x015 + (0.094495)*x016 + (0.077160)*x017 + (-0.089010)*x018 + (0.176957)*x019 + (0.039807)*x020 + (0.258216)
x12 = (-0.059404)*x00 + (0.510139)*x01 + (0.379097)*x02 + (0.323692)*x03 + (-0.093169)*x04 + (0.137172)*x05 + (0.105264)*x06 + (-0.079181)*x07 + (-0.081621)*x08 + (-0.001171)*x09 + (0.039777)*x010 + (0.475672)*x011 + (0.952308)*x012 + (0.007092)*x013 + (1.008717)*x014 + (-0.126608)*x015 + (0.275889)*x016 + (-0.062462)*x017 + (-0.211627)*x018 + (-0.316815)*x019 + (-0.538344)*x020 + (0.038858)
x13 = (0.364688)*x00 + (0.290076)*x01 + (0.263976)*x02 + (-0.206586)*x03 + (-0.491492)*x04 + (-0.281475)*x05 + (0.218734)*x06 + (0.229847)*x07 + (-0.284167)*x08 + (-0.456046)*x09 + (-0.262078)*x010 + (1.139240)*x011 + (-0.192585)*x012 + (0.216776)*x013 + (0.688489)*x014 + (-0.247354)*x015 + (-0.277323)*x016 + (0.138067)*x017 + (0.321696)*x018 + (-0.302368)*x019 + (0.101703)*x020 + (-0.051215)
x14 = (-0.322411)*x00 + (-0.292821)*x01 + (0.054927)*x02 + (0.472687)*x03 + (0.113781)*x04 + (0.009844)*x05 + (0.092038)*x06 + (0.218663)*x07 + (-0.032742)*x08 + (0.001049)*x09 + (0.111911)*x010 + (0.410273)*x011 + (-0.389996)*x012 + (-0.177192)*x013 + (0.347749)*x014 + (0.217429)*x015 + (-0.130162)*x016 + (-0.455284)*x017 + (0.387810)*x018 + (0.049501)*x019 + (0.386380)*x020 + (0.146898)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.044682)*x10 + (0.437875)*x11 + (-0.471924)*x12 + (-0.100132)*x13 + (-0.748128)*x14 + (0.089756)
x21 = (-0.530470)*x10 + (-0.503553)*x11 + (0.752091)*x12 + (-0.231114)*x13 + (0.588198)*x14 + (0.186910)
x22 = (0.316950)*x10 + (0.633039)*x11 + (-0.514179)*x12 + (0.237745)*x13 + (0.140905)*x14 + (0.033419)
x23 = (-0.464920)*x10 + (-0.509475)*x11 + (0.380341)*x12 + (-0.196222)*x13 + (-0.322623)*x14 + (0.167283)
x24 = (0.793936)*x10 + (0.479878)*x11 + (-0.242645)*x12 + (-0.696736)*x13 + (-0.042408)*x14 + (0.230838)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.659782)*x20 + (-0.435473)*x21 + (0.509218)*x22 + (-0.489081)*x23 + (0.885872)*x24 + (0.008904)
x31 = (0.402230)*x20 + (0.243908)*x21 + (0.138546)*x22 + (-0.827168)*x23 + (0.567184)*x24 + (-0.058316)
x32 = (0.353553)*x20 + (0.251287)*x21 + (0.259107)*x22 + (0.264608)*x23 + (-0.248831)*x24 + (0.316234)
x33 = (-0.695755)*x20 + (0.574714)*x21 + (0.170936)*x22 + (0.730680)*x23 + (0.073380)*x24 + (0.272364)
x34 = (-0.469321)*x20 + (0.609550)*x21 + (-0.597415)*x22 + (-0.201257)*x23 + (-0.122001)*x24 + (0.197094)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.388460)*x30 + (0.274942)*x31 + (0.217847)*x32 + (-0.064647)*x33 + (0.835378)*x34 + (0.109717)
x41 = (-0.226574)*x30 + (-0.399246)*x31 + (0.636734)*x32 + (0.553400)*x33 + (-0.230626)*x34 + (0.315401)
x42 = (-0.753596)*x30 + (-0.576475)*x31 + (0.575098)*x32 + (-0.263343)*x33 + (-0.347550)*x34 + (-0.078816)
x43 = (-0.039891)*x30 + (-0.826770)*x31 + (0.382850)*x32 + (0.263815)*x33 + (0.512760)*x34 + (0.195892)
x44 = (0.784975)*x30 + (0.213977)*x31 + (-0.349396)*x32 + (0.210272)*x33 + (-0.773346)*x34 + (-0.002523)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.738634)*x40 + (-0.527537)*x41 + (0.615717)*x42 + (-1.284912)*x43 + (0.933234)*x44 + (-0.612887)
x51 = (0.423014)*x40 + (-0.531951)*x41 + (0.277006)*x42 + (-0.829654)*x43 + (-0.591005)*x44 + (0.044288)
x52 = (-0.831816)*x40 + (0.994004)*x41 + (-0.734997)*x42 + (0.229855)*x43 + (-0.736358)*x44 + (0.479439)
#

