#A felhsználó dönti el, hogy szerkezet- vagy kulcsrakész házat szertne, ha a kulcsrakészt választja akkor a program hozzá számol munkadijjat. Ha a ház teljes mérete nem éri el a 200m2-t, akkor 10% felárral számol ezek mellet a program számol hozzá 5% áfát függetlenül a lakotér tipusától.

alapt=int(input("Kérjük adja meg az alapterület méretét(m2): "))

kerdes=input("Kulcsrakész házat vagy csak a szerkezetét szeretné? ")
#árak
munkadij1=190000
munkadij2=75000
munkadij3=25000

teraszar=alapt*35000
erkelyar=alapt*110000
foldszintar=215000
emeletar=185000
#számitások
szamitas1=alapt*(foldszintar+munkadij1)
szamitas2=alapt*(emeletar+munkadij1)
szamitas3=alapt*(teraszar+munkadij3)
szamitas4=alapt*(erkelyar+munkadij2)
#kulcsrakész
if kerdes=="kulcsrakész":
    felepites=input("Lakótér - földszint, emeletet szeretne? ")
    if felepites=="földszint":
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="taraszt":
            osszeg=szamitas1+szamitas3
        elif egyeb=="erkélyt":
            osszeg=szamitas1+szamitas4
        else:
            osszeg=szamitas1
    else:
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="igen":
            osszeg=szamitas2+szamitas3
        elif egyeb=="erkélyt":
            osszeg=szamitas2+szamitas4  
        else:
            osszeg=szamitas2 
#szerkezetes  
else:
    felepites=input("Lakótér - földszint, emeletet szeretne? ")
    if felepites=="földszint":
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="igen":
            osszeg=szamitas1+(alapt*35000)
        elif egyeb=="erkélyt":
            osszeg=szamitas1+(alapt*110000)
        else:
            osszeg=szamitas1
    else:
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="igen":
            osszeg=szamitas2+(alapt*35000)
        elif egyeb=="erkélyt":
            osszeg=szamitas2+(alapt*110000)
        else:
            osszeg=szamitas2
#+10% számoló
if alapt < 200:
    print((osszeg/100*10)+(osszeg/100*5)+osszeg)
else:
    print((osszeg/100*5)+osszeg)