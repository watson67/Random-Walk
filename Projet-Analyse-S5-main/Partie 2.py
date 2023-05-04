# %%
import os
from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import random
import statistics as st
from collections import Counter
# matplotlib.rcParams["figure.dpi"] = 50

# %% Questions 2/3
print("\n \n Questions 2/3")
# -------------------- Marche aléatoire 2D
print("\n Marche aléatoire 2D \n")


def marche2(n):
    # Initialisation des variables
    posX = 0
    posY = 0
    size = 2
    temp = []
    resultX = []
    resultY = []
    resultXdr = []
    resultYdr = []
    resultX.append(posX)
    resultY.append(posY)

    # Pour n pas
    for i in range(1, n+1):
        # On choisit d'avancer dans une direction aléatoire
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            posX += 1
        elif (rdm <= 0.5) & (rdm > 0.25):
            posX += -1
        elif (rdm <= 0.75) & (rdm > 0.5):
            posY += 1
        else:
            posY += -1

        resultX.append(posX)
        resultY.append(posY)

        # Afin d'avoir un gradient pour mieux visualiser le sens de progression
        # on crée 100 points entre chaques pas, ces points seront colorés via une colorscale
        if resultX[i] != resultX[i-1]:
            if resultX[i] > resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], 0.01)
            if resultX[i] < resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], -0.01)
            for j in range(0, 99):
                resultXdr.append(temp[j])
                resultYdr.append(resultY[i])
            temp = []
        if resultY[i] != resultY[i-1]:
            if resultY[i] > resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], 0.01)
            if resultY[i] < resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], -0.01)
            for j in range(0, 99):
                resultYdr.append(temp[j])
                resultXdr.append(resultX[i])
            temp = []

    # On modifie la largeur du trait
    if n > 500:
        size = 1
    elif n > 2000:
        size = 0.5
    elif n > 6000:
        size = 0.01

    # Traçé de la courbe (en fait une série de points)
    color = [k for k in range(len(resultXdr))]
    plt.title("Marche aléatoire 2D avec n = " + str(n))
    plt.scatter(resultXdr, resultYdr, c=color, cmap='Spectral', s=size)
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.grid()
    plt.show()


marche2(3000)


# -------------------- Marche aléatoire 2D sans retour en arrière
print("\n Marche aléatoire 2D sans retour en arrière \n")


def marche2SR(n):
    posX = 0
    posY = 0
    size = 2
    done = False
    addX = False
    subX = False
    addY = False
    subY = False
    temp = []
    resultX = []
    resultY = []
    resultXdr = []
    resultYdr = []
    resultX.append(posX)
    resultY.append(posY)

    # Pour le premier pas toutes les directions sont autorisées
    rdm = random.uniform(0, 1)
    if rdm <= 0.25:
        addX = True
    elif (rdm <= 0.5) & (rdm > 0.25):
        subX = True
    elif (rdm <= 0.75) & (rdm > 0.5):
        addY = True
    else:
        subY = True

    # Il faut ensutie choisir avec une meme probabilité une direction
    # qu'y ne fait pas retourner en arrière
    for i in range(1, n+1):
        rdm = random.uniform(0, 1)
        if (addX == True) & (done == False):
            if rdm <= 1/3:
                posX += 1
                addX = False
                addX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posY += 1
                addX = False
                addY = True
            else:
                posY += -1
                addX = False
                subY = True
            done = True
        if (subX == True) & (done == False):
            if rdm <= 1/3:
                posX += -1
                subX = False
                subX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posY += 1
                subX = False
                addY = True
            else:
                posY += -1
                subX = False
                subY = True
            done = True
        if (addY == True) & (done == False):
            if rdm <= 1/3:
                posX += 1
                addY = False
                addX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posY += 1
                addY = False
                addY = True
            else:
                posX += -1
                addY = False
                subX = True
            done = True
        if (subY == True) & (done == False):
            if rdm <= 1/3:
                posX += 1
                subY = False
                addX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posX += -1
                subY = False
                subX = True
            else:
                posY += -1
                subY = False
                subY = True
            done = True
        done = False

        resultX.append(posX)
        resultY.append(posY)

        if resultX[i] != resultX[i-1]:
            if resultX[i] > resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], 0.01)
            if resultX[i] < resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], -0.01)
            for j in range(0, 99):
                resultXdr.append(temp[j])
                resultYdr.append(resultY[i])
            temp = []
        if resultY[i] != resultY[i-1]:
            if resultY[i] > resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], 0.01)
            if resultY[i] < resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], -0.01)
            for j in range(0, 99):
                resultYdr.append(temp[j])
                resultXdr.append(resultX[i])
            temp = []

    if n > 500:
        size = 1
    elif n > 2000:
        size = 0.5
    elif n > 6000:
        size = 0.01

    color = [k for k in range(len(resultXdr))]
    plt.title("Marche aléatoire 2D sans retour avec n = " + str(n))
    plt.scatter(resultXdr, resultYdr, c=color, cmap='Spectral', s=size)
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.grid()
    plt.show()


marche2SR(3000)


# %% Question 4
print("\n \n Question 4")
# -------------------- Distance moyenne à l'origine
print("\n Distance moyenne à l'origine \n")


def distance(n, nbsample):
    posX = 0
    posY = 0
    distance = []

    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            else:
                posY += -1

        # On stocke les distances à l'origine dans un tableau dont on pourra ensuite faire la moyenne
        distance.append(math.sqrt(posX * posX + posY * posY))
        # On place un point bleu sur chaque fin de parcours (Xn,Yn)
        plt.plot(posX, posY, marker="o", markersize=10,
                 markeredgecolor="blue", markerfacecolor="cyan")
        posX = 0
        posY = 0

    # On place un point rose à l'origine du repère
    plt.plot(0, 0, marker="o", markersize=10,
             markeredgecolor="red", markerfacecolor="purple")
    plt.title("Marche 2D avec n = " + str(n) +
              " et " + str(nbsample) + " répétitions")
    plt.grid()
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.show()
    print("Pour n=", n, " la distance moyenne à l'origine est de ", st.mean(distance))

    distance.sort()
    for i in range(len(distance)):
        distance[i] = round(distance[i])

    Liste = Counter(distance).most_common()
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    x = []
    for i in Liste:
        x.append(i[0])

    x.sort()
    N, bins, patches = axs.hist(distance, bins=range(
        len(x)), histtype='bar', align='left')
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.xlabel("distance")
    plt.ylabel("Fréquence")
    plt.title("Histogramme des distances obtenues pour n = "
              + str(n))
    plt.show()


# distance(n,nbsample) avec n le nombre de pas et nbsample le nombre d'échantillons
# les points bleu représentent tout les points (Xn,Yn) et le rose l'origine
distance(1000, 10000)


# -------------------- Distance moyenne à l'origine sans retour en arrière
print("\n Distance moyenne à l'origine sans retour en arrière \n")


def distanceSR(n, nbsample):
    posX = 0
    posY = 0
    done = False
    addX = False
    subX = False
    addY = False
    subY = False
    distance = []

    for i in range(0, nbsample):
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            addX = True
        elif (rdm <= 0.5) & (rdm > 0.25):
            subX = True
        elif (rdm <= 0.75) & (rdm > 0.5):
            addY = True
        else:
            subY = True

        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if (addX == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addX = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addX = False
                    addY = True
                else:
                    posY += -1
                    addX = False
                    subY = True
                done = True
            if (subX == True) & (done == False):
                if rdm <= 1/3:
                    posX += -1
                    subX = False
                    subX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    subX = False
                    addY = True
                else:
                    posY += -1
                    subX = False
                    subY = True
                done = True
            if (addY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addY = False
                    addY = True
                else:
                    posX += -1
                    addY = False
                    subX = True
                done = True
            if (subY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    subY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posX += -1
                    subY = False
                    subX = True
                else:
                    posY += -1
                    subY = False
                    subY = True
                done = True
            done = False
        distance.append(math.sqrt(posX * posX + posY * posY))
        plt.plot(posX, posY, marker="o", markersize=10,
                 markeredgecolor="blue", markerfacecolor="cyan")
        posX = 0
        posY = 0

    plt.plot(0, 0, marker="o", markersize=10,
             markeredgecolor="red", markerfacecolor="purple")
    plt.title("Marche 2D sans retour avec n = " + str(n) +
              " et " + str(nbsample) + " répétitions")
    plt.grid()
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.show()
    print("Pour n=", n, " la distance moyenne à l'origine est de ", st.mean(distance))

    distance.sort()
    for i in range(len(distance)):
        distance[i] = round(distance[i])

    Liste = Counter(distance).most_common()
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)
    x = []
    for i in Liste:
        x.append(i[0])
    x.sort()
    N, bins, patches = axs.hist(distance, bins=range(
        len(x)), histtype='bar', align='left')
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    plt.xlabel("Distance")
    plt.ylabel("Fréquence")
    plt.title("Histogramme des distances obtenues pour n = "
              + str(n))
    plt.show()


distanceSR(1000, 10000)
# %% Question 5
print("\n \n Question 5")
# -------------------- Probabilité de retour à (0,0)
print("\n Probabilité de retour à (0,0) \n")

n = 10000
Ntot = 1000


def retour02D(n, nbsample):
    j = 0
    nb0 = 0
    posX = 0
    posY = 0
    retour0 = False

    for i in range(0, nbsample):
        # On arrète la boucle dès que le parcours passe par (0,0) pour réduire le temps d'éxecution
        while (j != n+1) & (retour0 == False):
            rdm = random.uniform(0, 1)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            else:
                posY += -1
            if (posX == 0) & (posY == 0):
                retour0 = True
                nb0 += 1
            j += 1
        retour0 = False
        posX = 0
        posY = 0
        j = 0

    print("On a un nombre de pas ", n)
    print("Nombre de retours à 0 pour ",
          nbsample, " marches aléatoires : ", nb0)
    print("Soit une probabilité de retourner à 0 de : ", round(nb0/nbsample, 3))


retour02D(n, Ntot)


# -------------------- Probabilité de retour à (0,0) sans retour en arrière
print("\n Probabilité de retour à (0,0) sans retour en arrière \n")


def retour02DSR(n, nbsample):
    j = 0
    nb0 = 0
    posX = 0
    posY = 0
    done = False
    addX = False
    subX = False
    addY = False
    subY = False
    retour0 = False

    for i in range(0, nbsample):
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            addX = True
        elif (rdm <= 0.5) & (rdm > 0.25):
            subX = True
        elif (rdm <= 0.75) & (rdm > 0.5):
            addY = True
        else:
            subY = True

        while (j != n+1) & (retour0 == False):
            rdm = random.uniform(0, 1)
            if (addX == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addX = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addX = False
                    addY = True
                else:
                    posY += -1
                    addX = False
                    subY = True
                done = True
            if (subX == True) & (done == False):
                if rdm <= 1/3:
                    posX += -1
                    subX = False
                    subX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    subX = False
                    addY = True
                else:
                    posY += -1
                    subX = False
                    subY = True
                done = True
            if (addY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addY = False
                    addY = True
                else:
                    posX += -1
                    addY = False
                    subX = True
                done = True
            if (subY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    subY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posX += -1
                    subY = False
                    subX = True
                else:
                    posY += -1
                    subY = False
                    subY = True
                done = True
            done = False
            if (posX == 0) & (posY == 0):
                retour0 = True
                nb0 += 1
            j += 1
        retour0 = False
        posX = 0
        posY = 0
        j = 0

    print("On a un nombre de pas ", n)
    print("Nombre de retours à 0 pour ",
          nbsample, " marches aléatoires : ", nb0)
    print("Soit une probabilité de retourner à 0 de : ",
          round(nb0/nbsample, 3))


retour02DSR(n, Ntot)


# %% Question 6
print("\n \n Question 6")
# -------------------- Fréquence de passage dans chaque secteur
print("\n Fréquence de passage dans chaque secteur \n")


def secteurs2D(n, nbsample):
    posX = 0
    posY = 0
    xposypos = 0
    xnegypos = 0
    xnegyneg = 0
    xposyneg = 0
    interface = 0

    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            else:
                posY += -1

            # On compare le signe des coordonnées pour déterminer dans quel quadrant se situe le marcheur
            if (posX > 0) & (posY > 0):
                xposypos += 1
            elif (posX < 0) & (posY > 0):
                xnegypos += 1
            elif (posX < 0) & (posY < 0):
                xnegyneg += 1
            elif (posX > 0) & (posY < 0):
                xposyneg += 1
            else:
                interface += 1
        posX = 0
        posY = 0

    # Nombre total de pas
    totalpas = xposypos + xnegypos + xnegyneg + xposyneg
    print("On a un nombre de pas ", n, " et ", nbsample, " marches aléatoires")
    print("Le marcheur fait :")
    print(xposypos, " pas dans le quadrant X positif Y positif soit ",
          100*xposypos/totalpas, "% des pas")
    print(xnegypos, " pas dans le quadrant X négatif Y positif soit ",
          100*xnegypos/totalpas, "% des pas")
    print(xnegyneg, " pas dans le quadrant X négatif Y négatif soit ",
          100*xnegyneg/totalpas, "% des pas")
    print(xposyneg, " pas dans le quadrant X positif Y négatif soit ",
          100*xposyneg/totalpas, "% des pas")
    print("On ommet le nombre de pas situés pile entre deux quadrants, ils sont au nombre de ", interface)


n = 1000
Ntot = 1000
secteurs2D(n, Ntot)


# -------------------- Fréquence de passage dans chaque secteur sans retour en arrière
print("\n Fréquence de passage dans chaque secteur sans retour en arrière \n")


def secteurs2DSR(n, nbsample):
    posX = 0
    posY = 0
    done = False
    addX = False
    subX = False
    addY = False
    subY = False
    xposypos = 0
    xnegypos = 0
    xnegyneg = 0
    xposyneg = 0
    interface = 0

    for i in range(0, nbsample):
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            addX = True
        elif (rdm <= 0.5) & (rdm > 0.25):
            subX = True
        elif (rdm <= 0.75) & (rdm > 0.5):
            addY = True
        else:
            subY = True

        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if (addX == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addX = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addX = False
                    addY = True
                else:
                    posY += -1
                    addX = False
                    subY = True
                done = True
            if (subX == True) & (done == False):
                if rdm <= 1/3:
                    posX += -1
                    subX = False
                    subX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    subX = False
                    addY = True
                else:
                    posY += -1
                    subX = False
                    subY = True
                done = True
            if (addY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addY = False
                    addY = True
                else:
                    posX += -1
                    addY = False
                    subX = True
                done = True
            if (subY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    subY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posX += -1
                    subY = False
                    subX = True
                else:
                    posY += -1
                    subY = False
                    subY = True
                done = True
            done = False

            if (posX > 0) & (posY > 0):
                xposypos += 1
            elif (posX < 0) & (posY > 0):
                xnegypos += 1
            elif (posX < 0) & (posY < 0):
                xnegyneg += 1
            elif (posX > 0) & (posY < 0):
                xposyneg += 1
            else:
                interface += 1
        posX = 0
        posY = 0

    totalpas = xposypos + xnegypos + xnegyneg + xposyneg
    print("On a un nombre de pas ", n, " et ", nbsample, " marches aléatoires")
    print("Le marcheur fait :")
    print(xposypos, " pas dans le quadrant X positif Y positif soit ",
          100*xposypos/totalpas, "% des pas")
    print(xnegypos, " pas dans le quadrant X négatif Y positif soit ",
          100*xnegypos/totalpas, "% des pas")
    print(xnegyneg, " pas dans le quadrant X négatif Y négatif soit ",
          100*xnegyneg/totalpas, "% des pas")
    print(xposyneg, " pas dans le quadrant X positif Y négatif soit ",
          100*xposyneg/totalpas, "% des pas")
    print("On ommet le nombre de pas situés pile entre deux quadrants, ils sont au nombre de ", interface)


secteurs2DSR(n, Ntot)


# %% Question 7
print("\n \n Question 7")
# -------------------- Définition des secteurs
print("\n Définition des secteurs \n")

n = 100
Ntot = 10000
# Array réunissant les angles des demi droites partant de l'origine
angles = []


# Fonction qui permet à l'utilisateur de choisir n demi droites via des points
def demidroites():
    print("Vous allez définir les droites délimitant les secteurs")
    print("et pour cela entrer dans l'ordre des coordonnées x et y.")
    print("Si un (0,0) est entré cela mettra fin à la détermination des coordonnées")

    x = 1
    y = 1
    first = True

    while (x+y != 0.0):
        if first != True:
            print("Votre point : (", x, ",", y, ")")
        first = False
        x = float(input("Entrez X : "))
        y = float(input("Entrez Y : "))

        if (x+y != 0.0):
            if (x >= 0.0) & (y >= 0.0):
                if x != 0.0:
                    angles.append(math.degrees(math.atan(y/x)))
                else:
                    angles.append(90)
            elif (x <= 0.0) & (y >= 0.0):
                if y != 0.0:
                    angles.append(-1*math.degrees(math.atan(x/y))+90)
                else:
                    angles.append(180)

            elif (x <= 0.0) & (y <= 0.0):
                if x != 0.0:
                    angles.append(math.degrees(math.atan(y/x))+180)
                else:
                    angles.append(270)
            else:
                if y != 0.0:
                    angles.append(-1*math.degrees(math.atan(x/y))+270)
                else:
                    angles.append(0)
    print("Fin du choix des points.")
    angles.sort()


print("Voulez vous choisir vos droites (1) ou utiliser des valeurs préremplies (2) ?")
choix = input("1/2 : ")
choisi = False
while choisi == False:
    if choix == "1":
        # Choix des demi droites
        demidroites()
        choisi = True
    elif choix == "2":
        # Exemples préremplis (on devrait avoir 25%, 25%, 25%, 12.5%, 12.5%)
        angles = [45, 90, 180, 270, 315]
        choisi = True
    else:
        print(
            "Voulez vous choisir vos droites (1) ou utiliser des valeurs préremplies (2) ?")
        choix = input("1/2 : ")


# -------------------- Fréquence de passage dans chaque secteur
print("\n Fréquence de passage dans chaque secteur \n")


def secteursCustom2D(n, nbsample):
    k = 0
    posX = 0
    posY = 0
    anglePas = 0
    done = False
    repartitionPas = np.zeros(len(angles))
    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            else:
                posY += -1

            # On calcule l'angle du nouveau point par rapport à l'origine
            if (posX+posY != 0.0):
                if (posX >= 0.0) & (posY >= 0.0):
                    if posX != 0.0:
                        anglePas = math.degrees(math.atan(posY/posX))
                    else:
                        anglePas = 90
                elif (posX <= 0.0) & (posY >= 0.0):
                    if posY != 0.0:
                        anglePas = -1*math.degrees(math.atan(posX/posY))+90
                    else:
                        anglePas = 180

                elif (posX <= 0.0) & (posY <= 0.0):
                    if posX != 0.0:
                        anglePas = math.degrees(math.atan(posY/posX))+180
                    else:
                        anglePas = 270
                else:
                    if posY != 0.0:
                        anglePas = -1 * \
                            math.degrees(math.atan(posX/posY))+270
                    else:
                        anglePas = 0

            # On compare l'angle pour déterminer dans quel quadrant se situe le marcheur
            while (k <= len(angles)) & (done == False):
                if (k == len(angles)) & (anglePas >= angles[k-1]):
                    repartitionPas[0] += 1
                    done = True
                elif k != len(angles):
                    if (k == 0) & (anglePas <= angles[k]):
                        repartitionPas[0] += 1
                        done = True
                    elif (angles[k-1] < anglePas <= angles[k]) & (k != 0):
                        repartitionPas[k] += 1
                        done = True

                k += 1
            k = 0
            done = False
        posX = 0
        posY = 0

    totalPas = 0
    for i in range(len(repartitionPas)):
        totalPas += repartitionPas[i]
    print("Fréquences de passage : ")
    for i in range(len(repartitionPas)):
        print("Secteur ", i+1, " a une fréquence de passage de : ",
              100*repartitionPas[i]/totalPas)
    print("Pas totaux : ", totalPas)
    # ----------histogramme-------------

    c = 1
    freq = []
    for i in repartitionPas:
        for j in range(int(i)):
            freq.append(c)
        c += 1
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    N, bins, patches = axs.hist(freq, bins=range(
        0, len(repartitionPas)+2), align='left', rwidth=0.6)
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.xlabel("Secteur")
    plt.ylabel("Nombre de passage")
    plt.title("Histogramme de la fréquence de passage dans les secteurs n = "
              + str(n) + " pour " + str(Ntot)+" marches simulées")
    plt.show()


secteursCustom2D(n, Ntot)


# -------------------- Fréquence de passage dans chaque secteur sans retour
print("\n Fréquence de passage dans chaque secteur sans retour \n")


def secteursCustom2DSR(n, nbsample):
    k = 0
    posX = 0
    posY = 0
    anglePas = 0
    addX = False
    subX = False
    addY = False
    subY = False
    done = False
    done2 = False
    repartitionPas = np.zeros(len(angles))
    for i in range(0, nbsample):
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            addX = True
        elif (rdm <= 0.5) & (rdm > 0.25):
            subX = True
        elif (rdm <= 0.75) & (rdm > 0.5):
            addY = True
        else:
            subY = True

        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if (addX == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addX = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addX = False
                    addY = True
                else:
                    posY += -1
                    addX = False
                    subY = True
                done = True
            if (subX == True) & (done == False):
                if rdm <= 1/3:
                    posX += -1
                    subX = False
                    subX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    subX = False
                    addY = True
                else:
                    posY += -1
                    subX = False
                    subY = True
                done = True
            if (addY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addY = False
                    addY = True
                else:
                    posX += -1
                    addY = False
                    subX = True
                done = True
            if (subY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    subY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posX += -1
                    subY = False
                    subX = True
                else:
                    posY += -1
                    subY = False
                    subY = True
                done = True
            done = False
            # On calcule l'angle du nouveau point
            if (posX+posY != 0.0):
                if (posX >= 0.0) & (posY >= 0.0):
                    if posX != 0.0:
                        anglePas = math.degrees(math.atan(posY/posX))
                    else:
                        anglePas = 90
                elif (posX <= 0.0) & (posY >= 0.0):
                    if posY != 0.0:
                        anglePas = -1*math.degrees(math.atan(posX/posY))+90
                    else:
                        anglePas = 180

                elif (posX <= 0.0) & (posY <= 0.0):
                    if posX != 0.0:
                        anglePas = math.degrees(math.atan(posY/posX))+180
                    else:
                        anglePas = 270
                else:
                    if posY != 0.0:
                        anglePas = -1 * \
                            math.degrees(math.atan(posX/posY))+270
                    else:
                        anglePas = 0
            # On compare l'angle pour déterminer dans quel quadrant se situe le marcheur
            while (k <= len(angles)) & (done2 == False):
                if (k == len(angles)) & (anglePas >= angles[k-1]):
                    repartitionPas[0] += 1
                    done2 = True
                elif k != len(angles):
                    if (k == 0) & (anglePas <= angles[k]):
                        repartitionPas[0] += 1
                        done2 = True
                    elif (angles[k-1] < anglePas <= angles[k]) & (k != 0):
                        repartitionPas[k] += 1
                        done2 = True

                k += 1
            k = 0
            done2 = False
        posX = 0
        posY = 0

    totalPas = 0
    for i in range(len(repartitionPas)):
        totalPas += repartitionPas[i]
    print("Fréquences de passage : ")
    for i in range(len(repartitionPas)):
        print("Secteur ", i+1, " a une fréquence de passage de : ",
              100*repartitionPas[i]/totalPas)
    print("Pas totaux : ", totalPas)

    # ----------histogramme-------------

    c = 1
    freq = []
    for i in repartitionPas:
        for j in range(int(i)):
            freq.append(c)
        c += 1
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    N, bins, patches = axs.hist(freq, bins=range(
        0, len(repartitionPas)+2), align='left', rwidth=0.6)
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.xlabel("Secteur")
    plt.ylabel("Nombre de passage")
    plt.title("Histogramme de la fréquence de passage dans les secteurs n = "
              + str(n) + " pour " + str(Ntot)+" marches simulées")
    plt.show()


secteursCustom2DSR(n, Ntot)

# %%
os.system("pause")
