import random

class Torneio:
    def __init__(self, equipes):
        self.equipes = equipes
        self.pontuacao = {equipe: 0 for equipe in equipes}
        self.classificados = []

    def simular_partida(self, equipe1, equipe2):
        # Lógica para simular uma partida entre duas equipes
        # Atualize a pontuação com base no resultado da partida
        resultado = random.choice(['vitoria', 'empate', 'derrota'])
        if resultado == 'vitoria':
            self.pontuacao[equipe1] += 3
        elif resultado == 'empate':
            self.pontuacao[equipe1] += 1
            self.pontuacao[equipe2] += 1
        else:
            self.pontuacao[equipe2] += 3

    def simular_grupo(self, grupo):
        # Lógica para simular todos os jogos de um grupo
        equipes_grupo = self.equipes[grupo * 6: (grupo + 1) * 6]
        for i in range(len(equipes_grupo)):
            for j in range(i + 1, len(equipes_grupo)):
                self.simular_partida(equipes_grupo[i], equipes_grupo[j])

    def simular_fase_de_grupos(self):
        # Lógica para simular a fase de grupos do torneio
        for grupo in range(2):
            self.simular_grupo(grupo)
        
        # Classificar equipes para a próxima fase
        classificados_grupo1 = sorted(self.equipes[:6], key=lambda equipe: self.pontuacao[equipe], reverse=True)
        classificados_grupo2 = sorted(self.equipes[6:], key=lambda equipe: self.pontuacao[equipe], reverse=True)
        self.classificados = classificados_grupo1[:4] + classificados_grupo2[:4]

    def simular_quartas_de_final(self):
        # Lógica para simular as quartas de final
        random.shuffle(self.classificados)  # Embaralhar a ordem dos classificados
        confrontos = [(self.classificados[i], self.classificados[7 - i]) for i in range(4)]
        
        for confronto in confrontos:
            self.simular_partida(confronto[0], confronto[1])

    def simular_semi_finais(self):
        # Lógica para simular as semifinais
        confrontos = [
            (self.classificados[0], self.classificados[3]),
            (self.classificados[1], self.classificados[2]),
        ]

        for confronto in confrontos:
            self.simular_partida(confronto[0], confronto[1])

    def simular_final(self):
        # Lógica para simular a final
        self.simular_partida(self.classificados[0], self.classificados[1])

    def obter_campeao(self):
        # Retorna o campeão do torneio com base na pontuação final
        return max(self.classificados, key=lambda equipe: self.pontuacao[equipe])
