# Água e fogo no CIn, sem água e sem fogo - Projeto Introdução à Programação
Projeto final da Equipe 3 para a disciplina de Introdução à Programação de Ciência da Computação do Centro de Informática da UFPE.

Integrantes:

Ádson Viana &lt;aav&gt;

Elena Pimentel &lt;epao&gt;

Giovanna Bardi &lt;gmcb&gt;

Maria Amorim &lt;maca&gt;

Raissa Machado &lt;rmf5&gt;

Romero Cavalcanti &lt;rrcf&gt;

# Descrição da arquitetura do projeto

O projeto está distribuído em alguns arquivos, cada um desempenhando uma função específica no jogo:

main.py:
Arquivo principal do jogo que contém o loop e as
# Capturas de tela

# Ferramentas, bibliotecas e frameworks utilizados

# Divisão de tarefas
Delegação de tarefas:
As tarefas foram incialmente delegadas de acordo com os objetos do mapa. Cada um deveria pesquisar as funcionalidades de seus objetos específicos (Player, Livro, Plataforma, Poça, Coletáveis, Ilustrações) e implementar experimentalmente num código.
Assim surgiram algumas classes arcaicas nas quais trabalhamos, mas não por muito tempo.

Logo, surgiram outras demandas que eram atualizadas a cada checkpoint:
Ex. Correção da colisão com obstáculos, criação da catraca, criação da poça de água, entre outros.

Percebendo a necessidade de otimização de certos, arquivos, e de acordo com a aptidão e o perfil de cada participante, trocamos as tarefas iniciais por outras. Todas elas estão registradas na lista de participantes que virá logo em seguida.

As tarefas eram registradas no notion anexado, prontamente depois de combinadas. 

Ádson Viana &lt;aav&gt;
Responsável por idealizar os obstáculos do mundo. Prototipou o sistema de colisão de obstáculos, e corrigiu diversos problemas posteriores relacionados com a classe de personagem e sua colisão. Contribuiu na criação da tela de menu/ game over/ vitória.

Elena Pimentel &lt;epao&gt;
Responsável porprototipar a classe de colecionáveis e implementar a grade do mapa ao jogo. Otimizou e organizou o código durante todo o projeto. Ajudou o grupo a organizar melhor o sistemas de classes e a herança da classe sprite do pygame. Criou o sistema de crachá e catraca.

Giovanna Bardi &lt;gmcb&gt;
Idealizou o mapa e o cenário. Criou e aperfeiçoou o modo como se comporta com/sem café. Criou o timer para o café e o sistema de contagem de coletáveis. Criou o sistem de "reset" do mapa e dos coletáveis. Criou a classe dos botões.

Maria Amorim &lt;maca&gt;
Responsável pela maior parte dos sprites e figuras realizadas no trabalho. Criou os frames de animação e cada detalhe ilustrativo do projeto. Aprimorou a dinâmica das telas de instrução, game over e vitória. Criou os botões e tornou eles clicáveis. Ajudou no sistema de contagem dos itens.

Raissa Machado &lt;rmf5&gt;
Também contribuiu com algumas sprites utilizadas. Prototipou a organização das plataformas, colisão com os livros e implementação dos objetos. Contribuiu na criação da tela de menu/ game over/ vitória.

Romero Cavalcanti &lt;rrcf&gt;
Prototipador da classe player. Iniciou o sistema  de colisões centrado no player e pôs no código a animação da sprite. Implementou as dinâmicas de movimento à classe player. Contribuiu,também para a implementação das telas de game-over/ vitória. 

# Conceitos apresentados na disciplina que foram utilizados no projeto

A utilização das condicionais (if/ else) permearam todo o projeto, sendo utilizados para,  entre outros: 
- A detecção de teclas pressionadas/ mouse clicando
- As condições de vitória e derrota dos players
- O sistema de colisões
- A contagem dos coletáveis
- A limitação do espaço de movimentação do player

Loops (while / for)
- Animação de sprites
- Loop principal do jogo
- Iteração/ leitura do mapa para colisões com o jogador e criação do mundo de plataformas
- Iteração pelos eventos imbutidos no pygame, para deteccção de teclas pressionadas, por exemplo

Listas/ matrizes
- Matriz do mapa de plataformas
- Lista de frames de animação
- Indexação de eventos do pygame

Tuplas
- Amplamente utilizado como variáveis dos métodos do pygame
- Utilizado em sistema de coordenadas de diversos objetos
- Tamanho dos objetos
- Cores RGB

Funções
- Utilizadas para funcionalidades gerais do jogo (loop principal, telas de game over/ vitória/ instruções)
-Utilizadas no arquivo funções para partes do código que exigiam funcionalidades específicas e repetitivas

Orientação a objetos
- Base de modularização de todo o trabalho
- Lida com herança da classe Sprite
- Métodos e atributos da biblioteca pygame



# Desafios, erros e aprendizados
  Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
  
  Divisão prematura das classes de objetos. Não tinhamos uma noção de como estruturar o código e começamos com pequenas gambiarras incompletas. Começamos com o intuito de entender melhor a biblioteca para posteriormente encaixar cada parte do código. No fim das contas acabou por ser mais difícil encaixar as partes entre si do que fazer cada uma separadamente. A falta de uma estruturação inicial tornou o projeto mais complicado que deveria. (cada um começou fazendo do seu jeito, sem pensar no todo)
  
  Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
  O maior desafio do trabalho foi aprender a cooperar com pessoas que pensam diferente de você (não apenas opiniões, mas lógica de programação e estruturação de  código, principalmente). Entender o que cada parte do código estava fazendo sem ter sido a pessoa que a projetou e como fazer para com que as  classes funcionassem harmonicamente entre si
  
  Quais as lições aprendidas durante o projeto?
  Uma das maiores lições foi a importâncio do planejamento prévio na realização de qualquer trabalho. A importância de, não somente deixar o código funcioal, mas também, compreensível (Adicionar comentários, espaçamentos, etc.). Além do conhecimento técnico, aprendemos como lidar com uma biblioteca completamente nova. Vamos usufruir com coisas novas na maior parte do tempo, a nossa flexibilidade (apesar de custosa) e capacidade de aprendizado/ adaptação foi uma coisa muito interessante de se perceber. Além disso, deu pra percerber a importância de uma plataforme da repositório na lida com arquivos que estão em constante mudança. A lida com orientação a objetos foi marcante, pois era o único assunto que não tinhamos exercitado no dikastis. Implementar essas funcionalidades diretamente no projeto final contribuiu para aumentar o domínio desse assunto.

# Links
Notion: https://www.notion.so/Projeto-IP-1c2392021be480a48f9debd60174520a

Documento: https://docs.google.com/document/d/1WZ9rB6pWkI9Ye3umbNvmfdzllDLxfnOzBjCPjfMOhQQ/edit?tab=t.0#heading=h.7g61vqyk87mu
