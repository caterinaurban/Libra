
x10 = (0.230939)*x00 + (0.367144)*x01 + (0.001312)*x02 + (-0.112271)*x03 + (-0.275650)*x04 + (0.367652)*x05 + (0.409322)*x06 + (0.103634)*x07 + (0.394006)*x08 + (-0.146980)*x09 + (0.049689)*x010 + (-0.081711)*x011 + (-0.199710)*x012 + (0.394286)*x013 + (-0.322005)*x014 + (-0.587016)*x015 + (0.353737)*x016 + (-0.012997)
x11 = (-0.124128)*x00 + (-0.300848)*x01 + (-0.282198)*x02 + (0.026454)*x03 + (-0.471964)*x04 + (0.469191)*x05 + (0.376916)*x06 + (0.412269)*x07 + (0.016064)*x08 + (0.040520)*x09 + (-0.242506)*x010 + (-0.382246)*x011 + (-0.085956)*x012 + (0.230164)*x013 + (-0.064650)*x014 + (-0.068068)*x015 + (-0.344616)*x016 + (0.056140)
x12 = (0.078817)*x00 + (-0.306604)*x01 + (-0.240470)*x02 + (0.040505)*x03 + (-0.266229)*x04 + (0.407955)*x05 + (-0.110168)*x06 + (-0.216079)*x07 + (-0.133409)*x08 + (0.151012)*x09 + (0.118017)*x010 + (-0.230311)*x011 + (0.173576)*x012 + (0.034950)*x013 + (0.518165)*x014 + (-0.180182)*x015 + (0.596595)*x016 + (0.054330)
x13 = (-0.511135)*x00 + (0.334395)*x01 + (0.184404)*x02 + (0.174143)*x03 + (-0.296172)*x04 + (-0.169295)*x05 + (-0.173801)*x06 + (-0.475828)*x07 + (0.350807)*x08 + (-0.355106)*x09 + (0.228740)*x010 + (0.120006)*x011 + (0.345102)*x012 + (-0.382960)*x013 + (-0.087915)*x014 + (0.434773)*x015 + (-0.084397)*x016 + (0.085006)
x14 = (-0.331753)*x00 + (-0.376723)*x01 + (0.098070)*x02 + (-0.239525)*x03 + (-0.216123)*x04 + (0.227603)*x05 + (-0.256326)*x06 + (-0.313281)*x07 + (-0.211363)*x08 + (-0.500511)*x09 + (-0.325616)*x010 + (0.446133)*x011 + (-0.110102)*x012 + (-0.372233)*x013 + (-0.261212)*x014 + (0.057475)*x015 + (-0.306606)*x016 + (0.000000)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.273655)*x10 + (-0.476048)*x11 + (0.076396)*x12 + (-0.315186)*x13 + (-0.362240)*x14 + (-0.131616)
x21 = (-0.554888)*x10 + (-0.761641)*x11 + (-0.095823)*x12 + (-0.250369)*x13 + (-0.735186)*x14 + (0.000000)
x22 = (-0.641458)*x10 + (0.418001)*x11 + (0.373019)*x12 + (-0.330374)*x13 + (0.165261)*x14 + (0.101801)
x23 = (-0.431225)*x10 + (0.661055)*x11 + (-0.533010)*x12 + (-0.501334)*x13 + (-0.622529)*x14 + (0.139545)
x24 = (-0.395942)*x10 + (-0.520764)*x11 + (0.058652)*x12 + (0.529402)*x13 + (-0.225008)*x14 + (-0.043914)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.542006)*x20 + (-0.401556)*x21 + (0.840912)*x22 + (-0.575811)*x23 + (-0.208015)*x24 + (-0.003174)
x31 = (0.708020)*x20 + (-0.742433)*x21 + (0.319526)*x22 + (-0.576031)*x23 + (0.439397)*x24 + (-0.111593)
x32 = (0.347309)*x20 + (0.310264)*x21 + (0.512946)*x22 + (-0.645940)*x23 + (-0.427213)*x24 + (0.093005)
x33 = (-0.530676)*x20 + (0.739207)*x21 + (-0.242235)*x22 + (-0.156525)*x23 + (-0.555796)*x24 + (0.000000)
x34 = (0.541403)*x20 + (-0.275605)*x21 + (-0.396364)*x22 + (0.166636)*x23 + (0.690155)*x24 + (0.134617)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.755178)*x30 + (-0.084550)*x31 + (0.350151)*x32 + (-0.112710)*x33 + (-0.701859)*x34 + (0.054329)
x41 = (0.850653)*x30 + (-0.502887)*x31 + (0.813290)*x32 + (-0.031629)*x33 + (-0.629988)*x34 + (0.002451)
x42 = (0.839701)*x30 + (0.263720)*x31 + (0.323642)*x32 + (-0.396915)*x33 + (-0.067342)*x34 + (-0.025412)
x43 = (-0.742991)*x30 + (0.115094)*x31 + (0.214438)*x32 + (0.526946)*x33 + (0.120777)*x34 + (0.253790)
x44 = (0.521646)*x30 + (0.639347)*x31 + (0.274276)*x32 + (0.452692)*x33 + (0.243198)*x34 + (-0.059303)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.465211)*x40 + (-1.017916)*x41 + (-0.334755)*x42 + (0.741233)*x43 + (-0.662435)*x44 + (0.242025)
x51 = (1.006336)*x40 + (0.717146)*x41 + (0.092422)*x42 + (-0.797796)*x43 + (-0.244092)*x44 + (-0.242025)
