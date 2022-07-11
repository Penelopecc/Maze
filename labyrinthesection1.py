#CESSAC Pénélope & LUBINEAU Delphine
#Projet info - Labyrinthe
#CPI1 C2

import random

# Fonction demandant la saisie d’un nombre entier en s’assurant que l’utilisateur entre bien un nombre
# Entrée : phrase d’invite
# Sortie : le nombre saisi
def saisieNombre (invite):
    # Nombre saisi.
    x = None
    while not x:
        try:
            x = int(input(invite))
        except ValueError:
            print('Entrée invalide.')
    return x

# Création du labyrinthe initiale
# Entrées : hauteur et largeur du labyrinthe
# Sortie : tableau de support du labyrinthe
def initMatrice(l,h):
    Matrice=[]
    A=[]
    a=0
    for j in range (0, h):
        for i in range (0, l):
            if (j%2!=0) & (i%2!=0):
                A.append(a)
                a+=1
            else:
                pos = [j, i]
                if not((j == 0) | (j == h-1) | (i == l-1) | (i == 0)):
                    if not((i % 2==0) & (j % 2==0)):
                        Lmur.append (pos)
                A.append (-1)
        Matrice.append (A)
        A=[]
    return Matrice

# Procédure pour mettre la plus petite valeur (p) dans toutes les cases adjacentes de la case XY
# Entrées : Matrice : tableau contenant la matrice, p : plus petite valeur, coordonnées (x,y) du point choisi
def propagervaleur(Matrice, p, x, y):
    if (Matrice[y][x] != -1) & (Matrice[y][x] != p): # Si ce n'est pas un mur ou si ce n'est pas la plus petite valeur
        Matrice[y][x] = p
        propagervaleur(Matrice, p, x+1, y)
        propagervaleur(Matrice, p, x-1, y)
        propagervaleur(Matrice, p, x, y+1)
        propagervaleur(Matrice, p, x, y-1)

# Procédure qui casse les murs valides et propage la plus petite valeur
# Entrées : Matrice : tableau contenant la matrice, coordonnées (x,y) du point choisi
def cassermur(Matrice, x, y):
    p = plusPetite(x, y,Matrice)
    pg = plusGrand(x, y, Matrice)
    if (p < pg):
        Matrice[y][x] = -2
        propagervaleur(Matrice, p, x, y)

# Détermine la plus petite valeur autour d'une certaine case
# Entrées : Matrice : tableau contenant la matrice, coordonnées (x,y) de la case
# Sortie : plus petite valeur
def plusPetite(x,y,Matrice):
    a=99999
    if (Matrice[y][x+1] >= 0):
        a= Matrice[y][x+1]
    if (Matrice[y][x-1] >= 0):
        a = min(a, Matrice[y][x-1])
    if (Matrice[y+1][x] >= 0):
        a = min(a, Matrice[y+1][x])
    if (Matrice[y-1][x] >= 0):
        a = min(a, Matrice[y-1][x])
    return a

# Trouve les coordonnées de la case contenant la plus petite valeur à côté d'une case
# Entrées : Matrice : tableau contenant la matrice; coordonnées (x,y) de la case; t : liste d'entiers
def plusPetite2(x,y,Matrice,t):
    r=0
    s=0
    if (Matrice[y][x+1] > 0):
        s=x+1
        r=y
    if (Matrice[y][x-1] > 0):
        s=x-1
        r=y
    if (Matrice[y+1][x] > 0):
        r=y+1
        s=x
    if (Matrice[y-1][x] > 0):
        r=y-1
        s=x
    t.append(r)
    t.append(s)

# Détermine la plus grande valeur autour d'une certaine case
# Entrées : Matrice : tableau contenant la matrice, coordonnées (x,y) de la case
# Sortie : plus grande valeur
def plusGrand(x,y,Matrice):
    a=-2
    if (Matrice[y][x+1] >= 0):
        a= Matrice[y][x+1]
    if (Matrice[y][x-1] >= 0):
        a = max(a, Matrice[y][x-1])
    if (Matrice[y+1][x] >= 0):
        a = max(a, Matrice[y+1][x])
    if (Matrice[y-1][x] >= 0):
        a = max(a, Matrice[y-1][x])
    return a

# Procédure affichant le labyrinthe
# Entrées : labyrinthe : tableau contenant le labyrinthe
def afficheLabyrinthe (labyrinthe):
    for ligne in labyrinthe:
        for col in ligne:
            if (col == -1):
                print(' *', sep = "", end = "")
            elif (col == 1):
                print(" A", sep = "", end = "")
            elif (col == -2):
                print(" B", sep = "", end = "")
            elif (col == 999):
                print(" .", sep = "", end = "")
            else:
                print("  ", sep = "", end = "")
        print('')

# Numérote la case si elle est égale à 0 ou à un nombre plus grand que la valeur d'entrée afin de trouver le plus court chemin
# Entrées : M : tableau contenant la matrice; x, y : coordonnées d'une case; a, b : coordonnées d'une case adjacente
def autre(M, a, b, x, y):
    if (M[b][a] != -1):
        if (M[b][a]==0):
            M[b][a]=M[y][x]+1
            chemin(M, a, b)
        else:
            if (M[b][a]>M[y][x]+1):
                M[b][a] = M[y][x] + 1
                chemin(M, a, b)

# Numérote les cases dans leur ordre d’adjacence en partant du départ (A) avec comme valeur initiale 1
# Entrées : M : tableau contenant la matrice; x, y : coordonnées d'une case
def chemin(M,x,y):
    autre(M, x, y+1, x, y)
    autre(M, x, y-1, x, y)
    autre(M, x+1, y, x, y)
    autre(M, x-1, y, x, y)



# Etabli le chemin inverse du labyrinthe pour déterminer le chemin le plus court
# Entrées : Matrice : tableau contenant la matrice; x, y : coordonnées d'une case; e : entier de la case suivante
def InverseChemin(Matrice,x, y,e):
    if (Matrice[y][x] != 1 ):
        if (Matrice[y][x] == e ):
            Matrice[y][x] = 999
            InverseChemin(Matrice, x+1, y,e-1)
            InverseChemin(Matrice, x-1, y,e-1)
            InverseChemin(Matrice, x, y+1,e-1)
            InverseChemin(Matrice, x, y-1,e-1)


# --------------- Main ------------------

# Liste des murs potentiellement cassables
Lmur = []

# Demander les dimensions du labyrinthe
print("Entrer la taille de votre labyrinthe : ")
# Nombre de lignes dans le labyrinthe
L = saisieNombre("Largeur : ")
l = L*2+1
# Nombre de colonnes dans le labyrinthe
H = saisieNombre("Hauteur : ")
h = H*2 +1
# Initialise la matrice du labyrinthe
Matrice = initMatrice(l,h)

# Casse des murs valides pour générer un labyrinthe
while(len(Lmur)>0):
    numMur = random.randint(0,len(Lmur)-1)
    x=Lmur[numMur][1]
    y=Lmur[numMur][0]
    del Lmur[numMur]
    cassermur(Matrice, x, y)

# Affiche le labyrinthe initial
print("Voici le labyrinthe aléatoire généré : ")
afficheLabyrinthe(Matrice)

# Vérifie que la case choisie par l'utilisateur est un endroit valide pour y mettre le point de départ du labyrinthe
depok = 0
while (depok==0):
    print("Entrer les coordonnées du point de départ : ")
    A = saisieNombre("X : ")
    B = saisieNombre("Y : ")
    if ((Matrice[B+1][A] != -1) | (Matrice[B-1][A] != -1) | (Matrice[B][A+1] != -1) | (Matrice[B][A-1] != -1)):
        depok = 1
Matrice[B][A]=1

# Vérifie que la case choisie par l'utilisateur est un endroit valide pour y mettre le point d'arrivée du labyrinthe
arok = 0
while (arok==0):
    print("Entrer les coordonnées du point d'arrivée : ")
    X = saisieNombre("X : ")
    Y = saisieNombre("Y : ")
    if ((Matrice[Y+1][X] != -1) | (Matrice[Y-1][X] != -1) | (Matrice[Y][X+1] != -1) | (Matrice[Y][X-1] != -1)):
        arok = 1
Matrice[Y][X]=-2

# Numérote les cases dans leur ordre d’adjacence en partant du départ
chemin(Matrice,A,B)

# Liste contenant les coordonnées de la case de la plus petite valeur
t=[]

# Trouve les coordonnées de la case contenant la plus petite valeur à coté du point d'arrivée et l'associe a e
plusPetite2(X,Y,Matrice,t)
z=t[0]
u=t[1]
e=Matrice[z][u]

# Etabli le chemin inverse du labyrinthe
InverseChemin(Matrice,u,z,e)

# Affiche la solution du labyrinthe
print("Voici le plus court chemin : ")
afficheLabyrinthe(Matrice)
