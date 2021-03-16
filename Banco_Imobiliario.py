import random 
# import datetime

# # Verifica a Quantidade de Players Inativos
def verificaPlayersInativos(jogadores):
    playersInativo = 0
    for player in jogadores:
        if jogadores[player]['Status'] == 'Inativo': 
            playersInativo += 1
    return playersInativo

# # Processo de Analise para Decidir o Vencedor por TimeOut
def calVencedorTimeOut(jogadores):
    valorMax = 0
    # # Verifica o Maior Saldo em Caso de TimeOut
    for jogador in jogadores:
        if valorMax < jogadores[jogador]['Saldo']:
            valorMax = jogadores[jogador]['Saldo']

    # # Verifica Quais Jogadores tem o Maior Saldo
    res = {}    
    for key, jogador in jogadores.items():
        if jogador['Saldo'] == valorMax:
            res[key] = valorMax

    # # Em caso de Multiplos Jogadores com o Maior Saldo, Vencedor é o com a Ordem de Jogada Menor
    if len(res) > 1:
        ordemJogador = 4
        for jogador in res:
            if jogadores[jogador]['Ordem'] <= ordemJogador:
                ordemJogador = jogadores[jogador]['Ordem']
                vencedor = jogador
    # # Em caso de um Unico Jogador ter o Maior Saldo, ele é o Vencedor
    else:
        for jogador in res:
            vencedor = jogador
    return vencedor

# # Calcula a Porcentagem de Vitórias
def porcentoVitorias(numVitoriasPlayer, resumo):
    media = (numVitoriasPlayer / len(resumo['Vencedores'])) * 100
    return media

# inicioExec = datetime.datetime.now()

# # Lista de Players
ordemJogadores = ['Player1', 'Player2', 'Player3', 'Player4']
# # Ordem Aleatória da Lista de Players
random.shuffle(ordemJogadores)

# # Dicionario de Resumo das Simulações
resumo = {'PartidasConcTimeOut': 0, 'NumTurnos': [], 'Vencedores': []}

# # Rodando 300 Simulações
for simulacaoNum in range(300):
    # # Contador de Rodadas
    numRodada = 0

    # # Verifica se Partida deve Finalizar por Timeout (mais de 100 Rodadas)
    concTimeOut = False

    # # Estrutura Dicionario dos Jogadores 
    jogadores = {'Player1': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Impulsivo'},
    'Player2': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Exigente'},
    'Player3': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Cauteloso'},
    'Player4': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Aleatorio'}}

    # # Imprime atual ordem dos Jogadores
    # print('Ordem dos Jogadores:')
    # for numOrdem, ordem in enumerate(ordemJogadores):
    #     jogadores[ordem]['Ordem'] = numOrdem+1
    #     print(str(numOrdem+1) + 'º Jogador: ' + str(ordem))

    # # Listagem das Propriedades
    tabuleiro = ['Propriedade 01', 'Propriedade 02', 'Propriedade 03', 'Propriedade 04', 'Propriedade 05', 
    'Propriedade 06', 'Propriedade 07', 'Propriedade 08', 'Propriedade 09', 'Propriedade 10', 'Propriedade 11', 
    'Propriedade 12', 'Propriedade 13', 'Propriedade 14', 'Propriedade 15', 'Propriedade 16', 'Propriedade 17', 
    'Propriedade 18', 'Propriedade 19', 'Propriedade 20']

    # # Dicionario das Propriedades
    infoPropriedade = {'Propriedade 01' : {'Venda': 210, 'Aluguel': 42, 'Proprietario': None, 'Posicao': 0},
    'Propriedade 02': {'Venda': 210, 'Aluguel': 42, 'Proprietario': None, 'Posicao': 1},
    'Propriedade 03': {'Venda': 220, 'Aluguel': 44, 'Proprietario': None, 'Posicao': 2},
    'Propriedade 04': {'Venda': 220, 'Aluguel': 44, 'Proprietario': None, 'Posicao': 3},
    'Propriedade 05': {'Venda': 230, 'Aluguel': 46, 'Proprietario': None, 'Posicao': 4},
    'Propriedade 06': {'Venda': 230, 'Aluguel': 46, 'Proprietario': None, 'Posicao': 5},
    'Propriedade 07': {'Venda': 240, 'Aluguel': 48, 'Proprietario': None, 'Posicao': 6},
    'Propriedade 08': {'Venda': 240, 'Aluguel': 48, 'Proprietario': None, 'Posicao': 7},
    'Propriedade 09': {'Venda': 250, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 8},
    'Propriedade 10': {'Venda': 250, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 9},
    'Propriedade 11': {'Venda': 255, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 10},
    'Propriedade 12': {'Venda': 255, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 11},
    'Propriedade 13': {'Venda': 255, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 12},
    'Propriedade 14': {'Venda': 260, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 13},
    'Propriedade 15': {'Venda': 260, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 14},
    'Propriedade 16': {'Venda': 260, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 15},
    'Propriedade 17': {'Venda': 265, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 16},
    'Propriedade 18': {'Venda': 265, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 17},
    'Propriedade 19': {'Venda': 265, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 18},
    'Propriedade 20': {'Venda': 270, 'Aluguel': 54, 'Proprietario': None, 'Posicao': 19}}

    # # Quantidade Inical de Players Inativos / Derrotados
    playersInativo = 0
    # # Continua jogo até somente 1 player estar Ativo 
    while playersInativo != 3:

        # # Loop de Jogada de Cada Player
        for jogador in ordemJogadores:
            
            # # Pula para Proximo Player se Player Atual estiver Inativo
            if jogadores[jogador]['Status'] == 'Inativo':
                continue
            
            # # Roda o Dado de 6 Lados adicionando a Posição do Player
            jogadores[jogador]['Posicao'] += random.randrange(1, 7)

            # # Completou a volta no Tabuleiro
            if jogadores[jogador]['Posicao'] >= 20:
                # # Mais 100 de Saldo devido a Completar Volta pelo Tabuleiro
                jogadores[jogador]['Saldo'] += 100
                # # -20 Posições / Retornar ao Inicio
                jogadores[jogador]['Posicao'] -= 20

            # # Verifica se a Propriedade onde o Player caiu pertence a alguem
            if infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario'] == None:
                # # Verifica Comportamento do Player
                if jogadores[jogador]['Comportamento'] == 'Impulsivo':
                    # # O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
                    if (jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']) >= 0:
                        jogadores[jogador]['Saldo'] = jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']
                        infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario'] = jogador
                    else:
                        pass
                elif jogadores[jogador]['Comportamento'] == 'Exigente':
                    # # O jogador exigente compra qualquer propriedade, desde que 
                    # # o valor do aluguel dela seja maior do que 50.
                    if (jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']) >= 0:
                        if infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Aluguel'] >= 50:
                            jogadores[jogador]['Saldo'] = jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']
                            infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario'] = jogador
                        else:
                            pass
                    else:
                        pass
                elif jogadores[jogador]['Comportamento'] == 'Cauteloso':
                    # # O jogador cauteloso compra qualquer propriedade desde que 
                    # # ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
                    if (jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']) >= 80:
                        jogadores[jogador]['Saldo'] = jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']
                        infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario'] = jogador
                    else:
                        pass
                elif jogadores[jogador]['Comportamento'] == 'Aleatorio':
                    # # O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
                    if (jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']) >= 0:
                        # # Aleatório de 0 ou 1, onde somente nos casos de 1 (Aprox. 50% de Chance), 
                        # # a Propriedade é Comprada
                        if random.randrange(0, 2) == 1:
                            jogadores[jogador]['Saldo'] = jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Venda']
                            infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario'] = jogador
                        else:
                            pass
                    else:
                        pass
                else:
                    print('Comportamento Não Definido.')
                    pass
            else:
                jogadores[jogador]['Saldo'] = jogadores[jogador]['Saldo'] - infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Aluguel']
                jogadores[infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario']]['Saldo'] = jogadores[infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Proprietario']]['Saldo'] + infoPropriedade[tabuleiro[jogadores[jogador]['Posicao']]]['Aluguel']

            # # Ao Ficar com Saldo Negativo o Player é Inativado e Suas Propriedades Voltam a Não ter Dono.
            if jogadores[jogador]['Saldo'] < 0:
                jogadores[jogador]['Status'] = 'Inativo'
                for propriedade in infoPropriedade:
                    if infoPropriedade[propriedade]['Proprietario'] == jogador:
                        infoPropriedade[propriedade]['Proprietario'] = None
        
            playersInativo = verificaPlayersInativos(jogadores)

        # # Contador de Rodadas
        numRodada += 1

        # # Verifica se Numero de Rodadas é Maior que 1000, caso seja, sai do Loop Inicial e 
        # # Adiciona Mais 1 ao Numero de Particas Concluidas por TimeOut
        if numRodada > 1000:
            resumo['PartidasConcTimeOut'] += 1
            concTimeOut = True
            break

        # # Imprime o Resumo da Rodada
        # print('Resumo da Rodada Nº: ' + str(numRodada))
        # print(jogadores)
        # print(infoPropriedade)

    # # Verifica Quantidade de Players Inativos, caso igual a 3, adicona o unico Player Ativo como Vencedor
    if playersInativo == 3:
        for playerAtual in jogadores: 
            if jogadores[playerAtual]['Status'] == 'Ativo': 
                resumo['Vencedores'].append(playerAtual)
    # # Caso Rodada tenha Finalizado por TimeOut, Vencedor entra como Player com Maior Saldo
    elif concTimeOut == True:
        vencedorTimeOut = calVencedorTimeOut(jogadores)
        resumo['Vencedores'].append(vencedorTimeOut)

    # # Insere Numero de Turnos Totais Para Conclusão da Partida em uma Lista
    resumo['NumTurnos'].append(numRodada)
        
# print('Resumo das Simulações:')
# print(resumo)

# # Calcula a Média de Turnos que as Partidas levaram
totalTurnos = 0
for turnos in resumo['NumTurnos']:
    totalTurnos += turnos
mediaTurnos = totalTurnos / len(resumo['NumTurnos'])

print('Partidas Concluidas por TimeOut: ' + str(resumo['PartidasConcTimeOut']))
print('Quantidade de Turnos em Média por Simulação: ' + str(int(mediaTurnos)))

numVitoriasP1, numVitoriasP2, numVitoriasP3, numVitoriasP4 = 0, 0, 0, 0
# # Calcula quantas Vitórias cada Jogador teve
for resumoVencedor in resumo['Vencedores']:
    if resumoVencedor == 'Player1':
        numVitoriasP1 += 1
    elif resumoVencedor == 'Player2':
        numVitoriasP2 += 1
    elif resumoVencedor == 'Player3':
        numVitoriasP3 += 1
    elif resumoVencedor == 'Player4':
        numVitoriasP4 += 1
    else:
        print('Vencedor Desconhecido!')
        pass

print('O Comportamento ' + jogadores['Player1']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(porcentoVitorias(numVitoriasP1, resumo)) + r'% das Vezes.')
print('O Comportamento ' + jogadores['Player2']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(porcentoVitorias(numVitoriasP2, resumo)) + r'% das Vezes.')
print('O Comportamento ' + jogadores['Player3']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(porcentoVitorias(numVitoriasP3, resumo)) + r'% das Vezes.')
print('O Comportamento ' + jogadores['Player4']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(porcentoVitorias(numVitoriasP4, resumo)) + r'% das Vezes.')

# # Calcula qual Jogador ganhou mais Partidas dentre as Simulações
jogadorMaisVitorias = max(set(resumo['Vencedores']), key = resumo['Vencedores'].count)
# print('Jogador com Mais Vitórias: ' + str(jogadorMaisVitorias))
print('Comportamento com Mais Vitórias: ' + str(jogadores[jogadorMaisVitorias]['Comportamento']))
# print('Tempo Total de Execução das Simulações: ' + str(datetime.datetime.now() - inicioExec))

# # Gera um Dicionario como Saida com Informações Pertinentes
saida = {'ConcTimeOut': int(resumo['PartidasConcTimeOut']),
'QtdMediaTurnos': int(mediaTurnos),
'PorcentoVitoriaComportamento': {jogadores['Player1']['Comportamento']: "{:.2f}".format(porcentoVitorias(numVitoriasP1, resumo)) + r'%',
jogadores['Player2']['Comportamento']: "{:.2f}".format(porcentoVitorias(numVitoriasP2, resumo)) + r'%',
jogadores['Player3']['Comportamento']: "{:.2f}".format(porcentoVitorias(numVitoriasP3, resumo)) + r'%',
jogadores['Player4']['Comportamento']: "{:.2f}".format(porcentoVitorias(numVitoriasP4, resumo)) + r'%'},
'ComportamentoMaisVitorioso': jogadores[jogadorMaisVitorias]['Comportamento']}

print(saida)