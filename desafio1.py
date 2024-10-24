# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Função que gera a sequência de Fibonacci até o número dado ou maior
def gera_fibonacci(numero):
    sequencia = [0, 1]  # Inicia a sequência com 0 e 1
    while sequencia[-1] < numero:  # Continua até que o último número seja maior ou igual ao número dado
        proximo = sequencia[-1] + sequencia[-2]  # Soma os dois últimos números da sequência
        sequencia.append(proximo)  # Adiciona o próximo número à sequência
    return sequencia

# Função que verifica se o número está na sequência de Fibonacci
def verifica_fibonacci(numero):
    sequencia = gera_fibonacci(numero)  # Gera a sequência até o número
    if numero in sequencia:  # Verifica se o número está na sequência
        return f'O número {numero} pertence à sequência de Fibonacci.'
    else:
        return f'O número {numero} não pertence à sequência de Fibonacci.'

        return f'O número {numero} não pertence à sequência de Fibonacci.'

# Solicita o número do usuário
numero = int(input("Informe um número: "))

# Exibe o resultado da verificação
print(verifica_fibonacci(numero))