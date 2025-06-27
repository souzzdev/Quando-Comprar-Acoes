# 🌟 **Quando-Comprar-Acoes** 🌟

**Quando-Comprar-Acoes** é uma ferramenta interativa para **análise fundamentalista de ações**, oferecendo cálculos essenciais para ajudar investidores a tomar decisões mais informadas.
O projeto realiza análises com base em indicadores como:

* **PVP-PA (Preço/Valor Patrimonial)**
* **P/L (Preço/Lucro)**
* **Dividend Yield**
* **Valor Intrínseco**
* **RSI (Índice de Força Relativa)**

Tudo isso por meio de uma interface simples no terminal, com possibilidade de **salvar os resultados em um arquivo `.csv`** para consulta futura.

---

## 🧩 **Por que existem duas versões?**

Este projeto está disponível em **Python** e **Java** por dois motivos principais:

1. **Didática e Aprendizado**: Serve como comparação prática entre duas linguagens amplamente utilizadas.
2. **Desempenho e Portabilidade**:

   * A versão em **Python** é ideal para quem quer algo simples e rápido de testar.
   * A versão em **Java** é mais robusta e oferece melhor desempenho em cenários com maior carga de processamento.

> 🔄 Ambas funcionam da mesma forma e produzem os mesmos resultados — escolha a linguagem com a qual você se sente mais confortável ou deseja praticar!

---

## 💡 **Funcionalidades**

* 📊 **PVP-PA**: Avalia se a ação está subvalorizada, com preço justo ou supervalorizada.
* 📈 **P/L**: Verifica se a ação está barata, com preço justo ou cara.
* 💰 **Dividend Yield**: Calcula o rendimento de dividendos.
* 💎 **Valor Intrínseco**: Calcula o valor justo da ação com base em crescimento e retorno esperado.
* ⚖️ **RSI**: Analisa o momento da ação (sobrecomprada, sobrevendida, neutra).
* 💾 **Histórico em CSV**: Resultados podem ser salvos automaticamente ou manualmente.

---

## 🐍 **Como Usar a Versão Python**

### ✅ Pré-requisitos:

* Python 3.7 ou superior
* Biblioteca `colorama`

### 📦 Instalar dependências:

```bash
pip install colorama
````
<h2>▶️ Executar:</h2>
python quando_comprar_acoes.py

<br>

<h2>☕ Como Usar a Versão Java</h2>
✅ Pré-requisitos:
Java 17 ou superior instalado (JDK)

IDE como Eclipse, IntelliJ ou terminal com javac e java

📁 Arquivos:
AnaliseAcoesApp.java

(opcionalmente, separado em múltiplas classes se desejar modularizar)

▶️ Compilar e Executar:
bash
javac AnaliseAcoesApp.java
java AnaliseAcoesApp 
<br>
📂 Saída CSV
Os resultados das análises são armazenados no arquivo:

````
resultados_analise.csv
Formato:

Data,Opção,Resultado
2025-06-27 10:42:03,Calcular P/L,📈 P/L: 9.45 → A ação está barata.
`````
<h2>👨‍💻 Autor</h2>
<p><a href="https://www.linkedin.com/in/guilhermesouzadev">Guilherme Souza 💼</a></p>



