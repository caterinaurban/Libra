
x10 = (-0.307622)*x00 + (-0.196333)*x01 + (-0.151284)*x02 + (0.490525)*x03 + (0.947941)*x04 + (-0.101603)*x05 + (0.053747)*x06 + (0.159710)*x07 + (0.250317)*x08 + (0.387641)*x09 + (0.493217)*x010 + (-0.227513)*x011 + (0.180452)*x012 + (-0.073060)*x013 + (0.249084)*x014 + (0.361052)*x015 + (0.715569)*x016 + (-0.155332)*x017 + (-0.268274)*x018 + (0.398469)*x019 + (-0.061925)*x020 + (-0.032444)*x021 + (-0.173435)*x022 + (0.061339)
x11 = (-0.115505)*x00 + (-0.022954)*x01 + (0.352607)*x02 + (0.237420)*x03 + (1.334871)*x04 + (-0.484568)*x05 + (0.219222)*x06 + (-0.138012)*x07 + (0.346701)*x08 + (0.083659)*x09 + (0.322971)*x010 + (0.368010)*x011 + (-0.245804)*x012 + (-0.016517)*x013 + (0.079757)*x014 + (-0.332944)*x015 + (0.697848)*x016 + (0.771741)*x017 + (0.440005)*x018 + (0.443719)*x019 + (0.059566)*x020 + (0.158171)*x021 + (0.181267)*x022 + (0.332027)
x12 = (0.165268)*x00 + (0.362157)*x01 + (0.187587)*x02 + (0.098004)*x03 + (1.421801)*x04 + (-0.726792)*x05 + (0.277644)*x06 + (0.380000)*x07 + (0.535096)*x08 + (0.429453)*x09 + (0.239646)*x010 + (0.232048)*x011 + (0.062049)*x012 + (0.123675)*x013 + (0.284278)*x014 + (0.016105)*x015 + (0.334027)*x016 + (-0.187158)*x017 + (0.052322)*x018 + (0.196413)*x019 + (0.319584)*x020 + (0.338293)*x021 + (-0.387286)*x022 + (0.233829)
x13 = (-1.148075)*x00 + (0.138050)*x01 + (0.048123)*x02 + (0.000947)*x03 + (1.312092)*x04 + (-0.403930)*x05 + (-0.104995)*x06 + (0.107038)*x07 + (-0.009292)*x08 + (0.063909)*x09 + (0.251887)*x010 + (0.086997)*x011 + (-0.019054)*x012 + (0.011422)*x013 + (0.107821)*x014 + (0.031805)*x015 + (0.554891)*x016 + (0.484859)*x017 + (0.672109)*x018 + (0.423066)*x019 + (0.185074)*x020 + (0.201263)*x021 + (-0.678394)*x022 + (0.206410)
x14 = (0.314372)*x00 + (0.379409)*x01 + (0.153793)*x02 + (0.129751)*x03 + (-0.540744)*x04 + (0.829704)*x05 + (0.291655)*x06 + (-0.219097)*x07 + (-0.214734)*x08 + (-0.043940)*x09 + (0.181524)*x010 + (0.166060)*x011 + (-0.112221)*x012 + (-0.347842)*x013 + (0.461780)*x014 + (-0.267354)*x015 + (-0.743901)*x016 + (-0.177202)*x017 + (0.262682)*x018 + (0.077177)*x019 + (0.043864)*x020 + (0.103400)*x021 + (0.680552)*x022 + (-0.004735)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (0.763373)*x10 + (0.531444)*x11 + (0.646645)*x12 + (0.568030)*x13 + (-0.541664)*x14 + (0.344571)
x21 = (0.673662)*x10 + (0.370814)*x11 + (0.083519)*x12 + (-1.295269)*x13 + (0.730424)*x14 + (0.131500)
x22 = (0.220829)*x10 + (0.472757)*x11 + (0.774269)*x12 + (1.547978)*x13 + (-0.424570)*x14 + (0.109470)
x23 = (-0.537415)*x10 + (-0.423052)*x11 + (0.326012)*x12 + (0.137922)*x13 + (0.023810)*x14 + (0.047892)
x24 = (-0.295373)*x10 + (0.475348)*x11 + (-0.922756)*x12 + (-0.112740)*x13 + (0.366864)*x14 + (0.073859)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.223671)*x20 + (0.403750)*x21 + (1.466247)*x22 + (0.833207)*x23 + (0.285963)*x24 + (0.031478)
x31 = (-1.380170)*x20 + (0.885673)*x21 + (-0.077951)*x22 + (0.050166)*x23 + (1.024082)*x24 + (-0.031477)