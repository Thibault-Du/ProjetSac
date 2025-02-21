tabId = []
tabProfit = []
tabPoids = []
maxCap = 0


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

lireFichier("data\pi-12-100-1000-001.kna")
print(tabProfit)
print(tabPoids)