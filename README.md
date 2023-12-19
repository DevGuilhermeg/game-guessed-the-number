# Guessed The Number - Jogo de Adivinhação
Este é um jogo simples de adivinhação em Python, onde o jogador tenta adivinhar um número aleatório. O jogo possui vários níveis, cada um com um intervalo de números diferentes. O jogador pode digitar "x" a qualquer momento para sair do jogo.

Configurações
O jogo possui algumas configurações básicas:

python
Copy code
# Nível atual do jogador (inicializado em 0).
lvl = 0

# Lista de intervalos de números para cada nível.
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Valor máximo do intervalo para o nível atual.
esc = numeros[lvl]

# Número aleatório a ser adivinhado.
numero = randint(1, esc)

# Variável de controle para o loop principal do jogo.
loop = True
Instruções
O jogo exibe uma mensagem inicial e aguarda por 4 segundos antes de começar.
Durante o jogo, o jogador é informado sobre o nível atual.
O jogador insere um número para adivinhar dentro do intervalo.
O jogador pode digitar "x" a qualquer momento para sair do jogo.
Se o jogador adivinhar corretamente, avança para o próximo nível.
Quando o jogador completa todos os 10 níveis, o jogo é concluído.
Mensagens indicam se o número é mais alto ou mais baixo.
O jogo limpa a tela entre as interações para melhor legibilidade.
Funções
cont(ini): Função para exibir uma contagem regressiva antes do início do jogo.
sair(): Função para exibir uma mensagem de encerramento do jogo.
Observações
Certifique-se de executar o código em um ambiente que suporte a limpeza do terminal com os.system('cls').
O jogo utiliza a biblioteca time para pausas entre as mensagens.
A saída do jogo inclui uma mensagem de parabéns se o jogador concluir todos os níveis.
Divirta-se jogando!
