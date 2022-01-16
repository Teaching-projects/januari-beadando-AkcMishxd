#A felhsználó dönti el, hogy szerkezet- vagy kulcsrakész házat szertne, ha a kulcsrakészt választja akkor a program hozzá számol munkadijjat. Ha a ház teljes mérete nem éri el a 200m2-t, akkor 10% felárral számol ezek mellet a program számol hozzá 5% áfát függetlenül a lakotér tipusától.

alapt=int(input("Kérjük adja meg az alapterület méretét(m2): "))

kerdes=input("Kulcsrakész házat vagy csak a szerkezetét szeretné? ")
#árak Ft/m2
munkadijhaz=190000 
munkadijterasz=75000
munkadijerkely=25000

teraszar=35000
erkelyar=110000
foldszintar=215000
emeletar=185000
#számitások
szamitasfoldszint=alapt*(foldszintar+munkadijhaz)
szamitasemelet=alapt*(emeletar+munkadijhaz)
szamitasterasz=teraszar+munkadijerkely
szamitaserkely=erkelyar+munkadijterasz
#kulcsrakész
if kerdes=="kulcsrakész":
    felepites=input("Lakótér - földszint, emeletet szeretne? ")
    if felepites=="földszint":
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="teraszt":
            teraszterulet=int(input("Kérjük adja meg az teraszterületének méretét(m2): "))
            osszeg=szamitasfoldszint+(teraszterulet*szamitasterasz)
        elif egyeb=="erkélyt":
            erkelyterulet=int(input("Kérjük adja meg az erkélyterületének méretét(m2): "))
            osszeg=szamitasfoldszint+(erkelyterulet*szamitasterasz)
        else:
            osszeg=szamitasfoldszint
    else:
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="teraszt":
           teraszterulet=int(input("Kérjük adja meg az teraszterületének méretét(m2): "))
           osszeg=szamitasemelet+(teraszterulet*szamitasterasz)
        elif egyeb=="erkélyt":
            erkelyterulet=int(input("Kérjük adja meg az erkélyületének méretét(m2): "))
            osszeg=szamitasemelet+(erkelyterulet*szamitasterasz)  
        else:
            osszeg=szamitasemelet 
#szerkezetes  
else:
    felepites=input("Lakótér - földszint, emeletet szeretne? ")
    if felepites=="földszint":
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="teraszt":
            teraszterulet=int(input("Kérjük adja meg az teraszterületének méretét(m2): "))
            osszeg=szamitasfoldszint+(teraszterulet*teraszar)
        elif egyeb=="erkélyt":
            erkelyterulet=int(input("Kérjük adja meg az erkélyületének méretét(m2): "))
            osszeg=szamitasfoldszint+(erkelyterulet*erkelyar)
        else:
            osszeg=szamitasfoldszint
    else:
        egyeb=input("teraszt vagy erkélyt szeretne? ")
        if egyeb=="teraszt":
            teraszterulet=int(input("Kérjük adja meg az teraszterületének méretét(m2): "))
            osszeg=szamitasemelet+(teraszterulet*teraszar)
        elif egyeb=="erkélyt":
            erkelyterulet=int(input("Kérjük adja meg az erkélyületének méretét(m2): "))
            osszeg=szamitasemelet+(erkelyterulet*erkelyar)
        else:
            osszeg=szamitasemelet
#+10% számoló
if alapt < 200:
    print((osszeg/100*10)+(osszeg/100*5)+osszeg,"Ft")
else:
    print((osszeg/100*5)+osszeg,"Ft")