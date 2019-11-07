
assume(0 <= x05 <= 0)
assume(1 <= x06 <= 1)
assume(0 <= x07 <= 0)
assume(0 <= x08 <= 0)
assume(0 <= x09 <= 0)
assume(0 <= x010 <= 0)

x10 = (-0.201764)*x00 + (-0.643181)*x01 + (-0.371388)*x02 + (0.086387)*x03 + (0.084019)*x04 + (-0.242008)*x05 + (0.243026)*x06 + (-0.204890)*x07 + (0.303516)*x08 + (0.367308)*x09 + (0.254156)*x010 + (0.091952)*x011 + (-0.020869)*x012 + (-0.017793)*x013 + (0.303347)*x014 + (0.328961)*x015 + (-0.276909)*x016 + (0.433552)*x017 + (0.045769)*x018 + (0.123843)*x019 + (0.269206)*x020 + (-0.016136)
x11 = (-0.480641)*x00 + (-0.202077)*x01 + (-0.327978)*x02 + (-0.238024)*x03 + (0.375478)*x04 + (-0.410578)*x05 + (-0.219122)*x06 + (-0.210559)*x07 + (-0.144865)*x08 + (-0.164091)*x09 + (-0.197060)*x010 + (0.606673)*x011 + (0.044649)*x012 + (0.279828)*x013 + (-0.034566)*x014 + (0.075358)*x015 + (0.130355)*x016 + (-0.021195)*x017 + (0.310215)*x018 + (-0.295486)*x019 + (0.247399)*x020 + (-0.090877)
x12 = (0.374104)*x00 + (-0.141380)*x01 + (0.156597)*x02 + (-0.393894)*x03 + (0.329789)*x04 + (0.241563)*x05 + (-0.278585)*x06 + (0.281177)*x07 + (0.324732)*x08 + (-0.315995)*x09 + (-0.272063)*x010 + (0.799895)*x011 + (0.602499)*x012 + (0.664677)*x013 + (1.070932)*x014 + (0.340801)*x015 + (-0.209170)*x016 + (0.230518)*x017 + (-0.397240)*x018 + (-0.190745)*x019 + (-0.342390)*x020 + (-0.008966)
x13 = (0.260837)*x00 + (0.161208)*x01 + (-0.261086)*x02 + (0.158967)*x03 + (0.161341)*x04 + (-0.050256)*x05 + (-0.096574)*x06 + (-0.042180)*x07 + (-0.187829)*x08 + (-0.029106)*x09 + (-0.112884)*x010 + (1.168555)*x011 + (0.981704)*x012 + (0.689755)*x013 + (0.972618)*x014 + (-0.033765)*x015 + (-0.007350)*x016 + (0.031195)*x017 + (0.104390)*x018 + (-0.301807)*x019 + (-0.324494)*x020 + (0.021376)
x14 = (-0.174069)*x00 + (0.329365)*x01 + (-0.182249)*x02 + (0.341208)*x03 + (0.248862)*x04 + (-0.035458)*x05 + (0.269719)*x06 + (-0.062218)*x07 + (0.066222)*x08 + (0.443204)*x09 + (0.295421)*x010 + (0.597453)*x011 + (0.627398)*x012 + (-0.011771)*x013 + (1.051020)*x014 + (0.193764)*x015 + (0.426089)*x016 + (0.199838)*x017 + (0.368783)*x018 + (-0.149220)*x019 + (-0.291336)*x020 + (-0.047227)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.527164)*x10 + (0.400321)*x11 + (-0.199317)*x12 + (0.676174)*x13 + (-0.701527)*x14 + (-0.064018)
x21 = (0.407707)*x10 + (-0.654629)*x11 + (-0.642681)*x12 + (-0.974010)*x13 + (0.527213)*x14 + (0.109577)
x22 = (0.872800)*x10 + (0.361283)*x11 + (0.303029)*x12 + (0.091231)*x13 + (-0.703060)*x14 + (0.151729)
x23 = (0.577208)*x10 + (0.146181)*x11 + (0.368277)*x12 + (0.598771)*x13 + (0.485828)*x14 + (-0.071517)
x24 = (-0.497660)*x10 + (-0.076677)*x11 + (0.722886)*x12 + (-0.900911)*x13 + (-0.038308)*x14 + (0.036110)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (0.588012)*x20 + (-1.269380)*x21 + (-0.303127)*x22 + (0.512723)*x23 + (0.372152)*x24 + (-0.148922)
x31 = (0.142341)*x20 + (-0.133316)*x21 + (0.236212)*x22 + (-0.105419)*x23 + (0.556438)*x24 + (-0.086497)
x32 = (0.490126)*x20 + (-0.149501)*x21 + (-0.112656)*x22 + (0.512366)*x23 + (0.391467)*x24 + (-0.090846)
x33 = (-0.314226)*x20 + (-0.661397)*x21 + (-0.468047)*x22 + (0.782439)*x23 + (-0.307347)*x24 + (0.001167)
x34 = (0.335066)*x20 + (-0.312149)*x21 + (0.422169)*x22 + (-0.142017)*x23 + (0.136241)*x24 + (0.108129)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.295893)*x30 + (-0.234053)*x31 + (-0.256599)*x32 + (-0.185403)*x33 + (-0.289613)*x34 + (-0.003000)
x41 = (-0.621011)*x30 + (-0.824243)*x31 + (0.223976)*x32 + (0.236456)*x33 + (-0.012167)*x34 + (-0.078330)
x42 = (-0.347177)*x30 + (0.334873)*x31 + (0.664945)*x32 + (0.935943)*x33 + (-0.239259)*x34 + (-0.086938)
x43 = (-0.021380)*x30 + (-0.076585)*x31 + (0.022752)*x32 + (-0.514455)*x33 + (-0.587915)*x34 + (-0.013592)
x44 = (-0.017265)*x30 + (0.576958)*x31 + (0.819203)*x32 + (1.056755)*x33 + (-0.923194)*x34 + (-0.088625)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.488871)*x40 + (-0.395311)*x41 + (-1.106876)*x42 + (-0.688987)*x43 + (-1.091526)*x44 + (0.193286)
x51 = (-0.404351)*x40 + (-0.327333)*x41 + (0.007339)*x42 + (-0.436249)*x43 + (0.087466)*x44 + (0.088966)
x52 = (-0.664427)*x40 + (1.287475)*x41 + (0.871641)*x42 + (0.091277)*x43 + (0.870375)*x44 + (-0.236972)
#

