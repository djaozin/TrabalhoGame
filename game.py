import os
import time
import random
os.system('cls')
print('''----------A Lenda de Eldoria II----------
---Sua aventura está prestes a começar---''')

nome = input('Nome do personagem: ')
hp = 5
atk = 3
df = 1
exp = 0
coinsB = 0
coinsP = 0

player = [nome, hp, atk, df, exp, coinsB, coinsP]

mf_nome = 'Monstrinho (nvl 1)'
mf_hp = 5
mf_atk = 2
mf_df = 0

monstro1 = [mf_nome, mf_hp, mf_atk, mf_df]

mm_nome = 'Monstro (nvl 2)'
mm_hp = 10
mm_atk = 4
mm_df = 1

monstro2 = [mm_nome, mm_hp, mm_atk, mm_df]

md_nome = 'Monstrão (nvl 3)'
md_hp = 15
md_atk = 4
md_df = 1

monstro3 = [md_nome, md_hp, md_atk, md_df]

mb_nome = 'Boss (nvl max.)'
mb_hp = 50
mb_atk = 10
mb_df = 5

monstro4 = [mb_nome, mb_hp, mb_atk, mb_df]

os.system('cls')
print(f'Seja bem vindo, {nome}. Você está entrando na caverna... ')
print('Carregando...')
time.sleep(0.8)

os.system('cls')
while (1):
    op = int(input('''Escolha a opção desejada:
1- Entrar na caverna
2- Sair (Fim do jogo)
'''))
    if op == 1:
        mons = random.randint(0,100)
        fase = 1
        print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')

    
        if mons >= 0 and mons <= 39:
            print(f'''Monstro encontrado.
Fase: {fase}
{nome} VS {mf_nome}
{mf_nome}:
HP: {monstro1[1]}
Ataque: {monstro1[2]}
Defesa: {monstro1[3]}''')
            fase += 1
            start = int(input('''Escolha a opção desejada:
    1- Atacar
    2- Desistir (Fim do jogo)'''))
                
            if start == 1:
                    while player[1] > 0 and monstro1[1] > 0:
                        dano = player[2] - monstro1[3]  # player[2] = atk, monstro1[3] = df
                        hit = monstro1[2] - player[3]  # monstro1[2] = atk, player[3] = df
                        monstro1[1] -= dano if dano > 0 else 0  # Reduz o HP do monstro
                        player[1] -= hit if hit > 0 else 0  # Reduz o HP do jogador
                        print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')
                        if hp <= 0:
                            print('Você morreu. Estatisticas: ')
                            print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')
                            break
                        elif mf_hp <= 0:
                            print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')
                            seguir = input('Inimigo abatido. Deseja continuar a aventura? (S/N)')
                            if seguir == 'N' or seguir =='n':
                                print('Fim de jogo. Estatisticas: ')
                                print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')
                                break
                            elif seguir == 'S' or seguir == 's':
                                print(f'{nome} está continuando sua aventura.')

                            else:
                                print('erro')

            else:
                print('Você morreu. Estatisticas: ')
                print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')

                
        elif mons > 39 and mons <= 69:
            print(f'''Monstro encontrado.
            Fase: {fase}
            {nome} VS {mm_nome}''')
            fase += 1
        
            
        elif mons > 69 and mons <= 89:
            print(f'''Monstro encontrado.
            Fase: {fase}
            {nome} VS {md_nome}''')
            fase += 1
            
        else:
            print(f'''Nome: {player[0]}
HP: {player[1]}
Ataque: {player[2]}
Defesa: {player[3]}
Experiência: {player[4]}
Moedas Bronze: {player[5]}
Moedas Prata: {player[6]}''')
