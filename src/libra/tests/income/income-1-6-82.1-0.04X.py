x00 = float(input())
x01 = float(input())
x02 = float(input())
x03 = float(input())
x04 = float(input())
x05 = float(input())
x06 = float(input())
x07 = float(input())
x08 = float(input())
x09 = float(input())
x010 = float(input())
x011 = float(input())
x012 = float(input())
x013 = float(input())
x014 = float(input())
x015 = float(input())
x016 = float(input())

x10 = (0.596223)*x00 + (0.212688)*x01 + (0.047146)*x02 + (0.315803)*x03 + (-0.555265)*x04 + (0.758739)*x05 + (-0.382463)*x06 + (-0.214813)*x07 + (-0.584624)*x08 + (-0.662200)*x09 + (-0.120513)*x010 + (0.266373)*x011 + (0.010064)*x012 + (-0.013238)*x013 + (0.063163)*x014 + (-0.310753)*x015 + (0.619484)*x016 + (-0.076259)
x11 = (-0.050122)*x00 + (-0.061149)*x01 + (-0.194528)*x02 + (0.014733)*x03 + (0.919079)*x04 + (-0.612314)*x05 + (0.250734)*x06 + (-0.292053)*x07 + (-0.059624)*x08 + (0.043496)*x09 + (0.464668)*x010 + (0.404504)*x011 + (0.191852)*x012 + (0.310385)*x013 + (0.580990)*x014 + (0.452109)*x015 + (-0.366552)*x016 + (0.344438)
x12 = (-0.288366)*x00 + (0.106812)*x01 + (-0.198493)*x02 + (-0.093434)*x03 + (0.208588)*x04 + (-0.188724)*x05 + (-0.511943)*x06 + (0.035082)*x07 + (-0.103508)*x08 + (-0.185822)*x09 + (0.002232)*x010 + (-0.361681)*x011 + (0.142920)*x012 + (-0.398208)*x013 + (-0.300685)*x014 + (0.262065)*x015 + (-0.532372)*x016 + (-0.196949)
x13 = (0.327544)*x00 + (0.083785)*x01 + (-0.156906)*x02 + (0.174731)*x03 + (0.380883)*x04 + (0.454944)*x05 + (-0.075875)*x06 + (-0.124706)*x07 + (0.481372)*x08 + (1.431159)*x09 + (0.413435)*x010 + (0.125180)*x011 + (0.300368)*x012 + (0.135964)*x013 + (-0.345362)*x014 + (0.565139)*x015 + (0.176413)*x016 + (0.053329)
x14 = (0.098345)*x00 + (-0.143743)*x01 + (-0.240917)*x02 + (-0.042719)*x03 + (-0.407570)*x04 + (0.693303)*x05 + (-0.260430)*x06 + (-0.273212)*x07 + (-0.412178)*x08 + (-0.163970)*x09 + (0.004250)*x010 + (0.065777)*x011 + (-0.605916)*x012 + (-0.090276)*x013 + (0.018744)*x014 + (-0.059689)*x015 + (0.216335)*x016 + (-0.092507)
x15 = (-0.096171)*x00 + (0.160218)*x01 + (-0.399202)*x02 + (0.447405)*x03 + (1.016034)*x04 + (-0.139145)*x05 + (0.024494)*x06 + (0.081585)*x07 + (0.362536)*x08 + (-0.066267)*x09 + (0.151476)*x010 + (0.594871)*x011 + (0.408174)*x012 + (0.235703)*x013 + (-0.202578)*x014 + (0.022170)*x015 + (0.165024)*x016 + (0.264362)
#
x10 = x10 if x10 > 0 else 0
x11 = x11 if x11 > 0 else 0
x12 = x12 if x12 > 0 else 0
x13 = x13 if x13 > 0 else 0
x14 = x14 if x14 > 0 else 0
x15 = x15 if x15 > 0 else 0

x20 = (-0.402846)*x10 + (-0.321606)*x11 + (-0.337326)*x12 + (-0.272713)*x13 + (0.474830)*x14 + (-0.286002)*x15 + (0.000000)
x21 = (0.445173)*x10 + (-1.177842)*x11 + (-0.221282)*x12 + (0.358458)*x13 + (0.943607)*x14 + (0.436668)*x15 + (-0.038089)
x22 = (-0.545817)*x10 + (0.583193)*x11 + (0.018106)*x12 + (0.193836)*x13 + (-0.797087)*x14 + (0.402481)*x15 + (0.225986)
x23 = (-0.550857)*x10 + (-0.035216)*x11 + (-0.248341)*x12 + (0.013250)*x13 + (-0.673160)*x14 + (-0.163167)*x15 + (-0.022624)
x24 = (-0.758908)*x10 + (0.544409)*x11 + (-0.452082)*x12 + (0.404816)*x13 + (0.211927)*x14 + (-0.138266)*x15 + (0.124387)
x25 = (0.019038)*x10 + (0.949152)*x11 + (-0.088806)*x12 + (-0.664432)*x13 + (0.030979)*x14 + (0.285888)*x15 + (0.174417)
#
x20 = x20 if x20 > 0 else 0
x21 = x21 if x21 > 0 else 0
x22 = x22 if x22 > 0 else 0
x23 = x23 if x23 > 0 else 0
x24 = x24 if x24 > 0 else 0
x25 = x25 if x25 > 0 else 0

x30 = (-0.289059)*x20 + (-0.432571)*x21 + (1.179019)*x22 + (-0.130143)*x23 + (0.296585)*x24 + (0.681725)*x25 + (0.142705)
x31 = (0.699698)*x20 + (1.065142)*x21 + (-1.165120)*x22 + (0.471685)*x23 + (-1.099620)*x24 + (-0.606226)*x25 + (-0.142705)

if x31 <= x30:
    raise ValueError
