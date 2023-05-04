# %%
import os
from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from collections import Counter

# %% Question 1
print("\n \n Question 1")
# -------------------- Simulation de marche
print("\n Simulation de marche 1D \n")


def marche1(n):
    pos = 0
    x = [k for k in range(n+1)]
    axeabsisse = [0 for k in range(n+1)]
    result = []
    result.append(pos)
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < 0.5:
            pos += 1
        else:
            pos += -1
        result.append(pos)
    plt.title("Simulation marche aléatoire 1D avec n = " + str(n))
    plt.plot(x, result, label="Position à l'instant k")
    plt.plot(x, axeabsisse, label="position x=0")
    plt.legend()
    plt.grid()
    plt.show()


marche1(10)

# %% Question 2
print("\n \n Question 2")
# -------------------- Histogrammes
print("\n Histogrammes \n")


def marche1(n):
    pos = 0
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < 0.5:
            pos += 1
        else:
            pos += -1
    return pos


def histogramme1D(Ntot, n):
    Xn = []
    for i in range(Ntot):
        Xn.append(marche1(n))
    Xn.sort()
    # Permet d'obtenir un tableau à partir d'un autre en comptant les occurences
    Liste = Counter(Xn).most_common()
    # Exemple : tableau 1 : [1,0,0,3] , tableau 2 en sortie : [(0,2),(3,1),(1,1)]
    # On a (0,2) puisque l'on a 2x la valeur 0 dans le tableau 1
    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    x = []
    y = []
    for i in Liste:
        x.append(i[0])
        y.append(i[1])

    N, bins, patches = axs.hist(
        Xn, bins=range(-len(x), len(x)+1), histtype='bar', align='left')
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.xlabel("Position")
    plt.ylabel("Fréquence")
    plt.gca().xaxis.set_ticks(x)
    plt.title("Histogramme des positions finales obtenues pour n = "
              + str(n) + " pour " + str(Ntot)+" marches simulées")

    plt.show()
    proba = y[0]/Ntot
    print("La probabilité de finir à 0 au bout de " +
          str(n) + " pas est de "+str(proba))


Ntot = 10000
n = 1000
histogramme1D(Ntot, n)

# %% Question 3
print("\n \n Question 3")
# -------------------- Probabilité de repasser au moins une fois par 0 au bout de n étape
print("\n Probabilité de repasser au moins une fois par 0 \n")


def marche1_passage_à_0(n):
    pos = 0
    test = False
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < 0.5:
            pos += 1
        else:
            pos += -1
        if pos == 0 and i != 0 and test == False:
            test = True
    return test


def proba_passage_à_0(Ntot, n):
    Xn = []
    for i in range(Ntot):
        Xn.append(marche1_passage_à_0(n))
    Xn.sort()
    nb = 0
    for i in Xn:
        if i == True:
            nb += 1
    proba = nb/Ntot
    print("La probabilité de passer au moins une fois à 0 au bout de " +
          str(n) + " pas est de "+str(proba))


Ntot = 10000
n = 1000
proba_passage_à_0(Ntot, n)


# %% Question 4
print("\n \n Question 4")
# -------------------- temps moyen
print("\n Temps moyen\n")


def marche1_retour_à_0(Ntot, n):
    pos = 0
    temps = 0
    nb = 0
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < 0.5:
            pos += 1
        else:
            pos += -1
        if pos == 0 and nb == 0:
            nb = 1
            temps = i+1
    if nb == 0:
        temps = -3
    return temps


def histogramme1D_retour_à_0(Ntot, n):
    Xn = []
    for i in range(Ntot):
        Xn.append(marche1_retour_à_0(Ntot, n))
    # Permet d'obtenir un tableau à partir d'un autre en comptant les occurences
    Liste = Counter(Xn).most_common()
    # Exemple : tableau 1 : [1,0,0,3] , tableau 2 en sortie : [(0,2),(3,1),(1,1)]
    # On a (0,2) puisque l'on a 2x la valeur 0 dans le tableau 1
    x = []
    for i in Liste:
        x.append(i[0])

    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    N, bins, patches = axs.hist(
        Xn, bins=range(-4, len(x)+1), histtype='bar', align='left')
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    plt.xlabel("Temps moyen")
    plt.ylabel("Fréquence")
    plt.title("Histogramme du temps de passage à 0 pour n = "
              + str(n) + " pour " + str(Ntot)+" marches simulées")
    moyenne = 0
    for i in Liste:
        if i[0] == -3:
            moyenne = (n+2)*i[1] + moyenne
            moyenne = moyenne
        else:
            moyenne = i[0]*i[1]+moyenne
    moyenne = moyenne/Ntot
    print(moyenne)
    plt.show()


Ntot = 1000
n = 10000
histogramme1D_retour_à_0(Ntot, n)

# %% Question 5
print("\n \n Question 5")
# -------------------- autres valeurs de p
print("\n Autres valeurs de p \n")


def marche1(n, p):
    pos = 0
    x = [k for k in range(n+1)]
    axeabsisse = [0 for k in range(n+1)]
    result = []
    result.append(pos)
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < p:
            pos += 1
        else:
            pos += -1
        result.append(pos)
    plt.title("Simulation marche aléatoire 1D avec n = " + str(n))
    plt.plot(x, result, label="Position à l'instant k")
    plt.plot(x, axeabsisse, label="position x=0")
    plt.legend()
    plt.grid()
    plt.show()


def marche1_retour_à_0(n, p):
    pos = 0
    temps = 0
    nb = 0
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < p:
            pos += 1
        else:
            pos += -1
        if pos == 0 and nb == 0:
            nb = 1
            temps = i+1
    if nb == 0:
        temps = -3
    return temps


def histogramme1D_retour_à_0(Ntot, n, p):
    Xn = []
    for i in range(Ntot):
        Xn.append(marche1_retour_à_0(n, p))
    # Permet d'obtenir un tableau à partir d'un autre en comptant les occurences
    Liste = Counter(Xn).most_common()
    # Exemple : tableau 1 : [1,0,0,3] , tableau 2 en sortie : [(0,2),(3,1),(1,1)]
    # On a (0,2) puisque l'on a 2x la valeur 0 dans le tableau 1
    x = []
    for i in Liste:
        x.append(i[0])

    fig, axs = plt.subplots(1, 1,
                            figsize=(10, 7),
                            tight_layout=True)

    N, bins, patches = axs.hist(
        Xn, bins=range(-4, len(x)+1), histtype='bar', align='left')
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    plt.xlabel("Temps moyen")
    plt.ylabel("Fréquence")
    plt.title("Histogramme du temps de passage à 0 pour n = "
              + str(n) + " pour " + str(Ntot)+" marches simulées")
    moyenne = 0
    for i in Liste:
        moyenne = i[0]*i[1] + moyenne
    plt.plot(label="position x=0")
    plt.show()


Ntot = 10000
n = 100
p = 0.4

histogramme1D_retour_à_0(Ntot, n, p)

# %%
os.system("pause")
