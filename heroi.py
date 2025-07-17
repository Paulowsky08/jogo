from personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, idade, vida, ataque=10, defesa=5):
        super().__init__(nome, idade, vida)
        self.ataque = ataque
        self.defesa = defesa
        self.itens = {"poção": 1}

    def usar_pocao(self):
        if self.itens["poção"] > 0:
            self.vida += 30
            self.itens["poção"] -= 1
            print(f"{self.nome} usou uma poção e recuperou 30 de vida! Vida atual: {self.vida}")
        else:
            print(f"{self.nome} não tem poções para usar!")

    def atacar(self, alvo, tipo_ataque):
        if tipo_ataque == "basico":
            dano = 10
            print(f"{self.nome} usou golpe básico. Causou 10 de dano. (Consistente, mas fraco)")
        elif tipo_ataque == "forte":
            dano = 20
            print(f"{self.nome} usou golpe forte. Causou 20 de dano. (Forte, mas arriscado)")
        elif tipo_ataque == "flecha":
            dano = 20
            print(f"{self.nome} usou flecha. Causou 20 de dano. (Rápido, mas consome recursos)")
        else:
            print("Ataque inválido.")
            return

        dano_final = max(0, dano - getattr(alvo, "defesa", 0))
        alvo.vida -= dano_final
        print(f"Vida de {alvo.nome} após ataque: {alvo.vida}")

    def dialogar(self, texto):
        print(f"{self.nome} diz: {texto}")
