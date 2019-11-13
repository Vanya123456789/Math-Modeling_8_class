def polnaya_mechanicheskaya_E(m,h,v):
    g = 10
    Ep = m*g*h
    Ek = m*(v**2)/2
    const = Ep+Ek
    print(const)
polnaya_mechanicheskaya_E(100,10,100)