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

def calcular_pl(preco_acao, lpa):
    """
    Calcula o P/L (Preço sobre Lucro) de uma ação.
    """
    pl = preco_acao / lpa
    if pl < 10:
        return pl, f"P/L: {pl:.2f}. A ação está barata em relação ao lucro."
    elif pl == 10:
        return pl, f"P/L: {pl:.2f}. A ação está com preço justo em relação ao lucro."
    else:
        return pl, f"P/L: {pl:.2f}. A ação está cara em relação ao lucro."

def calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento):
    """
    Calcula o valor intrínseco de uma ação usando o modelo de fluxo de dividendos descontados (DDM).
    """
    valor_intrinseco = dividendo_esperado * (1 + taxa_crescimento) / (taxa_desconto - taxa_crescimento)
    return valor_intrinseco, f"Valor Intrínseco: {valor_intrinseco:.2f}"

def calcular_rsi(ganhos, perdas):
    """
    Calcula o Índice de Força Relativa (RSI) com base nos ganhos e perdas médias.
    """
    rs = ganhos / perdas
    rsi = 100 - (100 / (1 + rs))
    if rsi > 70:
        return rsi, f"RSI: {rsi:.2f}. A ação está sobrecomprada, atenção com a queda."
    elif rsi < 30:
        return rsi, f"RSI: {rsi:.2f}. A ação está sobrevendida, pode ser uma oportunidade de compra."
    else:
        return rsi, f"RSI: {rsi:.2f}. A ação está em uma faixa neutra."

def calcular_pvp(preco_cota, valor_patrimonial_cota):
    """
    Calcula o preço sobre valor patrimonial (P/VP) do FII.
    """
    pvp = preco_cota / valor_patrimonial_cota
    if pvp < 1:
        return pvp, f"P/VP: {pvp:.2f}. O FII está subvalorizado, pode ser interessante analisar para compra."
    elif pvp == 1:
        return pvp, f"P/VP: {pvp:.2f}. O FII está com preço justo."
    else:
        return pvp, f"P/VP: {pvp:.2f}. O FII está supervalorizado, cuidado com o preço."

def calcular_dy_fii(rendimento_mensal, preco_cota):
    """
    Calcula o Dividend Yield (DY) anualizado do FII.
    """
    dy = (rendimento_mensal * 12 / preco_cota) * 100
    if dy > 6:
        return dy, f"Dividend Yield: {dy:.2f}%. O FII tem um bom rendimento."
    else:
        return dy, f"Dividend Yield: {dy:.2f}%. O rendimento é baixo para um FII."

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

def analisar_fii(preco_cota, valor_patrimonial_cota, rendimento_mensal):
    """
    Faz a análise de um FII com base no preço, valor patrimonial e rendimento mensal.
    """
    print("\n--- Análise do FII ---")
    
    # Calcular e exibir P/VP
    pvp, msg_pvp = calcular_pvp(preco_cota, valor_patrimonial_cota)
    print(msg_pvp)
    
    # Calcular e exibir DY
    dy, msg_dy = calcular_dy_fii(rendimento_mensal, preco_cota)
    print(msg_dy)

    # Recomendação final com base nas métricas
    if pvp < 1 and dy > 6:
        print("Recomendação: O FII apresenta bom rendimento e está subvalorizado. Pode ser uma boa oportunidade de compra.")
    elif dy > 6:
        print("Recomendação: O rendimento é atrativo, mas analise o P/VP antes de investir.")
    elif pvp < 1:
        print("Recomendação: O FII está subvalorizado, mas o rendimento pode ser baixo.")
    else:
        print("Recomendação: O FII não apresenta características atrativas neste momento.")

def menu():
    while True:
        print("\n--- Menu de Análise de Ações e FIIs ---")
        print("1. Calcular PVP-PA (Ações)")
        print("2. Calcular P/L (Ações)")
        print("3. Calcular Dividend Yield (Ações)")
        print("4. Calcular Valor Intrínseco (Ações)")
        print("5. Calcular RSI (Ações)")
        print("6. Analisar FII")
        print("7. Comparar duas ações")
        print("8. Sair")
        print("9. Fechar Programa")
        print("10. Saber o que cada opção faz")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            preco_acao = float(input("Digite o preço da ação: "))
            valor_patrimonial = float(input("Digite o valor patrimonial da ação: "))
            print(calcular_pvpa(preco_acao, valor_patrimonial))

        elif opcao == "2":
            preco_acao = float(input("Digite o preço da ação: "))
            lpa = float(input("Digite o LPA (Lucro por Ação): "))
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
            preco_cota = float(input("Digite o preço da cota do FII: "))
            valor_patrimonial_cota = float(input("Digite o valor patrimonial por cota do FII: "))
            rendimento_mensal = float(input("Digite o rendimento mensal do FII: "))
            analisar_fii(preco_cota, valor_patrimonial_cota, rendimento_mensal)

        elif opcao == "7":
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

        elif opcao == "8":
            print("Saindo...")
            break

        elif opcao == "9":
            print("Fechando o programa...")
            exit()

        elif opcao == "10":
            print("1. Calcular PVP-PA (Ações): Calcula o Preço sobre o Valor Patrimonial da ação.")
            print("2. Calcular P/L (Ações): Calcula o Preço sobre Lucro da ação.")
            print("3. Calcular Dividend Yield (Ações): Calcula o rendimento em dividendos da ação.")
            print("4. Calcular Valor Intrínseco (Ações): Calcula o valor intrínseco de uma ação com base no fluxo de dividendos.")
            print("5. Calcular RSI (Ações): Calcula o Índice de Força Relativa (RSI) para análise técnica.")
            print("6. Analisar FII: Realiza análise de FIIs com base no preço, valor patrimonial e rendimento mensal.")
            print("7. Comparar duas ações: Compara duas ações com base em P/VPA e Dividend Yield.")

# Chamada para rodar o menu
menu()
