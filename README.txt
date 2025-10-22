🛸 Aventura Espacial (PC Edition)

Um jogo 2D arcade feito em Python + Pygame Zero.
Controle sua nave, destrua inimigos e desvie de meteoros!

🚀 Funcionalidades

Controle com o mouse

Dificuldades: fácil, médio e difícil

Efeitos sonoros (tiro, game over)

Música de fundo estilo 8-bit retrô

Menu inicial e tela de fim de jogo

Totalmente portátil (sem caminhos fixos)

📁 Estrutura de Pastas
Aventura_Espacial/
│
├── launcher.py           → menu inicial estilizado
├── index.py              → jogo principal
│
├── images/               → sprites do jogo
│   ├── ship.png
│   ├── enemy.png
│   ├── meteor.png
│   ├── bullet.png
│   └── space.jpg
│
└── sounds/               → efeitos e músicas
    ├── tiro.wav
    ├── gameover.wav
    └── musica_fundo_8bit.mp3

🧠 Como Rodar no Windows

Instale o Python 3.11+

Instale as dependências:

pip install pygame pgzero


Execute o menu inicial:

python launcher.py


Ou execute o jogo direto:

pgzrun index.py

🏗️ Gerar Executável (.exe)

Instale o PyInstaller:

pip install pyinstaller


Gere o executável com:

pyinstaller --onefile --noconsole --add-data "images;images" --add-data "sounds;sounds" --icon "icon.ico" --name "AventuraEspacial" launcher.py


O executável ficará em:

dist/AventuraEspacial.exe

👨‍💻 Créditos

Programador: Totoi

Engine: Pygame Zero + Pygame

Edição Deluxe: ChatGPT Game Assistant

💡 Dica

Coloque a pasta Aventura_Espacial completa no mesmo diretório do .exe
para garantir que as imagens e sons sejam encontrados corretamente.
