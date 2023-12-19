from random import randint
import time
import os


# CONFIGURAÇÕES
os.system('cls')
lvl = 0
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
esc = numeros[lvl]
numero = randint(1,esc)
loop = True
print('-'*50)
print('-'*50)
print('')
print('Game Guessed The Number')
print('')
print('(Obs: Digite "x" para sair do Game)')
print('')
print('-'*50)
print('-'*50)
time.sleep(4)


# CONTADOR
def cont(ini):
    for i in range(3, 0, -1):
        os.system('cls') # LIMPAR TERMINAL
        print(f'{ini} em "{i}".')
        time.sleep(1)
cont(ini="Começando")
# SAIR
def sair():
    print('-'*50)
    print('')
    print('Fim do jogo...')
    time.sleep(2)

# GAME
while loop:
    os.system('cls')
    print(f'----------Level: {lvl + 1}-10-----------')
    escolha = input(f'Escolha um número de 1 a {esc}: ')
    # ESCOLHA "SAIR"
    if escolha == "x":
        pass
    else:
        escolha = int(escolha)

    if escolha == "x":
        sair()
        break
    
    # GANHOU
    elif escolha == numero:
        os.system('cls')
        print(f'Parabéns você acertou, você escolheu: "{escolha}"')
        print(f'e o número é exatamente: "{numero}"')
        
        lvl += 1
        if lvl == 10:
            print('')
            print('----------Parabéns-----------')
            print('')
            print('-----Você Concluiu o Game-----')
            print('')
            sair()
            break
            
        numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        esc = numeros[lvl]
        numero = randint(1, esc)
        time.sleep(3)
        
    # NUMERO MAIS BAIXO
    elif escolha > numero:
        os.system('cls')
        print(f'Você escolheu: "{escolha}" o número é mais baixo!')
        time.sleep(2)
    # NUMERO MAIS ALTO        
    elif escolha < numero:
        os.system('cls')
        print(f'Você escolheu: "{escolha}" o número é mais alto')
        time.sleep(2)
