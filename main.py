from personagem import Personagem
from vilao import Vilao

def main():
    # Criando personagens e vilões
    heroi = Personagem('Link', 30, 100)
    npc = Personagem('Zelda', 28, 80)
    vilao = Vilao('Ganon', 45, 120, 'Alta')

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.ataque(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
import time

def pausa():
    input("\n[Aperte Enter para continuar...]")

def introducao():
    print("=== A Lenda de Hyrule ===\n")
    print("O reino de Hyrule está em perigo. O malvado Ganon sequestrou a princesa Zelda, e o herói Link precisa salvar o dia!")
    print("Durante a jornada, Link enfrentará lacaios e deverá contar com a ajuda de aliados para vencer o mal.")
    pausa()

def mostrar_status(personagem):
    print(f"\nStatus de {personagem.nome}: Vida = {personagem.vida}, Ataque básico = 10, Ataque forte = 20, Flecha = 20")

def interacao_npc_bondoso(heroi):
    print("\nLink encontra um velho sábio que oferece uma poção mágica.")
    print("Velho Sábio: 'Esta poção vai te ajudar na batalha contra Ganon. Use com sabedoria!'")
    heroi.itens['poção'] = 1
    pausa()

def primeira_luta(heroi):
    print("\nPrimeira batalha: Lacaios de Ganon aparecem para testar Link!")
    lacaios = [Vilao("Lacaio 1", 20, 80, "Baixa"), Vilao("Lacaio 2", 25, 80, "Média")]

    for lacaio in lacaios:
        print(f"\nLuta contra {lacaio.nome} com {lacaio.vida} de vida.")
        while lacaio.vida > 0:
            print("Escolha o ataque:")
            print("1 - Ataque básico (10 de dano)")
            print("2 - Ataque forte (20 de dano)")
            print("3 - Flecha (20 de dano)")
            escolha = input("Digite 1, 2 ou 3: ")

            if escolha == "1":
                dano = 10
                print(f"Você usou ataque básico causando {dano} de dano.")
            elif escolha == "2":
                dano = 20
                print(f"Você usou ataque forte causando {dano} de dano.")
            elif escolha == "3":
                dano = 20
                print(f"Você usou a flecha causando {dano} de dano.")
            else:
                print("Ataque inválido, tente novamente.")
                continue

            lacaio.vida -= dano
            if lacaio.vida <= 0:
                print(f"{lacaio.nome} derrotado!")
            else:
                print(f"Vida restante do {lacaio.nome}: {lacaio.vida}")

            # Link é imortal nessa luta tutorial, não perde vida
            pausa()

def interacao_npc_mentiroso(heroi):
    print("\nLink encontra um mercador estranho.")
    print("Mercador: 'Tenho uma poção poderosa que garante a vitória contra Ganon. Apenas 10 pontos de vida, aceita?'")
    escolha = input("Deseja comprar? (sim/não): ").strip().lower()
    if escolha == "sim":
        if heroi.vida > 10:
            heroi.vida -= 10
            heroi.itens['poção falsa'] = 1
            print("Você comprou a poção... mas parece que não tem efeito nenhum.")
        else:
            print("Vida insuficiente para comprar a poção.")
    else:
        print("Você recusou a oferta do mercador.")
    pausa()

def introducao_batalha_final():
    print("\nA batalha final se aproxima!")
    print("Link está pronto para enfrentar o poderoso Ganon e salvar a princesa Zelda.")
    pausa()

def batalha_final(heroi, vilao):
    print("\nBatalha final: Link vs Ganon!")
    while heroi.vida > 0 and vilao.vida > 0:
        print(f"\nVida de Link: {heroi.vida}")
        print(f"Vida de Ganon: {vilao.vida}")
        print("Escolha o ataque:")
        print("1 - Ataque básico (10 de dano)")
        print("2 - Ataque forte (20 de dano)")
        print("3 - Flecha (20 de dano)")
        print("4 - Usar poção")

        escolha = input("Digite 1, 2, 3 ou 4: ")

        if escolha == "1":
            dano = 10
            print(f"Você usou ataque básico causando {dano} de dano.")
            vilao.vida -= dano
        elif escolha == "2":
            dano = 20
            print(f"Você usou ataque forte causando {dano} de dano.")
            vilao.vida -= dano
        elif escolha == "3":
            dano = 20
            print(f"Você usou a flecha causando {dano} de dano.")
            vilao.vida -= dano
        elif escolha == "4":
            if heroi.itens.get('poção', 0) > 0:
                heroi.usar_pocao()
            else:
                print("Você não tem poções!")
                continue
        else:
            print("Opção inválida, tente novamente.")
            continue

        # Se Ganon ainda está vivo, ele ataca
        if vilao.vida > 0:
            vilao.ataque(heroi)
        pausa()

    if heroi.vida <= 0:
        print("\nLink foi derrotado... o reino de Hyrule caiu nas mãos do mal.")
        print("Fim de jogo.")
    else:
        print("\nGanon foi derrotado!")
        print("Link salva a princesa Zelda e traz a paz para Hyrule.")
        print("Parabéns, você venceu o jogo!")
    pausa()

def main():
    introducao()

    heroi = Heroi("Link", 30, 100, ataque=10, defesa=5)
    vilao_ganon = Vilao("Ganon", 45, 120, "Alta")

    mostrar_status(heroi)

    interacao_npc_bondoso(heroi)

    primeira_luta(heroi)

    interacao_npc_mentiroso(heroi)

    introducao_batalha_final()

    batalha_final(heroi, vilao_ganon)

if __name__ == "__main__":
    main()
