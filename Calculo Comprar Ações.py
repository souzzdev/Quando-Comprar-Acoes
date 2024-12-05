import random
import time
from colorama import Fore

class CalculadoraInvestimentos:
    # Métodos para cálculos
    def calcular_pvpa(self, preco_acao, valor_patrimonial):
        try:
            pvpa = preco_acao / valor_patrimonial
            if pvpa < 1:
                return pvpa, f"P/VPA: {pvpa:.2f}. A ação está subvalorizada, pode ser um bom momento para comprar."
            elif pvpa == 1:
                return pvpa, f"P/VPA: {pvpa:.2f}. A ação está com preço justo."
            else:
                return pvpa, f"P/VPA: {pvpa:.2f}. A ação está supervalorizada."
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

class ChatbotInvestimentos:
    def __init__(self):
        self.calculadora = CalculadoraInvestimentos()
        print(Fore.CYAN + "Bem-vindo ao Chatbot de Investimentos!")
        print(Fore.CYAN + "Estou aqui para ajudá-lo a analisar ações e FIIs. Vamos começar!\n")
    
    def menu(self):
        while True:
            print(Fore.CYAN + "\nEscolha uma das opções abaixo:")
            print(Fore.GREEN + "1. Calcular P/VPA de uma Ação")
            print(Fore.GREEN + "2. Calcular Dividend Yield de uma Ação")
            print(Fore.GREEN + "3. Calcular P/L de uma Ação")
            print(Fore.GREEN + "4. Calcular Valor Intrínseco de uma Ação")
            print(Fore.GREEN + "5. Calcular RSI de uma Ação")
            print(Fore.GREEN + "6. Calcular P/VP de um FII")
            print(Fore.GREEN + "7. Calcular Dividend Yield de um FII")
            print(Fore.GREEN + "8. Analisar FII")
            print(Fore.GREEN + "9. Comparar Ações")
            print(Fore.RED + "0. Sair")
            escolha = input(Fore.YELLOW + "Escolha a opção: ")

            if escolha == "1":
                self.calcular_pvpa()
            elif escolha == "2":
                self.calcular_dy()
            elif escolha == "3":
                self.calcular_pl()
            elif escolha == "4":
                self.calcular_valor_intrinseco()
            elif escolha == "5":
                self.calcular_rsi()
            elif escolha == "6":
                self.calcular_pvp()
            elif escolha == "7":
                self.calcular_dy_fii()
            elif escolha == "8":
                self.analisar_fii()
            elif escolha == "9":
                self.comparar_acoes()
            elif escolha == "0":
                print(Fore.CYAN + "Até logo!")
                break
            else:
                print(Fore.RED + "Opção inválida, tente novamente.")

    def calcular_pvpa(self):
        try:
            preco_acao = float(input("Informe o preço da ação: "))
            valor_patrimonial = float(input("Informe o valor patrimonial da ação: "))
            pvpa, mensagem = self.calculadora.calcular_pvpa(preco_acao, valor_patrimonial)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def calcular_dy(self):
        try:
            dividendos_anuais = float(input("Informe os dividendos anuais da ação: "))
            preco_acao = float(input("Informe o preço da ação: "))
            dy, mensagem = self.calculadora.calcular_dy(dividendos_anuais, preco_acao)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def calcular_pl(self):
        try:
            preco_acao = float(input("Informe o preço da ação: "))
            lpa = float(input("Informe o LPA (Lucro por Ação): "))
            pl, mensagem = self.calculadora.calcular_pl(preco_acao, lpa)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def calcular_valor_intrinseco(self):
        try:
            dividendo_esperado = float(input("Informe o dividendo esperado: "))
            taxa_desconto = float(input("Informe a taxa de desconto: "))
            taxa_crescimento = float(input("Informe a taxa de crescimento: "))
            valor_intrinseco, mensagem = self.calculadora.calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def calcular_rsi(self):
        try:
            ganhos = float(input("Informe os ganhos: "))
            perdas = float(input("Informe as perdas: "))
            rsi, mensagem = self.calculadora.calcular_rsi(ganhos, perdas)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def calcular_pvp(self):
        try:
            preco_cota = float(input("Informe o preço da cota do FII: "))
            valor_patrimonial_cota = float(input("Informe o valor patrimonial da cota do FII: "))
            pvp, mensagem = self.calculadora.calcular_pvp(preco_cota, valor_patrimonial_cota)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def calcular_dy_fii(self):
        try:
            rendimento_mensal = float(input("Informe o rendimento mensal do FII: "))
            preco_cota = float(input("Informe o preço da cota do FII: "))
            dy_fii, mensagem = self.calculadora.calcular_dy_fii(rendimento_mensal, preco_cota)
            print(mensagem)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def analisar_fii(self):
        try:
            preco_cota = float(input("Informe o preço da cota do FII: "))
            valor_patrimonial_cota = float(input("Informe o valor patrimonial da cota do FII: "))
            rendimento_mensal = float(input("Informe o rendimento mensal do FII: "))
            self.calculadora.analisar_fii(preco_cota, valor_patrimonial_cota, rendimento_mensal)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

    def comparar_acoes(self):
        try:
            acao1 = {
                "preco_acao": float(input("Informe o preço da ação 1: ")),
                "valor_patrimonial": float(input("Informe o valor patrimonial da ação 1: ")),
                "dividendos_anuais": float(input("Informe os dividendos anuais da ação 1: ")),
            }
            acao2 = {
                "preco_acao": float(input("Informe o preço da ação 2: ")),
                "valor_patrimonial": float(input("Informe o valor patrimonial da ação 2: ")),
                "dividendos_anuais": float(input("Informe os dividendos anuais da ação 2: ")),
            }
            self.calculadora.comparar_acoes(acao1, acao2)
        except ValueError:
            print(Fore.RED + "Por favor, insira valores numéricos válidos.")

# Inicializar o chatbot
chatbot = ChatbotInvestimentos()
chatbot.menu()
