from ascii import *
import getpass as gt

def inicio():

    while True:
        print(f"""\
        Você está preste a entrar na DeepWeb...
    
        Nada que você encontrar aqui pode ser compartilhado com NINGUÉM!
    
        Se está ciente disso faça os seguintes passos na ordem correta!
    
        1. Digite ESTOU CIENTE, SEM apertar Enter
        2. Levante sua mão ESQUERDA
        3. Aperte Enter
        """)

        termo = input("Digite aqui: ")

        if termo.lower() == ("estou ciente"):
            ascii_picture()
            print(f"\nSabemos quem você é _{gt.getuser()}_....\n")
            break

        else:
            print("\nDesligue o programa, isso nunca aconteceu... ")
            exit()
            break