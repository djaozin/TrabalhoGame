import os
import time
import random
os.system('cls')

print('''----------A Lenda de Eldoria II----------
---Sua aventura está prestes a começar---''')

nome = input('Nome do personagem: ')

#Uso de dicionario para armazenar as informações do usuario
personagem = {'nome' : nome,
'hp': 8,
'atk': 2,
'df': 1,
'esq': 1,
'exp': 0}

#Dicionario unico que armazena todos os monstros de uma vez, porém separados
monstros = {'MonstroFraco' : {
nome : 'Monstro Nvl1',
'atk' : 3,
'def' : 1,
'hp' : 8,
'esq' : 2},
'MonstroMedio' : {
nome : 'Monstro Nvl2',
'atk' : 4,
'def' : 1,
'hp' : 12,
'esq' : 4},
'MonstroDificil' : {
nome : 'Monstro Nvl3',
'atk' : 6,
'def' : 2,
'hp' : 20,
'esq' : 6},
'MonstroChefe' : {
nome : 'Boss',
'atk' : 10,
'def' : 5,
'hp' : 45,
'esq' : 8}}

print(f'Seja bem-vindo, {nome}. Você está entrando na caverna... ')
print('Carregando...')
time.sleep(1)

while True:
    desafio = random.randint(1 , 20)
    if desafio >= 1 and desafio <=4:
        print('Você entrou em um desafio do baú!')
        time.sleep(0.5)
        tipo_bau = random.randint(1, 10)
        if tipo_bau == 1 or tipo_bau == 2:
            print('Você encontrou um baú do tipo mimico') #Prosseguir com o codigo abaixo

        else:
            print('Você encontrou um baú! Iniciando tentativas de abertura...')

            tentativas = 3 #Maximo de tentativas 
            cont_tent = 1 #Contagem pra mostrar ao usuario a tentativa atual
            while tentativas > 0:
                print(f'Tentativa {cont_tent}:')
                time.sleep(0.5)
                abrir = random.randint(1, 20)
                
                if abrir >= 1 and abrir <= 9:
                    print('Você não conseguiu abrir o baú.')
                    tentativas -= 1
                    cont_tent += 1
                elif abrir >= 10 and abrir <= 20:
                    print('''Você conseguiu abrir o baú!!
    Conteúdo:
    1 poção de vida''')
                    break

            if tentativas == 0:
                print('Baú perdido... Avançando para o proximo desafio.')
    else:
        print('Nenhum desafio encontrado. Avançando...')
                
    continuar = input('Deseja continuar enfrentando desafios? (s/n)')
    if continuar.lower() != 's':
        print('Saindo do jogo. Até a proxima!')
        break


