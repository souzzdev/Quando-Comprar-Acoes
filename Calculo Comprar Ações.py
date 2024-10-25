def calcular_pvpa(preco_acao, valor_patrimonial):
    # Calcula o PVP-PA (Preço sobre Valor Patrimonial)
    pvpa = preco_acao / valor_patrimonial
    if pvpa < 1:
        return f"PVP-PA: {pvpa:.2f}. A ação está subvalorizada, pode ser um bom momento para comprar."
    elif pvpa == 1:
        return f"PVP-PA: {pvpa:.2f}. A ação está com preço justo."
    else:
        return f"PVP-PA: {pvpa:.2f}. A ação está supervalorizada."

def calcular_pl(preco_acao, lpa):
    # Calcula o P/L (Preço sobre Lucro)
    pl = preco_acao / lpa
    if pl < 10:
        return f"P/L: {pl:.2f}. A ação está barata."
    elif 10 <= pl <= 20:
        return f"P/L: {pl:.2f}. A ação está com preço justo."
    else:
        return f"P/L: {pl:.2f}. A ação está cara."

def calcular_dy(dividendos_anuais, preco_acao):
    # Calcula o Dividend Yield (Rendimento de Dividendos)
    dy = (dividendos_anuais / preco_acao) * 100
    if dy > 5:
        return f"Dividend Yield: {dy:.2f}%. A ação tem um bom rendimento em dividendos."
    else:
        return f"Dividend Yield: {dy:.2f}%. O rendimento em dividendos é baixo."

def calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento):
    # Calcula o Valor Intrínseco da ação
    if taxa_desconto <= taxa_crescimento:
        return "A taxa de desconto deve ser maior que a taxa de crescimento."
    valor_intrinseco = dividendo_esperado / (taxa_desconto - taxa_crescimento)
    return f"Valor intrínseco da ação: {valor_intrinseco:.2f}"

def calcular_rsi(ganhos, perdas):
    # Calcula o RSI (Índice de Força Relativa)
    if perdas == 0:
        return "RSI: 100. A ação está sobrecomprada."
    rs = ganhos / perdas
    rsi = 100 - (100 / (1 + rs))
    if rsi > 70:
        return f"RSI: {rsi:.2f}. A ação está sobrecomprada. Pode ser um bom momento para vender."
    elif rsi < 30:
        return f"RSI: {rsi:.2f}. A ação está sobrevendida. Pode ser um bom momento para comprar."
    else:
        return f"RSI: {rsi:.2f}. A ação está em zona neutra."

def mostrar_ajuda():
    # Explica cada opção do menu
    print("\n--- Ajuda para as opções ---")
    print("1. Calcular PVP-PA: Analisa se a ação está subvalorizada ou supervalorizada.")
    print("2. Calcular P/L: Verifica se a ação está barata, com preço justo ou cara.")
    print("3. Calcular Dividend Yield: Informa o rendimento em dividendos da ação.")
    print("4. Calcular Valor Intrínseco: Determina o valor real da ação com base em dividendos esperados.")
    print("5. Calcular RSI: Indica se a ação está sobrecomprada, sobrevendida ou em zona neutra.")
    print("6. Sair: Encerra o programa.")
    print("7. Fechar Programa: Fecha imediatamente o programa.")
    print("8. Saber o que cada opção faz: Mostra a descrição de cada cálculo disponível.")

def menu():
    # Exibe o menu e processa a seleção do usuário
    while True:
        print("\n--- Menu de Análise de Ações ---")
        print("1. Calcular PVP-PA")
        print("2. Calcular P/L")
        print("3. Calcular Dividend Yield")
        print("4. Calcular Valor Intrínseco")
        print("5. Calcular RSI")
        print("6. Sair")
        print("7. Fechar Programa")
        print("8. Saber o que cada opção faz")  # Opção para exibir ajuda
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            preco_acao = float(input("Digite o preço da ação: "))
            valor_patrimonial = float(input("Digite o valor patrimonial da ação: "))
            print(calcular_pvpa(preco_acao, valor_patrimonial))

        elif opcao == "2":
            preco_acao = float(input("Digite o preço da ação: "))
            lpa = float(input("Digite o lucro por ação (LPA): "))
            print(calcular_pl(preco_acao, lpa))

        elif opcao == "3":
            dividendos_anuais = float(input("Digite os dividendos anuais por ação: "))
            preco_acao = float(input("Digite o preço da ação: "))
            print(calcular_dy(dividendos_anuais, preco_acao))

        elif opcao == "4":
            dividendo_esperado = float(input("Digite o dividendo esperado: "))
            taxa_desconto = float(input("Digite a taxa de desconto (ex: 0.10 para 10%): "))
            taxa_crescimento = float(input("Digite a taxa de crescimento (ex: 0.02 para 2%): "))
            print(calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento))

        elif opcao == "5":
            ganhos = float(input("Digite os ganhos médios: "))
            perdas = float(input("Digite as perdas médias: "))
            print(calcular_rsi(ganhos, perdas))

        elif opcao == "6":
            print("Saindo do programa...")
            break

        elif opcao == "7":
            print("Fechando o programa imediatamente.")
            exit()

        elif opcao == "8":
            mostrar_ajuda()  # Chama a função para exibir ajuda

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()