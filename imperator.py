from lib_imperator import *

escolha = input("--> ")

if escolha == "start":
    while True:
        entrada = input("-> ")
        print(usuario(entrada))
elif escolha == "interacao":
    while True:
        entrada = input("-> ")
        print(interacao(entrada))
