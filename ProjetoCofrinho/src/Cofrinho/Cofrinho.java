package Cofrinho;
import java.util.ArrayList;

public class Cofrinho {
    private ArrayList<Moeda> moedas;

    public Cofrinho() {
        this.moedas = new ArrayList<>();
    }

    public void adicionarMoeda(Moeda moeda) {
        moedas.add(moeda);
    }

    public void removerMoeda(int indice) {
        if (indice >= 0 && indice < moedas.size()) {
            moedas.remove(indice);
        } else {
            System.out.println("Índice inválido!");
        }
    }

    public void listarMoedas() {
        for (int i = 0; i < moedas.size(); i++) {
            System.out.println((i + 1) + ". " + moedas.get(i));
        }
    }

    public double calcularTotalEmReais() {
        double total = 0;
        for (Moeda moeda : moedas) {
            total += moeda.converterParaReal();
        }
        return total;
    }
}