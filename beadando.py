alapt=int(input("Kérjük adja meg az alapterület méretét(m2): "))

kerdes=input("Kulcsrakész házat vagy csak a szerkezetét szeretné? ")

munkadij1=190000
munkadij2=75000
munkadij3=25000

teraszar=alapt*35000
erkelyar=alapt*110000
foldszintar=215000
emeletar=185000

szamitas1=alapt*(foldszintar+munkadij1)
szamitas2=alapt*(emeletar+munkadij1)
szamitas3=alapt*(teraszar+munkadij3)
szamitas4=alapt*(erkelyar+munkadij2)

if kerdes=="kulcsrakész":
    felepites=input("Lakótér - földszint, emeletet szeretne? ")
    if felepites=="földszint":
        terasz=input("Szeretne e teraszt? ")
        if terasz=="igen":
            osszeg=szamitas1+szamitas3
        else:
            erkely=input("Szeretne e erkélyt? ")
        if erkely=="igen":
            osszeg=szamitas1+szamitas4
        else:
            osszeg=szamitas1
    else:
        terasz=input("Szeretne e teraszt?")
        if terasz=="igen":
            osszeg=szamitas2+szamitas3
        else:
            erkely=input("Szeretne e erkélyt? ")
        if erkely=="igen":
            osszeg=szamitas2+szamitas4  
        else:
            osszeg=szamitas2   
else:
    felepites=input("Lakótér - földszint, emeletet szeretne? ")
    if felepites=="földszint":
        terasz=input("Szeretne e teraszt? ")
        if terasz=="igen":
            osszeg=szamitas1+(alapt*35000)
        else:
            erkely=input("Szeretne e erkélyt? ")
        if erkely=="igen":
            osszeg=szamitas1+(alapt*110000)
        else:
            osszeg=szamitas1
    else:
        terasz=input("Szeretne e teraszt?")
        if terasz=="igen":
            osszeg=szamitas2+(alapt*35000)
        else:
              erkely=input("Szeretne e erkélyt? ")
        if erkely=="igen":
            osszeg=szamitas2+(alapt*110000)
        else:
            osszeg=szamitas2
if alapt < 200:
    print((osszeg/100*10)+osszeg)
else:
    print(osszeg)