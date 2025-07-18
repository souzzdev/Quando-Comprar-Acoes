import csv
from datetime import datetime
import os
import sys

class AnaliseAcoesApp:
    CSV_FILE = "resultados_analise.csv"
    
    def __init__(self):
        self.analise = AnaliseAcao(self.CSV_FILE)
        self.analise.criar_cabecalho_se_necessario()
    
    def run(self):
        while True:
            self.mostrar_menu()
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                self.calcular_pvpa()
            elif escolha == "2":
                self.analisar_pvpa()
            elif escolha == "3":
                self.calcular_pl()
            elif escolha == "4":
                self.analisar_pl()
            elif escolha == "5":
                self.calcular_dy()
            elif escolha == "6":
                self.analisar_dy()
            elif escolha == "7":
                self.calcular_valor_intrinseco()
            elif escolha == "8":
                self.analisar_valor_intrinseco()
            elif escolha == "9":
                self.calcular_rsi()
            elif escolha == "10":
                self.analisar_rsi()
            elif escolha == "11":
                self.analise.mostrar_resultados()
            elif escolha == "12":
                self.mostrar_ajuda()
            elif escolha == "13":
                self.sair_programa()
            elif escolha == "14":
                self.fechar_programa()
            else:
                print("\033[31m❌ Opção inválida. Tente novamente.\033[0m")
    
    def mostrar_menu(self):
        print("\n\033[36m--- 📊 Menu de Análise de Ações ---\033[0m")
        print("1. Calcular PVP-PA")
        print("2. Analisar PVP-PA (já calculado)")
        print("3. Calcular P/L")
        print("4. Analisar P/L (já calculado)")
        print("5. Calcular Dividend Yield")
        print("6. Analisar Dividend Yield (já calculado)")
        print("7. Calcular Valor Intrínseco")
        print("8. Analisar Valor Intrínseco (já calculado)")
        print("9. Calcular RSI")
        print("10. Analisar RSI (já calculado)")
        print("11. Ver Histórico de Análises")
        print("12. Saber o que cada opção faz")
        print("13. Sair")
        print("14. Fechar Programa")
    
    def mostrar_ajuda(self):
        print("\n\033[36m--- 📖 Ajuda para as opções ---\033[0m")
        print("1. Calcular PVP-PA: Analisa se a ação está subvalorizada ou supervalorizada a partir dos dados.")
        print("2. Analisar PVP-PA: Forneça o valor já calculado e obtenha a recomendação.")
        print("3. Calcular P/L: Verifica se a ação está barata, com preço justo ou cara a partir dos dados.")
        print("4. Analisar P/L: Forneça o P/L já calculado e veja a análise.")
        print("5. Calcular Dividend Yield: Informa o rendimento em dividendos da ação a partir dos dados.")
        print("6. Analisar Dividend Yield: Forneça o DY já calculado e obtenha a interpretação.")
        print("7. Calcular Valor Intrínseco: Determina o valor real da ação com base em dividendos esperados.")
        print("8. Analisar Valor Intrínseco: Compare valor intrínseco estimado e preço atual.")
        print("9. Calcular RSI: Indica se a ação está sobrecomprada, sobrevendida ou neutra a partir dos dados.")
        print("10. Analisar RSI: Forneça o RSI já calculado e veja a recomendação.")
        print("11. Ver Histórico de Análises: Mostra resultados salvos em CSV.")
        print("12. Saber o que cada opção faz: Mostra esta ajuda.")
    
    def obter_double(self, mensagem):
        while True:
            try:
                entrada = input(f"\033[33m{mensagem}\033[0m").replace(",", ".")
                return float(entrada)
            except ValueError:
                print("\033[31m❌ Erro: Digite um número válido.\033[0m")
    
    def perguntar_salvar(self):
        while True:
            resposta = input("\033[33mDeseja salvar o resultado no arquivo CSV? (s/n): \033[0m").strip().lower()
            if resposta == "s":
                return True
            elif resposta == "n":
                return False
            print("\033[31m❌ Resposta inválida. Digite 's' ou 'n'.\033[0m")
    
    # ------------------- CALCULAR -------------------------
    
    def calcular_pvpa(self):
        preco = self.obter_double("Digite o preço da ação: ")
        vp = self.obter_double("Digite o valor patrimonial da ação: ")
        if vp <= 0:
            print("\033[31mErro: O valor patrimonial deve ser maior que zero.\033[0m")
            return
        pvpa = preco / vp
        status = "subvalorizada" if pvpa < 1 else "com preço justo" if pvpa == 1 else "supervalorizada"
        resultado = f"📊 PVP-PA: {pvpa:.2f} → A ação está {status}."
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Calcular PVP-PA", resultado)
    
    def calcular_pl(self):
        preco = self.obter_double("Digite o preço da ação: ")
        lpa = self.obter_double("Digite o lucro por ação (LPA): ")
        if lpa <= 0:
            print("\033[31mErro: O LPA deve ser maior que zero.\033[0m")
            return
        pl = preco / lpa
        status = "barata" if pl < 10 else "com preço justo" if pl <= 20 else "cara"
        resultado = f"📈 P/L: {pl:.2f} → A ação está {status}."
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Calcular P/L", resultado)
    
    def calcular_dy(self):
        dividendos = self.obter_double("Digite os dividendos anuais por ação: ")
        preco = self.obter_double("Digite o preço da ação: ")
        if preco <= 0:
            print("\033[31mErro: O preço da ação deve ser maior que zero.\033[0m")
            return
        dy = (dividendos / preco) * 100
        status = "um bom rendimento" if dy > 5 else "um rendimento baixo"
        resultado = f"💰 Dividend Yield: {dy:.2f}% → A ação tem {status}."
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Calcular Dividend Yield", resultado)
    
    def calcular_valor_intrinseco(self):
        dividendo = self.obter_double("Digite o dividendo esperado: ")
        taxa_desconto = self.obter_double("Digite a taxa de desconto (ex: 0.10 para 10%): ")
        taxa_crescimento = self.obter_double("Digite a taxa de crescimento (ex: 0.02 para 2%): ")
        if taxa_desconto <= taxa_crescimento:
            print("\033[31mErro: A taxa de desconto deve ser maior que a taxa de crescimento.\033[0m")
            return
        valor = dividendo / (taxa_desconto - taxa_crescimento)
        resultado = f"💎 Valor Intrínseco: R$ {valor:.2f}"
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Calcular Valor Intrínseco", resultado)
    
    def calcular_rsi(self):
        ganhos = self.obter_double("Digite os ganhos médios: ")
        perdas = self.obter_double("Digite as perdas médias: ")
        if perdas == 0:
            resultado = "📊 RSI: 100 → A ação está sobrecomprada."
        else:
            rs = ganhos / perdas
            rsi = 100 - (100 / (1 + rs))
            status = "sobrecomprada" if rsi > 70 else "sobrevendida" if rsi < 30 else "em zona neutra"
            resultado = f"📊 RSI: {rsi:.2f} → A ação está {status}."
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Calcular RSI", resultado)
    
    # ------------------- ANALISAR -------------------------
    
    def analisar_pvpa(self):
        pvpa = self.obter_double("Digite o valor já calculado do PVP-PA: ")
        if pvpa < 1:
            status = "subvalorizada → bom potencial de valorização. Interessante para compra."
        elif pvpa == 1:
            status = "com preço justo → avalie outros fundamentos."
        else:
            status = "supervalorizada → potencial limitado ou sobrevalorização. Atenção antes de comprar."
        resultado = f"📊 PVP-PA: {pvpa:.2f} → {status}"
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Analisar PVP-PA", resultado)
    
    def analisar_pl(self):
        pl = self.obter_double("Digite o valor já calculado do P/L: ")
        if pl < 10:
            status = "barata → bom potencial de alta, interessante para compra."
        elif pl <= 20:
            status = "com preço justo → avalie outros indicadores antes de comprar."
        else:
            status = "cara → pode estar supervalorizada. Avalie o risco antes de entrar."
        resultado = f"📈 P/L: {pl:.2f} → {status}"
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Analisar P/L", resultado)
    
    def analisar_dy(self):
        dy = self.obter_double("Digite o valor já calculado do Dividend Yield (em %): ")
        status = "um bom rendimento → interessante para quem busca renda passiva." if dy > 5 else "um rendimento baixo → avalie se o crescimento compensa o DY mais baixo."
        resultado = f"💰 Dividend Yield: {dy:.2f}% → A ação tem {status}"
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Analisar Dividend Yield", resultado)
    
    def analisar_valor_intrinseco(self):
        valor_intrinseco = self.obter_double("Digite o valor intrínseco estimado: R$ ")
        preco_mercado = self.obter_double("Digite o preço de mercado atual: R$ ")
        if valor_intrinseco > preco_mercado:
            status = "A ação está abaixo do valor intrínseco → potencial de valorização. Interessante para compra."
        else:
            status = "A ação está acima ou no valor intrínseco → crescimento limitado. Avalie bem antes de comprar."
        resultado = f"💎 Valor Intrínseco: R$ {valor_intrinseco:.2f} vs Preço de Mercado: R$ {preco_mercado:.2f} → {status}"
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Analisar Valor Intrínseco", resultado)
    
    def analisar_rsi(self):
        rsi = self.obter_double("Digite o valor já calculado do RSI: ")
        if rsi > 70:
            status = "sobrecomprada → melhor aguardar uma correção antes de comprar."
        elif rsi < 30:
            status = "sobrevendida → pode ser oportunidade de compra."
        else:
            status = "em zona neutra → sem sinais fortes de compra ou venda."
        resultado = f"📊 RSI: {rsi:.2f} → A ação está {status}"
        print(f"\033[32m{resultado}\033[0m")
        if self.perguntar_salvar():
            self.analise.adicionar_resultado("Analisar RSI", resultado)
    
    def sair_programa(self):
        print("\033[31m🔚 Saindo do programa...\033[0m")
        sys.exit(0)
    
    def fechar_programa(self):
        print("\033[31m❌ Fechando imediatamente.\033[0m")
        sys.exit(0)

class AnaliseAcao:
    def __init__(self, arquivo):
        self.arquivo = arquivo
    
    def criar_cabecalho_se_necessario(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Data", "Opção", "Resultado"])
    
    def adicionar_resultado(self, opcao, resultado):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([data, opcao, resultado.replace(",", " ")])
    
    def mostrar_resultados(self):
        if not os.path.exists(self.arquivo):
            print("\033[33mNão há resultados para exibir.\033[0m")
            return
        
        print("\n\033[36m--- Histórico de Análises ---\033[0m")
        with open(self.arquivo, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Pular cabeçalho
            for linha in reader:
                print(f"\033[32m{', '.join(linha)}\033[0m")

if __name__ == "__main__":
    app = AnaliseAcoesApp()
    app.run()
