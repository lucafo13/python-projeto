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
# Objetivo
O sistema tem como o objetivo ser um jogo simples baseado na franquia de Pokémon da game freak e Nintendo, com objetivos dentro do jogo simples como capturar e batalhar com outras criaturas dentro do mapa.

# Controles

 - **WASD** - Movimentação
 - **Space** - Arremeço de bola
 - **IJKL** - Movimentação de Pokémon
 - **M** - Ataque

# Funcionamento

**Arquitetura:**
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
  <br>
 **sprites.py** -- >  É o arquivo que cuida das entidades presentes no jogo, seja o player ou os próprios pokémons e objetos, possui classes como a Player para o jogador e projectile que cuida das pookeballs e é herdada pelos  projéteis de ataque dos pokémons.
  <br>
 **settings.py** --> É o arquivo que guarda as configurações do jogo, como os tipos, velocidade, pokémons e etc. Estes valores são usados por diferentes áreas do código do jogo.
  <br>
 **tilemap.py** --> Arquivo que toma de conta do mapa e da câmera, sendo o responsável por ler os arquivos .tmx, que levam consigo os tileset presente no mapa.
  <br>
 **menu.py** -->  Se trata da barrinha lateral que traz informações como Pokémons capturados, seus tipos e hp, nela contém a classe Menu, que é responsável pelos métodos que criam a barra e definem suas características.
  <br>
 **fonts.py** --> Esse arquivo é diferente dos outros pelo fato de não conter classes, é movido por funções para renderizar os textos que aparecem no jogo, fazendo isso de uma só vez com, por exemplo, a função def drawn_text2()
  <br>
 **outro.py** -->  Código responsável para fazer a cena final do jogo, que acontece após coletar todos os 8 pokémons do jogo, nela tem uma classe chamada Ending, que reaproveitadas imagens carregadas da outra classe do arquivo main.py chamada Game.
 <br> <br>
***Sobre os Tileset** : Para o mapa, são usados tileset presentes nos arquivos .tmx guiados pelo arquivo .tsx presente na mesma pasta, para organiza-los da maneira desejada, foi-se usado o aplicativo Tiled, que foi capaz de ler os arquivos e corrigir erros causados pelos novos tiles que colocamos no projeto
<img width="1917" height="1077" alt="image" src="https://github.com/user-attachments/assets/4717fe7e-fa96-4f88-b133-2104c764654b" />

# Alterações feitas em relação ao repositório original :
 <br> 
 O repositório que escolhemos é chamado de PokeGame, qual abordava de maneira simples o conceito do jogo, tendo artes e mecanicas simplificadas, para o projeto, alteramos toda a arte do jogo, adicionamos novos tipos de pokémon ( apenas tinham 'grass', 'water' e 'fire' mas adicionamos os tipos flying, ground e eletric, graças à analise feita do código ), além da mecânica de tipos, onde cada pokémon pode dar mais ou menos dano de acordo com o tipo de seu adversário (água > fogo > grama > água).

 # diferenças :
 **original**
 <img width="1176" height="998" alt="image" src="https://github.com/user-attachments/assets/4f47c341-f687-4c57-9270-0cadf918c242" />
<br>

**atual** : 
<img width="1281" height="956" alt="image" src="https://github.com/user-attachments/assets/93c09440-90ce-4b05-be39-4023ef27db87" />
