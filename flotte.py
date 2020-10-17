#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
from navire import Navire

class Flotte():
    taille_grille = 9
    nom = "flotte"
    nb_bateaux = 5
    random_positions = []
    position_safe = False
    noms_bateaux = ["porte_avion", "croiseur", "contre torpilleur", "sous-marin", "torpilleur", "cuirassé", "croiseur lourd", "SNLE", "flotille", "frégate"]
    liste_navires = []

    def __init__(self, nom, nombre):
        #Pour créer une flotte avant une grille il faut déterminer le nombre de cases de la grille
        #car les instances de navires sont générées dans la flotte, et leurs positions
        #sont aléatoirement générées dans la grille
        while self.taille_grille > 20 or self.taille_grille < 10:
            self.taille_grille = round(int(input("Saisir la Taille de la grille entre 10 et 20")))
             
        self.nom = nom
        self.nb_bateaux = nombre
        self.init_positions(self.nb_bateaux)
        self.init_navires()

    def init_navires(self):
        for i in range(self.nb_bateaux):
            navire = Navire(self.noms_bateaux[i], self.random_positions[i], self.nom)
            self.liste_navires.append(navire)

    def init_positions(self, nombre):
        #initialisation pour démarrer la boucle de vérification avec
        #deux positions identiques qui permettent de lancer la boucle
        while(not self.position_safe):
            self.random_positions = []
            #Retourne un dictionnaire de bateaux contenant leurs coordonnées et leur état initial
            #Les longueurs de bateaux sont prévues jusqu'à un nombre de 10 bateaux

            longueur_navires = [5, 4, 3, 3, 2, 4, 3, 5, 2, 3]
            sens_navires = []
            position_navire = [0, 0, 0, 0, 0]
            temp = []
            for i in range(nombre):
                sens_navires.append(random.choice([0, 1]))
                ligne_depart = random.randint(1, self.taille_grille)
                colonne_depart = random.randint(1, self.taille_grille)
                coord_depart = ligne_depart, colonne_depart
                depart_navire = (coord_depart)

                navire = {}
                # if sens ==1 => horizontal
                if sens_navires[i] == 1:
                    # if longueur navire non collable à gauche, colle on colle à droite
                    if (depart_navire[1] - (int(longueur_navires[i]))) <= 0 or not (
                            (depart_navire[1] + longueur_navires[i]) > self.taille_grille):
                        for j in range(longueur_navires[i]):
                            coord = (depart_navire[0], depart_navire[1] + j)
                            navire[coord] = True
                    # sinon colle à gauche
                    else:
                        for j in range(longueur_navires[i]):
                            coord = (depart_navire[0], depart_navire[1] - j)
                            navire[coord] = True

                    self.random_positions.append(navire)

                if sens_navires[i] == 0:
                    # if longueur navire collable en bas colle en bas
                    if (depart_navire[0] - (int(longueur_navires[i]))) <= 0 or not (depart_navire[0] + longueur_navires[i]) > self.taille_grille:
                        for j in range(longueur_navires[i]):
                            coord = (depart_navire[0] + j, depart_navire[1])
                            navire[coord] = True
                    # sinon colle en hauteur
                    else:
                        for j in range(longueur_navires[i]):
                            coord = (depart_navire[0] - j, depart_navire[1])
                            navire[coord] = True


                    self.random_positions.append(navire)
                print(navire)
            self.test_positions()

    def test_positions(self):
        liste_coord = []
        somme_len_dict = 0

        for navire in self.random_positions :
            for coord in navire.keys():
                liste_coord.append(coord)
                somme_len_dict += 1
        print(liste_coord)
        print(len(set(liste_coord)))
        print(somme_len_dict)
        #on supprime les clés en doublon dans la liste des coordonnées grâce à un set
        #si la longueur du set est la meme que celle de la liste alors il n'y a pas de doublons
        if len(set(liste_coord)) == somme_len_dict:
            self.position_safe = True
        else :
            self.position_safe = False
            print("Changement de la position des bateaux")
