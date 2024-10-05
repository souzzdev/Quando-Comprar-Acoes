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
        print("7. Fechar Programa")  # Opção para fechar o programa
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Solicita preço da ação e valor patrimonial para calcular o PVP-PA
            preco_acao = float(input("Digite o preço da ação: "))
            valor_patrimonial = float(input("Digite o valor patrimonial da ação: "))
            print(calcular_pvpa(preco_acao, valor_patrimonial))

        elif opcao == "2":
            # Solicita preço da ação e LPA para calcular o P/L
            preco_acao = float(input("Digite o preço da ação: "))
            lpa = float(input("Digite o lucro por ação (LPA): "))
            print(calcular_pl(preco_acao, lpa))

        elif opcao == "3":
            # Solicita dividendos e preço da ação para calcular o Dividend Yield
            dividendos_anuais = float(input("Digite os dividendos anuais por ação: "))
            preco_acao = float(input("Digite o preço da ação: "))
            print(calcular_dy(dividendos_anuais, preco_acao))

        elif opcao == "4":
            # Solicita dados para calcular o valor intrínseco da ação
            dividendo_esperado = float(input("Digite o dividendo esperado: "))
            taxa_desconto = float(input("Digite a taxa de desconto (ex: 0.10 para 10%): "))
            taxa_crescimento = float(input("Digite a taxa de crescimento (ex: 0.02 para 2%): "))
            print(calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento))

        elif opcao == "5":
            # Solicita os ganhos e perdas para calcular o RSI
            ganhos = float(input("Digite os ganhos médios: "))
            perdas = float(input("Digite as perdas médias: "))
            print(calcular_rsi(ganhos, perdas))

        elif opcao == "6":
            # Encerra o loop do menu, saindo do programa
            print("Saindo do programa...")
            break

        elif opcao == "7":
            # Encerra imediatamente o programa sem seguir para a próxima iteração
            print("Fechando o programa imediatamente.")
            exit()

        else:
            # Mensagem para entrada inválida
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()