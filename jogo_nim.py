def campeonato():
    i = 1

    while i <= 3:
        print("**** Rodada ",i," ****")
        partida()
        i += 1
        
    print("Placar: Você 0 X 3 Computador")

def computador_escolhe_jogada(n, m):
    retira_computador = 1

    while retira_computador <= n and retira_computador <= m:
        if (n - retira_computador) % (m + 1) == 0:
            break
        else:
            if retira_computador == m:
                break
            else:
                retira_computador+=1
    
    return retira_computador

def usuario_escolhe_jogada(n, m):
    continuar = True
    
    while continuar:
        jogada_usuario = int(input("Quantas peças você vai tirar?\n"))
        if jogada_usuario > n or jogada_usuario <= 0 or jogada_usuario > m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            continuar = False

    return jogada_usuario

def partida():
        n = int(input("Quantas peças?\n"))
        m = int(input("Limite de peças por jogada?\n"))

        if n % (m + 1) == 0:
            print("Você começa!")
            while n > 0:
                retira_usuario = usuario_escolhe_jogada(n, m)
                n = n - retira_usuario
                print("Voce tirou",retira_usuario,"peças.")
                print("Agora resta apenas",n,"peça no tabuleiro.")

                print("O computador tirou",computador_escolhe_jogada(n, m),"peça.")
                n = n - computador_escolhe_jogada(n, m)
                if n != 0:
                    print("Agora resta apenas",n,"peça no tabuleiro.")
                else:
                    print("Fim do jogo! O computador ganhou!")
                    break
        else:
            print("Computador começa!")
            while n > 0:
                print("O computador tirou",computador_escolhe_jogada(n, m),"peça.")
                n = n - computador_escolhe_jogada(n, m)
                if n != 0:
                    print("Agora resta apenas",n,"peça no tabuleiro.")
                else:
                    print("Fim do jogo! O computador ganhou!")
                    break

                retira_usuario = usuario_escolhe_jogada(n, m)
                n = n - retira_usuario
                print("Voce tirou",retira_usuario,"peças.")
                print("Agora resta apenas",n,"peça no tabuleiro.")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    escolha_jogo = int(input("2 - para jogar um campeonato\n"))
    
    if escolha_jogo == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha_jogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
    else:
        print("Opção inválida.")

main()

