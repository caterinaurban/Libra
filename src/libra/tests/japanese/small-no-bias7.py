
x10 = (0.351218)*x00 + (0.353330)*x01 + (-0.149090)*x02 + (-0.069296)*x03 + (-0.030327)*x04 + (0.733889)*x05 + (-0.361569)*x06 + (0.061321)*x07 + (-0.364746)*x08 + (0.079540)*x09 + (-0.318351)*x010 + (-0.033064)*x011 + (-0.100325)*x012 + (0.091941)*x013 + (0.343010)*x014 + (-0.120326)*x015 + (0.032071)*x016 + (0.101776)
x11 = (0.337286)*x00 + (0.204685)*x01 + (0.344896)*x02 + (0.250145)*x03 + (0.207169)*x04 + (-0.266788)*x05 + (0.338594)*x06 + (0.177217)*x07 + (0.099310)*x08 + (0.376397)*x09 + (-0.103338)*x010 + (0.589217)*x011 + (-0.249282)*x012 + (0.666450)*x013 + (-0.635282)*x014 + (0.114036)*x015 + (0.692653)*x016 + (0.172576)
x12 = (0.173319)*x00 + (0.146102)*x01 + (-0.035875)*x02 + (-0.088705)*x03 + (-0.026346)*x04 + (0.189079)*x05 + (0.360288)*x06 + (-0.007049)*x07 + (-0.343503)*x08 + (0.375032)*x09 + (0.384401)*x010 + (-0.462471)*x011 + (-0.112561)*x012 + (-0.486990)*x013 + (0.446393)*x014 + (-0.211398)*x015 + (0.107992)*x016 + (0.131566)
x13 = (0.449327)*x00 + (-0.350965)*x01 + (0.473300)*x02 + (-0.514300)*x03 + (-0.011331)*x04 + (-0.132658)*x05 + (-0.245251)*x06 + (-0.419523)*x07 + (-0.458794)*x08 + (0.084027)*x09 + (-0.424822)*x010 + (0.110455)*x011 + (-0.252086)*x012 + (-0.242503)*x013 + (-0.571627)*x014 + (-0.326589)*x015 + (-0.181307)*x016 + (-0.046858)
x14 = (-0.168034)*x00 + (-0.172399)*x01 + (0.316315)*x02 + (-0.229488)*x03 + (0.043503)*x04 + (0.128711)*x05 + (-0.340644)*x06 + (0.037517)*x07 + (0.341828)*x08 + (-0.506600)*x09 + (-0.277110)*x010 + (0.242515)*x011 + (-0.364146)*x012 + (-0.037179)*x013 + (-0.287009)*x014 + (-0.259419)*x015 + (-0.063407)*x016 + (-0.059834)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.286019)*x10 + (0.417695)*x11 + (-0.693808)*x12 + (-0.505872)*x13 + (-0.196708)*x14 + (0.172227)
x21 = (-0.495256)*x10 + (-0.150905)*x11 + (0.635629)*x12 + (0.694494)*x13 + (-0.693576)*x14 + (-0.045013)
x22 = (0.074818)*x10 + (0.260007)*x11 + (-0.387828)*x12 + (0.565763)*x13 + (0.480712)*x14 + (0.131576)
x23 = (-0.638812)*x10 + (0.196212)*x11 + (0.387684)*x12 + (-0.422647)*x13 + (0.335921)*x14 + (0.119870)
x24 = (0.358695)*x10 + (0.081706)*x11 + (-0.558905)*x12 + (-0.376995)*x13 + (0.512985)*x14 + (0.061702)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.058583)*x20 + (0.026630)*x21 + (-0.395174)*x22 + (-0.042119)*x23 + (0.048870)*x24 + (0.158562)
x31 = (-0.102768)*x20 + (0.297434)*x21 + (-0.028789)*x22 + (-0.147479)*x23 + (-0.671117)*x24 + (-0.090883)
x32 = (-0.217842)*x20 + (-0.600610)*x21 + (-0.455189)*x22 + (0.368370)*x23 + (0.222970)*x24 + (-0.024762)
x33 = (-0.181134)*x20 + (-0.395783)*x21 + (-0.245690)*x22 + (-0.006051)*x23 + (0.465320)*x24 + (-0.041689)
x34 = (0.953386)*x20 + (0.397784)*x21 + (0.373257)*x22 + (0.695247)*x23 + (0.674068)*x24 + (0.029522)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (-0.830587)*x30 + (-0.347608)*x31 + (0.623238)*x32 + (0.612991)*x33 + (0.696653)*x34 + (0.066345)
x41 = (0.861003)*x30 + (-0.572634)*x31 + (0.596644)*x32 + (-0.466001)*x33 + (0.191794)*x34 + (0.234562)
x42 = (-0.398889)*x30 + (-0.733318)*x31 + (-0.155077)*x32 + (-0.493252)*x33 + (-0.763541)*x34 + (0.000000)
x43 = (0.612464)*x30 + (0.204108)*x31 + (0.160404)*x32 + (0.352633)*x33 + (-0.195584)*x34 + (0.253677)
x44 = (-0.309067)*x30 + (-0.744808)*x31 + (-0.548038)*x32 + (-0.042809)*x33 + (0.018804)*x34 + (-0.034068)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.745088)*x40 + (-0.029467)*x41 + (0.214202)*x42 + (0.104193)*x43 + (0.711272)*x44 + (0.232760)
x51 = (1.066397)*x40 + (-0.351601)*x41 + (-0.532454)*x42 + (-0.598656)*x43 + (0.502345)*x44 + (-0.232760)
