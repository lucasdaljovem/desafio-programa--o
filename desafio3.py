#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?



# declaração das variáveis
INDICE = 12
SOMA = 0
K = 1

# Loop enquanto K for menor que INDICE
while K < INDICE:
    K = K + 1  # Incrementa K
    SOMA = SOMA + K  # Adiciona K à SOMA

# Imprimir o resultado
print(SOMA)
