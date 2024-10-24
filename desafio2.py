#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;


# Função para verificar a existência e contar a letra 'a', com e sem acentos
def verifica_letra_a(texto):
    # Converte o texto para minúsculas para facilitar a contagem
    texto_lower = texto.lower()

    # Conta quantas vezes as variantes da letra 'a' aparecem (com e sem acentos)
    contagem_a = texto_lower.count('a') + texto_lower.count('á') + texto_lower.count('â') + texto_lower.count('ã')

    # Verifica se alguma variante da letra 'a' aparece
    if contagem_a > 0:
        return f"A letra 'a' (incluindo á, â, ã) aparece {contagem_a} vezes."
    else:
        return "A letra 'a' (ou suas variantes) não aparece no texto."

# Solicita a entrada do usuário
texto = input("Digite um texto: ")

# Exibe o resultado
print(verifica_letra_a(texto))
