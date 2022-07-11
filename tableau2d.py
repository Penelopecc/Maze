#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Fonction demandant la saisie d’un nombre entier en s’assurant que
# l’utilisateur entre bien un nombre.
# Entrée : phrase d’invite.
# Retourne : le nombre saisi.
def saisieNombre (invite):
    # Nombre saisi.
    x = None
    while not x:
        try:
            x = int(input(invite))
        except ValueError:
            print('Entrée invalide.')
    return x

###
# Fonction créant le tableau de départ pour représenter un labyrinthe.
# Entrées : n : nombre de lignes.
#           m : nombre de colonnes.
# Sortie : un tableau pour représenter le labyrinthe.
def creerLabyrinthe (n, m):
    # Tableau contenant un labyrinthe.
    labyrinthe = [[-1] * m for _ in range(n)]

    # Compteur du nombre de cases.
    compteur = 0
    for i in range(1, n - 1, 2):
        for j in range(1, m - 1, 2):
            labyrinthe[i][j] = compteur
            compteur += 1

    return labyrinthe

###
# Procédure affichant le labyrinthe.
# Entrées : labyrinthe : tableau contenant le labyrinthe.
def afficheLabyrinthe (labyrinthe):
    for ligne in labyrinthe:
        for col in ligne:
            if col == -1:
                print(' * ', sep = "", end = "")
            else:
                print('{:03d}'.format(col), sep = "", end = "")
        print('')
    
# Nombre de lignes dans le labyrinthe.
n = saisieNombre('Nombre de lignes : ')
n = n * 2 + 1
# Nombre de colonnes dans le labyrinthe.
m = saisieNombre('Nombre de colonnes : ')
m = m * 2 + 1

# Tableau représentant le labyrinthe.
labyrinthe = creerLabyrinthe(n, m)

afficheLabyrinthe(labyrinthe)
