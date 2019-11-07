
assume(0 <= x02 <= 0)
assume(0 <= x03 <= 0)
assume(1 <= x04 <= 1)

x10 = (0.458856)*x00 + (0.230922)*x01 + (-0.130640)*x02 + (-0.382036)*x03 + (0.090726)*x04 + (-0.351998)*x05 + (0.276389)*x06 + (-0.015405)*x07 + (-0.115312)*x08 + (-0.025691)*x09 + (-0.203411)*x010 + (1.430666)*x011 + (1.228428)*x012 + (0.154707)*x013 + (0.222110)*x014 + (0.501249)*x015 + (0.460846)*x016 + (-0.198118)*x017 + (-0.406633)*x018 + (0.066806)
x11 = (-0.112492)*x00 + (-0.498467)*x01 + (-0.122755)*x02 + (0.579099)*x03 + (0.145168)*x04 + (0.112797)*x05 + (0.015972)*x06 + (-0.203140)*x07 + (-0.138640)*x08 + (0.087434)*x09 + (-0.315937)*x010 + (-0.701148)*x011 + (0.243004)*x012 + (-0.075639)*x013 + (-0.462974)*x014 + (-0.228877)*x015 + (-0.313685)*x016 + (0.403236)*x017 + (-0.315395)*x018 + (-0.087534)
x12 = (-0.242434)*x00 + (0.261295)*x01 + (-0.149681)*x02 + (0.321768)*x03 + (-0.256340)*x04 + (-0.288441)*x05 + (0.213888)*x06 + (-0.127387)*x07 + (-0.099029)*x08 + (-0.134894)*x09 + (-0.267415)*x010 + (-0.861646)*x011 + (-0.644095)*x012 + (-0.043972)*x013 + (0.587120)*x014 + (0.016301)*x015 + (-0.063983)*x016 + (0.324199)*x017 + (0.336351)*x018 + (0.123361)
x13 = (-0.195784)*x00 + (-0.182253)*x01 + (-0.130927)*x02 + (0.302565)*x03 + (0.256944)*x04 + (-0.465321)*x05 + (0.440190)*x06 + (-0.126564)*x07 + (-0.483784)*x08 + (-0.156509)*x09 + (0.295880)*x010 + (-0.318239)*x011 + (-0.043422)*x012 + (-0.493181)*x013 + (0.091757)*x014 + (-0.326547)*x015 + (-0.026863)*x016 + (-0.272386)*x017 + (-0.107483)*x018 + (0.067658)
x14 = (0.177927)*x00 + (-0.412216)*x01 + (-0.088430)*x02 + (-0.031639)*x03 + (-0.174999)*x04 + (-0.055439)*x05 + (0.358979)*x06 + (-0.446406)*x07 + (0.146271)*x08 + (0.167294)*x09 + (0.152770)*x010 + (-0.509208)*x011 + (-1.130894)*x012 + (-0.274446)*x013 + (-0.348424)*x014 + (-0.038144)*x015 + (-0.058699)*x016 + (0.562782)*x017 + (-0.371873)*x018 + (0.113245)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.782045)*x10 + (-0.419623)*x11 + (-0.138937)*x12 + (0.374162)*x13 + (0.464527)*x14 + (0.036243)
x21 = (-0.237850)*x10 + (0.208896)*x11 + (-0.448904)*x12 + (-0.206292)*x13 + (-0.451699)*x14 + (-0.031922)
x22 = (-0.245844)*x10 + (0.341068)*x11 + (0.185211)*x12 + (-0.495855)*x13 + (0.910305)*x14 + (0.183022)
x23 = (0.918655)*x10 + (-0.298822)*x11 + (-0.063482)*x12 + (0.030759)*x13 + (-0.436300)*x14 + (0.080636)
x24 = (0.104070)*x10 + (0.573367)*x11 + (0.863443)*x12 + (0.429559)*x13 + (0.433340)*x14 + (0.147412)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.001185)*x20 + (0.516772)*x21 + (-0.625220)*x22 + (0.167307)*x23 + (0.742916)*x24 + (0.225631)
x31 = (0.452669)*x20 + (-0.055790)*x21 + (-0.330180)*x22 + (0.546601)*x23 + (-0.307109)*x24 + (-0.002697)
x32 = (0.521146)*x20 + (-0.028748)*x21 + (0.470758)*x22 + (-0.534888)*x23 + (0.587532)*x24 + (-0.055853)
x33 = (-0.655360)*x20 + (0.678558)*x21 + (0.497418)*x22 + (-0.077284)*x23 + (0.013822)*x24 + (0.077028)
x34 = (0.596310)*x20 + (0.530986)*x21 + (-0.940182)*x22 + (0.510409)*x23 + (-0.084488)*x24 + (0.108658)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.056545)*x30 + (0.245346)*x31 + (0.309576)*x32 + (0.204996)*x33 + (-0.648141)*x34 + (0.166206)
x41 = (0.397032)*x30 + (0.631310)*x31 + (-0.227793)*x32 + (-0.413629)*x33 + (1.062486)*x34 + (0.194943)
x42 = (0.667953)*x30 + (-0.567121)*x31 + (-0.288671)*x32 + (0.081149)*x33 + (-0.342557)*x34 + (0.119138)
x43 = (-0.216342)*x30 + (-0.276600)*x31 + (-0.499607)*x32 + (0.266824)*x33 + (0.180759)*x34 + (0.000000)
x44 = (0.527183)*x30 + (-0.914150)*x31 + (-0.293982)*x32 + (0.419945)*x33 + (0.114180)*x34 + (0.087799)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (0.923441)*x40 + (-0.456766)*x41 + (0.736124)*x42 + (-0.009478)*x43 + (0.414709)*x44 + (-0.272932)
x51 = (-0.218385)*x40 + (0.020628)*x41 + (0.637865)*x42 + (-0.851434)*x43 + (0.247167)*x44 + (0.085373)
x52 = (0.755008)*x40 + (0.830463)*x41 + (-0.858749)*x42 + (0.097793)*x43 + (-0.738348)*x44 + (0.182392)
#

