
assume(1 <= x02 <= 1)
assume(0 <= x03 <= 0)
assume(0 <= x04 <= 0)

x10 = (0.241248)*x00 + (-0.537230)*x01 + (0.382879)*x02 + (-0.095715)*x03 + (0.349231)*x04 + (-0.316798)*x05 + (-0.202543)*x06 + (0.187782)*x07 + (-0.194949)*x08 + (0.067161)*x09 + (-0.366460)*x010 + (0.073959)*x011 + (-0.752101)*x012 + (0.193970)*x013 + (-0.473436)*x014 + (0.218426)*x015 + (-0.227626)*x016 + (-0.033107)*x017 + (0.161805)*x018 + (0.219211)*x019 + (0.108108)*x020 + (-0.063603)
x11 = (0.027094)*x00 + (0.447310)*x01 + (0.710602)*x02 + (0.258010)*x03 + (-0.093399)*x04 + (0.162882)*x05 + (-0.050305)*x06 + (0.481319)*x07 + (-0.191052)*x08 + (0.041943)*x09 + (0.062204)*x010 + (0.941060)*x011 + (0.614763)*x012 + (0.229722)*x013 + (1.358647)*x014 + (0.194565)*x015 + (-0.211898)*x016 + (0.411444)*x017 + (-0.049337)*x018 + (0.487478)*x019 + (0.397114)*x020 + (0.081605)
x12 = (-0.459415)*x00 + (-0.125373)*x01 + (0.257020)*x02 + (-0.255606)*x03 + (0.137477)*x04 + (-0.413772)*x05 + (0.120572)*x06 + (0.233357)*x07 + (-0.348603)*x08 + (-0.121121)*x09 + (0.012733)*x010 + (-0.364479)*x011 + (-0.085922)*x012 + (0.322422)*x013 + (-0.287431)*x014 + (-0.116214)*x015 + (-0.454927)*x016 + (-0.349688)*x017 + (0.094285)*x018 + (-0.042191)*x019 + (-0.125596)*x020 + (-0.056663)
x13 = (-0.124984)*x00 + (0.043523)*x01 + (0.036218)*x02 + (0.079377)*x03 + (-0.121310)*x04 + (0.143780)*x05 + (0.108023)*x06 + (0.241228)*x07 + (0.059811)*x08 + (0.160111)*x09 + (0.137562)*x010 + (-0.620632)*x011 + (-0.722602)*x012 + (-0.678431)*x013 + (-1.155375)*x014 + (-0.020649)*x015 + (-0.074969)*x016 + (0.312441)*x017 + (0.133086)*x018 + (-0.048686)*x019 + (-0.049544)*x020 + (0.072676)
x14 = (0.285878)*x00 + (0.234506)*x01 + (-0.065797)*x02 + (-0.170256)*x03 + (0.801874)*x04 + (0.561679)*x05 + (0.340792)*x06 + (0.234960)*x07 + (0.342645)*x08 + (-0.026593)*x09 + (0.493156)*x010 + (-1.279335)*x011 + (-0.606788)*x012 + (0.140565)*x013 + (-1.021291)*x014 + (0.191729)*x015 + (-0.016995)*x016 + (0.276462)*x017 + (0.124396)*x018 + (-0.357134)*x019 + (-0.062957)*x020 + (0.130953)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.137420)*x10 + (0.501626)*x11 + (0.567846)*x12 + (0.188288)*x13 + (-0.440838)*x14 + (-0.051782)
x21 = (-0.763769)*x10 + (0.461005)*x11 + (-0.588003)*x12 + (-0.184639)*x13 + (-0.921643)*x14 + (0.178610)
x22 = (-0.041351)*x10 + (0.795993)*x11 + (0.272781)*x12 + (-1.004745)*x13 + (0.451639)*x14 + (0.088950)
x23 = (0.359571)*x10 + (0.254088)*x11 + (-0.302657)*x12 + (-1.319423)*x13 + (-0.014664)*x14 + (0.131872)
x24 = (-0.123950)*x10 + (-0.451165)*x11 + (-0.590980)*x12 + (-0.070495)*x13 + (0.575766)*x14 + (-0.046353)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.609397)*x20 + (-0.673194)*x21 + (-0.664927)*x22 + (0.590367)*x23 + (-0.489591)*x24 + (0.023459)
x31 = (-0.732458)*x20 + (0.354222)*x21 + (0.430351)*x22 + (0.913439)*x23 + (-0.783225)*x24 + (-0.168232)
x32 = (0.674587)*x20 + (1.357246)*x21 + (0.379778)*x22 + (1.129351)*x23 + (-0.283781)*x24 + (-0.007566)
x33 = (-0.606562)*x20 + (-0.296655)*x21 + (0.488194)*x22 + (-0.506326)*x23 + (-0.168477)*x24 + (0.186145)
x34 = (-0.525096)*x20 + (-0.177243)*x21 + (-0.553010)*x22 + (-0.427825)*x23 + (0.431953)*x24 + (-0.005825)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (-0.631126)*x30 + (-0.932448)*x31 + (0.298298)*x32 + (-0.359803)*x33 + (0.599786)*x34 + (0.052986)
x41 = (-0.643661)*x30 + (0.197349)*x31 + (-0.086214)*x32 + (0.011258)*x33 + (0.334908)*x34 + (-0.128205)
x42 = (0.050846)*x30 + (-0.240993)*x31 + (-0.622250)*x32 + (-0.000722)*x33 + (0.174042)*x34 + (-0.003162)
x43 = (0.440414)*x30 + (-1.001989)*x31 + (0.205920)*x32 + (0.724359)*x33 + (-0.682625)*x34 + (0.128103)
x44 = (0.160515)*x30 + (-0.026733)*x31 + (1.112251)*x32 + (-0.931896)*x33 + (0.691771)*x34 + (-0.011986)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (0.857859)*x40 + (-0.086488)*x41 + (0.673118)*x42 + (1.155059)*x43 + (0.041644)*x44 + (-0.142770)
x51 = (-0.074535)*x40 + (-0.392482)*x41 + (-0.220684)*x42 + (-0.760241)*x43 + (0.602535)*x44 + (0.234556)
x52 = (-0.446825)*x40 + (-0.244764)*x41 + (-0.482175)*x42 + (-0.858808)*x43 + (1.184899)*x44 + (-0.177904)
#

