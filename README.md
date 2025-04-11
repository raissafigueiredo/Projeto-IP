# CIn Saída - Projeto Introdução à Programação
Projeto final da Equipe 3 para a disciplina de Introdução à Programação de Ciência da Computação do Centro de Informática da UFPE.

#Integrantes 👨‍💻:

- Ádson Viana &lt;aav&gt;
- Elena Pimentel &lt;epao&gt;
- Giovanna Bardi &lt;gmcb&gt;
- Maria Alice Amorim &lt;maca&gt;
- Raissa Machado &lt;rmf5&gt;
- Romero Cavalcanti &lt;rrcf&gt;

# Descrição da arquitetura do projeto 🏛

O projeto está distribuído em alguns arquivos, cada um desempenhando uma função específica no jogo:

main.py:
- Arquivo principal do jogo
- Providencia as funcionalidades de jogo e telas (game over/instrução)
- Chama as outras classes e os outros arquivos com suas funcionalidades
- Contabiliza e reinicia os coletáveis

mundo.py:
- Cria todos os objetos listados em mapa.py

mapa.py:
- Matriz que indica onde está cada tipo de objeto no mapa

jogador.py:
- Cria movimentação do player
- Estabelece colisões e física
- Animação do player

objetos.py
- Arquivo onde estão armazenadas as classes de objetos que serão instanciadas

botão.py
- Armazena classe de botão, usado para interagir com o mouse

globais.py
- Tem funções específicas e constantes que são usadas no decorrer do código

assets.py
- Contém imagens da pasta Source que serão usadas no código

Source
- Pasta que contém imagens das sprites e cenário

# Sobre o jogo
O jogo consiste em uma jovem caloura desastrada, que deixou cair o seu crachá em um lugar inesperado e precisa exercitar suas técnicas de ninja para recuperar seu item perdido. Para isso, ela utilizará de sua poção mágica: o café, que será fonte de energia e força quando o perigo parece iminente. Ajude a jovem caloura a sair do centro e a coletar as moedas que os estudantes destraídos deixaram pelo caminho!

**TELA INICIAL**
![image](https://github.com/raissafigueiredo/Projeto-IP/blob/main/Sources/tela_inicial1.png)

**INSTRUÇÕES**
![image](https://github.com/raissafigueiredo/Projeto-IP/blob/main/Sources/tela_instrucoes.png)

**AMBIENTE**
![image](https://github.com/raissafigueiredo/Projeto-IP/blob/main/Sources/tela_jogo.png)

**VITÓRIA**
![image](https://github.com/raissafigueiredo/Projeto-IP/blob/main/Sources/tela_venceu.png)

**DERROTA**
![image](https://github.com/raissafigueiredo/Projeto-IP/blob/main/Sources/tela_perdeu.png)





# Ferramentas, bibliotecas e frameworks utilizados
Notion
- Atribuição de tarefas
- Planejamento e organização

GitHub
- Repositório principal

Visual Studio Code
- Estúdio para criação do código

Pixil e Piskel
- Sites utilizados para criação de pixel arts

WhatsApp
- Meio de comunicação principal entre membros do grupo
  
Pygame
- Biblioteca utilizada para a execução das funcionalidades do jogo
- Mecânica de colisões e física
- Lida com sprites, display do jogo, cores, retângulos e display

Sys
- Importada para utilização do cursor


# Divisão de tarefas

Delegação de tarefas:
- Inicialmente delegadas de acordo com os objetos do mapa.
- Cada um deveria pesquisar as funcionalidades de seus objetos específicos (Player, Livro, Plataforma, Poça, Coletáveis, Ilustrações) e implementar experimentalmente num código.
- Assim surgiram algumas classes arcaicas nas quais trabalhamos, mas não por muito tempo.

- Logo, surgiram outras demandas que eram atualizadas a cada checkpoint:
- Ex. Correção da colisão com obstáculos, criação da catraca, criação da poça de água, entre outros.

- Percebendo a necessidade de otimização de certos arquivos, e de acordo com a aptidão e o perfil de cada participante, trocamos as tarefas iniciais por outras.
- Todas elas estão registradas na lista de participantes que virá logo em seguida.


Ádson Viana &lt;aav&gt;
- Responsável por idealizar os obstáculos do mundo
- Prototipou o sistema de colisão de obstáculos
- Corrigiu diversos problemas posteriores relacionados com a classe de personagem e sua colisão
- Contribuiu na criação da tela de menu, game over e vitória.

Elena Pimentel &lt;epao&gt;
- Responsável por prototipar a classe de colecionáveis e implementar a grade do mapa ao jogo
- Otimizou e organizou o código durante todo o projeto.
- Ajudou o grupo a organizar melhor o sistemas de classes e a herança da classe sprite do pygame
- Criou o sistema de crachá e catraca.

Giovanna Bardi &lt;gmcb&gt;
- Responsável por criar as poças de água e a dinâmica de morte
- Idealizou o mapa e o cenário
- Criou e aperfeiçoou o modo como a personagem se comporta com/sem café
- Criou o timer para o café e o sistema de contagem de coletáveis
- Criou o sistema de "reset" do mapa e dos coletáveis
- Criou a classe dos botões

Maria Alice Amorim &lt;maca&gt;
- Responsável pela maior parte dos sprites e figuras contidas no trabalho
- Criou os frames de animação e cada detalhe ilustrativo do projeto
- Aprimorou a dinâmica das telas de instrução, game over e vitória
- Criou os botões e os tornou clicáveis
- Ajudou no sistema de contagem dos itens

Raissa Machado &lt;rmf5&gt;
- Responsável por prototipar a organização das plataformas
- Iniciou a colisão com os livros e implementação dos objetos
- Contribuiu na criação das telas de menu, game over e vitória
- Criação de diversas sprites e artes

Romero Cavalcanti &lt;rrcf&gt;
- Responsável pela classe jogador
- Iniciou o sistema  de colisões centrado no jogador e implementou no código a animação da sprite
- Implementou as dinâmicas de movimento à classe jogador
- Contribuiu para a implementação das telas de game over e vitória

# Conceitos apresentados na disciplina que foram utilizados no projeto 👨‍🏫

A utilização das condicionais (if/else) permearam todo o projeto, sendo utilizados para,  entre outros: 
- A detecção de teclas pressionadas e clique do mouse
- As condições de vitória e derrota dos players
- O sistema de colisões
- A contagem dos coletáveis
- A limitação do espaço de movimentação do player

Loops (while/for)
- Animação de sprites
- Loop principal do jogo
- Iteração e leitura do mapa para colisões com o jogador e criação do mundo de plataformas
- Iteração pelos eventos imbutidos no pygame, para detecção de teclas pressionadas, por exemplo

Listas/matrizes
- Matriz do mapa de plataformas
- Lista de frames de animação
- Indexação de eventos do pygame

Tuplas
- Amplamente utilizado como variáveis dos métodos do pygame
- Utilizado em sistema de coordenadas de diversos objetos
- Tamanho dos objetos
- Cores RGB

Funções
- Utilizadas para funcionalidades gerais do jogo (loop principal, telas de game over, vitória e instruções)
- Utilizadas no arquivo funções para partes do código que exigiam funcionalidades específicas e repetitivas

Orientação a objetos
- Base de modularização de todo o trabalho
- Lida com herança da classe Sprite
- Métodos e atributos da biblioteca pygame



# Desafios, erros e aprendizados 💥
Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
  
  - Divisão prematura das classes de objetos
  - Não tinhamos uma noção de como estruturar o código e começamos com pequenas gambiarras incompletas
  - Começamos com o intuito de entender melhor a biblioteca para posteriormente encaixar cada parte do código
  - No fim das contas acabou por ser mais difícil encaixar as partes entre si do que fazer cada uma separadamente
  - A falta de uma estruturação inicial tornou o projeto mais complicado que deveria (cada um começou fazendo do seu jeito, sem pensar no todo)

Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
  
- O maior desafio do trabalho foi aprender a cooperar com pessoas que pensam diferente de você (não apenas opiniões, mas lógica de programação e estruturação de  código, principalmente)
- Entender o que cada parte do código estava fazendo sem ter sido a pessoa que a projetou e como fazer para com que as  classes funcionassem harmonicamente entre si
  
Quais as lições aprendidas durante o projeto?
  
  - Uma das maiores lições foi a importâncio do planejamento prévio na realização de qualquer trabalho
  - A importância de, não somente deixar o código funcioal, mas também, compreensível (adicionar comentários, espaçamentos, etc.)
  - Além do conhecimento técnico, aprendemos como lidar com uma biblioteca completamente nova
  - Vamos usufruir com coisas novas na maior parte do tempo, a nossa flexibilidade (apesar de custosa) e capacidade de aprendizado e adaptação foram coisas muito interessantes de se perceber
  - Além disso, deu pra perceber a importância de uma plataforma de repositório para lidar com arquivos que estão em constante mudança
  - Lidar com orientação a objetos foi marcante, pois era o único assunto que não tinhamos exercitado no Dikastis
  - Implementar essas funcionalidades diretamente no projeto final contribuiu para aumentar o domínio desse assunto

# Links
Apresentação: https://docs.google.com/presentation/d/1el1toBAG2vcACBF9yUU1r8igBtxO7gJAbUSWJVbbzyE/edit?usp=sharing

Notion: https://big-stingray-48f.notion.site/Projeto-IP-1c2392021be480a48f9debd60174520a?pvs=4 

Documento: https://docs.google.com/document/d/1WZ9rB6pWkI9Ye3umbNvmfdzllDLxfnOzBjCPjfMOhQQ/edit?tab=t.0#heading=h.7g61vqyk87mu
