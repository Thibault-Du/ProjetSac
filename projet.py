tabId = []
tabProfit = []
tabPoids = []


#Remplissage des tableaux qui représente le graphe
def lireFichier(f):
    fichier = open(f, "r")
    fichier.readline()
    fichier.readline()
    fichier.readline()
    nbItem = ((fichier.readline()).split(" "))[1]
    maxCap = ((fichier.readline()).split(" "))[1]
    fichier.readline()
    fichier.readline()
    for i in range(int(nbItem)):
        element = (fichier.readline()).split(" ")
        tabId.append(element[0])
        tabProfit.append(element[1])
        tabPoids.append(element[2].replace("\n", ""))

    fichier.close()
    return int(nbItem), int(maxCap)

nbItem, maxCap = lireFichier("data\pi-12-100-1000-001.kna")

def tabuSearch():
    maxIter = 12
    xmin = solutionInitial()
    x = xmin
    fmin = sommeProfit(xmin)
    i = 0
    tabTabu = []
    for i in range (0,maxIter):
        listVoisin = listerVoisin(tabTabu, x)
        xbis = maximiserProfit(listVoisin) 
        deltaf = sommeProfit(xbis) - sommeProfit(x)
        if deltaf >= 0 :
            if(len(tabTabu)==1):
                tabTabu.clear()
            tabTabu.append(xbis)
        if sommeProfit(xbis) < sommeProfit(xmin):
            xmin = xbis
            fmin = sommeProfit(xbis)
        print(x)
        x = xbis
    return xmin, fmin

def sommeProfit(listItem):
    sum = 0
    i=0
    for i in range(0, nbItem):
        if listItem[i] == 1 :
            sum += int(tabProfit[i])
    return sum

def isAccepted(listItem):
    sum = 0
    i=0
    for i in range(0, nbItem):
        if listItem[i] == 1 :
            sum += int(tabPoids[i])
    return sum < maxCap

def listerVoisin(tabTabu, listItem):
    listVoisin = []
    i=0
    for i in range(0,nbItem):
        voisin = listItem.copy()
        if voisin[i] == 0 :
            voisin[i] = 1
        else :
            voisin[i] = 0
        if not voisin in tabTabu and isAccepted(voisin):
            listVoisin.append(voisin)
    return listVoisin

def maximiserProfit(listVoisin):
    max=0
    betterVoisin = []
    i=0
    for i in range(0, len(listVoisin)):
        if max < sommeProfit(listVoisin[i]) : 
            max = sommeProfit(listVoisin[i])
            betterVoisin = listVoisin[i]
    return betterVoisin

def solutionInitial():
    return [0] * int(nbItem)

print(maxCap)
print(tabuSearch())