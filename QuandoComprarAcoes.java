import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class AnaliseAcoesApp {

    private static final Scanner scanner = new Scanner(System.in);
    private static final String CSV_FILE = "resultados_analise.csv";
    private static AnaliseAcao analise;

    public static void main(String[] args) {
        analise = new AnaliseAcao(CSV_FILE);

        analise.criarCabecalhoSeNecessario();

        while (true) {
            mostrarMenu();
            System.out.print("Escolha uma opção: ");
            String escolha = scanner.nextLine();

            switch (escolha) {
                case "1" -> calcularPvpa();
                case "2" -> analisarPvpa();
                case "3" -> calcularPl();
                case "4" -> analisarPl();
                case "5" -> calcularDy();
                case "6" -> analisarDy();
                case "7" -> calcularValorIntrinseco();
                case "8" -> analisarValorIntrinseco();
                case "9" -> calcularRsi();
                case "10" -> analisarRsi();
                case "11" -> analise.mostrarResultados();
                case "12" -> mostrarAjuda();
                case "13" -> sairPrograma();
                case "14" -> fecharPrograma();
                default -> System.out.println("\u001B[31m❌ Opção inválida. Tente novamente.\u001B[0m");
            }
        }
    }

    private static void mostrarMenu() {
        System.out.println("\n\u001B[36m--- 📊 Menu de Análise de Ações ---\u001B[0m");
        System.out.println("1. Calcular PVP-PA");
        System.out.println("2. Analisar PVP-PA (já calculado)");
        System.out.println("3. Calcular P/L");
        System.out.println("4. Analisar P/L (já calculado)");
        System.out.println("5. Calcular Dividend Yield");
        System.out.println("6. Analisar Dividend Yield (já calculado)");
        System.out.println("7. Calcular Valor Intrínseco");
        System.out.println("8. Analisar Valor Intrínseco (já calculado)");
        System.out.println("9. Calcular RSI");
        System.out.println("10. Analisar RSI (já calculado)");
        System.out.println("11. Ver Histórico de Análises");
        System.out.println("12. Saber o que cada opção faz");
        System.out.println("13. Sair");
        System.out.println("14. Fechar Programa");
    }

    private static void mostrarAjuda() {
        System.out.println("\n\u001B[36m--- 📖 Ajuda para as opções ---\u001B[0m");
        System.out.println("1. Calcular PVP-PA: Analisa se a ação está subvalorizada ou supervalorizada a partir dos dados.");
        System.out.println("2. Analisar PVP-PA: Forneça o valor já calculado e obtenha a recomendação.");
        System.out.println("3. Calcular P/L: Verifica se a ação está barata, com preço justo ou cara a partir dos dados.");
        System.out.println("4. Analisar P/L: Forneça o P/L já calculado e veja a análise.");
        System.out.println("5. Calcular Dividend Yield: Informa o rendimento em dividendos da ação a partir dos dados.");
        System.out.println("6. Analisar Dividend Yield: Forneça o DY já calculado e obtenha a interpretação.");
        System.out.println("7. Calcular Valor Intrínseco: Determina o valor real da ação com base em dividendos esperados.");
        System.out.println("8. Analisar Valor Intrínseco: Compare valor intrínseco estimado e preço atual.");
        System.out.println("9. Calcular RSI: Indica se a ação está sobrecomprada, sobrevendida ou neutra a partir dos dados.");
        System.out.println("10. Analisar RSI: Forneça o RSI já calculado e veja a recomendação.");
        System.out.println("11. Ver Histórico de Análises: Mostra resultados salvos em CSV.");
        System.out.println("12. Saber o que cada opção faz: Mostra esta ajuda.");
    }

    private static double obterDouble(String mensagem) {
        while (true) {
            System.out.print("\u001B[33m" + mensagem + "\u001B[0m");
            try {
                String entrada = scanner.nextLine().replace(",", ".");
                return Double.parseDouble(entrada);
            } catch (NumberFormatException e) {
                System.out.println("\u001B[31m❌ Erro: Digite um número válido.\u001B[0m");
            }
        }
    }

    private static boolean perguntarSalvar() {
        while (true) {
            System.out.print("\u001B[33mDeseja salvar o resultado no arquivo CSV? (s/n): \u001B[0m");
            String resposta = scanner.nextLine().trim().toLowerCase();
            if (resposta.equals("s")) return true;
            if (resposta.equals("n")) return false;
            System.out.println("\u001B[31m❌ Resposta inválida. Digite 's' ou 'n'.\u001B[0m");
        }
    }

    // ------------------- CALCULAR -------------------------

    private static void calcularPvpa() {
        double preco = obterDouble("Digite o preço da ação: ");
        double vp = obterDouble("Digite o valor patrimonial da ação: ");
        if (vp <= 0) {
            System.out.println("\u001B[31mErro: O valor patrimonial deve ser maior que zero.\u001B[0m");
            return;
        }
        double pvpa = preco / vp;
        String status = (pvpa < 1) ? "subvalorizada" : (pvpa == 1) ? "com preço justo" : "supervalorizada";
        String resultado = String.format("📊 PVP-PA: %.2f → A ação está %s.", pvpa, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Calcular PVP-PA", resultado);
    }

    private static void calcularPl() {
        double preco = obterDouble("Digite o preço da ação: ");
        double lpa = obterDouble("Digite o lucro por ação (LPA): ");
        if (lpa <= 0) {
            System.out.println("\u001B[31mErro: O LPA deve ser maior que zero.\u001B[0m");
            return;
        }
        double pl = preco / lpa;
        String status = (pl < 10) ? "barata" : (pl <= 20) ? "com preço justo" : "cara";
        String resultado = String.format("📈 P/L: %.2f → A ação está %s.", pl, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Calcular P/L", resultado);
    }

    private static void calcularDy() {
        double dividendos = obterDouble("Digite os dividendos anuais por ação: ");
        double preco = obterDouble("Digite o preço da ação: ");
        if (preco <= 0) {
            System.out.println("\u001B[31mErro: O preço da ação deve ser maior que zero.\u001B[0m");
            return;
        }
        double dy = (dividendos / preco) * 100;
        String status = (dy > 5) ? "um bom rendimento" : "um rendimento baixo";
        String resultado = String.format("💰 Dividend Yield: %.2f%% → A ação tem %s.", dy, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Calcular Dividend Yield", resultado);
    }

    private static void calcularValorIntrinseco() {
        double dividendo = obterDouble("Digite o dividendo esperado: ");
        double taxaDesconto = obterDouble("Digite a taxa de desconto (ex: 0.10 para 10%): ");
        double taxaCrescimento = obterDouble("Digite a taxa de crescimento (ex: 0.02 para 2%): ");
        if (taxaDesconto <= taxaCrescimento) {
            System.out.println("\u001B[31mErro: A taxa de desconto deve ser maior que a taxa de crescimento.\u001B[0m");
            return;
        }
        double valor = dividendo / (taxaDesconto - taxaCrescimento);
        String resultado = String.format("💎 Valor Intrínseco: R$ %.2f", valor);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Calcular Valor Intrínseco", resultado);
    }

    private static void calcularRsi() {
        double ganhos = obterDouble("Digite os ganhos médios: ");
        double perdas = obterDouble("Digite as perdas médias: ");
        String resultado;
        if (perdas == 0) {
            resultado = "📊 RSI: 100 → A ação está sobrecomprada.";
        } else {
            double rs = ganhos / perdas;
            double rsi = 100 - (100 / (1 + rs));
            String status = (rsi > 70) ? "sobrecomprada" : (rsi < 30) ? "sobrevendida" : "em zona neutra";
            resultado = String.format("📊 RSI: %.2f → A ação está %s.", rsi, status);
        }
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Calcular RSI", resultado);
    }

    // ------------------- ANALISAR -------------------------

    private static void analisarPvpa() {
        double pvpa = obterDouble("Digite o valor já calculado do PVP-PA: ");
        String status = (pvpa < 1) ? "subvalorizada → bom potencial de valorização. Interessante para compra."
                                   : (pvpa == 1) ? "com preço justo → avalie outros fundamentos."
                                   : "supervalorizada → potencial limitado ou sobrevalorização. Atenção antes de comprar.";
        String resultado = String.format("📊 PVP-PA: %.2f → %s", pvpa, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Analisar PVP-PA", resultado);
    }

    private static void analisarPl() {
        double pl = obterDouble("Digite o valor já calculado do P/L: ");
        String status = (pl < 10) ? "barata → bom potencial de alta, interessante para compra."
                                  : (pl <= 20) ? "com preço justo → avalie outros indicadores antes de comprar."
                                  : "cara → pode estar supervalorizada. Avalie o risco antes de entrar.";
        String resultado = String.format("📈 P/L: %.2f → %s", pl, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Analisar P/L", resultado);
    }

    private static void analisarDy() {
        double dy = obterDouble("Digite o valor já calculado do Dividend Yield (em %): ");
        String status = (dy > 5) ? "um bom rendimento → interessante para quem busca renda passiva."
                                 : "um rendimento baixo → avalie se o crescimento compensa o DY mais baixo.";
        String resultado = String.format("💰 Dividend Yield: %.2f%% → A ação tem %s", dy, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Analisar Dividend Yield", resultado);
    }

    private static void analisarValorIntrinseco() {
        double valorIntrinseco = obterDouble("Digite o valor intrínseco estimado: R$ ");
        double precoMercado = obterDouble("Digite o preço de mercado atual: R$ ");
        String status = (valorIntrinseco > precoMercado) 
            ? "A ação está abaixo do valor intrínseco → potencial de valorização. Interessante para compra."
            : "A ação está acima ou no valor intrínseco → crescimento limitado. Avalie bem antes de comprar.";
        String resultado = String.format("💎 Valor Intrínseco: R$ %.2f vs Preço de Mercado: R$ %.2f → %s", 
                                          valorIntrinseco, precoMercado, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Analisar Valor Intrínseco", resultado);
    }

    private static void analisarRsi() {
        double rsi = obterDouble("Digite o valor já calculado do RSI: ");
        String status = (rsi > 70) ? "sobrecomprada → melhor aguardar uma correção antes de comprar."
                                   : (rsi < 30) ? "sobrevendida → pode ser oportunidade de compra."
                                   : "em zona neutra → sem sinais fortes de compra ou venda.";
        String resultado = String.format("📊 RSI: %.2f → A ação está %s", rsi, status);
        System.out.println("\u001B[32m" + resultado + "\u001B[0m");
        if (perguntarSalvar()) analise.adicionarResultado("Analisar RSI", resultado);
    }

    private static void sairPrograma() {
        System.out.println("\u001B[31m🔚 Saindo do programa...\u001B[0m");
        System.exit(0);
    }

    private static void fecharPrograma() {
        System.out.println("\u001B[31m❌ Fechando imediatamente.\u001B[0m");
        System.exit(0);
    }
}

/**
 * Classe para gerenciar o histórico de análises e o CSV.
 */
class AnaliseAcao {
    private final String arquivo;
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

    public AnaliseAcao(String arquivo) {
        this.arquivo = arquivo;
    }

    public void criarCabecalhoSeNecessario() {
        File file = new File(arquivo);
        if (!file.exists()) {
            try (PrintWriter writer = new PrintWriter(new FileWriter(arquivo, true))) {
                writer.println("Data,Opção,Resultado");
            } catch (IOException e) {
                System.out.println("\u001B[31mErro ao criar o arquivo CSV: " + e.getMessage() + "\u001B[0m");
            }
        }
    }

    public void adicionarResultado(String opcao, String resultado) {
        String data = LocalDateTime.now().format(formatter);
        try (PrintWriter writer = new PrintWriter(new FileWriter(arquivo, true))) {
            writer.printf("%s,%s,%s%n", data, opcao, resultado.replace(",", " "));
        } catch (IOException e) {
            System.out.println("\u001B[31mErro ao salvar no CSV: " + e.getMessage() + "\u001B[0m");
        }
    }

    public void mostrarResultados() {
        File file = new File(arquivo);
        if (!file.exists()) {
            System.out.println("\u001B[33mNão há resultados para exibir.\u001B[0m");
            return;
        }
        System.out.println("\n\u001B[36m--- Histórico de Análises ---\u001B[0m");
        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {
            String linha;
            boolean header = true;
            while ((linha = br.readLine()) != null) {
                if (header) {
                    header = false;
                    continue;
                }
                System.out.println("\u001B[32m" + linha + "\u001B[0m");
            }
        } catch (IOException e) {
            System.out.println("\u001B[31mErro ao ler o CSV: " + e.getMessage() + "\u001B[0m");
        }
    }
}

