import csv
from datetime import datetime
from colorama import Fore, Style, init
import sys

# Inicializa a colorama para melhorar a legibilidade no terminal
init(autoreset=True)

class AnaliseAcao:
    """Classe para representar as análises feitas sobre as ações."""
    def __init__(self, salvar_csv=True):
        self.resultados = []
        self.salvar_csv = salvar_csv  # Define se deve ou não salvar no CSV

    def adicionar_resultado(self, dados):
        """Adiciona um novo resultado à lista de resultados e salva no CSV, se necessário."""
        self.resultados.append(dados)
        if self.salvar_csv:
            self.salvar_dados_csv(dados)

    def salvar_dados_csv(self, dados):
        """Salva os dados da análise em um arquivo CSV."""
        try:
            with open('resultados_analise.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(dados)
        except Exception as e:
            print(Fore.RED + f"Erro ao salvar no CSV: {e}" + Style.RESET_ALL)

    def mostrar_resultados(self):
        """Exibe todos os resultados armazenados."""
        if not self.resultados:
            print(Fore.YELLOW + "Não há resultados para exibir." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "\n--- Histórico de Análises ---" + Style.RESET_ALL)
            for resultado in self.resultados:
                print(f"{Fore.GREEN}{resultado[0]} | {resultado[1]} | {resultado[2]}{Style.RESET_ALL}")


def calcular_pvpa(preco_acao, valor_patrimonial):
    """Calcula o PVP-PA (Preço sobre Valor Patrimonial)."""
    if valor_patrimonial <= 0:
        return Fore.RED + "Erro: O valor patrimonial deve ser maior que zero."
    pvpa = preco_acao / valor_patrimonial
    status = "subvalorizada" if pvpa < 1 else "com preço justo" if pvpa == 1 else "supervalorizada"
    return f"{Fore.GREEN}📊 PVP-PA: {pvpa:.2f} → A ação está {status}."


def calcular_pl(preco_acao, lpa):
    """Calcula o P/L (Preço sobre Lucro)."""
    if lpa <= 0:
        return Fore.RED + "Erro: O LPA deve ser maior que zero."
    pl = preco_acao / lpa
    status = "barata" if pl < 10 else "com preço justo" if pl <= 20 else "cara"
    return f"{Fore.GREEN}📈 P/L: {pl:.2f} → A ação está {status}."


def calcular_dy(dividendos_anuais, preco_acao):
    """Calcula o Dividend Yield (Rendimento de Dividendos)."""
    if preco_acao <= 0:
        return Fore.RED + "Erro: O preço da ação deve ser maior que zero."
    dy = (dividendos_anuais / preco_acao) * 100
    status = "um bom rendimento" if dy > 5 else "um rendimento baixo"
    return f"{Fore.GREEN}💰 Dividend Yield: {dy:.2f}% → A ação tem {status}."


def calcular_valor_intrinseco(dividendo_esperado, taxa_desconto, taxa_crescimento):
    """Calcula o Valor Intrínseco da ação."""
    if taxa_desconto <= taxa_crescimento:
        return Fore.RED + "Erro: A taxa de desconto deve ser maior que a taxa de crescimento."
    valor_intrinseco = dividendo_esperado / (taxa_desconto - taxa_crescimento)
    return f"{Fore.GREEN}💎 Valor Intrínseco: R$ {valor_intrinseco:.2f}"


def calcular_rsi(ganhos, perdas):
    """Calcula o RSI (Índice de Força Relativa)."""
    if perdas == 0:
        return f"{Fore.GREEN}📊 RSI: 100 → A ação está sobrecomprada."
    rs = ganhos / perdas
    rsi = 100 - (100 / (1 + rs))
    status = "sobrecomprada" if rsi > 70 else "sobrevendida" if rsi < 30 else "em zona neutra"
    return f"{Fore.GREEN}📊 RSI: {rsi:.2f} → A ação está {status}."


def obter_float(mensagem):
    """Lê e valida entradas numéricas do usuário."""
    while True:
        try:
            return float(input(Fore.YELLOW + mensagem + Style.RESET_ALL).replace(",", "."))
        except ValueError:
            print(Fore.RED + "❌ Erro: Digite um número válido." + Style.RESET_ALL)


def perguntar_salvar_resultado():
    """Pergunta ao usuário se deseja salvar o resultado no CSV."""
    while True:
        resposta = input(Fore.YELLOW + "Deseja salvar o resultado no arquivo CSV? (s/n): " + Style.RESET_ALL).strip().lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        print(Fore.RED + "❌ Resposta inválida. Digite 's' para sim ou 'n' para não." + Style.RESET_ALL)


def mostrar_ajuda():
    """Exibe explicações sobre cada opção do menu."""
    print(Fore.CYAN + "\n--- 📖 Ajuda para as opções ---" + Style.RESET_ALL)
    print("1. Calcular PVP-PA: Analisa se a ação está subvalorizada ou supervalorizada.")
    print("2. Calcular P/L: Verifica se a ação está barata, com preço justo ou cara.")
    print("3. Calcular Dividend Yield: Informa o rendimento em dividendos da ação.")
    print("4. Calcular Valor Intrínseco: Determina o valor real da ação com base em dividendos esperados.")
    print("5. Calcular RSI: Indica se a ação está sobrecomprada, sobrevendida ou em zona neutra.")
    print("6. Sair: Encerra o programa.")
    print("7. Fechar Programa: Fecha imediatamente o programa.")
    print("8. Saber o que cada opção faz: Mostra a descrição de cada cálculo disponível.")


def menu():
    """Interface do menu interativo."""
    salvar_csv = True  # Por padrão, salvará no CSV
    analise = AnaliseAcao(salvar_csv)  # Instancia a classe para gerenciar resultados

    opcoes = {
        "1": ("Calcular PVP-PA", lambda: calcular_pvpa(
            obter_float("Digite o preço da ação: "), obter_float("Digite o valor patrimonial da ação: "))),
        "2": ("Calcular P/L", lambda: calcular_pl(
            obter_float("Digite o preço da ação: "), obter_float("Digite o lucro por ação (LPA): "))),
        "3": ("Calcular Dividend Yield", lambda: calcular_dy(
            obter_float("Digite os dividendos anuais por ação: "), obter_float("Digite o preço da ação: "))),
        "4": ("Calcular Valor Intrínseco", lambda: calcular_valor_intrinseco(
            obter_float("Digite o dividendo esperado: "), obter_float("Digite a taxa de desconto (ex: 0.10 para 10%): "),
            obter_float("Digite a taxa de crescimento (ex: 0.02 para 2%): "))),
        "5": ("Calcular RSI", lambda: calcular_rsi(
            obter_float("Digite os ganhos médios: "), obter_float("Digite as perdas médias: "))),
        "6": ("Sair", lambda: sys.exit(Fore.RED + "🔚 Saindo do programa...")),
        "7": ("Fechar Programa", lambda: sys.exit(Fore.RED + "❌ Fechando imediatamente.")),
        "8": ("Saber o que cada opção faz", mostrar_ajuda),
        "9": ("Ver Histórico de Análises", lambda: analise.mostrar_resultados())
    }

    while True:
        print(Fore.CYAN + "\n--- 📊 Menu de Análise de Ações ---" + Style.RESET_ALL)
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave}. {descricao}")

        escolha = input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL)

        if escolha in opcoes:
            resultado = opcoes[escolha][1]()
            if resultado:
                print(resultado)
                # Pergunta ao usuário se deseja salvar o resultado
                if perguntar_salvar_resultado():
                    analise.adicionar_resultado([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), opcoes[escolha][0], resultado])
        else:
            print(Fore.RED + "❌ Opção inválida. Tente novamente." + Style.RESET_ALL)


# ======================== EXECUÇÃO ========================

if __name__ == "__main__":
    # Verifica se o arquivo CSV existe, caso contrário cria o cabeçalho
    try:
        with open('resultados_analise.csv', mode='r'):
            pass
    except FileNotFoundError:
        with open('resultados_analise.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Data", "Opção", "Resultado"])

    menu()
