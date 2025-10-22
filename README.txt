Aventura Espacial - pacote portátil
Como usar:
1) Extraia esta pasta em qualquer lugar.
2) Abra a pasta e execute launcher.py com Python:
   - Recomendado: criar um atalho para launcher.exe após empacotar com PyInstaller.
3) Certifique-se de ter Python e dependências (pygame, pgzero) instaladas para rodar sem empacotar.
   - Para gerar .exe: pyinstaller --onefile --noconsole launcher.py
Notas:
- Os arquivos de imagens estão em /images e sons em /sounds.
- Se a música de fundo estiver ausente, o jogo ainda roda (fallback).
