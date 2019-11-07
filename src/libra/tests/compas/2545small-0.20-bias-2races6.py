
assume(1 <= x02 <= 1)
assume(0 <= x03 <= 0)
assume(0 <= x04 <= 0)

x10 = (0.235653)*x00 + (-0.124999)*x01 + (-0.100275)*x02 + (-0.483158)*x03 + (-0.017812)*x04 + (0.418980)*x05 + (0.520666)*x06 + (0.112201)*x07 + (0.429847)*x08 + (0.231324)*x09 + (0.177236)*x010 + (-1.018485)*x011 + (-0.566066)*x012 + (0.451659)*x013 + (0.334017)*x014 + (0.076704)*x015 + (-0.088927)*x016 + (0.185203)*x017 + (-0.111616)*x018 + (0.036307)
x11 = (-0.412859)*x00 + (0.171744)*x01 + (-0.142558)*x02 + (-0.233106)*x03 + (-0.290556)*x04 + (-0.063386)*x05 + (0.423600)*x06 + (-0.448490)*x07 + (0.348369)*x08 + (0.268249)*x09 + (0.335497)*x010 + (-0.430850)*x011 + (-0.214837)*x012 + (0.371421)*x013 + (0.019584)*x014 + (-0.487679)*x015 + (0.015190)*x016 + (-0.304244)*x017 + (-0.255659)*x018 + (-0.034526)
x12 = (0.289326)*x00 + (-0.160707)*x01 + (0.333627)*x02 + (0.100890)*x03 + (-0.125620)*x04 + (-0.145614)*x05 + (0.399903)*x06 + (-0.519242)*x07 + (0.021134)*x08 + (-0.031131)*x09 + (-0.214159)*x010 + (0.290304)*x011 + (1.068283)*x012 + (0.049246)*x013 + (0.317365)*x014 + (0.149279)*x015 + (0.434941)*x016 + (0.325409)*x017 + (0.342609)*x018 + (0.044158)
x13 = (0.435039)*x00 + (0.361054)*x01 + (-0.188950)*x02 + (-0.198527)*x03 + (-0.513918)*x04 + (0.325870)*x05 + (0.111063)*x06 + (0.148681)*x07 + (0.136263)*x08 + (0.164947)*x09 + (0.016766)*x010 + (0.811124)*x011 + (0.429916)*x012 + (-0.036723)*x013 + (-0.386613)*x014 + (0.320911)*x015 + (0.153766)*x016 + (-0.139770)*x017 + (-0.599622)*x018 + (-0.043498)
x14 = (-0.290488)*x00 + (-0.414494)*x01 + (0.174512)*x02 + (0.129291)*x03 + (-0.255650)*x04 + (0.016527)*x05 + (0.154910)*x06 + (-0.067806)*x07 + (0.053552)*x08 + (0.073848)*x09 + (0.109082)*x010 + (-0.943759)*x011 + (-1.074088)*x012 + (-0.072717)*x013 + (0.192583)*x014 + (-0.498517)*x015 + (0.462682)*x016 + (-0.034467)*x017 + (0.075679)*x018 + (0.137945)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.041064)*x10 + (-0.746347)*x11 + (0.692078)*x12 + (-0.392227)*x13 + (0.656277)*x14 + (0.117272)
x21 = (-0.239625)*x10 + (-0.029161)*x11 + (-0.350503)*x12 + (-0.539493)*x13 + (0.511424)*x14 + (0.016355)
x22 = (-0.527769)*x10 + (-0.510341)*x11 + (0.230298)*x12 + (0.569245)*x13 + (-0.161785)*x14 + (0.052015)
x23 = (-0.091924)*x10 + (0.404535)*x11 + (0.036085)*x12 + (-0.210667)*x13 + (-0.512732)*x14 + (0.087778)
x24 = (-0.785462)*x10 + (-0.597101)*x11 + (0.806082)*x12 + (0.182749)*x13 + (-0.714338)*x14 + (0.039781)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.053978)*x20 + (0.201875)*x21 + (-0.549501)*x22 + (0.577070)*x23 + (0.262428)*x24 + (0.017965)
x31 = (0.739141)*x20 + (-0.498942)*x21 + (-0.456152)*x22 + (-0.047082)*x23 + (-0.209738)*x24 + (0.113629)
x32 = (-0.195543)*x20 + (0.670633)*x21 + (-0.465012)*x22 + (0.462280)*x23 + (-0.522462)*x24 + (-0.054118)
x33 = (0.350580)*x20 + (0.649632)*x21 + (0.139869)*x22 + (-0.125785)*x23 + (0.973865)*x24 + (-0.006309)
x34 = (-0.097447)*x20 + (0.430978)*x21 + (0.857963)*x22 + (0.447792)*x23 + (0.732008)*x24 + (-0.039392)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (-1.041198)*x30 + (0.748419)*x31 + (-0.120935)*x32 + (0.183909)*x33 + (0.715913)*x34 + (-0.070116)
x41 = (0.478399)*x30 + (0.092181)*x31 + (0.368801)*x32 + (0.162817)*x33 + (0.809374)*x34 + (0.059957)
x42 = (-0.077860)*x30 + (0.461255)*x31 + (-0.376756)*x32 + (-0.006259)*x33 + (-0.168094)*x34 + (-0.111507)
x43 = (0.261110)*x30 + (-0.353474)*x31 + (0.399945)*x32 + (0.819834)*x33 + (0.903036)*x34 + (0.047827)
x44 = (-0.035270)*x30 + (0.647414)*x31 + (0.231857)*x32 + (0.010550)*x33 + (-0.724381)*x34 + (0.171474)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.465593)*x40 + (-1.156037)*x41 + (0.026901)*x42 + (-1.144761)*x43 + (1.145722)*x44 + (-0.013585)
x51 = (-0.928477)*x40 + (0.287172)*x41 + (-0.617664)*x42 + (-0.418163)*x43 + (0.741569)*x44 + (0.050990)
x52 = (0.591971)*x40 + (-0.059057)*x41 + (-0.337689)*x42 + (-0.307317)*x43 + (-0.789761)*x44 + (-0.064412)
#

