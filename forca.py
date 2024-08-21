"""Programa que simula um jogo da forca"""

# pylint: disable=c0103, r0912

# Imports Gerais
from random import choice
from estilo import limpaTela, l, msgAnimada, valorInvalido


def boneco(contador):

    """Função que Monta um boneco na Tela"""

    if contador == 0:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                    |
                    |     """, ANIMACAO, "", 0.018)


        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 1:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
                    |     """, ANIMACAO, "", 0.018)

        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 2:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
                |   |     """, ANIMACAO, "", 0.018)

        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 3:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|   |     """, ANIMACAO, "", 0.018)

        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 4:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\\  |     """, ANIMACAO, "", 0.018)

        #Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        #Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        #2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 5:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\\  |     """, ANIMACAO, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        #Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")


        #2ª perte do desenho da forca
        msgAnimada("""
               /    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 6:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\\  |     """, ANIMACAO, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        #Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")


        #2ª perte do desenho da forca
        msgAnimada("""
               / \\  |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)


# Contantes
TAM = 40

# Variáveis globais
ANIMACAO = True
TEMPO = 0.02

# Definindo as palavras
palavras = {
    "alimentos":
    ["Pizza", "Pão", "Arroz", "Frango", "Sopa", "Bolo", "Queijo",
    "Maçã", "Batata", "Peixe", "Manga", "Torta", "Uva", "Cereal",
    "Milho", "Carne", "Salada", "Feijão", "Banana", "Melancia", "Ovo",
    "Cenoura", "Morango", "Abacate", "Laranja", "Tomate", "Coco", "Melão",
    "Biscoito", "Iogurte", "Macarrão", "Abobrinha", "Pimenta", "Pêra",
    "Alface", "Berinjela", "Espinafre", "Azeitona", "Brócolis", "Castanha",
    "Noz", "Amendoim", "Batata-doce", "Granola", "Açúcar", "Mel", "Goiaba",
    "Lentilha", "Rabanete", "Couve"],
    "sentimentos":
    ["amigo", "futuro", "coragem", "felicidade", "alegria", "esperança",
    "amizade", "sabedoria", "liberdade", "saudade", "aventura", "carinho",
    "honestidade", "solidariedade", "justiça", "confiança", "RESPeito",
    "gentileza", "humildade", "empatia", "persistência", "gratidao",
    "determinação", "integridade", "paciência", "resiliência", "criatividade",
    "inspiração", "equilíbrio", "tranquilidade", "sabedoria", "generosidade",
    "compaixão", "tolerância", "serenidade", "fidelidade", "otimismo",
    "entusiasmo", "prudência", "temperança", "lealdade", "altruísmo",
    "compromisso", "serenidade", "honra", "dignidade", "coragem", "valentia",
    "liderança", "vigilância", "disciplina", "versatilidade", "sabedoria",
    "imparcialidade", "decisão", "criatividade", "dedicação", "zelo",
    "firmeza", "confiança", "Respeito", "sabedoria", "amizade", "esperança"],
    "games":
    ["Super Mario", "The Legend of Zelda", "Minecraft", "Fortnite", "Call of Duty",
    "Overwatch", "The Witcher", "Red Dead Redemption", "Grand Theft Auto", "Halo",
    "Assassin's Creed", "FIFA", "League of Legends", "Valorant","Cyberpunk 2077",
    "Dark Souls", "Elden Ring", "Animal Crossing", "Pokémon", "Metroid", "Tetris",
    "Street Fighter", "Mortal Kombat", "Tekken", "Resident Evil", "Silent Hill",
    "Bloodborne", "Horizon Zero Dawn", "God of War", "Uncharted", "Tomb Raider",
    "Final Fantasy", "Dragon Quest", "World of Warcraft", "Starcraft", "Diablo",
    "The Sims", "SimCity", "Fallout", "Mass Effect", "Half-Life", "Dota 2",
    "Counter-Strike", "Portal", "Apex Legends", "Rocket League", "PUBG", "Among Us",
    "Celeste", "Stardew Valley", "Terraria", "Hades", "Undertale", "Bioshock",
    "Gears of War", "Borderlands", "Far Cry", "Splatoon", "Destiny"],
    "instrumentos":
    ["Guitarra", "Piano", "Violino", "Bateria", "Baixo", "Flauta", "Trompete",
    "Saxofone", "Clarinete", "Violoncelo", "Harpa", "Oboé", "Trombone", "Acordeão",
    "Banjo", "Bandolim", "Ukulele", "Sintetizador", "Xilofone", "Harmônica", "Gaita de fole",
    "Tímpano", "Marimba", "Conga", "Bongo", "Pandeiro", "Djembe", "Cajón",
    "Flauta doce", "Órgão", "Fagote", "Piccolo", "Lira", "Triângulo", "Metalofone",
    "Pratos", "Sitar", "Alaúde", "Rabeca", "Didgeridoo", "Flautas de pã", "Vibrafone",
    "Clavicórdio", "Melódica", "Cítara", "Balalaica", "Kalimba", "Koto", "Tambura",
    "Viola", "Maracas", "Tuba", "Eufônio", "Caixa", "Sinos", "Bumbo",
    "Steel drum", "Handpan", "Ocarina"],
    "filmes":
    ["Titanic", "A Origem", "Avatar", "O Poderoso Chefão", "Pulp Fiction", "O Cavaleiro das Trevas",
    "Forrest Gump", "Clube da Luta", "Matrix", "Gladiador", "Jurassic Park",
    "Um Sonho de Liberdade", "Star Wars", "O Senhor dos Anéis", "Interestelar", "Os Vingadores",
    "De Volta para o Futuro", "O Rei Leão", "A Lista de Schindler", "O Silêncio dos Inocentes",
    "O Resgate do Soldado Ryan", "Alien", "O Exterminador do Futuro", "Coração Valente",
    "Indiana Jones", "Os Bons Companheiros", "Casablanca", "Os Suspeitos", "Tubarão", "Rocky",
    "E.T. - O Extraterrestre", "O Iluminado", "Scarface", "O Sexto Sentido",
    "Seven: Os Sete Crimes Capitais", "Coringa", "Piratas do Caribe", "Vingadores: Ultimato",
    "Harry Potter", "Capitão América", "Pantera Negra", "O Homem de Ferro", "O Hobbit",
    "Guardiões da Galáxia", "O Lobo de Wall Street", "Django Livre", "O Grande Gatsby",
    "A Origem dos Guardiões", "O Código Da Vinci", "Missão Impossível", "Os Incríveis",
    "Homem-Aranha", "Thor: Ragnarok", "Jurassic World", "Os Oito Odiados", "A Bela e a Fera"]

}


# Temas disponíveis
temasPossiveis = ["alimentos", "sentimentos", "games", "instrumentos", "filmes"]

# Mostrando menus
TEMAS = MAINTITLE = True


while True:

    # Mostrar erros
    letrasUsadas = []

    # Resetando as letras
    LETRA = ""
    C = PRIMEIROERRO = 0

    # Gerando a frase completa
    frase = []

    while True:

        # ---------------------------------------------------------------------------

        # Adicionando tema
        if TEMAS:
            while True:

                # Título de apresentação
                if MAINTITLE:
                    limpaTela()
                    l("——")
                    msgAnimada(f"{'Jogo da Forca':^{TAM}}", ANIMACAO)
                    l("——")
                    msgAnimada("Escolha um tema abaixo:", ANIMACAO)
                    l("——")
                else:
                    limpaTela()
                    l("——")
                    msgAnimada("Escolha um outro tema abaixo:", ANIMACAO)
                    l("——")

                # Escolhendo as categorias
                msgAnimada("1 - Alimentos", ANIMACAO)
                msgAnimada("2 - Sentimentos", ANIMACAO)
                msgAnimada("3 - Games", ANIMACAO)
                msgAnimada("4 - Instrumentos", ANIMACAO)
                msgAnimada("5 - Filmes", ANIMACAO)
                l("——")

                # Pegando o tema que o usuário escolheu
                msgAnimada("Sua escolha: ", ANIMACAO, "")

                try:
                    TEMA = str(input())
                    TEMA = int(TEMA)

                except ValueError:
                    valorInvalido("Digita apenas números", "——")
                    limpaTela()
                    ANIMACAO = False
                    continue

                if TEMA not in [1, 2, 3, 4, 5]:
                    valorInvalido("Valor fora intervalo", "——")
                    limpaTela()
                    ANIMACAO = False
                    continue

                ANIMACAO = True
                break

            # Escolhendo a palavra de acordo com o tema
            word = choice(palavras[temasPossiveis[(TEMA-1)]]).lower()

            # Espaço para preencher as palavras
            for ele in word.split():
                frase += ["_ "] * len(ele)
                frase += " "
        # ---------------------------------------------------------------------------

        # Título para mostrar letras inválidas
        limpaTela()
        if PRIMEIROERRO != 0:

            if LETRA not in word and not LETRA.isnumeric():
                if LETRA not in letrasUsadas:
                    letrasUsadas.append(LETRA[0])

            # Mostrando as letras inválidas
            print()
            if len(letrasUsadas) == 1:
                LETRASJUNTAS = "Letra Usada: "
                LETRASJUNTAS += " ".join(v.upper() for v in letrasUsadas)
            else:
                LETRASJUNTAS = "Letras Usadas: "
                LETRASJUNTAS += " ".join(v.upper() for v in letrasUsadas)

            print(f'{LETRASJUNTAS:^{TAM*2}} ')
            print()

        # Mostrando o tema selecionado
        l("——", TAM)
        TEMAESCOLHIDO = "Tema Escolhido: " + "".join(temasPossiveis[TEMA-1])
        msgAnimada(f"{TEMAESCOLHIDO:^{TAM*2}}", ANIMACAO)

        # 1ª Mostrando o boneco
        l("——", TAM)
        boneco(C)

        # ---------------------------------------------------------------------------

        # Verificando a vitória ou derrota
        if "_ " not in frase:
            break

        # Pedindo as letra para o usuário
        TEMAS = False
        ANIMACAO = True
        l("——", 40)
        msgAnimada("Insira uma letra: ", ANIMACAO, "")
        ANIMACAO = False
        LETRA = input().strip()
        try:
            if not LETRA[0].isalpha():
                # Bloco inválido 1
                valorInvalido("Números ou símbolos não são válidos", "——", 80)
                limpaTela()
                continue

            # Bloco verdadeiro
            LETRA = LETRA[0]

            if LETRA not in word or LETRA.upper() + " " in frase:
                C += 1
                PRIMEIROERRO += 1

            if C == 6:
                break

            continue

        except IndexError:
            # Bloco inválido 2
            valorInvalido("Espaços não são válidos", "——", 80)
            limpaTela()
            continue

    # Status
    ANIMACAO = True
    limpaTela()
    l("——")

    if C == 6:
        msgAnimada(f"{'Você morreu!':^{TAM}}", ANIMACAO)
        l("——")
        msgAnimada(f"A palavra era: {word}")
        l("——")

    else:
        msgAnimada(f"{'Você sobreviveu!':^{TAM}}", ANIMACAO)
        l("——")

    # Perguntando se o jogador deseja jogar novamente
    SAIR = False
    while True:

        msgAnimada("Deseja jogar novamente [S/N]: ", ANIMACAO, "")
        RESP = str(input())

        if RESP[0] in ["s", "S"]:
            TEMAS = True
            MAINTITLE = False
            break

        if RESP[0] in ["n", "N"]:
            SAIR = True
            break

        valorInvalido('Digite apenas "S" ou "N"', "——")
        continue

    if SAIR:
        break
