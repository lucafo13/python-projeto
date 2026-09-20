# Projeto Python para PA ---- Pokémon Pocket

**Participantes:**
 - Davi Lucas,
 - Edelcio Miguel

# Jogo: Pókemon Pocket
**Repositório original: https://github.com/jlaframboise/PokeGame.git**
<br>
<img width="1265" height="945" alt="image" src="https://github.com/user-attachments/assets/92f4c60e-9582-4462-98b4-9d30b7b386a0" />

<br />
Jogo sobre pokémon feito em python onde o jogador deve capturar todos as espécies de pokémons possiveis disponiveis dentro do jogo

<br />
**Pokémons adicionados**: 

- Bulbasaur
- Charmander
- Bellsprout
- Squirtle
- Pidgey
- Dratini
- Diglett
- Pikachu

<br />
No jogo, para capturar um pokémon, é preciso se encontrar com ele e entrar em batalha, onde caso já tiver algum, terá que usar de ataques para combater o pokémon adversário ou simplesmente tentar capturá-lo
<img width="1177" height="957" alt="image" src="https://github.com/user-attachments/assets/cd6ca802-7bab-4fa5-89c7-82738732ca6f" />

<br>

# Controles

 - **WASD** - Movimentação
 - **Space** - Arremeço de bola
 - **IJKL** - Movimentação de Pokémon
 - ***M** - Ataque

# Funcionamento

**Arquitetura: **
```
python-projeto/
├── main.py          
├── sprites.py         
├── settings.py      
├── tilemap.py      
├── menu.py           
├── fonts.py         
├── outro.py          
├── engenhoca.py       
├── maps/
│   ├── map1.tmx       
│   ├── b_map.tmx      
│   └── spritesheet_tiles.tsx
├── img/               
├── PlanningWeek0-4.docx
├── README.md
└── .gitignore
```
<br>

O projeto funciona com boa base em POO(Programação Orientada a Objetos) onde atual classes, como por exemplo a classe de cada pokémon

 <br>

 **main.py** --> Mantém o jogo funcional, controlando o loop principal e também as batalhas, com por exemplo a classe game que faz desde o tamanho da janela até o carregamento de algumas imagens do mapa.
 **sprites.py** -- >  É o arquivo que cuida das entidades presentes no jogo, seja o player ou os próprios pokémons e objetos, possui classes como a Player para o jogador e projectile que cuida das pookeballs e é herdada pelos  projéteis de ataque dos pokémons.
 **settings.py** --> É o arquivo que guarda as configurações do jogo, como os tipos, velocidade, pokémons e etc. Estes valores são usados por diferentes áreas do código do jogo.
 **tilemap.py** --> Arquivo que toma de conta do mapa e da câmera, sendo o responsável por ler os arquivos .tmx, que levam consigo os tileset presente no mapa.
 **menu.py** -->  Se trata da barrinha lateral que traz informações como Pokémons capturados, seus tipos e hp, nela contém a classe Menu, que é responsável pelos métodos que criam a barra e definem suas características.
 **fonts.py** --> 
