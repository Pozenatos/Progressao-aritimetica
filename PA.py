import os
import time

os.system('cls')

print('Seja bem vindo ao meu programa de Progressão aritimética!')
print('Você ira definir qual é o Primeiro termo e a razão, com esses dados este programa irá contruir uma PA que vai até o décimo termo (por favor apenas números inteiros)\n')
input('Pressione ENTER para continuar...')

c = int
termo = int(0)
loop = True

while loop == True:

    user_respo = str("")

    os.system('cls')
   
    termo1 = int(input('Insira o primeiro termo: '))
    r = int(input('Insira a razão da PA: '))

    for c in range (1, 11):

        termo = termo1 + (c - 1) * r
        if c == 10:
         print(termo, end="... ")
        else:
            print(termo, end=", ")
    if r <= -1:
        print('Sua progressão aritimética é: ', end="", flush= True)
        time.sleep(2)
        print('Decrescente!\n')
    elif r == 0:
        print('Sua progressão aritimética é: ', end="", flush= True)
        time.sleep(2)
        print('Constante!\n')
    else:
        print('Sua progressão aritimética é: ', end='', flush= True)
        time.sleep(2)
        print('Crescente!\n')
        time.sleep(1)

    while user_respo != "Y" and user_respo != "N":
        user_respo = str(input('Deseja construir outra progressão aritimética? (y/n): ')).upper().strip()
        if user_respo == 'N':
            loop = False
        elif user_respo == 'Y':
            loop = True
        else:
            print("\nResposta inválida, tente novamente\n")
print('\nObrigado por usar o meu programa :D')
   

