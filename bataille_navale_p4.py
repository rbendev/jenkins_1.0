#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from flotte import Flotte
from grille import Grille


flotte = Flotte("version_5_nav", 1)
grille = Grille(flotte, flotte.taille_grille)

while(flotte.liste_navires):
    grille.jouer_coup()

print('Bravo, vous avez coulé tous les navires')
