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
# matplotlib.rcParams["figure.dpi"] = 500

# %% Questions 2/3
print("\n \n Questions 2/3")
# -------------------- Marche aléatoire 3D
print("\n Marche aléatoire 3D \n")


def marche3(n):
    # Initialisation des variables
    posX = 0
    posY = 0
    posZ = 0
    size = 1
    temp = []
    resultX = []
    resultY = []
    resultZ = []
    resultXdr = []
    resultYdr = []
    resultZdr = []
    resultX.append(posX)
    resultY.append(posY)
    resultZ.append(posZ)

    # Pour n pas
    for i in range(1, n+1):
        # On choisit d'avancer dans une direction aléatoire
        rdm = random.uniform(0, 1.5)
        if rdm <= 0.25:
            posX += 1
        elif (rdm <= 0.5) & (rdm > 0.25):
            posX += -1
        elif (rdm <= 0.75) & (rdm > 0.5):
            posY += 1
        elif (rdm <= 1) & (rdm > 0.75):
            posY += -1
        elif (rdm <= 1.25) & (rdm > 1):
            posZ += 1
        else:
            posZ += -1

        resultX.append(posX)
        resultY.append(posY)
        resultZ.append(posZ)

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
                resultZdr.append(resultZ[i])
            temp = []
        if resultY[i] != resultY[i-1]:
            if resultY[i] > resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], 0.01)
            if resultY[i] < resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], -0.01)
            for j in range(0, 99):
                resultXdr.append(resultX[i])
                resultYdr.append(temp[j])
                resultZdr.append(resultZ[i])
            temp = []
        if resultZ[i] != resultZ[i-1]:
            if resultZ[i] > resultZ[i-1]:
                temp = np.arange(resultZ[i-1], resultZ[i], 0.01)
            if resultZ[i] < resultZ[i-1]:
                temp = np.arange(resultZ[i-1], resultZ[i], -0.01)
            for j in range(0, 99):
                resultXdr.append(resultX[i])
                resultYdr.append(resultY[i])
                resultZdr.append(temp[j])
            temp = []

    # On modifie la largeur du trait
    if n > 500:
        size = 0.5
    elif n > 2000:
        size = 0.1
    elif n > 6000:
        size = 0.005

    # Traçé de la courbe (en fait une série de points)
    color = [k for k in range(len(resultXdr))]
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plt.title("Marche aléatoire 3D avec n = " + str(n))
    ax.scatter(resultXdr, resultYdr, resultZdr,
               c=color, cmap='Spectral', s=size)
    plt.grid()
    plt.show()


marche3(4000)


# %% Question 4
print("\n \n Question 4")
# -------------------- Distance moyenne à l'origine
print("\n Distance moyenne à l'origine \n")


def distance(n, nbsample):
    posX = 0
    posY = 0
    posZ = 0
    distance = []

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1.5)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            elif (rdm <= 1) & (rdm > 0.75):
                posY += -1
            elif (rdm <= 1.25) & (rdm > 1):
                posZ += 1
            else:
                posZ += -1

        # On stocke les distances à l'origine dans un tableau dont on pourra ensuite faire la moyenne
        distance.append(math.sqrt(posX * posX + posY * posY + posZ * posZ))
        # On place un point bleu sur chaque fin de parcours (Xn,Yn,Zn)
        plt.plot(posX, posY, posZ, marker="o", markersize=1,
                 markeredgecolor="blue", markerfacecolor="cyan")
        posX = 0
        posY = 0
        posZ = 0

    # On place un point rose à l'origine du repère
    plt.plot(0, 0, 0, marker="o", markersize=5,
             markeredgecolor="red", markerfacecolor="purple")
    plt.title("Marche 3D avec n = " + str(n) +
              " et " + str(nbsample) + " répétitions")
    plt.grid()
    plt.show()
    print("Pour n=", n, " la distance moyenne à l'origine est de ", st.mean(distance))


# distance(n,nbsample) avec n le nombre de pas et nbsample le nombre d'échantillons
# les points bleu représentent tout les points (Xn,Yn,Zn) et le rose l'origine
distance(1000, 10000)


# %% Question 5
print("\n \n Question 5")
# -------------------- Probabilité de retour à (0,0)
print("\n Probabilité de retour à (0,0) \n")


def retour03D(n, nbsample):
    j = 0
    nb0 = 0
    posX = 0
    posY = 0
    posZ = 0
    retour0 = False

    for i in range(0, nbsample):
        # On arrète la boucle dès que le parcours passe par (0,0,0) pour réduire le temps d'éxecution
        while (j != n+1) & (retour0 == False):
            rdm = random.uniform(0, 1.5)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            elif (rdm <= 1) & (rdm > 0.75):
                posY += -1
            elif (rdm <= 1.25) & (rdm > 1):
                posZ += 1
            else:
                posZ += -1
            if (posX == 0) & (posY == 0) & (posZ == 0):
                retour0 = True
                nb0 += 1
            j += 1
        retour0 = False
        posX = 0
        posY = 0
        posZ = 0
        j = 0

    print("On a un nombre de pas ", n)
    print("Nombre de retours à 0 pour ",
          nbsample, " marches aléatoires : ", nb0)
    print("Soit une probabilité de retourner à 0 de : ", round(nb0/nbsample, 3))


retour03D(1000, 10000)


# %% Question 6
print("\n \n Question 6")
# -------------------- Fréquence de passage dans chaque secteur
print("\n Fréquence de passage dans chaque secteur \n")


def secteurs3D(n, nbsample):
    posX = 0
    posY = 0
    posZ = 0
    XposYposZpos = 0
    XposYposZneg = 0
    XposYnegZpos = 0
    XposYnegZneg = 0
    XnegYposZpos = 0
    XnegYposZneg = 0
    XnegYnegZpos = 0
    XnegYnegZneg = 0
    interface = 0

    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1.5)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            elif (rdm <= 1) & (rdm > 0.75):
                posY += -1
            elif (rdm <= 1.25) & (rdm > 1):
                posZ += 1
            else:
                posZ += -1

            # On compare le signe des coordonnées pour déterminer dans quel quadrant se situe le marcheur
            if (posX > 0) & (posY > 0) & (posZ > 0):
                XposYposZpos += 1
            elif (posX > 0) & (posY > 0) & (posZ < 0):
                XposYposZneg += 1
            elif (posX > 0) & (posY < 0) & (posZ > 0):
                XposYnegZpos += 1
            elif (posX > 0) & (posY < 0) & (posZ < 0):
                XposYnegZneg += 1
            elif (posX < 0) & (posY > 0) & (posZ > 0):
                XnegYposZpos += 1
            elif (posX < 0) & (posY > 0) & (posZ < 0):
                XnegYposZneg += 1
            elif (posX < 0) & (posY < 0) & (posZ > 0):
                XnegYnegZpos += 1
            elif (posX < 0) & (posY < 0) & (posZ < 0):
                XnegYnegZneg += 1
            else:
                interface += 1
        posX = 0
        posY = 0
        posZ = 0

    # Nombre total de pas
    totalpas = XposYposZpos + XposYposZneg + \
        XposYnegZpos + XposYnegZneg + XnegYposZpos + \
        XnegYposZneg + XnegYnegZpos + XnegYnegZneg
    print("On a un nombre de pas " + str(n) + " et " +
          str(nbsample) + " marches aléatoires")
    print("Le marcheur fait :")
    print(XposYposZpos, " pas dans le quadrant X positif Y positif Z positif soit ",
          100*XposYposZpos/totalpas, "% des pas")
    print(XposYposZneg, " pas dans le quadrant X positif Y positif Z négatif soit ",
          100*XposYposZneg/totalpas, "% des pas")
    print(XposYnegZpos, " pas dans le quadrant X positif Y négatif Z positif soit ",
          100*XposYnegZpos/totalpas, "% des pas")
    print(XposYnegZneg, " pas dans le quadrant X positif Y négatif Z négatif soit ",
          100*XposYnegZneg/totalpas, "% des pas")
    print(XnegYposZpos, " pas dans le quadrant X négatif Y positif Z positif soit ",
          100*XnegYposZpos/totalpas, "% des pas")
    print(XnegYposZneg, " pas dans le quadrant X négatif Y positif Z négatif soit ",
          100*XnegYposZneg/totalpas, "% des pas")
    print(XnegYnegZpos, " pas dans le quadrant X négatif Y négatif Z positif soit ",
          100*XnegYnegZpos/totalpas, "% des pas")
    print(XnegYnegZneg, " pas dans le quadrant X négatif Y négatif Z négatif soit ",
          100*XnegYnegZneg/totalpas, "% des pas")
    print("On ommet le nombre de pas situés pile entre deux quadrants, ils sont au nombre de ", interface)


secteurs3D(1000, 10000)


# %% Question 7
print("\n \n Question 7")
# -------------------- Fréquence de passage dans deux secteur (espace 3D divisé en deux)
print("\n Fréquence de passage dans deux secteur (espace 3D divisé en deux) \n")


def secteurs3D(n, nbsample):
    posX = 0
    posY = 0
    posZ = 0

    Zpos = 0
    Zneg = 0
    interface = 0

    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1.5)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            elif (rdm <= 1) & (rdm > 0.75):
                posY += -1
            elif (rdm <= 1.25) & (rdm > 1):
                posZ += 1
            else:
                posZ += -1

            # On compare le signe des coordonnées pour déterminer dans quel quadrant se situe le marcheur
            if (posZ > 0):
                Zpos += 1
            elif (posZ < 0):
                Zneg += 1
            else:
                interface += 1

        posX = 0
        posY = 0
        posZ = 0

    # Nombre total de pas
    totalpas = Zpos + Zneg
    print("On a un nombre de pas ", n, " et ", nbsample, " marches aléatoires")
    print("Le marcheur fait :")
    print(Zpos, " pas dans le quadrant Z positif soit ",
          100*Zpos/totalpas, "% des pas")
    print(Zneg, " pas dans le quadrant Z négatif soit ",
          100*Zneg/totalpas, "% des pas")
    print("On ommet le nombre de pas situés pile entre deux quadrants, ils sont au nombre de ", interface)

    # ----------histogramme-------------

    val = []
    val.append(Zpos)
    val.append(Zneg)
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)
    etiquette = ['Z positif', 'Z négatif']
    axs.bar(etiquette, val, color='#fde725')

    plt.xlabel("Secteur")
    plt.ylabel("Nombre de passage")
    plt.title("Histogramme de la fréquence de passage dans les secteurs Z>0 et Z<0, n = "
              + str(n) + " pour " + str(nbsample)+" marches simulées")
    plt.show()


secteurs3D(100, 10000)

# %%
os.system("pause")
