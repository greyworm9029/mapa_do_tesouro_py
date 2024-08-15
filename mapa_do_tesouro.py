# Mapa do Tesouro
print("Seja Bem-Vindo(a) a Ilha do Tesouro!🏴‍☠️\nSua missao será encontrar o tesouro.💵")
opcao1 = input('Há dois percursos para voce percorrer.\nEscolha qual percurso voce quer. "esquerda"⬅️  ou "direta"➡️  ? ')

if opcao1 == 'esquerda':
    opcao2 = input("Agora voce está diante de um lago.🏞️\nVoce decide 'nadar'🏊 ou 'esperar'✋ ? ")
    if opcao2 == 'esperar':
        opcao3 = input("Voce escolheu esperar e andar pelo terreno.\nVoce encontrou tres portas no caminho: 'vermelha'🔴, 'amarela'🟡 e 'azul'🔵 .\nQual voce vai escolher? ")
        if opcao3 == 'vermelha':
            print("Voce entrou numa sala dominada pelo fogo e se queimou.🔥  Voce perdeu!")
        elif opcao3 == 'amarela':
            print("Parabens! Voce ganhou!👏👏")
        elif opcao3 == 'azul':
            print("Voce foi devorado por monstros.🧌  Voce perdeu!")
        else:
            print("Voce perdeu!")
    else:
        print("Voce foi atacado por um monstro.👹  Voce perdeu!")
else:
    print("Voce caiu numa armadilha.🕸️\nVoce perdeu!")