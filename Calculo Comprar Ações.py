import random
import time
from colorama import Fore

class ChatbotInvestimentos:
    def __init__(self):
        print(Fore.CYAN + "Bem-vindo ao Chatbot de Investimentos!")
        print(Fore.CYAN + "Estou aqui para ajudá-lo a analisar ações e FIIs. Vamos começar!\n")
    
    def calcular_pvpa(self, preco_acao, valor_patrimonial):
        try:
            pvpa = preco_acao / valor_patrimonial
            if pvpa < 1:
                return pvpa, f"PVP-PA: {pvpa:.2f}. A ação está subvalorizada, pode ser um bom momento para comprar."
            elif pvpa == 1:
                return pvpa, f"PVP-PA: {pvpa:.2f}. A ação está com preço justo."
            else:
                return pvpa, f"PVP-PA: {pvpa:.2f}. A ação está supervalorizada."
        except ZeroDivisionError:
            return None, Fore.RED + "Erro: O valor patrimonial não pode ser zero."

    def calcular_dy(self, dividendos_anuais, preco_acao):
        try:
            dy = (dividendos_anuais / preco_acao) * 100
            if dy > 5:
                return dy, f"Dividend Yield: {dy:.2f}%. A ação tem um bom rendimento em dividendos."
            else:
                return dy, f"Dividend Yield: {dy:.2f}%. O rendimento em dividendos é baixo."
        except ZeroDivisionError:
            return None, Fore.RED + "Erro: O preço da ação não pode ser zero."
    
    def calcular_pl(self, preco_acao, lpa):
        try:
            pl = preco_acao / lpa
            if pl < 10:
                return pl, f"P/L: {pl:.2f}. A ação está barata em relação ao lucro."
            elif pl == 10:
                return pl, f"P/L: {pl:.2f}. A ação está com preço justo em relação ao lucro."
            else:
                return pl, f"P/L: {pl:.2f}. A ação está cara em relação ao lucro."
        except ZeroDivisionError:
            return None, Fore.RED + "Erro: O LPA não pode ser zero."

    def calcular_valor_intrinseco(self, dividendo_esperado, taxa_desconto, taxa_crescimento):
        try:
            valor_intrinseco = dividendo_esperado * (1 + taxa_crescimento) / (taxa_desconto - taxa_crescimento)
            return valor_intrinseco, f"Valor Intrínseco: {valor_intrinseco:.2f}"
        except ZeroDivisionError:
            return None, Fore.RED + "Erro: A taxa de desconto não pode ser igual à taxa de crescimento."
    
    def calcular_rsi(self, ganhos, perdas):
        try:
            rs = ganhos / perdas
            rsi = 100 - (100 / (1 + rs))
            if rsi > 70:
                return rsi, f"RSI: {rsi:.2f}. A ação está sobrecomprada, atenção com a queda."
            elif rsi < 30:
                return rsi, f"RSI: {rsi:.2f}. A ação está sobrevendida, pode ser uma oportunidade de compra."
            else:
                return rsi, f"RSI: {rsi:.2f}. A ação está em uma faixa neutra."
        except ZeroDivisionError:
            return None, Fore.RED + "Erro: Não é possível calcular o RSI sem perdas."

    def calcular_pvp(self, preco_cota, valor_patrimonial_cota):
        try:
            pvp = preco_cota / valor_patrimonial_cota
            if pvp < 1:
                return pvp, f"P/VP: {pvp:.2f}. O FII está subvalorizado, pode ser interessante analisar para compra."
            elif pvp == 1:
                return pvp, f"P/VP: {pvp:.2f}. O FII está com preço justo."
            else:
                return pvp, f"P/VP: {pvp:.2f}. O FII está supervalorizado, cuidado com o preço."
        except ZeroDivisionError:
            return None, Fore.RED + "Erro: O valor patrimonial da cota não pode ser zero."

    def calcular_dy_fii(self, rendimento_mensal, preco_cota):
        try:
            if preco_cota == 0:
                return None, Fore.RED + "Erro: O preço da cota não pode ser zero."
            # Garantir que o cálculo do DY seja preciso
            dy = (rendimento_mensal * 12 / preco_cota) * 100
            if dy > 6:
                return dy, Fore.GREEN + f"Dividend Yield: {dy:.2f}%. O FII tem um bom rendimento."
            else:
                return dy, Fore.RED + f"Dividend Yield: {dy:.2f}%. O rendimento é baixo para um FII."
        except Exception as e:
            return None, Fore.RED + f"Erro: {str(e)}"

    def analisar_fii(self, preco_cota, valor_patrimonial_cota, rendimento_mensal):
        pvp, msg_pvp = self.calcular_pvp(preco_cota, valor_patrimonial_cota)
        dy, msg_dy = self.calcular_dy_fii(rendimento_mensal, preco_cota)
        print(msg_pvp)
        print(msg_dy)

        if pvp < 1 and dy > 6:
            print(Fore.GREEN + "Recomendação: O FII apresenta bom rendimento e está subvalorizado. Pode ser uma boa oportunidade de compra.")
        elif dy > 6:
            print(Fore.YELLOW + "Recomendação: O rendimento é atrativo, mas analise o P/VP antes de investir.")
        elif pvp < 1:
            print(Fore.YELLOW + "Recomendação: O FII está subvalorizado, mas o rendimento pode ser baixo.")
        else:
            print(Fore.RED + "Recomendação: O FII não apresenta características atrativas neste momento.")

    def comparar_acoes(self, acao1, acao2):
        print(Fore.CYAN + "\n--- Comparação de Ações ---")
        pvpa1, msg_pvpa1 = self.calcular_pvpa(acao1['preco_acao'], acao1['valor_patrimonial'])
        pvpa2, msg_pvpa2 = self.calcular_pvpa(acao2['preco_acao'], acao2['valor_patrimonial'])
        print(f"Ação 1 - {msg_pvpa1}")
        print(f"Ação 2 - {msg_pvpa2}")

        dy1, msg_dy1 = self.calcular_dy(acao1['dividendos_anuais'], acao1['preco_acao'])
        dy2, msg_dy2 = self.calcular_dy(acao2['dividendos_anuais'], acao2['preco_acao'])
        print(f"Ação 1 - {msg_dy1}")
        print(f"Ação 2 - {msg_dy2}")

        if pvpa1 < pvpa2 and dy1 > dy2:
            print(Fore.GREEN + "Ação 1 é a melhor escolha para compra com base em P/VPA e Dividend Yield.")
        elif pvpa2 < pvpa1 and dy2 > dy1:
            print(Fore.GREEN + "Ação 2 é a melhor escolha para compra com base em P/VPA e Dividend Yield.")
        elif pvpa1 < pvpa2:
            print(Fore.GREEN + "Ação 1 é a melhor escolha com base em P/VPA.")
        elif pvpa2 < pvpa1:
            print(Fore.GREEN + "Ação 2 é a melhor escolha com base em P/VPA.")
        elif dy1 > dy2:
            print(Fore.GREEN + "Ação 1 é a melhor escolha com base em Dividend Yield.")
        elif dy2 > dy1:
            print(Fore.GREEN + "Ação 2 é a melhor escolha com base em Dividend Yield.")
        else:
            print(Fore.YELLOW + "Ambas as ações têm características similares; pode ser interessante analisar outros fatores.")

    def menu(self):
        print(Fore.CYAN + "\nEscolha uma das opções abaixo:")
        print(Fore.GREEN + "1. Calcular P/VPA de uma Ação")
        print(Fore.GREEN + "2. Calcular Dividend Yield de uma Ação")
        print(Fore.GREEN + "3. Calcular P/L de uma Ação")
        print(Fore.GREEN + "4. Calcular Valor Intrínseco de uma Ação")
        print(Fore.GREEN + "5. Calcular RSI de uma Ação")
        print(Fore.GREEN + "6. Calcular P/VP de um FII")
        print(Fore.GREEN + "7. Calcular Dividend Yield de um FII")
        print(Fore.GREEN + "8. Analisar FII")
        print(Fore.GREEN + "9. Comparar duas Ações")
        print(Fore.RED + "0. Sair")
        
    def start_conversation(self):
        while True:
            self.menu()
            escolha = input(Fore.YELLOW + "Digite sua escolha: ")
            
            if escolha == "1":
                preco_acao = float(input(Fore.GREEN + "Digite o preço da ação: "))
                valor_patrimonial = float(input(Fore.GREEN + "Digite o valor patrimonial da ação: "))
                pvpa, msg = self.calcular_pvpa(preco_acao, valor_patrimonial)
                print(msg)
            
            elif escolha == "2":
                dividendos_anuais = float(input(Fore.GREEN + "Digite os dividendos anuais por ação: "))
                preco_acao = float(input(Fore.GREEN + "Digite o preço da ação: "))
                dy, msg = self.calcular_dy(dividendos_anuais, preco_acao)
                print(msg)
                
            elif escolha == "3":
                preco_acao = float(input(Fore.GREEN + "Digite o preço da ação: "))
                lpa = float(input(Fore.GREEN + "Digite o LPA (Lucro por Ação): "))
                pl, msg = self.calcular_pl(preco_acao, lpa)
                print(msg)
                
            elif escolha == "4":
                dividendo_esperado = float(input(Fore.GREEN + "Digite o dividendo esperado (em reais): "))
                taxa_desconto = float(input(Fore.GREEN + "Digite a taxa de desconto (%): ")) / 100
                taxa_crescimento = float(input(Fore.GREEN + "Digite a taxa de crescimento (%): ")) / 100
                valor_intrinseco, msg = self.calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento)
                print(msg)
                
            elif escolha == "5":
                ganhos = float(input(Fore.GREEN + "Digite os ganhos: "))
                perdas = float(input(Fore.GREEN + "Digite as perdas: "))
                rsi, msg = self.calcular_rsi(ganhos, perdas)
                print(msg)
                
            elif escolha == "6":
                preco_cota = float(input(Fore.GREEN + "Digite o preço da cota do FII: "))
                valor_patrimonial_cota = float(input(Fore.GREEN + "Digite o valor patrimonial da cota: "))
                pvp, msg = self.calcular_pvp(preco_cota, valor_patrimonial_cota)
                print(msg)
                
            elif escolha == "7":
                rendimento_mensal = float(input(Fore.GREEN + "Digite o rendimento mensal por cota (em reais): "))
                preco_cota = float(input(Fore.GREEN + "Digite o preço da cota do FII: "))
                dy, msg = self.calcular_dy_fii(rendimento_mensal, preco_cota)
                print(msg)
                
            elif escolha == "8":
                preco_cota = float(input(Fore.GREEN + "Digite o preço da cota do FII: "))
                valor_patrimonial_cota = float(input(Fore.GREEN + "Digite o valor patrimonial da cota: "))
                rendimento_mensal = float(input(Fore.GREEN + "Digite o rendimento mensal por cota (em reais): "))
                self.analisar_fii(preco_cota, valor_patrimonial_cota, rendimento_mensal)
                
            elif escolha == "9":
                acao1 = {
                    'preco_acao': float(input(Fore.GREEN + "Digite o preço da ação 1: ")),
                    'valor_patrimonial': float(input(Fore.GREEN + "Digite o valor patrimonial da ação 1: ")),
                    'dividendos_anuais': float(input(Fore.GREEN + "Digite os dividendos anuais da ação 1: ")),
                    'lpa': float(input(Fore.GREEN + "Digite o LPA da ação 1: ")),
                }

                acao2 = {
                    'preco_acao': float(input(Fore.GREEN + "Digite o preço da ação 2: ")),
                    'valor_patrimonial': float(input(Fore.GREEN + "Digite o valor patrimonial da ação 2: ")),
                    'dividendos_anuais': float(input(Fore.GREEN + "Digite os dividendos anuais da ação 2: ")),
                    'lpa': float(input(Fore.GREEN + "Digite o LPA da ação 2: ")),
                }

                self.comparar_acoes(acao1, acao2)
            
            elif escolha == "0":
                print(Fore.GREEN + "Obrigado por usar o Chatbot de Investimentos. Até a próxima!")
                break
                
            else:
                print(Fore.RED + "Opção inválida, por favor, escolha uma opção válida.")

if __name__ == "__main__":
    chatbot = ChatbotInvestimentos()
    chatbot.start_conversation()
    
