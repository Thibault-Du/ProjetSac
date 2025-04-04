import random
from collections import deque
import math

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

nbItem, maxCap = lireFichier("/Users/kawtharalaouimhammedi/Documents/POLYTECH/polytech_S8/Projet_Sac_à_dos/ProjetSac/data/pi-12-100-1000-001.kna")

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

#print(maxCap)
#print(tabuSearch())




def recuitSimule():
    T = 100  # Température initiale
    alpha = 0.99  # Facteur de refroidissement
    Tmin = 0.1  # Température minimale
    iterMax = 1000  # Nombre d'itérations

    x = solutionInitial()  # Solution initiale
    x_best = x.copy()
    f_best = sommeProfit(x)
    
    print("Début du recuit simulé...")
    print(f"Température initiale: {T}")
    
    for iter in range(iterMax):
        if T < Tmin:
            break  # on arrete sii la température est trop basse
        
        voisin = genererVoisin(x)
        deltaE = sommeProfit(voisin) - sommeProfit(x)
        
        if deltaE > 0 or random.random() < math.exp(deltaE / T):
            x = voisin.copy()
            if sommeProfit(x) > f_best:
                x_best = x.copy()
                f_best = sommeProfit(x)
        
        T *= alpha  # Réduction de la température
        
        if iter % 100 == 0:  # pour afficher l'état toutes les 100 itérations
            print(f"Iteration {iter}, Température: {T:.2f}, Profit actuel: {sommeProfit(x)}")
    
    print("Recuit simulé terminé!!!!!!")
    return x_best, f_best

def genererVoisin(solution):
    voisin = solution.copy()
    i = random.randint(0, nbItem - 1)  # pour qu'onn change un élément aléatoirement
    voisin[i] = 1 - voisin[i]  
    return voisin if isAccepted(voisin) else solution  

def solutionInitial():
    return [0] * nbItem  

# test
fichier_test = "/Users/kawtharalaouimhammedi/Documents/POLYTECH/polytech_S8/Projet_Sac_à_dos/ProjetSac/data/pi-12-100-1000-001.kna"
lireFichier(fichier_test)
print(f"Capacité max: {maxCap}")
best_solution, best_profit = recuitSimule()
print(f"Meilleure solution trouvée: {best_solution}")
print(f"Profit maximal obtenu: {best_profit}")

