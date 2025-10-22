=============================
 AVENTURA ESPACIAL (PC EDITION)
=============================

Um jogo 2D arcade feito em Python + Pygame Zero.
Controle sua nave, destrua inimigos e desvie de meteoros!

---------------------------------
 FUNCIONALIDADES
---------------------------------
- Controle com o mouse
- Dificuldades: fácil, médio e difícil
- Efeitos sonoros (tiro, game over)
- Música de fundo 8-bit
- Menu inicial e tela de fim de jogo
- Totalmente portátil (sem caminhos fixos)

---------------------------------
 ESTRUTURA DE PASTAS
---------------------------------
Aventura_Espacial/
│
├── launcher.py           -> menu inicial estilizado
├── index.py              -> jogo principal
│
├── images/               -> sprites do jogo
│   ├── ship.png
│   ├── enemy.png
│   ├── meteor.png
│   ├── bullet.png
│   └── space.jpg
│
└── sounds/               -> efeitos e músicas
    ├── tiro.wav
    ├── gameover.wav
    └── musica_fundo_8bit.mp3

---------------------------------
 COMO RODAR NO WINDOWS
---------------------------------
1. Instale o Python 3.11 ou superior.
2. Instale as dependências:
   pip install pygame pgzero
3. Execute o menu inicial:
   python launcher.py
4. Ou execute o jogo direto:
   pgzrun index.py

---------------------------------
 GERAR EXECUTÁVEL (EXE)
---------------------------------
1. Instale o PyInstaller:
   pip install pyinstaller

2. Gere o arquivo .exe com:
   pyinstaller --onefile --noconsole --add-data "images;images" --add-data "sounds;sounds" --icon "icon.ico" --name "AventuraEspacial" launcher.py

O executável será criado na pasta:
   dist\AventuraEspacial.exe

---------------------------------
 CRÉDITOS
---------------------------------
- Programador: Totoi
- Engine: Pygame Zero + Pygame
- Edição Deluxe: ChatGPT Game Assistant

---------------------------------
 DICA
---------------------------------
Coloque a pasta "Aventura_Espacial" inteira no mesmo local do EXE
para garantir que as imagens e sons sejam encontrados corretamente.

=================================
