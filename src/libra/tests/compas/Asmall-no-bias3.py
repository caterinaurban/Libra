
assume(0 <= x05 <= 0)
assume(0 <= x06 <= 0)
assume(1 <= x07 <= 1)
assume(0 <= x08 <= 0)
assume(0 <= x09 <= 0)
assume(0 <= x010 <= 0)

x10 = (0.091269)*x00 + (0.308747)*x01 + (0.283505)*x02 + (0.210767)*x03 + (-0.199231)*x04 + (-0.025185)*x05 + (-0.068593)*x06 + (-0.061797)*x07 + (-0.128366)*x08 + (0.052729)*x09 + (-0.267748)*x010 + (0.015715)*x011 + (0.349115)*x012 + (-0.416415)*x013 + (-0.225718)*x014 + (-0.306607)*x015 + (-0.366684)*x016 + (-0.237277)*x017 + (-0.165226)*x018 + (-0.268783)*x019 + (-0.039947)*x020 + (-0.052521)
x11 = (-0.237716)*x00 + (-0.030614)*x01 + (0.348237)*x02 + (0.306626)*x03 + (0.213215)*x04 + (0.090940)*x05 + (0.079497)*x06 + (0.339778)*x07 + (-0.057591)*x08 + (0.142828)*x09 + (0.019248)*x010 + (0.478274)*x011 + (0.844632)*x012 + (0.250873)*x013 + (1.436354)*x014 + (0.041407)*x015 + (-0.100693)*x016 + (0.258929)*x017 + (0.368546)*x018 + (-0.294752)*x019 + (-0.331759)*x020 + (0.054809)
x12 = (0.406602)*x00 + (0.338426)*x01 + (0.200291)*x02 + (-0.165740)*x03 + (0.295151)*x04 + (-0.231935)*x05 + (-0.134203)*x06 + (-0.319420)*x07 + (0.379187)*x08 + (0.340557)*x09 + (0.354765)*x010 + (0.657439)*x011 + (0.982331)*x012 + (0.000972)*x013 + (1.324064)*x014 + (0.238618)*x015 + (0.386736)*x016 + (0.449477)*x017 + (-0.093449)*x018 + (0.108002)*x019 + (0.377617)*x020 + (0.010773)
x13 = (-0.069503)*x00 + (0.108596)*x01 + (0.166195)*x02 + (0.311321)*x03 + (0.801854)*x04 + (-0.058784)*x05 + (-0.016073)*x06 + (0.157927)*x07 + (0.054280)*x08 + (0.237983)*x09 + (0.123071)*x010 + (-1.562547)*x011 + (-0.607012)*x012 + (-0.601241)*x013 + (-0.790943)*x014 + (-0.210269)*x015 + (-0.295130)*x016 + (0.262977)*x017 + (0.062730)*x018 + (0.188985)*x019 + (0.112574)*x020 + (0.225806)
x14 = (-0.022756)*x00 + (0.124612)*x01 + (-0.106354)*x02 + (-0.302670)*x03 + (0.674055)*x04 + (0.389319)*x05 + (-0.052982)*x06 + (-0.110981)*x07 + (0.174605)*x08 + (-0.036233)*x09 + (0.069864)*x010 + (-0.600076)*x011 + (0.124678)*x012 + (-0.340647)*x013 + (0.269248)*x014 + (0.146300)*x015 + (0.121994)*x016 + (-0.599909)*x017 + (0.031056)*x018 + (0.255604)*x019 + (-0.279346)*x020 + (0.021906)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.734386)*x10 + (-0.079014)*x11 + (-0.126496)*x12 + (0.848093)*x13 + (0.408853)*x14 + (0.090295)
x21 = (-0.339232)*x10 + (0.115102)*x11 + (-0.611338)*x12 + (-0.530506)*x13 + (-0.083887)*x14 + (-0.022583)
x22 = (-0.322783)*x10 + (0.887233)*x11 + (0.313365)*x12 + (-0.300644)*x13 + (0.144434)*x14 + (0.017958)
x23 = (0.086990)*x10 + (-0.711518)*x11 + (-0.035065)*x12 + (-0.534457)*x13 + (0.298235)*x14 + (-0.036846)
x24 = (0.611817)*x10 + (-0.196491)*x11 + (-0.761205)*x12 + (0.017790)*x13 + (-0.563788)*x14 + (-0.003160)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.534544)*x20 + (-0.166115)*x21 + (1.031396)*x22 + (0.132860)*x23 + (-0.360662)*x24 + (0.090898)
x31 = (0.223519)*x20 + (-0.304736)*x21 + (0.566671)*x22 + (0.555636)*x23 + (0.112289)*x24 + (-0.263796)
x32 = (0.593859)*x20 + (-0.467453)*x21 + (-0.335510)*x22 + (0.200042)*x23 + (-0.762551)*x24 + (0.270706)
x33 = (0.831955)*x20 + (0.640699)*x21 + (-0.055968)*x22 + (-0.797414)*x23 + (0.543176)*x24 + (-0.012501)
x34 = (-0.637723)*x20 + (0.122097)*x21 + (-0.366397)*x22 + (0.446430)*x23 + (-0.485758)*x24 + (-0.052830)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.868591)*x30 + (0.119161)*x31 + (-0.634497)*x32 + (-0.552713)*x33 + (-0.703184)*x34 + (0.108706)
x41 = (0.566739)*x30 + (0.198594)*x31 + (-0.060326)*x32 + (-1.035819)*x33 + (0.170858)*x34 + (-0.041637)
x42 = (-0.479577)*x30 + (0.390848)*x31 + (0.568708)*x32 + (-0.708462)*x33 + (0.556103)*x34 + (-0.062284)
x43 = (0.705031)*x30 + (0.578769)*x31 + (-0.164740)*x32 + (0.294906)*x33 + (-0.059945)*x34 + (-0.202643)
x44 = (0.901190)*x30 + (-0.063184)*x31 + (-0.046062)*x32 + (-0.918532)*x33 + (-0.461643)*x34 + (-0.047256)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.829637)*x40 + (-0.154086)*x41 + (0.715905)*x42 + (-0.436759)*x43 + (-0.952830)*x44 + (0.231028)
x51 = (0.045438)*x40 + (-0.470084)*x41 + (-0.165526)*x42 + (0.742491)*x43 + (-0.381234)*x44 + (-0.066386)
x52 = (0.923617)*x40 + (0.699845)*x41 + (-0.057519)*x42 + (-0.107227)*x43 + (0.094670)*x44 + (-0.152788)
#

