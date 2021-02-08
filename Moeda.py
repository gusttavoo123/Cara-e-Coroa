# Projeto 1

from random import random

def moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(moeda())