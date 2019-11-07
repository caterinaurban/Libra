
assume(0 <= x05 <= 0)
assume(0 <= x06 <= 0)
assume(0 <= x07 <= 0)
assume(0 <= x08 <= 0)
assume(1 <= x09 <= 1)
assume(0 <= x010 <= 0)

x10 = (0.224569)*x00 + (0.439154)*x01 + (-0.070739)*x02 + (-0.303828)*x03 + (0.585932)*x04 + (-0.394992)*x05 + (0.384135)*x06 + (0.309378)*x07 + (-0.286531)*x08 + (0.132355)*x09 + (0.230962)*x010 + (0.423873)*x011 + (0.756158)*x012 + (0.524375)*x013 + (-0.218592)*x014 + (-0.277968)*x015 + (0.190794)*x016 + (0.185234)*x017 + (0.295779)*x018 + (0.099455)
x11 = (-0.097815)*x00 + (0.068488)*x01 + (0.128165)*x02 + (-0.165426)*x03 + (0.166580)*x04 + (-0.082111)*x05 + (0.237926)*x06 + (0.120541)*x07 + (0.105724)*x08 + (0.138818)*x09 + (0.107115)*x010 + (-1.236966)*x011 + (-1.099235)*x012 + (0.414087)*x013 + (0.154633)*x014 + (0.013591)*x015 + (0.387174)*x016 + (-0.146123)*x017 + (-0.137956)*x018 + (0.159103)
x12 = (0.194038)*x00 + (-0.180099)*x01 + (0.297806)*x02 + (-0.202031)*x03 + (0.252292)*x04 + (-0.080236)*x05 + (-0.177767)*x06 + (-0.050388)*x07 + (0.260051)*x08 + (-0.083181)*x09 + (-0.026338)*x010 + (0.364669)*x011 + (0.683532)*x012 + (-0.349333)*x013 + (0.163153)*x014 + (0.157620)*x015 + (0.120725)*x016 + (-0.183387)*x017 + (-0.074658)*x018 + (-0.058256)
x13 = (-0.132063)*x00 + (0.065268)*x01 + (-0.209934)*x02 + (0.589628)*x03 + (-0.318952)*x04 + (-0.260368)*x05 + (0.050193)*x06 + (-0.140207)*x07 + (0.033115)*x08 + (-0.448084)*x09 + (0.113201)*x010 + (-0.230686)*x011 + (0.215660)*x012 + (0.125906)*x013 + (0.235761)*x014 + (-0.520656)*x015 + (-0.100504)*x016 + (-0.309526)*x017 + (0.227040)*x018 + (0.107118)
x14 = (0.077042)*x00 + (0.481716)*x01 + (0.200407)*x02 + (-0.361269)*x03 + (0.237649)*x04 + (0.270964)*x05 + (0.201385)*x06 + (0.224841)*x07 + (0.188127)*x08 + (0.276035)*x09 + (0.012716)*x010 + (0.793386)*x011 + (0.829269)*x012 + (0.455343)*x013 + (0.059220)*x014 + (-0.368318)*x015 + (-0.084620)*x016 + (-0.220760)*x017 + (-0.201155)*x018 + (0.049580)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.557137)*x10 + (-0.878754)*x11 + (-0.287091)*x12 + (0.479521)*x13 + (0.404621)*x14 + (0.215941)
x21 = (-0.267932)*x10 + (-0.390805)*x11 + (0.422370)*x12 + (0.726807)*x13 + (-0.651981)*x14 + (-0.034594)
x22 = (-0.157430)*x10 + (0.416520)*x11 + (0.489810)*x12 + (0.333998)*x13 + (0.497037)*x14 + (0.030997)
x23 = (0.458411)*x10 + (-1.009755)*x11 + (0.566497)*x12 + (0.149351)*x13 + (0.588723)*x14 + (-0.016048)
x24 = (-0.619607)*x10 + (-0.256650)*x11 + (-0.611666)*x12 + (0.465859)*x13 + (0.321973)*x14 + (-0.206449)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.257912)*x20 + (0.909525)*x21 + (0.469673)*x22 + (0.362786)*x23 + (0.397204)*x24 + (0.095599)
x31 = (0.452741)*x20 + (-0.611761)*x21 + (-0.064783)*x22 + (0.815584)*x23 + (0.051719)*x24 + (-0.052640)
x32 = (0.628512)*x20 + (0.681538)*x21 + (-0.598558)*x22 + (-0.016098)*x23 + (-0.411764)*x24 + (0.229158)
x33 = (-0.593311)*x20 + (0.485534)*x21 + (-0.488772)*x22 + (-0.209341)*x23 + (0.566093)*x24 + (-0.067815)
x34 = (0.211592)*x20 + (0.571165)*x21 + (0.001572)*x22 + (0.845082)*x23 + (-0.270210)*x24 + (-0.048792)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.323705)*x30 + (0.692716)*x31 + (-1.091469)*x32 + (0.522689)*x33 + (0.778339)*x34 + (-0.095345)
x41 = (0.681957)*x30 + (-0.507558)*x31 + (-0.425430)*x32 + (-0.148091)*x33 + (-0.441775)*x34 + (0.184438)
x42 = (0.097713)*x30 + (0.836205)*x31 + (-0.686661)*x32 + (-0.304795)*x33 + (-0.136763)*x34 + (-0.070582)
x43 = (0.409092)*x30 + (0.825323)*x31 + (-0.113099)*x32 + (-0.031786)*x33 + (-0.612376)*x34 + (-0.114277)
x44 = (0.496354)*x30 + (-0.079062)*x31 + (0.582543)*x32 + (-0.372690)*x33 + (0.775343)*x34 + (-0.066897)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-1.243062)*x40 + (0.563713)*x41 + (0.179510)*x42 + (-0.767339)*x43 + (-0.804700)*x44 + (0.160942)
x51 = (-0.149922)*x40 + (-0.711545)*x41 + (-0.272138)*x42 + (-0.560059)*x43 + (0.313487)*x44 + (0.030751)
x52 = (0.654394)*x40 + (-1.195956)*x41 + (1.022618)*x42 + (-0.170444)*x43 + (-0.239421)*x44 + (-0.150558)
#

