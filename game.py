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
'hp_max': 8,
'atk': 2,
'def': 1,
'esq': 1,
'exp': 0,
'nivel': 1,
'exp_prox_nivel': 100,
'vocacao': []}

#Dicionario unico que armazena todos os monstros de uma vez, porém separados
monstros = {'MonstroFraco' : {
'nome' : 'Monstro Nvl1',
'atk' : 3,
'def' : 1,
'hp' : 8,
'esq' : 2},
'MonstroMedio' : {
'nome' : 'Monstro Nvl2',
'atk' : 4,
'def' : 1,
'hp' : 12,
'esq' : 4},
'MonstroDificil' : {
'nome' : 'Monstro Nvl3',
'atk' : 6,
'def' : 2,
'hp' : 20,
'esq' : 6},
'MonstroChefe' : {
'nome' : 'Boss',
'atk' : 10,
'def' : 5,
'hp' : 45,
'esq' : 8}}

escolha_vocs = {
'1' : 'Guerreiro',
'2' : 'Arqueiro',
'3' : 'Paladino'
}

vocs = {
'Guerreiro' : {
'atk': 2,
'def': 1,
'esq': -1,
'hp': 0
},

'Arqueiro' : {
'atk': 3,
'def': 1,
'esq': 0,
'hp' : -1
},

'Paladino' : {
'atk': 1,
'def': 1,
'hp' : 1,
'esq': -1,
}
}

escolha_raca = {
    '1' : 'Anões',
    '2' : 'Elfos',
    '3' : 'Humanos'
}
raca = {
'Anões' : {
'atk' : 0,
'def': 1,
'esq' : 0,
'hp': 2
},
'Elfos' : {
'atk': 1,
'def': 0,
'esq': 2,
'hp':0
    },
'Humanos' : {
'atk': 1,
'def': 1,
'esq': 1,
'hp' : 1
}
}
def escolher_vocacao():
    print("Escolha sua vocacao:")
    for chave, valor in escolha_vocs.items():
        print(f"{chave} - {valor}")
    voc = input("Digite o numero correspondente: ")
    return voc

def escolher_raca():
    for chave, valor in escolha_raca.items():
        print(f"{chave} - {valor}")
        raca_selecionada = input("Digite o numero correspondente: ")
        return raca_selecionada


def usar_pocao_vida():
    cura = int(personagem['hp']* 0.5)
    personagem['hp'] = min(personagem['hp'] + cura, personagem['hp_max'])
    print (f"{personagem['nome']} usou uma poção de vida e recuperou {cura} de HP! HP atual: {personagem['hp']}/{personagem['hp_max']}")
def testeEsq(): #Teste de Esquiva
    res_esq = 0
    d20_e = random.randint(0,20)
    res_esq = d20_e + personagem['esq']
    return res_esq

def testeEsqM(monstro_tipo): #Teste de Esquiva dos monstros
    res_esqm = 0
    monstro = monstro_tipo
    d20_em = random.randint(0,20)
    res_esqm = d20_em + monstros[monstro]['esq']
    return res_esqm

def testeAtk(): #Teste de Ataque
    res_atk = 0
    d20_a = random.randint(0,20)
    if d20_a == 20:
        tipo_dano = "Dano Crítico"
        res_atk = (d20_a + personagem['atk']) * 2
    else:
        res_atk = d20_a + personagem['atk']
        tipo_dano = "Dano Normal"
    return res_atk, tipo_dano

def testeAtkM(monstro_tipo): #Teste de Ataque dos monstros
    monstro = monstro_tipo
    res_atkm = 0
    d20_am = random.randint(0,20)
    res_atkm = d20_am + monstros[monstro]['atk']
    if d20_am == 20:
        tipo_dano = "Dano Crítico"
        res_atkm *= 2
    else:
        tipo_dano = "Dano Normal"
    return res_atkm, tipo_dano

def dano_causado(monstro_tipo): #Dano causado geral podendo ser usado para todos os monstros
    res_atk, tipo_dano = testeAtk()
    res_esqm = testeEsqM(monstro_tipo)
    monstro = monstros[monstro_tipo]
    mos = monstro_tipo
    if res_esqm > res_atk: #Usa o teste da esquiva do monstro
        print(f'{monstro["nome"]} esquivou do seu ataque! Você não causou dano.')
        return "Esquiva"

    else:
        if res_atk > monstro['def']: #Caso ele nao esquive, agr verifica se o dano é > defesa
            dano = res_atk - monstro['def']
            monstro['hp'] = max(0, monstro['hp'] - dano)
            print(f"{personagem['nome']} causou um {tipo_dano} de {dano} atk ao {monstro['nome']}. HP restante do monstro: {monstro['hp']}")
            if monstro['hp'] == 0:
                print(f"{monstro['nome']} foi derrotado!")
                if mos == "MonstroFraco":
                    personagem['exp'] += 50
                    print('XP Obtido: 50')
                elif mos == "MonstroMedio":
                    personagem['exp'] += 100
                    print('XP Obtido: 100')
                elif mos == "MonstroDificil":
                    personagem['exp'] += 200
                    print('XP Obtido: 200')
                
            return dano
        else:
            print(f"O ataque de {personagem['nome']} falhou! Defesa de {monstro['nome']} foi muito alta.")
            return "Esquiva"
    
def dano_recebido(monstro_tipo):
    monstro = monstro_tipo
    res_atkm, tipo_dano = testeAtkM(monstro_tipo)
    res_esq = testeEsq()
    if res_esq > res_atkm:
        print(f"{personagem['nome']} esquivou do ataque do oponente! Nenhum dano recebido.")
        return "Esquiva"

    else:
        if res_atkm > personagem['def']:
            dano = res_atkm - personagem['def']
            personagem['hp'] = max(0, personagem['hp'] - dano)
            print(f"{monstros[monstro]['nome']} causou um {tipo_dano} de {dano} atk ao {personagem['nome']}. HP restante do personagem: {personagem['hp']}")
            return dano
        else:
            print(f"O ataque do {monstros[monstro]['nome']} falhou! Defesa do {personagem['nome']} foi muito alta.")
            return 0

def nivel_jogador():
    if personagem['exp'] >= personagem['exp_prox_nivel']:
        personagem['nivel'] += 1
        personagem['exp'] -= personagem['exp_prox_nivel']
        print(f"{personagem['nome']} subiu para o nível {personagem['nivel']}!")
        personagem['exp_prox_nivel'] = int(personagem['exp_prox_nivel'] * 1.4)
        print(f"Você tem {personagem['exp']}EXP. Experiencia necessaria para o nível {personagem['nivel']}: {personagem['exp_prox_nivel'] - personagem['exp']} ")
    
    else:
        print(f"Você tem {personagem['exp']} EXP. Experiencia necessaria para o nível {personagem['nivel']}: {personagem['exp_prox_nivel']}")

def status():
    return f'''Seus status:
HP: {personagem['hp']}
ATK: {personagem['atk']}
DEF: {personagem['def']}
ESQ: {personagem['esq']}
EXP: {personagem['exp']}'''

print(f'Seja bem-vindo, {nome}. Você está entrando na caverna... ')
print('Carregando...')
time.sleep(1)

print ('-----Você chegou na caverna-----')

menu = int(input ('''1 - Para entrar na caverna!
2 - Não entrar na caverna
'''))
if menu == 1:
    print ('Você entrou!!')
elif menu == 2:
    print ('Você saiu da caverna...')
    exit()

while True:
    desafio = random.randint(1 , 20)
    if desafio >= 1 and desafio <=4: #Abertura de baús
        print('Você entrou em um desafio do baú!')
        time.sleep(0.5)
        tipo_bau = random.randint(1, 10)
        if tipo_bau == 1 or tipo_bau == 2:
            print('Você encontrou um baú com uma armadilha!') #Prosseguir com o codigo abaixo
            print(f"{personagem['nome']} VS {monstros['MonstroMedio']['nome']}")
            while personagem['hp'] > 0 and monstros['MonstroMedio']['hp'] > 0:
                print('''1 - Atacar
2 - Defender
3 - Correr ''')
                op = int(input())
                if op == 1: #Ataque
                        testeEsqM("MonstroMedio")
                        resultado_causado = dano_causado("MonstroMedio")
                        if resultado_causado == "Esquiva":
                            print(f"Turno do {monstros['MonstroMedio']['nome']}...")
                        if monstros['MonstroMedio']['hp'] > 0:
                            dano_recebido("MonstroMedio")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()

                elif op == 2: #defesa
                    defesa_original = personagem['def']
                    personagem['def'] = personagem['def'] + 5
                    print(f"Sua defesa aumentou de {personagem['def'] - 5} para {personagem['def']}.")
                    print(f"Turno do {monstros['MonstroMedio']['nome']}...")
                    if monstros['MonstroMedio']['hp'] > 0:
                            dano_recebido("MonstroMedio")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                            else:
                                personagem['def'] = defesa_original


                elif op == 3:
                        correr=random.randint(1, 10)
                        if correr >= 1 and correr <= 4:
                            print('Você conseguiu correr!')
                            break
                        elif correr >= 5 and correr <= 10:
                            print ('Você Morreu tentando correr...')
                            print (status())
                            exit()

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
                    usar_pocao_vida()
                    break

            if tentativas == 0:
                print('Baú perdido... Avançando para o proximo desafio.')
    
    elif desafio >= 5 and desafio <= 20: #Combate contra monstros
        print('Você Encontrou um monstro!')
        mons = random.randint(0,100)
        
        if mons >= 0 and mons <= 39: #monstro 1
            print(f"{personagem['nome']} VS {monstros['MonstroFraco']['nome']}")
            while personagem['hp'] > 0 and monstros['MonstroFraco']['hp'] > 0:
                print('''Seu turno...
1 - Atacar
2 - Defender
3 - Correr ''')
                op = int(input())
                if op == 1: #Ataque
                    testeEsqM("MonstroFraco")
                    resultado_causado = dano_causado("MonstroFraco")
                    if resultado_causado == "Esquiva":
                        print(f"Turno do {monstros['MonstroFraco']['nome']}...")
                        if monstros['MonstroFraco']['hp'] > 0:
                            dano_recebido("MonstroFraco")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                elif op == 2: #defesa
                    defesa_original = personagem['def']
                    personagem['def'] = personagem['def'] + 5
                    print(f"Sua defesa aumentou de {personagem['def'] - 5} para {personagem['def']}.")
                    print(f"Turno do {monstros['MonstroFraco']['nome']}...")
                    if monstros['MonstroFraco']['hp'] > 0:
                            dano_recebido("MonstroFraco")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                            else:
                                personagem['def'] = defesa_original
                elif op == 3:
                    correr=random.randint(1, 10)
                    if correr >= 1 and correr <= 4:
                        print('Você conseguiu correr!')
                        break
                    elif correr >= 5 and correr <= 10:
                        print ('Você Morreu tentando correr...')
                        print (status())
                        exit()
            
        elif mons >= 40 and mons <= 69: #monstro 2
            print(f"{personagem['nome']} VS {monstros['MonstroMedio']['nome']}")
            while personagem['hp'] > 0 and monstros['MonstroMedio']['hp'] > 0:
                print('''1 - Atacar
2 - Defender
3 - Correr ''')
                op = int(input())
                if op == 1: #Ataque
                        testeEsqM("MonstroMedio")
                        resultado_causado = dano_causado("MonstroMedio")
                        if resultado_causado == "Esquiva":
                            print(f"Turno do {monstros['MonstroMedio']['nome']}...")
                        if monstros['MonstroMedio']['hp'] > 0:
                            dano_recebido("MonstroMedio")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()

                elif op == 2: #defesa
                    defesa_original = personagem['def']
                    personagem['def'] = personagem['def'] + 5
                    print(f"Sua defesa aumentou de {personagem['def'] - 5} para {personagem['def']}.")
                    print(f"Turno do {monstros['MonstroMedio']['nome']}...")
                    if monstros['MonstroMedio']['hp'] > 0:
                            dano_recebido("MonstroMedio")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                            else:
                                personagem['def'] = defesa_original


                elif op == 3:
                        correr=random.randint(1, 10)
                        if correr >= 1 and correr <= 4:
                            print('Você conseguiu correr!')
                            break
                        elif correr >= 5 and correr <= 10:
                            print ('Você Morreu tentando correr...')
                            print (status())
                            exit()

        elif mons >= 70 and mons <= 89:
            print(f"{personagem['nome']} VS {monstros['MonstroDificil']['nome']}")
            while personagem['hp'] > 0 and monstros['MonstroDificil']['hp'] > 0:
                print('''1 - Atacar
2 - Defender
3 - Correr ''')#monstro 3 
                op = int(input())
                if op == 1: #Ataque
                        testeEsqM("MonstroDificil")
                        resultado_causado = dano_causado("MonstroDificil")
                        if resultado_causado == "Esquiva":
                            print(f"Turno do {monstros['MonstroDificil']['nome']}...")
                        if monstros['MonstroDificil']['hp'] > 0:
                            dano_recebido("MonstroDificil")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                elif op == 2: #defesa
                    defesa_original = personagem['def']
                    personagem['def'] = personagem['def'] + 5
                    print(f"Sua defesa aumentou de {personagem['def'] - 5} para {personagem['def']}.")
                    print(f"Turno do {monstros['MonstroDificil']['nome']}...")
                    if monstros['MonstroDificil']['hp'] > 0:
                            dano_recebido("MonstroDificil")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                            else:
                                personagem['def'] = defesa_original
                elif op == 3:
                        correr=random.randint(1, 10)
                        if correr >= 1 and correr <= 4:
                            print('Você conseguiu correr!')
                            break
                        elif correr >= 5 and correr <= 10:
                            print ('Você Morreu tentando correr...')
                            print (status())
                            exit()

        elif mons >= 90 and mons <= 100:
            print(f"{personagem['nome']} VS {monstros['MonstroChefe']['nome']}")
            while personagem['hp'] > 0 and monstros['MonstroChefe']['hp'] > 0:
                print('''1 - Atacar
2 - Defender
3 - Correr ''')#boss
                op = int(input())
                if op == 1: #Ataque
                        testeEsqM("MonstroChefe")
                        resultado_causado = dano_causado("MonstroChefe")
                        if resultado_causado == "Esquiva":
                            print(f"Turno do {monstros['MonstroChefe']['nome']}...")
                        if monstros['MonstroChefe']['hp'] > 0:
                            dano_recebido("MonstroChefe")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                elif op == 2: #defesa
                    defesa_original = personagem['def']
                    personagem['def'] = personagem['def'] + 5
                    print(f"Sua defesa aumentou de {personagem['def'] - 5} para {personagem['def']}.")
                    print(f"Turno do {monstros['MonstroChefe']['nome']}...")
                    if monstros['MonstroChefe']['hp'] > 0:
                            dano_recebido("MonstroChefe")
                            if personagem['hp'] <= 0:
                                print ('Você Morreu...')
                                print (status())
                                exit()
                            else:
                                personagem['def'] = defesa_original
                elif op == 3:
                        correr=random.randint(1, 10)
                        if correr >= 1 and correr <= 4:
                            print('Você conseguiu correr!')
                            break
                        elif correr >= 5 and correr <= 10:
                            print ('Você Morreu tentando correr...')
                            print (status())
                            exit()
    
    nivel_jogador()
    if personagem['nivel'] == 2:
        for chave, valor in escolha_vocs.items():
            print(f"{chave} - {valor}")
        vocs_escolhida = int(input('Escolha sua vocação:'))
        
        for vocs_escolhida in escolha_vocs:
            vocacao = escolha_vocs[vocs_escolhida]
            personagem['atk'] += vocs[vocacao]['atk']
            personagem['def'] += vocs[vocacao]['def']
            personagem['esq'] += vocs[vocacao]['esq']
            personagem['hp'] += vocs[vocacao]['hp']
            
    continuar = input('Deseja continuar enfrentando desafios? (s/n)')
    for monstro in monstros.values(): #for utilizado para restaurar a vida dos monstros e o codigo ter continuidade
        if monstro['nome'] == 'Monstro Nvl1':
            monstro['hp'] = 8
        elif monstro['nome'] == 'Monstro Nvl2':
            monstro['hp'] = 12
        elif monstro['nome'] == 'Monstro Nvl3':
            monstro['hp'] = 20
        elif monstro['nome'] == 'Boss':
            monstro['hp'] = 45

    if continuar.lower() != 's':
        print('Saindo do jogo. Até a proxima!')
        print (status())
        #Criar tela final contendo dados do jogador, quantas kills,etc
        break   
