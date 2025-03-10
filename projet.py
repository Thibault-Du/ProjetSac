from collections import deque

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

nbItem, maxCap = lireFichier("data\pi-15-10000-1000-001.kna")

def tabuSearch():
    maxIter = 101
    xmin = solutionInitial()
    x = xmin.copy()
    fmin = sommeProfit(xmin)
    i = 0
    queueTabu = deque([])
    lenTabu = 4
    for i in range (0,maxIter):
        listVoisin = listerVoisin(queueTabu, x)
        xbis = maximiserProfit(listVoisin)
        deltaf = sommeProfit(xbis) - sommeProfit(x)
        if deltaf >= 0 :
            if(len(queueTabu)==lenTabu):
                queueTabu.popleft()
            queueTabu.append(xbis)
        if sommeProfit(xbis) > sommeProfit(xmin):
            xmin = xbis.copy()
            fmin = sommeProfit(xbis)
        x = xbis.copy()
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
    return (sum <= maxCap)

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
    max=-1
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