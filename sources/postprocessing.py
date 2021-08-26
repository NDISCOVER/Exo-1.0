#!/usr/bin/env python3
"""Fix the font names for the variable fonts"""
# TODO (M Foley) this shouldn't be required. Send fix to fontmake
from fontTools.ttLib import TTFont
from glob import glob
import os

font_paths = glob("fonts/variable/*.ttf")

for path in font_paths:
    font = TTFont(path)
    font["name"].setName("Exo", 1, 3, 1, 1033)
    if "Italic" in str(path):
        font["name"].setName("TINY;Exo-Italic", 3, 3, 1, 1033)
        font["name"].setName("Exo Italic", 4, 3, 1, 1033)
        font["name"].setName("Exo-Italic", 6, 3, 1, 1033)
    else:
        font["name"].setName("TINY;Exo-Regular", 3, 3, 1, 1033)
        font["name"].setName("Exo Regular", 4, 3, 1, 1033)
        font["name"].setName("Exo-Regular", 6, 3, 1, 1033)

    font.save(path + ".fix")
