"""

BIBLIOTECA DO BOT IMPERATOR!

lista de todos os comandos:
"""

import os
from random import shuffle, choice

# Lista de interação:

# Lista de comprimentos do usuario/ Bot
user_comp = ["Ola", "ola", "Oi", "oi", "Hey"]
bot_res = ["Olá, como vai? ", "Oi, Tudo bem? ", "Tudo bem? "]

# Resposta do usuario e pergunta;
user_per = ["Estou otimo e voce?", "Estou bem e voce?", "Sim e voce?"]
bot_est = [
        "Sou uma maquina, não sinto dor e nem emoção",
        "Não fui programado para sentir emoções"]

# Estado do usuario e resposta do Bot;
user_est = ["Bem", "Estou bem", "Estou otimo"]
bot_repp = ["Isso e ótimo!", "Que bom!", "Perfeito!"]

# Interação;
inte = ["O que voce pode fazer?"]
botinte = ["No momento posso jogar Jokempô..."]


# Função dedicada a interação do bot com o usuário;
def interacao(entrada):
    if entrada in user_comp:
        return bot_res.pop() #Resposta do bot
        
    elif entrada in user_per:
        return bot_est.pop() #Estado do bot

    elif entrada in user_est:
        return bot_repp.pop() #Resposta do bot
    
    elif entrada in inte:
        return botinte

    elif entrada == "Bye":
        return exit()

    # Jogo de pedra, papel e tesoura usando a função Choice() da 
    # biblioteca Random()
    
    elif entrada == "jokenpo":
        jogadas = ["pedra", "papel", "tesoura"] 
        jogar = input("Faca sua jogada: ")
        return choice(jogadas)

# Função de ações do bot;
def usuario(entrada): # A função recebe a entrada do user e processa;
    # Função 'start' inicia o nosso Bot;
    if entrada == "start":
        mensagem = "Bot startado"
        # Retorna a mensagem ao usuário;
        return mensagem

    elif entrada == "criador":
        # Criador do Bot;
        criador = "\033[1;31mCriador: UserDevz\033[0m"
        return criador

    elif entrada == "github":
        # GitHub do Bot;
        github = "github do bot: \033[1;31mhttps://github.com/UserDevz/imperator-bot\033[0m"
        return github

    elif entrada == "bye":
        # Fecha o Bot;
        print("God Bye")
        return exit()

    elif entrada == "ajuda":
        # Lista todas os comandos do bot;
        ajuda = [
                "start     - Inicia o bot",
                "criador   - Criador do bot",
                "github    - Github do bot",
                "bye       - Encerra o bot",
                "interacao - Ativa o modo interacao do bot",
                "search    - Realiza uma pesquisa no google"
                ]
        return ajuda

    # Chamada para o modo Interação do Bot;
    elif entrada == "interacao":
        print("!Modo interacao ativado!")
        interacao(*args, **kwargs)

    # Pesquisa no google;
    elif entrada == "search":
        from googlesearch import search
        query = input("Palavra chave-> ")
        result = list(
                search(
                    query,
                    lang='pt-br',
                    num_results=1
                    )
                )
        return result

    elif entrada == "imperator":
        os.system("figlet ImperatorBot|lolcat")
        print("""
\033[1;31mChatBot Imperator\033[0m
\033[1;31mCriador: \033[1;36mMaykonDev/UserDevz/Maykon~KKK\033[0m
\033[1;31mVersão: 1.0\033[0m
        """)
        return exit()
