#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


class Navire():
    nom = ""
    composants = {}
    vitalite = 0

    def __init__(self, nom, composants, flotte):
        self.nom = nom
        self.composants = composants
        self.flotte = flotte
        self.vitalite = len(composants)

    def analyser_tir(self, coord_tir):
        """Analyse les conséquences d'un tir sur un navire :
        - teste si le navire est touché par le tir, le signale et le mémorise alors
        - teste si le navire est alors coulé, le signale alors,
          et le supprime de la flotte
        :param navire: pour lequel on regarde si le tir le concerne
        :param coord_tir:
        """
        def navire_est_touche(navire, coord_tir):
            """Indique si un navire est touché par un tir aux coordonnées indiquées."""
            return coord_tir in navire.composants

        def navire_est_coule(navire):
            """Indique si un navire est coulé."""
            return not any(navire.composants)

        if navire_est_touche(self, coord_tir):
            print('Un navire a été touché par votre tir !')
            self.composants[coord_tir] = False
            self.vitalite -= 1
            if navire_est_coule(self):
                print('Le navire touché est coulé !!')
                # le navire est supprimé de la flotte
                if self in super.flotte:
                    super.flotte.remove(self)
