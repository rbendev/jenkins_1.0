#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from typing import Any, Union, Tuple

from navire import Navire

class Grille():
    TAILLE_GRILLE = 9
    # détermination de la liste des lettres utilisées pour identifier les colonnes :
    LETTRES = [chr(code_lettre) for code_lettre in range(ord('A'), ord('A') + TAILLE_GRILLE)]
    # différents états possibles pour une case de la grille de jeu
    MER, TIR_RATE, TIR_TOUCHE, TIR_COULE = 0, 1, 2, 3
    # représentation du contenu de ces différents états possible pour une case
    # (tableau indexé par chacun de ces états)
    REPR_ETAT_CASE = [' ', 'X', '#', '-']
    coups_joues = set()
    
    def __init__(self, flotte, taille_grille):
        self.TAILLE_GRILLE = taille_grille
        self.flotte = flotte
        self.init_grille()
        self.coups_joues = set()
        self.set_up_lettres()
    
    def set_up_lettres(self):
        self.LETTRES = [chr(code_lettre) for code_lettre in range(ord('A'), ord('A') + self.TAILLE_GRILLE)]
         
    def init_grille(self):
        """Construction de la grille de jeu contenant toutes les cases de bateau.
    
        :return: la grille construire est un dictionnaire dont chaque clé est les coordonnées
                 d'une case d'un navire, et sa valeur le navire en question
        """
        #print({ coord_navire: navire.composants for navire in self.flotte.liste_navires for coord_navire in navire.composants })

        self.grille = { coord_navire: navire.composants for navire in self.flotte.liste_navires for coord_navire in navire.composants }

    def demande_coord(self):
        coord_valides = False
    
        # ex. d'entrée attendue : 'A1'
        coord_joueur = input("Entrez les coordonnées de votre tir (ex. : 'A1', 'H8') : ")
    
        if 2 <= len(coord_joueur) <= 3:
            lettre, chiffre = coord_joueur[0], coord_joueur[1:]
            lettre = lettre.upper()
            try:
                # détermination de no_lig et no_col (comptés à partir de 1)
                no_lig = int(chiffre)
                no_col = ord(lettre) - ord('A') + 1
                if 1 <= no_lig <= self.TAILLE_GRILLE and lettre in self.LETTRES:
                    coord_valides = True
                    coord_tir = (no_lig, no_col)
            except ValueError:
                pass
    
        if not coord_valides:
            coord_tir = self.demande_coord()
    
        return coord_tir
    
    def etat_case_grille(self, coord):
        """Retourne l'état de la case coord de la grille
           (cf. constantes MER, TIR_RATE, TIR_TOUCHE, TIR_COULE)."""

        if coord in self.coups_joues:
            navire_case = self.grille.get(coord)
            if navire_case:
                for navire in self.flotte.liste_navires:
                    presence = any([True for key,value in navire.composants for k,v in navire_case if key == k])
                    if presence and navire.vitalite <= 0:
                        return self.TIR_COULE
                    else :
                        return self.TIR_TOUCHE
            else:
                return self.TIR_RATE
        else:
            return self.MER

    
    def affiche_grille(self):
        """Affichage de la grille de jeu."""
    
        print('    ', end = '')
        for x in range(self.TAILLE_GRILLE):
            lettre = self.LETTRES[x]
            print(' {}  '.format(lettre), end = '')
        print()
        print('  ', '+---' * self.TAILLE_GRILLE + '+')
        for no_lig in range(1, self.TAILLE_GRILLE + 1):
            print('{:>2} |'.format(no_lig), end = '')
            for no_col in range(1, self.TAILLE_GRILLE + 1):
                coord = (no_lig, no_col)
                etat_case = self.etat_case_grille(coord)
                etat_str = self.REPR_ETAT_CASE[etat_case]
                print(' {} |'.format(etat_str), end = '')
            print()
            print('  ', '+---' * self.TAILLE_GRILLE + '+')
    
    def jouer_coup(self):
        coord: Union[Tuple[int, int], Any] = self.demande_coord()
        print(coord)
        for navire in self.flotte.liste_navires:
            navire.analyser_tir(coord)
        self.coups_joues.add(coord)
        self.init_grille()
        self.affiche_grille()
