// Vinícius Gall Paes Leme - RU: 4665342

package Cofrinho;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();

        while (true) {
            System.out.println("\nMENU:");
            System.out.println("1. Adicionar moeda");
            System.out.println("2. Remover moeda");
            System.out.println("3. Listar moedas");
            System.out.println("4. Calcular total em Reais");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");

            int opcao = scanner.nextInt();
            scanner.nextLine();  // Limpar o buffer do scanner

            switch (opcao) {
                case 1:
                    System.out.print("Digite o valor da moeda: ");
                    double valor = scanner.nextDouble();
                    scanner.nextLine();  // Limpar o buffer do scanner

                    System.out.print("Digite o tipo de moeda (Dolar, Euro, Real): ");
                    String tipoMoeda = scanner.nextLine();

                    Moeda novaMoeda;
                    switch (tipoMoeda.toLowerCase()) {
                        case "dolar":
                            novaMoeda = new Dolar(valor);
                            break;
                        case "euro":
                            novaMoeda = new Euro(valor);
                            break;
                        case "real":
                            novaMoeda = new Real(valor);
                            break;
                        default:
                            System.out.println("Tipo de moeda inválido!");
                            continue;  // Volta para o início do loop
                    }

                    cofrinho.adicionarMoeda(novaMoeda);
                    System.out.println("Moeda adicionada com sucesso!");
                    break;

                case 2:
                    System.out.print("Digite o índice da moeda a ser removida: ");
                    int indice = scanner.nextInt();
                    cofrinho.removerMoeda(indice - 1);  // O usuário insere índices a partir de 1
                    break;

                case 3:
                    System.out.println("\nMoedas no cofrinho:");
                    cofrinho.listarMoedas();
                    break;

                case 4:
                    double totalReais = cofrinho.calcularTotalEmReais();
                    System.out.printf("\nTotal em Reais no cofrinho: R$ %.2f\n", totalReais);
                    break;

                case 5:
                    System.out.println("Saindo do programa...");
                    System.exit(0);

                default:
                    System.out.println("Opção inválida!");
                    break;
            }
        }
    }
}
