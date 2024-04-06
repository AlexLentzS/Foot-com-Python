import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import os

pygame.init()  # Inicialize o módulo pygame

# Obtém o caminho do diretório do script Python
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construa o caminho absoluto para os outros sons
gol_sound = pygame.mixer.Sound(os.path.join(script_dir, "assets", "gol.mp3"))
estadio_sound = pygame.mixer.Sound(os.path.join(script_dir, "assets", "estadio.mp3"))

# Carregue os sons
gol_sound = pygame.mixer.Sound(os.path.join(script_dir, "assets", "gol.mp3"))
estadio_sound = pygame.mixer.Sound(os.path.join(script_dir, "assets", "estadio.mp3"))

class Equipe:
    def __init__(self, nome, ataque, defesa, estrategia, tatica=None):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.estrategia = estrategia
        self.tatica = tatica

class Partida:
    def __init__(self, equipe1, equipe2, label_placar, label_tempo):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.tempo_decorrido = 0
        self.placar = {equipe1.nome: 0, equipe2.nome: 0}
        self.label_placar = label_placar
        self.label_tempo = label_tempo

        # Inicializar a tática do time adversário
        print(f"Time adversário: {equipe2.nome} - Tática: {equipe2.tatica}")

    def iniciar_partida(self):
        estadio_sound.play()  # Reproduza o som do estádio
        self.label_tempo.config(text=f"Tempo: {self.tempo_decorrido}'")
        self.atualizar_placar()
        self.simular_partida()

    def atualizar_placar(self):
        self.label_placar.config(text=f"{self.placar[self.equipe1.nome]} - {self.placar[self.equipe2.nome]}")
        self.label_placar.update_idletasks()

    def simular_partida(self):
        if self.tempo_decorrido < 90:
            if random.random() < 1.0:  # Probabilidade de 100% de ocorrer um gol
                if random.choice([True, False]):  # Escolha aleatória do time que marcará o gol
                    self.marcar_gol(self.equipe1)
                else:
                    self.marcar_gol(self.equipe2)
            self.tempo_decorrido += 1
            self.label_tempo.config(text=f"Tempo: {self.tempo_decorrido}'")
            self.atualizar_placar()  # Mova a chamada para atualizar_placar aqui
            self.label_tempo.update_idletasks()
            self.label_placar.after(1000, self.simular_partida)
        else:
            print("Fim do jogo!")

    def marcar_gol(self, equipe):
        impacto_estrategia = random.uniform(0.5, 1.5)
        gol_estrategia = random.random()

        if gol_estrategia < 0.05:
            self.placar[equipe.nome] += int(1 * impacto_estrategia)
            print(f"Gol marcado por {equipe.nome} - Tática: {equipe.tatica}")
            gol_sound.play()  # Reproduza o som de gol
            self.atualizar_placar() 

def criar_janela_placar(equipe1, equipe2):
    root = tk.Toplevel()
    root.title("Placar")
    largura, altura = 800, 400
    root.geometry(f"{largura}x{altura}")

    # Adicionar o logo das equipes
    imagem_logo_e1 = Image.open(f"assets/{equipe1.nome.lower()}.png")
    imagem_logo_e2 = Image.open(f"assets/{equipe2.nome.lower()}.png")
    imagem_logo_e1 = imagem_logo_e1.resize((120, 120))
    imagem_logo_e2 = imagem_logo_e2.resize((120, 120))
    imagem_logo_e1_tk = ImageTk.PhotoImage(imagem_logo_e1)
    imagem_logo_e2_tk = ImageTk.PhotoImage(imagem_logo_e2)

    label_logo_e1 = tk.Label(root, image=imagem_logo_e1_tk)
    label_logo_e1.image = imagem_logo_e1_tk
    label_logo_e1.grid(row=0, column=0)

    label_e1 = tk.Label(root, text=equipe1.nome)
    label_e1.grid(row=0, column=1)

    label_placar = tk.Label(root, text="0 - 0")
    label_placar.grid(row=0, column=2)

    label_logo_e2 = tk.Label(root, image=imagem_logo_e2_tk)
    label_logo_e2.image = imagem_logo_e2_tk
    label_logo_e2.grid(row=0, column=3)

    label_e2 = tk.Label(root, text=equipe2.nome)
    label_e2.grid(row=0, column=4)

    label_tempo = tk.Label(root, text="Tempo: 0'")
    label_tempo.grid(row=1, column=2)

    return root, label_placar, label_tempo

def click_select_team(equipe_nome):
    equipes = {
        "Reds": Equipe("Reds", 3, 3, 3),
        "Blues": Equipe("Blues", 3.5, 3.5, 3.5),
        "Greens": Equipe("Greens", 4, 4, 4),
        "Yellows": Equipe("Yellows", 4.5, 4.5, 4.5),
        "Oranges": Equipe("Oranges", 5, 5, 5),
        "Pinks": Equipe("Pinks", 3.8, 3.2, 4),
        "Purples": Equipe("Purples", 4.2, 3.8, 4.2),
        "Whites": Equipe("Whites", 4, 4, 4.5),
        "Blacks": Equipe("Blacks", 4.5, 4.5, 4.5),
        "Greys": Equipe("Greys", 3.5, 4, 3.5),
        "Browns": Equipe("Browns", 3.2, 3, 3.5),
        "Navys": Equipe("Navys", 4, 3.5, 4),
    }

    equipe_selecionada = equipes.get(equipe_nome)
    
    if equipe_selecionada:
        print(f"Equipe selecionada: {equipe_selecionada.nome}")
    else:
        print(f"Equipe '{equipe_nome}' não encontrada.")

    # Criar a janela de seleção de táticas
    janela_taticas = tk.Toplevel()
    janela_taticas.title("Seleção de Táticas")

    # Adicionar o fundo de imagem para a tela de seleção de táticas
    imagem_fundo_selecao = Image.open(f"assets/{equipe_selecionada.nome.lower()}_wall.png")
    largura_fundo, altura_fundo = imagem_fundo_selecao.size
    frame_fundo = tk.Frame(janela_taticas, width=largura_fundo, height=altura_fundo)
    frame_fundo.pack()
    imagem_fundo_selecao = ImageTk.PhotoImage(imagem_fundo_selecao)
    label_fundo_selecao = tk.Label(frame_fundo, image=imagem_fundo_selecao)
    label_fundo_selecao.image = imagem_fundo_selecao
    label_fundo_selecao.pack()

    # Adicionar miniatura da equipe selecionada
    imagem_miniatura = Image.open(f"assets/{equipe_selecionada.nome.lower()}2.png")
    imagem_miniatura = imagem_miniatura.resize((120, 120))
    imagem_miniatura_tk = ImageTk.PhotoImage(imagem_miniatura)
    label_miniatura = tk.Label(frame_fundo, image=imagem_miniatura_tk)
    label_miniatura.image = imagem_miniatura_tk
    label_miniatura.place(x=50, y=50)

    # Adicionar botões de tática
    botao_tatica_433 = tk.Button(frame_fundo, text="4-3-3", command=lambda: click_select_tactic(equipe_selecionada, "4-3-3"))
    botao_tatica_433.place(x=220, y=90)
    botao_tatica_442 = tk.Button(frame_fundo, text="4-4-2", command=lambda: click_select_tactic(equipe_selecionada, "4-4-2"))
    botao_tatica_442.place(x=200, y=50)
    botao_tatica_4231 = tk.Button(frame_fundo, text="4-2-3-1", command=lambda: click_select_tactic(equipe_selecionada, "4-2-3-1"))
    botao_tatica_4231.place(x=270, y=90)
    botao_tatica_532 = tk.Button(frame_fundo, text="5-3-2", command=lambda: click_select_tactic(equipe_selecionada, "5-3-2"))
    botao_tatica_532.place(x=250, y=50)
    botao_tatica_4132 = tk.Button(frame_fundo, text="4-1-3-2", command=lambda: click_select_tactic(equipe_selecionada, "4-1-3-2"))
    botao_tatica_4132.place(x=300, y=50)
    botao_tatica_4321 = tk.Button(frame_fundo, text="4-3-2-1", command=lambda: click_select_tactic(equipe_selecionada, "4-3-2-1"))
    botao_tatica_4321.place(x=370, y=50)
    botao_tatica_451 = tk.Button(frame_fundo, text="4-5-1", command=lambda: click_select_tactic(equipe_selecionada, "4-5-1"))
    botao_tatica_451.place(x=320, y=50)
    botao_tatica_352 = tk.Button(frame_fundo, text="3-5-2", command=lambda: click_select_tactic(equipe_selecionada, "3-5-2"))
    botao_tatica_352.place(x=330, y=90)
    botao_tatica_433 = tk.Button(frame_fundo, text="4-3-3", command=lambda: click_select_tactic(equipe_selecionada, "4-3-3"))
    botao_tatica_433.place(x=450, y=50)
    botao_tatica_442_diamond = tk.Button(frame_fundo, text="4-4-2 Diamond", command=lambda: click_select_tactic(equipe_selecionada, "4-4-2 Diamond"))
    botao_tatica_442_diamond.place(x=420, y=90)
    botao_tatica_343 = tk.Button(frame_fundo, text="3-4-3", command=lambda: click_select_tactic(equipe_selecionada, "3-4-3"))
    botao_tatica_343.place(x=375, y=90)
    botao_tatica_532 = tk.Button(frame_fundo, text="5-3-2", command=lambda: click_select_tactic(equipe_selecionada, "5-3-2"))
    botao_tatica_532.place(x=520, y=90)

def click_select_tactic(equipe, tatica):
    print(f"Tática selecionada para a equipe {equipe.nome}: {tatica}")
    equipe.tatica = tatica  # Atribuir a tática escolhida à equipe

    # Selecionar um time aleatório como adversário
    equipes_disponiveis = ["Reds", "Blues", "Greens", "Yellows", "Oranges", "Pinks", "Purples", "Whites",
                     "Blacks", "Greys", "Browns", "Navys"]
    equipes_disponiveis.remove(equipe.nome)  # Remover a equipe selecionada para evitar repetição
    adversario_nome = random.choice(equipes_disponiveis)
    adversario_tatica = random.choice(["4-3-3", "4-4-2", "4-2-3-1", "5-3-2", "4-1-3-2", "4-3-2-1"])
    adversario = Equipe(adversario_nome, 3, 3, 3, adversario_tatica)

    janela_placar, label_placar, label_tempo = criar_janela_placar(equipe, adversario)
    partida = Partida(equipe, adversario, label_placar, label_tempo)
    partida.iniciar_partida()

def click_new_game():
    nova_janela = tk.Toplevel()
    nova_janela.title("Seleção de Equipe")

    nomes_equipes = ["Reds", "Blues", "Greens", "Yellows", "Oranges", "Pinks", "Purples", "Whites",
                     "Blacks", "Greys", "Browns", "Navys"]
    for i, nome in enumerate(nomes_equipes):
        # Adicione um botão para cada equipe na tela de seleção
        imagem_logo = Image.open(f"assets/{nome.lower()}.png")
        imagem_logo = imagem_logo.resize((120, 120))
        imagem_logo_tk = ImageTk.PhotoImage(imagem_logo)

        botao_equipe = tk.Button(nova_janela, image=imagem_logo_tk, command=lambda n=nome: click_select_team(n))
        botao_equipe.image = imagem_logo_tk
        botao_equipe.grid(row=i // 4, column=i % 4, padx=10, pady=10)

    botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    botao_fechar.grid(row=len(nomes_equipes) // 4 + 1, column=0, columnspan=4, pady=10)

def click_load_game():
    print("Load Game button clicked")

def exibir_menu_com_imagem():
    def click_quit_game():
        print("Quit button clicked")
        root.destroy()  # Use destroy() para fechar a janela principal

    root = tk.Tk()
    root.title("Menu")
    imagem_fundo = Image.open("assets/menu.png")
    largura, altura = imagem_fundo.size
    frame = tk.Frame(root, width=largura, height=altura)
    frame.pack()
    imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
    label_fundo = tk.Label(frame, image=imagem_fundo)
    label_fundo.image = imagem_fundo
    label_fundo.pack()
    imagem_new_game = Image.open("assets/newgame.png")
    imagem_load_game = Image.open("assets/loadgame.png")
    imagem_quit_game = Image.open("assets/quitgame.png")
    imagem_new_game = ImageTk.PhotoImage(imagem_new_game)
    imagem_load_game = ImageTk.PhotoImage(imagem_load_game)
    imagem_quit_game = ImageTk.PhotoImage(imagem_quit_game)
    button_new_game = tk.Button(frame, image=imagem_new_game, command=click_new_game, borderwidth=0)
    button_new_game.place(x=150, y=450)
    button_load_game = tk.Button(frame, image=imagem_load_game, command=click_load_game, borderwidth=0)
    button_load_game.place(x=450, y=450)

    # Conectar o botão "Quit Game" à função click_quit_game
    button_quit_game = tk.Button(frame, image=imagem_quit_game, command=click_quit_game, borderwidth=0)
    button_quit_game.place(x=750, y=450)

    root.mainloop()

# Exibir o menu inicial
exibir_menu_com_imagem()
