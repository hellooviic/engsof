Jogo de Adivinhação

Um jogo simples de adivinhação desenvolvido em Python, onde o jogador precisa descobrir um número secreto entre 1 e 100.

O jogador possui 7 tentativas para acertar o número escolhido aleatoriamente pelo computador.

Como funciona
O computador escolhe aleatoriamente um número entre 1 e 100.
O jogador recebe 7 tentativas para descobrir o número.
A cada tentativa, o programa informa se o palpite é maior ou menor que o número secreto.
Se o jogador acertar, o programa informa em qual tentativa conseguiu.
Caso as 7 tentativas acabem, o número secreto é revelado.
Tecnologias utilizadas
Python 3
Biblioteca random
Como executar
1. Clone o repositório
git clone URL_DO_SEU_REPOSITORIO

2. Entre na pasta do projeto
cd nome-do-projeto

3. Execute o programa
python jogo.py


Caso seja necessário utilizar o Python 3 diretamente:

python3 jogo.py

Estrutura do projeto
jogo-adivinhacao/
│
├── jogo.py
└── README.md

Conceitos praticados

Este projeto foi desenvolvido para praticar conceitos básicos de programação em Python, como:

Variáveis
Estruturas condicionais (if, elif, else)
Estrutura de repetição (while)
Entrada de dados com input()
Conversão de tipos com int()
Uso da biblioteca random
Geração de números aleatórios com random.randint()
Operadores de comparação
Controle de tentativas
Exemplo de execução
Jogo de adivinhação - Você tem 7 tentativas
Tente adivinhar o número que estou pensando entre 1 e 100

Você tem 7 tentativas restantes
Digite o seu palpite: 50
Seu número é menor que o número secreto

Você tem 6 tentativas restantes
Digite o seu palpite: 25
Seu número é maior que o número secreto

Você tem 5 tentativas restantes
Digite o seu palpite: 37
Número correto! 37

Você acertou. Na tentativa: 3

Possíveis melhorias
 Impedir que o usuário digite números fora do intervalo de 1 a 100
 Tratar entradas que não sejam números
 Permitir que o jogador escolha a dificuldade
 Criar diferentes quantidades de tentativas
 Adicionar um sistema de pontuação
 Permitir jogar novamente sem reiniciar o programa
 Criar uma interface gráfica
Objetivo

Este projeto tem como objetivo servir como um exercício de aprendizado em Python, especialmente para quem está começando a estudar lógica de programação.
