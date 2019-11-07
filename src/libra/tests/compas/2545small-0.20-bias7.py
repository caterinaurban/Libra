
assume(0 <= x02 <= 0)
assume(1 <= x03 <= 1)
assume(0 <= x04 <= 0)

x10 = (0.342941)*x00 + (-0.173687)*x01 + (-0.240544)*x02 + (0.428156)*x03 + (0.392054)*x04 + (-0.021993)*x05 + (-0.147970)*x06 + (-0.132288)*x07 + (-0.108458)*x08 + (-0.197474)*x09 + (-0.124749)*x010 + (-0.417407)*x011 + (-0.375313)*x012 + (-0.940877)*x013 + (-1.408409)*x014 + (0.145594)*x015 + (0.276885)*x016 + (0.458194)*x017 + (0.016593)*x018 + (-0.149752)*x019 + (-0.305348)*x020 + (0.015167)
x11 = (-0.473823)*x00 + (0.548684)*x01 + (-0.076482)*x02 + (-0.284580)*x03 + (0.064900)*x04 + (-0.091086)*x05 + (0.182558)*x06 + (-0.000903)*x07 + (0.046811)*x08 + (-0.265920)*x09 + (0.280428)*x010 + (0.319259)*x011 + (-0.371290)*x012 + (0.454717)*x013 + (0.332583)*x014 + (-0.194811)*x015 + (-0.431944)*x016 + (-0.169641)*x017 + (-0.390033)*x018 + (0.388312)*x019 + (0.286394)*x020 + (0.129777)
x12 = (-0.206110)*x00 + (-0.196553)*x01 + (-0.270394)*x02 + (-0.205920)*x03 + (0.377380)*x04 + (-0.108985)*x05 + (0.113271)*x06 + (-0.566181)*x07 + (0.242048)*x08 + (0.479895)*x09 + (0.114486)*x010 + (0.235456)*x011 + (0.349284)*x012 + (0.274643)*x013 + (0.609256)*x014 + (-0.022571)*x015 + (-0.024038)*x016 + (-0.389426)*x017 + (-0.306657)*x018 + (0.384124)*x019 + (0.418252)*x020 + (-0.010052)
x13 = (-0.314396)*x00 + (-0.187908)*x01 + (-0.289836)*x02 + (0.195630)*x03 + (0.139836)*x04 + (0.239978)*x05 + (-0.046530)*x06 + (0.276439)*x07 + (-0.051789)*x08 + (0.188616)*x09 + (-0.095307)*x010 + (0.966612)*x011 + (0.795742)*x012 + (0.489610)*x013 + (0.797943)*x014 + (0.324524)*x015 + (0.084803)*x016 + (-0.044957)*x017 + (-0.287591)*x018 + (0.441846)*x019 + (0.409179)*x020 + (0.018705)
x14 = (0.403303)*x00 + (-0.317612)*x01 + (-0.548636)*x02 + (-0.100410)*x03 + (0.199407)*x04 + (-0.220843)*x05 + (-0.017873)*x06 + (-0.348935)*x07 + (0.008873)*x08 + (-0.097520)*x09 + (0.059446)*x010 + (0.910219)*x011 + (1.030069)*x012 + (-0.015546)*x013 + (1.037929)*x014 + (0.169291)*x015 + (0.463645)*x016 + (0.332075)*x017 + (0.305333)*x018 + (0.034847)*x019 + (-0.294012)*x020 + (-0.018667)
#
ReLU(x10)
ReLU(x11)
ReLU(x12)
ReLU(x13)
ReLU(x14)

x20 = (-0.431414)*x10 + (0.367511)*x11 + (-0.269446)*x12 + (-0.720367)*x13 + (0.257720)*x14 + (0.050165)
x21 = (0.088831)*x10 + (-0.309013)*x11 + (0.882460)*x12 + (-0.080373)*x13 + (-0.006847)*x14 + (-0.073523)
x22 = (-0.160792)*x10 + (0.303441)*x11 + (-0.280605)*x12 + (0.591957)*x13 + (-0.545859)*x14 + (-0.000698)
x23 = (-0.614486)*x10 + (-0.328648)*x11 + (-0.551644)*x12 + (0.737943)*x13 + (0.748295)*x14 + (-0.095645)
x24 = (-0.378620)*x10 + (0.615275)*x11 + (0.710555)*x12 + (0.141445)*x13 + (-0.293511)*x14 + (-0.045161)
#
ReLU(x20)
ReLU(x21)
ReLU(x22)
ReLU(x23)
ReLU(x24)

x30 = (-0.191316)*x20 + (0.668373)*x21 + (0.295737)*x22 + (1.254691)*x23 + (0.968295)*x24 + (-0.094014)
x31 = (-0.830963)*x20 + (0.711523)*x21 + (-0.532335)*x22 + (0.635397)*x23 + (0.360252)*x24 + (-0.027072)
x32 = (-0.133819)*x20 + (0.536450)*x21 + (-0.400838)*x22 + (0.069037)*x23 + (-0.660157)*x24 + (-0.033061)
x33 = (0.446982)*x20 + (0.033505)*x21 + (0.357022)*x22 + (-0.102012)*x23 + (-0.748405)*x24 + (0.111926)
x34 = (-0.351883)*x20 + (0.239286)*x21 + (-0.481404)*x22 + (0.373736)*x23 + (-0.000268)*x24 + (-0.176566)
#
ReLU(x30)
ReLU(x31)
ReLU(x32)
ReLU(x33)
ReLU(x34)

x40 = (0.973186)*x30 + (-0.235647)*x31 + (0.049252)*x32 + (0.241567)*x33 + (0.066413)*x34 + (-0.031763)
x41 = (0.272380)*x30 + (-0.350343)*x31 + (-0.302872)*x32 + (-0.399619)*x33 + (-0.317903)*x34 + (-0.037975)
x42 = (-0.286363)*x30 + (0.293615)*x31 + (-0.331353)*x32 + (0.509217)*x33 + (-0.564244)*x34 + (0.281327)
x43 = (0.737939)*x30 + (0.661837)*x31 + (0.392621)*x32 + (-0.694626)*x33 + (-0.090634)*x34 + (-0.046056)
x44 = (-0.004203)*x30 + (-0.669907)*x31 + (-0.121067)*x32 + (-0.131651)*x33 + (-0.235152)*x34 + (0.000000)
#
ReLU(x40)
ReLU(x41)
ReLU(x42)
ReLU(x43)
ReLU(x44)

x50 = (-0.818979)*x40 + (0.459983)*x41 + (1.165833)*x42 + (-0.942851)*x43 + (-0.624734)*x44 + (0.137819)
x51 = (0.513791)*x40 + (-0.415871)*x41 + (0.727899)*x42 + (-0.566900)*x43 + (0.410597)*x44 + (0.009474)
x52 = (-0.169703)*x40 + (0.780194)*x41 + (-0.532204)*x42 + (1.034667)*x43 + (-0.656372)*x44 + (-0.071589)
#

