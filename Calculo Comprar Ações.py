def calcular_pvpa(preco_acao, valor_patrimonial):
    pvpa = preco_acao / valor_patrimonial
    if pvpa < 1:
        return pvpa, f"PVP-PA: {pvpa:.2f}. A ação está subvalorizada, pode ser um bom momento para comprar."
    elif pvpa == 1:
        return pvpa, f"PVP-PA: {pvpa:.2f}. A ação está com preço justo."
    else:
        return pvpa, f"PVP-PA: {pvpa:.2f}. A ação está supervalorizada."

def calcular_dy(dividendos_anuais, preco_acao):
    dy = (dividendos_anuais / preco_acao) * 100
    if dy > 5:
        return dy, f"Dividend Yield: {dy:.2f}%. A ação tem um bom rendimento em dividendos."
    else:
        return dy, f"Dividend Yield: {dy:.2f}%. O rendimento em dividendos é baixo."

def comparar_acoes(acao1, acao2):
    print("\n--- Comparação de Valor Atual e Valor Patrimonial por Cota ---")
    print(f"Ação 1 - Valor Atual: {acao1['preco_acao']}, Valor Patrimonial por Cota: {acao1['valor_patrimonial']}")
    print(f"Ação 2 - Valor Atual: {acao2['preco_acao']}, Valor Patrimonial por Cota: {acao2['valor_patrimonial']}")

    print("\n--- Comparação de P/VPA ---")
    pvpa1, msg_pvpa1 = calcular_pvpa(acao1['preco_acao'], acao1['valor_patrimonial'])
    pvpa2, msg_pvpa2 = calcular_pvpa(acao2['preco_acao'], acao2['valor_patrimonial'])
    print(f"Ação 1 - {msg_pvpa1}")
    print(f"Ação 2 - {msg_pvpa2}")

    print("\n--- Comparação de Dividend Yield ---")
    dy1, msg_dy1 = calcular_dy(acao1['dividendos_anuais'], acao1['preco_acao'])
    dy2, msg_dy2 = calcular_dy(acao2['dividendos_anuais'], acao2['preco_acao'])
    print(f"Ação 1 - {msg_dy1}")
    print(f"Ação 2 - {msg_dy2}")

    print("\n--- Recomendação Final ---")
    if pvpa1 < pvpa2 and dy1 > dy2:
        print("Ação 1 é a melhor escolha para compra com base em P/VPA e Dividend Yield.")
    elif pvpa2 < pvpa1 and dy2 > dy1:
        print("Ação 2 é a melhor escolha para compra com base em P/VPA e Dividend Yield.")
    elif pvpa1 < pvpa2:
        print("Ação 1 é a melhor escolha com base em P/VPA.")
    elif pvpa2 < pvpa1:
        print("Ação 2 é a melhor escolha com base em P/VPA.")
    elif dy1 > dy2:
        print("Ação 1 é a melhor escolha com base em Dividend Yield.")
    elif dy2 > dy1:
        print("Ação 2 é a melhor escolha com base em Dividend Yield.")
    else:
        print("Ambas as ações têm características similares; pode ser interessante analisar outros fatores.")

def menu():
    while True:
        print("\n--- Menu de Análise de Ações ---")
        print("1. Calcular PVP-PA")
        print("2. Calcular P/L")
        print("3. Calcular Dividend Yield")
        print("4. Calcular Valor Intrínseco")
        print("5. Calcular RSI")
        print("6. Sair")
        print("7. Fechar Programa")
        print("8. Saber o que cada opção faz")
        print("9. Comparar duas ações")
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
            mostrar_ajuda()

        elif opcao == "9":
            acao1 = {
                'preco_acao': float(input("Ação 1 - Digite o preço atual da ação: ")),
                'valor_patrimonial': float(input("Ação 1 - Digite o valor patrimonial por cota: ")),
                'dividendos_anuais': float(input("Ação 1 - Digite os dividendos anuais por ação: "))
            }
            acao2 = {
                'preco_acao': float(input("Ação 2 - Digite o preço atual da ação: ")),
                'valor_patrimonial': float(input("Ação 2 - Digite o valor patrimonial por cota: ")),
                'dividendos_anuais': float(input("Ação 2 - Digite os dividendos anuais por ação: "))
            }
            comparar_acoes(acao1, acao2)

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()