# Função para identificar qual lâmpada é controlada por qual interruptor
def identificar_lampadas(interruptor_lampada):
    # Liga o Interruptor A
    print("Ligando o Interruptor A...")
    
    # Simula o estado das lâmpadas com base na entrada do usuário
    print("\nVerificando as lâmpadas:\n")
    
    # Armazenando qual interruptor controla cada lâmpada
    lampadas_controladas = {}

    for i in range(1, 4):
        if interruptor_lampada[i] == 1:
            print(f"Lâmpada {i}: acesa (controlada pelo Interruptor B).")
            lampadas_controladas[i] = "Interruptor B"
        else:
            print(f"Lâmpada {i}: apagada (controlada pelo Interruptor A ou C).")
            lampadas_controladas[i] = "Desconhecido"

    # A lâmpada que está apagada e não foi controlada pelo Interruptor B é controlada pelo Interruptor C
    for i in range(1, 4):
        if interruptor_lampada[i] == 0:
            if lampadas_controladas[i] == "Desconhecido":
                lampadas_controladas[i] = "Interruptor A" if i == 1 else "Interruptor C"

    # Imprime qual lâmpada é controlada por qual interruptor
    print("\nControle das lâmpadas:")
    for lampada, interruptor in lampadas_controladas.items():
        print(f"Lâmpada {lampada} é controlada pelo {interruptor}.")

# Definindo explicitamente qual interruptor controla qual lâmpada
# 1 = acesa, 0 = apagada
# Exemplo: {1: 0, 2: 1, 3: 0} significa que a lâmpada 1 e 3 estão apagadas, e a lâmpada 2 está acesa.
interruptor_lampada = {1: 0, 2: 1, 3: 0}

# Executa a função
identificar_lampadas(interruptor_lampada)
