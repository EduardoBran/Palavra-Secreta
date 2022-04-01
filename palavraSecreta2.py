palavraSecreta = 'programador'.upper()
listaLetrasDigitadas = []
listaLetrasRepetidas = []
contador = 7

while True:
    if contador == 0:
        print(f'\nAhhh, você gastou todas as suas tentativas. A palavra secreta era: {palavraSecreta}')
        break

    letraDigitada = input('\nDigite uma letra: ').upper()

    if len(letraDigitada) > 1:
        print('Favor digitar apenas uma letra, tente novamente')
        continue

    listaLetrasDigitadas.append(letraDigitada)

    if letraDigitada in listaLetrasRepetidas:
        print(f'\n*** Opa opa, vc já digitou a letra {letraDigitada}. Digite outra letra.')
        continue

    if letraDigitada in palavraSecreta:
        print(f'\nUHULLL, a letra "{letraDigitada}" existe na palavra secreta.')

    else:
        print(f'\nAFFF, a letra "{letraDigitada}" NÃO existe na palavra secreta.')
        listaLetrasDigitadas.pop()
        contador -= 1

    listaLetrasRepetidas.append(letraDigitada)

    palavraSecretaTemp = ''

    for letraSecreta in palavraSecreta:

        if letraSecreta in listaLetrasDigitadas:
            palavraSecretaTemp += letraSecreta
        else:
            palavraSecretaTemp += '*'

    if palavraSecretaTemp == palavraSecreta:
        print(f'\nQue legal, VOCÊ GANHOU!!! A palavra era {palavraSecretaTemp}.')
        break
    else:
        print(f'\nA palavra secreta está assim: {palavraSecretaTemp}')
        print(f'Você ainda tem {contador} chance(s)')

print('\n*** Jogo Finalizado! ***')
