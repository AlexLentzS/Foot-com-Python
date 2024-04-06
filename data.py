import os
from tkinter import Tk, Toplevel, Label, Button, PhotoImage
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET

# Função para exibir informações da jogadora
def exibir_jogadora(player_nome, player_info, player_imagem_path):
    player_window = Toplevel()
    player_window.title(player_nome)

    # Adicione aqui as informações adicionais da jogadora, como habilidades e dados
    label_info = Label(player_window, text=player_info)
    label_info.pack()

    # Carregue e redimensione a imagem da jogadora para 100x100 pixels
    if os.path.isfile(player_imagem_path):
        player_imagem = Image.open(player_imagem_path)
        player_imagem.thumbnail((100, 100))
        player_imagem = ImageTk.PhotoImage(player_imagem)
        label_imagem = Label(player_window, image=player_imagem)
        label_imagem.image = player_imagem  # Evitar que a imagem seja coletada pelo garbage collector
        label_imagem.pack()

# Função para criar botões das jogadoras
def criar_botao(root, player_nome, player_info, player_imagem_path, posicao):
    x, y = posicao
    # Use uma função lambda para garantir que os valores atuais dos parâmetros sejam capturados
    return Button(root, text=player_nome, command=lambda nome=player_nome, info=player_info, imagem=player_imagem_path: exibir_jogadora(nome, info, imagem))

# Função para exibir os elencos
def exibir_elencos(xml_content):
    root = Tk()
    root.title("Elencos")

    # Configuração das colunas
    num_colunas = 8  # Número de colunas desejado
    largura_grupo = 11  # Número de jogadores por grupo

    for i in range(num_colunas):
        root.grid_columnconfigure(i, weight=1)

    for coluna_atual in range(num_colunas):
        team = xml_content.findall('.//team')[coluna_atual]

        for player_id, player in enumerate(team.findall('.//player')[:11]):
            player_nome = player.find('name').text
            player_info = f"Position: {player.find('position').text}\nAge: {player.find('age').text}\nNationality: {player.find('nationality').text}\nHeight: {player.find('height').text}"

            posicao_no_grupo = player_id % largura_grupo
            grupo = player_id // largura_grupo

            player_imagem_path = f"C:/Users/alexa/Desktop/foot/faces/{player_id + 1 + coluna_atual * largura_grupo}.png"

            # Ajuste das posições individuais X e Y para cada jogadora
            posicao_x = coluna_atual * 150  # Ajuste conforme necessário
            posicao_y = posicao_no_grupo * 50

            posicao = (posicao_x, posicao_y)

            btn = criar_botao(root, player_nome, player_info, player_imagem_path, posicao)
            btn.grid(row=posicao_no_grupo, column=coluna_atual, sticky="nsew", padx=5, pady=5)

    root.mainloop()
    
# Carrega o conteúdo XML
xml_string = '''
<root>    
    <team>
    <player id="1">
        <name>Yvonne Vogler</name>
        <position>Goleiro</position>
        <age>21 anos</age>
        <nationality>EUA</nationality>
        <height>1,72</height>
    </player>
    <player id="2">
        <name>Julie Paulet</name>
        <position>Defensor</position>
        <age>20 anos</age>
        <nationality>França</nationality>
        <height>1,55</height>
    </player>
    <player id="3">
        <name>Sayami Osada</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Japao</nationality>
        <height>1,70</height>
    </player>
    <player id="4">
        <name>Sophia Demsas</name>
        <position>Defensor</position>
        <age>30 anos</age>
        <nationality>Nigeria</nationality>
        <height>1,71</height>
    </player>
    <player id="5">
        <name>Helena Kerney</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>EUA</nationality>
        <height>1,67</height>
    </player>
    <player id="6">
        <name>Alisha Mitchell</name>
        <position>Meio Campo</position>
        <age>25 anos</age>
        <nationality>Escocia</nationality>
        <height>1,56</height>
    </player>
    <player id="7">
        <name>Natasha MacPherson</name>
        <position>Meio Campo</position>
        <age>19 anos</age>
        <nationality>Australia</nationality>
        <height>1,72</height>
    </player>
    <player id="8">
        <name>Shu Meng</name>
        <position>Meio Campo</position>
        <age>30 anos</age>
        <nationality>China</nationality>
        <height>1,70</height>
    </player>
    <player id="9">
        <name>Manuela Castro</name>
        <position>Atacante</position>
        <age>19 anos</age>
        <nationality>Brasil</nationality>
        <height>1,69</height>
    </player>
    <player id="10">
        <name>Xiao Peng</name>
        <position>Atacante</position>
        <age>32 anos</age>
        <nationality>China</nationality>
        <height>1,54</height>
    </player>
    <player id="11">
        <name>Jill Strom</name>
        <position>Atacante</position>
        <age>25 anos</age>
        <nationality>Suecia</nationality>
        <height>1,78</height>
    </player>
</team>
<team>
    <player id="12">
        <name>Karina Seleznyova</name>
        <position>Goleiro</position>
        <age>32 anos</age>
        <nationality>Rússia</nationality>
        <height>1,74</height>
    </player>
    <player id="13">
        <name>Marisa Pisani</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Italia</nationality>
        <height>1,74</height>
    </player>
    <player id="14">
        <name>Isabella Rossi</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Italia</nationality>
        <height>1,68</height>
    </player>
    <player id="15">
        <name>Mia Johnson</name>
        <position>Defensor</position>
        <age>22 anos</age>
        <nationality>EUA</nationality>
        <height>1,60</height>
    </player>
    <player id="16">
        <name>Sofia Hernandez</name>
        <position>Meio Campo</position>
        <age>20 anos</age>
        <nationality>Mexico</nationality>
        <height>1,75</height>
    </player>
    <player id="17">
        <name>Alessia Conti</name>
        <position>Meio Campo</position>
        <age>25 anos</age>
        <nationality>Italia</nationality>
        <height>1,72</height>
    </player>
    <player id="18">
        <name>Maria Rodriguez</name>
        <position>Meio Campo</position>
        <age>23 anos</age>
        <nationality>Argentina</nationality>
        <height>1,70</height>
    </player>
    <player id="19">
        <name>Nina Petrovic</name>
        <position>Meio Campo</position>
        <age>21 anos</age>
        <nationality>Servia</nationality>
        <height>1,72</height>
    </player>
    <player id="20">
        <name>Ana Silva</name>
        <position>Atacante</position>
        <age>24 anos</age>
        <nationality>Brasil</nationality>
        <height>1,75</height>
    </player>
    <player id="21">
        <name>Lena Muller</name>
        <position>Atacante</position>
        <age>27 anos</age>
        <nationality>Alemanha</nationality>
        <height>1,68</height>
    </player>
    <player id="22">
        <name>Camila Gonzalez</name>
        <position>Atacante</position>
        <age>23 anos</age>
        <nationality>Argentina</nationality>
        <height>1,70</height>
    </player>
</team>
<team>
    <player id="23">
        <name>Fernanda Alves</name>
        <position>Goleiro</position>
        <age>26 anos</age>
        <nationality>Brasil</nationality>
        <height>1,78</height>
    </player>
    <player id="24">
        <name>Luisa Santos</name>
        <position>Defensor</position>
        <age>24 anos</age>
        <nationality>Portugal</nationality>
        <height>1,70</height>
    </player>
    <player id="25">
        <name>Emily Taylor</name>
        <position>Defensor</position>
        <age>22 anos</age>
        <nationality>Inglaterra</nationality>
        <height>1,68</height>
    </player>
    <player id="26">
        <name>Marta Fernandez</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Espanha</nationality>
        <height>1,73</height>
    </player>
    <player id="27">
        <name>Camila Oliveira</name>
        <position>Defensor</position>
        <age>25 anos</age>
        <nationality>Brasil</nationality>
        <height>1,75</height>
    </player>
    <player id="28">
        <name>Isabela Santos</name>
        <position>Meio Campo</position>
        <age>23 anos</age>
        <nationality>Brasil</nationality>
        <height>1,68</height>
    </player>
    <player id="29">
        <name>Ana Kim</name>
        <position>Meio Campo</position>
        <age>26 anos</age>
        <nationality>Coreia do Sul</nationality>
        <height>1,62</height>
    </player>
    <player id="30">
        <name>Larissa Rossi</name>
        <position>Meio Campo</position>
        <age>24 anos</age>
        <nationality>Italia</nationality>
        <height>1,73</height>
    </player>
    <player id="31">
        <name>Carolina Santos</name>
        <position>Atacante</position>
        <age>27 anos</age>
        <nationality>Brasil</nationality>
        <height>1,68</height>
    </player>
    <player id="32">
        <name>Emma Williams</name>
        <position>Atacante</position>
        <age>24 anos</age>
        <nationality>Inglaterra</nationality>
        <height>1,65</height>
    </player>
    <player id="33">
        <name>Maria Fernandez</name>
        <position>Atacante</position>
        <age>22 anos</age>
        <nationality>Espanha</nationality>
        <height>1,60</height>
     </player>
</team>
<team>
    <player id="34">
        <name>Gabriela Oliveira</name>
        <position>Goleiro</position>
        <age>24 anos</age>
        <nationality>Brasil</nationality>
        <height>1,75</height>
    </player>
    <player id="35">
        <name>Ana Garcia</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Espanha</nationality>
        <height>1,72</height>
    </player>
    <player id="36">
        <name>Leticia Martinez</name>
        <position>Defensor</position>
        <age>23 anos</age>
        <nationality>Argentina</nationality>
        <height>1,68</height>
    </player>
    <player id="37">
        <name>Maria Silva</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Brasil</nationality>
        <height>1,73</height>
    </player>
    <player id="38">
        <name>Carla Ferreira</name>
        <position>Defensor</position>
        <age>25 anos</age>
        <nationality>Brasil</nationality>
        <height>1,65</height>
    </player>
    <player id="39">
        <name>Emma Opia</name>
        <position>Meio Campo</position>
        <age>18 anos</age>
        <nationality>EUA</nationality>
        <height>1,50</height>
    </player>
    <player id="40">
        <name>Sofia Perez</name>
        <position>Meio Campo</position>
        <age>22 anos</age>
        <nationality>Espanha</nationality>
        <height>1,60</height>
    </player>
    <player id="41">
        <name>Isabel Rodriguez</name>
        <position>Meio Campo</position>
        <age>27 anos</age>
        <nationality>Espanha</nationality>
        <height>1,70</height>
    </player>
    <player id="42">
        <name>Lara Santos</name>
        <position>Atacante</position>
        <age>23 anos</age>
        <nationality>Brasil</nationality>
        <height>1,68</height>
    </player>
    <player id="43">
        <name>Kaitlyn Johnson</name>
        <position>Atacante</position>
        <age>25 anos</age>
        <nationality>EUA</nationality>
        <height>1,65</height>
    </player>
    <player id="44">
        <name>Mia Kim</name>
        <position>Atacante</position>
        <age>21 anos</age>
        <nationality>Coreia do Sul</nationality>
        <height>1,62</height>
    </player>
</team>
<team>
    <player id="45">
        <name>Ling Wei</name>
        <position>Goleiro</position>
        <age>26 anos</age>
        <nationality>China</nationality>
        <height>1,72</height>
    </player>
    <player id="46">
        <name>Juliana Oliveira</name>
        <position>Defensor</position>
        <age>27 anos</age>
        <nationality>Brasil</nationality>
        <height>1,70</height>
    </player>
    <player id="47">
        <name>Nicole Perez</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Argentina</nationality>
        <height>1,78</height>
    </player>
    <player id="48">
        <name>Larissa Santos</name>
        <position>Defensor</position>
        <age>24 anos</age>
        <nationality>Brasil</nationality>
        <height>1,73</height>
    </player>
    <player id="49">
        <name>Maxime Dubois</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Canadá</nationality>
        <height>1,75</height>
    </player>
    <player id="50">
        <name>Chika Onyeka</name>
        <position>Meio Campo</position>
        <age>25 anos</age>
        <nationality>Nigéria</nationality>
        <height>1,70</height>
    </player>
    <player id="51">
        <name>Gabriela Silva</name>
        <position>Meio Campo</position>
        <age>26 anos</age>
        <nationality>Brasil</nationality>
        <height>1,65</height>
    </player>
    <player id="52">
        <name>Amara Bangura</name>
        <position>Meio Campo</position>
        <age>23 anos</age>
        <nationality>Serra Leoa</nationality>
        <height>1,72</height>
    </player>
    <player id="53">
        <name>Lina Chen</name>
        <position>Atacante</position>
        <age>22 anos</age>
        <nationality>China</nationality>
        <height>1,63</height>
    </player>
    <player id="54">
        <name>Zara Al-Farsi</name>
        <position>Atacante</position>
        <age>21 anos</age>
        <nationality>Omã</nationality>
        <height>1,60</height>
    </player>
    <player id="55">
        <name>Bianca Schröder</name>
        <position>Atacante</position>
        <age>24 anos</age>
        <nationality>Alemanha</nationality>
        <height>1,75</height>
    </player>
</team>
<team>
    <player id="56">
        <name>Mia Park</name>
        <position>Goleiro</position>
        <age>27 anos</age>
        <nationality>Coreia do Sul</nationality>
        <height>1,78</height>
    </player>
    <player id="57">
        <name>Isabella Lopez</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Espanha</nationality>
        <height>1,72</height>
    </player>
    <player id="58">
        <name>Rafaela Silva</name>
        <position>Defensor</position>
        <age>23 anos</age>
        <nationality>Brasil</nationality>
        <height>1,69</height>
    </player>
    <player id="59">
        <name>Yuki Tanaka</name>
        <position>Defensor</position>
        <age>25 anos</age>
        <nationality>Japão</nationality>
        <height>1,67</height>
    </player>
    <player id="60">
        <name>Chiara Rossi</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Itália</nationality>
        <height>1,74</height>
    </player>
    <player id="61">
        <name>Aisha Ibrahim</name>
        <position>Meio Campo</position>
        <age>24 anos</age>
        <nationality>Africa do Sul</nationality>
        <height>1,68</height>
    </player>
    <player id="62">
        <name>Fatima Al-Hassan</name>
        <position>Meio Campo</position>
        <age>26 anos</age>
        <nationality>Arábia Saudita</nationality>
        <height>1,67</height>
    </player>
    <player id="63">
        <name>Sofia Ivanova</name>
        <position>Meio Campo</position>
        <age>24 anos</age>
        <nationality>Cazaquistão</nationality>
        <height>1,68</height>
    </player>
    <player id="64">
        <name>Haruka Suzuki</name>
        <position>Atacante</position>
        <age>23 anos</age>
        <nationality>Japão</nationality>
        <height>1,63</height>
    </player>
    <player id="65">
        <name>Juliana Costa</name>
        <position>Atacante</position>
        <age>25 anos</age>
        <nationality>Brasil</nationality>
        <height>1,70</height>
    </player>
    <player id="66">
        <name>Anna Becker</name>
        <position>Atacante</position>
        <age>25 anos</age>
        <nationality>Alemanha</nationality>
        <height>1,70</height>
    </player>
</team>
<team>
    <player id="67">
        <name>Lena Kovalenko</name>
        <position>Goleiro</position>
        <age>28 anos</age>
        <nationality>Rússia</nationality>
        <height>1,75</height>
    </player>
    <player id="68">
        <name>Valentina Costa</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Brasil</nationality>
        <height>1,72</height>
    </player>
    <player id="69">
        <name>Kaori Tanaka</name>
        <position>Defensor</position>
        <age>24 anos</age>
        <nationality>Japão</nationality>
        <height>1,68</height>
    </player>
    <player id="70">
        <name>Isabel Fernandez</name>
        <position>Defensor</position>
        <age>27 anos</age>
        <nationality>Espanha</nationality>
        <height>1,74</height>
    </player>
    <player id="71">
        <name>Eleni Papadopoulos</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Grécia</nationality>
        <height>1,78</height>
    </player>
    <player id="72">
        <name>Sakura Nakamura</name>
        <position>Meio Campo</position>
        <age>26 anos</age>
        <nationality>Japão</nationality>
        <height>1,68</height>
    </player>
    <player id="73">
        <name>Isabella Lentz</name>
        <position>Meio Campo</position>
        <age>25 anos</age>
        <nationality>Austria</nationality>
        <height>1,75</height>
    </player>
    <player id="74">
        <name>Nina Petrova</name>
        <position>Meio Campo</position>
        <age>23 anos</age>
        <nationality>Rússia</nationality>
        <height>1,72</height>
    </player>
    <player id="75">
        <name>Maya Silva</name>
        <position>Atacante</position>
        <age>23 anos</age>
        <nationality>Brasil</nationality>
        <height>1,70</height>
    </player>
    <player id="76">
        <name>Lee Ji-eun</name>
        <position>Atacante</position>
        <age>24 anos</age>
        <nationality>Coreia do Sul</nationality>
        <height>1,68</height>
    </player>
    <player id="77">
        <name>Aria Nguyen</name>
        <position>Atacante</position>
        <age>26 anos</age>
        <nationality>Vietnã</nationality>
        <height>1,65</height>
    </player>
</team>
<team>
    <player id="78">
        <name>Anastasia Ivanova</name>
        <position>Goleiro</position>
        <age>29 anos</age>
        <nationality>Rússia</nationality>
        <height>1,80</height>
    </player>
    <player id="79">
        <name>Grace White</name>
        <position>Defensor</position>
        <age>28 anos</age>
        <nationality>Inglaterra</nationality>
        <height>1,73</height>
    </player>
    <player id="80">
        <name>Lara Müller</name>
        <position>Defensor</position>
        <age>25 anos</age>
        <nationality>Alemanha</nationality>
        <height>1,75</height>
    </player>
    <player id="87">
        <name>Valeria Rossi</name>
        <position>Defensor</position>
        <age>27 anos</age>
        <nationality>Itália</nationality>
        <height>1,68</height>
    </player>
    <player id="82">
        <name>Maria Fernández</name>
        <position>Defensor</position>
        <age>26 anos</age>
        <nationality>Espanha</nationality>
        <height>1,74</height>
    </player>
    <player id="83">
        <name>Olivia Martinez</name>
        <position>Meio Campo</position>
        <age>27 anos</age>
        <nationality>Espanha</nationality>
        <height>1,72</height>
    </player>
    <player id="84">
        <name>Amelia Johnson</name>
        <position>Meio Campo</position>
        <age>26 anos</age>
        <nationality>Inglaterra</nationality>
        <height>1,68</height>
    </player>
    <player id="85">
        <name>Katarina Müller</name>
        <position>Meio Campo</position>
        <age>29 anos</age>
        <nationality>Alemanha</nationality>
        <height>1,75</height>
    </player>
    <player id="86">
        <name>Isabella Santos</name>
        <position>Atacante</position>
        <age>24 anos</age>
        <nationality>Brasil</nationality>
        <height>1,70</height>
    </player>
    <player id="87">
        <name>Lena Petrov</name>
        <position>Atacante</position>
        <age>25 anos</age>
        <nationality>Rússia</nationality>
        <height>1,65</height>
    </player>
    <player id="88">
        <name>Lea Dubois</name>
        <position>Atacante</position>
        <age>26 anos</age>
        <nationality>França</nationality>
        <height>1,68</height>
    </player>
    </team>
</root>  
'''
xml_content = ET.fromstring(xml_string)
exibir_elencos(xml_content)
