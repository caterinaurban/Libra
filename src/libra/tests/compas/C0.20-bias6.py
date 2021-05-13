
# caucasian
assume(1 <= x05 <= 1)
assume(0 <= x06 <= 0)
assume(0 <= x07 <= 0)
assume(0 <= x08 <= 0)
assume(0 <= x09 <= 0)
assume(0 <= x010 <= 0)

x10 = (0.367832)*x00 + (-0.520557)*x01 + (0.450905)*x02 + (-0.042198)*x03 + (-0.045778)*x04 + (0.103251)*x05 + (0.067362)*x06 + (0.014472)*x07 + (0.171191)*x08 + (0.238427)*x09 + (-0.276625)*x010 + (-0.504895)*x011 + (0.023278)*x012 + (0.253012)*x013 + (0.124718)*x014 + (0.215371)*x015 + (0.023566)*x016 + (0.074360)*x017 + (0.224998)*x018 + (-0.029021)
x11 = (0.131034)*x00 + (0.673319)*x01 + (-0.462088)*x02 + (-0.285712)*x03 + (-0.251660)*x04 + (-0.137786)*x05 + (-0.066895)*x06 + (-0.072241)*x07 + (0.083199)*x08 + (0.003481)*x09 + (-0.207307)*x010 + (0.071281)*x011 + (-1.024630)*x012 + (0.077631)*x013 + (0.092570)*x014 + (-0.408760)*x015 + (0.156170)*x016 + (-0.599119)*x017 + (0.408019)*x018 + (-0.037542)
x12 = (0.188481)*x00 + (0.405490)*x01 + (-0.160432)*x02 + (-0.156231)*x03 + (0.187492)*x04 + (0.139113)*x05 + (0.155821)*x06 + (0.414814)*x07 + (0.172876)*x08 + (0.150207)*x09 + (0.124767)*x010 + (0.980704)*x011 + (1.314913)*x012 + (0.215304)*x013 + (-0.244560)*x014 + (-0.311523)*x015 + (-0.205839)*x016 + (0.125999)*x017 + (0.412547)*x018 + (0.074639)
x13 = (-0.302689)*x00 + (-0.471486)*x01 + (0.220728)*x02 + (-0.709014)*x03 + (0.216304)*x04 + (0.014310)*x05 + (-0.031545)*x06 + (-0.071826)*x07 + (-0.013473)*x08 + (0.034482)*x09 + (-0.035440)*x010 + (0.683922)*x011 + (1.074895)*x012 + (-0.089171)*x013 + (0.133412)*x014 + (0.136323)*x015 + (0.068262)*x016 + (0.114159)*x017 + (0.092405)*x018 + (-0.042917)
x14 = (-0.118617)*x00 + (-0.747457)*x01 + (0.080736)*x02 + (-0.316864)*x03 + (0.214951)*x04 + (0.208856)*x05 + (0.223931)*x06 + (-0.036291)*x07 + (-0.045508)*x08 + (0.032224)*x09 + (-0.044749)*x010 + (-0.089173)*x011 + (-0.295513)*x012 + (-0.452353)*x013 + (-0.644425)*x014 + (-0.431216)*x015 + (0.351029)*x016 + (-0.080716)*x017 + (0.324448)*x018 + (-0.060054)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.279774)*x10 + (-0.293192)*x11 + (-0.168151)*x12 + (-0.861158)*x13 + (0.675669)*x14 + (0.231133)
x21 = (-0.005588)*x10 + (-0.339737)*x11 + (0.749431)*x12 + (0.595940)*x13 + (0.203347)*x14 + (-0.041126)
x22 = (-0.493073)*x10 + (0.974351)*x11 + (0.236168)*x12 + (-0.113102)*x13 + (-0.691243)*x14 + (-0.177204)
x23 = (-0.018157)*x10 + (-0.000963)*x11 + (-0.000464)*x12 + (0.978824)*x13 + (0.293174)*x14 + (-0.003089)
x24 = (0.433057)*x10 + (-0.683118)*x11 + (0.498765)*x12 + (-0.086319)*x13 + (-0.083227)*x14 + (-0.056295)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.986258)*x20 + (0.744704)*x21 + (-0.322138)*x22 + (0.533004)*x23 + (0.178341)*x24 + (0.002873)
x31 = (-0.024217)*x20 + (-0.691652)*x21 + (-0.462508)*x22 + (0.290350)*x23 + (-0.429691)*x24 + (-0.016214)
x32 = (0.201160)*x20 + (-0.184880)*x21 + (0.583365)*x22 + (0.016450)*x23 + (-0.415851)*x24 + (0.232849)
x33 = (-0.228658)*x20 + (0.687007)*x21 + (-0.054511)*x22 + (-0.179795)*x23 + (0.740862)*x24 + (-0.145595)
x34 = (-0.399969)*x20 + (0.786612)*x21 + (0.684924)*x22 + (0.866765)*x23 + (-0.468786)*x24 + (0.013933)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.162026)*x30 + (0.751457)*x31 + (0.444341)*x32 + (-0.486275)*x33 + (0.613287)*x34 + (-0.000844)
x41 = (0.176571)*x30 + (0.099720)*x31 + (0.375897)*x32 + (-0.467932)*x33 + (-0.350901)*x34 + (0.045981)
x42 = (0.960938)*x30 + (-0.692394)*x31 + (-0.055997)*x32 + (0.610402)*x33 + (0.211019)*x34 + (-0.162399)
x43 = (0.647064)*x30 + (-0.102214)*x31 + (-0.915087)*x32 + (-0.313946)*x33 + (0.720963)*x34 + (-0.050961)
x44 = (0.414323)*x30 + (0.631492)*x31 + (-0.026318)*x32 + (0.458285)*x33 + (0.843765)*x34 + (-0.067191)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.917806)*x40 + (0.929236)*x41 + (-1.045197)*x42 + (-0.243754)*x43 + (0.033856)*x44 + (0.303518)
x51 = (0.737682)*x40 + (-0.763232)*x41 + (-0.414971)*x42 + (-0.205905)*x43 + (0.716657)*x44 + (0.066477)
x52 = (-0.617873)*x40 + (0.389426)*x41 + (0.643560)*x42 + (0.389462)*x43 + (0.500985)*x44 + (-0.296252)
#
