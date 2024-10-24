def identificar_padrao(sequencia):
    n = len(sequencia)

    # Verifica se a sequência é aritmética -- comara as diferenças entre os elementos,  Se a diferença for constante, calcula o próximo elemento
    if n >= 2:
        diff = sequencia[1] - sequencia[0]
        if all(sequencia[i] - sequencia[i - 1] == diff for i in range(2, n)):
            return sequencia[-1] + diff  # Próximo elemento aritmético

    # Verifica se a sequência é geométrica --Compara as razões entre os elementos. Se a razão for constante, calcula o próximo elemento.
    if n >= 2 and sequencia[0] != 0:
        ratio = sequencia[1] / sequencia[0]
        if all(sequencia[i] / sequencia[i - 1] == ratio for i in range(2, n)):
            return sequencia[-1] * ratio  # Próximo elemento geométrico

    # Verifica se a sequência é quadrática (n^2) -- Verifica se cada elemento é igual ao quadrado de seu índice.
    if all(sequencia[i] == i**2 for i in range(n)):
        return n**2  # Próximo quadrado

    # Verifica se a sequência é de Fibonacci -- Verifica se o último elemento é a soma dos dois anteriores.
    if n >= 3 and sequencia[-1] == sequencia[-2] + sequencia[-3]:
        return sequencia[-1] + sequencia[-2]  # Próximo de Fibonacci

    return None  # Padrão não identificado

# Testando a função com várias sequências
sequencias = {
    "a": [1, 3, 5, 7],
    "b": [2, 4, 8, 16, 32, 64],
    "c": [0, 1, 4, 9, 16, 25, 36],
    "d": [4, 16, 36, 64],
    "e": [1, 1, 2, 3, 5, 8],
    "f": [2, 10, 12, 16, 17, 18, 19]
}

for nome, seq in sequencias.items():
    proximo = identificar_padrao(seq)
    print(f"Próximo elemento da sequência {nome}: {proximo}")
