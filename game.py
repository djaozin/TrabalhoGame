import os
import time
import random
os.system('cls')

print('''----------A Lenda de Eldoria II----------
---Sua aventura está prestes a começar---''')

nome = input('Nome do personagem: ')

hp = 8
atk = 2
df = 1
esq = 1
exp = 0

print(f'Seja bem-vindo, {nome}. Você está entrando na caverna... ')
print('Carregando...')
time.sleep(1)

desafio = random.randint(1 , 20)
if desafio >= 1 and desafio <=4:
    print('Você entrou em um desafio do baú!')
    time.sleep(0.5)
    tipo_bau = random.randint(1, 10)
    if tipo_bau == 1 or tipo_bau == 2:
        print('Você encontrou um baú do tipo mimico') #prosseguir com o codigo abaixo

    else:
        print('Você encontrou um baú! Iniciando tentativas de abertura...')

        tentativas = 3
        while tentativas > 0:
            print('Tentativa 1:')
            time.sleep(0.5)
            abrir = random.randint(1, 20)
            
            if abrir >= 1 and abrir <= 9:
                print('Você não conseguiu abrir o baú')
                tentativas -= 1
            elif abrir >= 10 and abrir <= 20:
                print('''Você conseguiu abrir o baú!!
Conteúdo:
1 poção de vida''')


