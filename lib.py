import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def espera(segundos = 3):
    time.sleep(segundos)

def mensagem(mensagem, segundos = 1):
    limpar_tela()
    print(mensagem)
    espera(segundos)