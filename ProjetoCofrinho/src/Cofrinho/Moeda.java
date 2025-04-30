package Cofrinho;
public abstract class Moeda {
    protected String pais;
    protected double valor;

    public Moeda(String pais, double valor) {
        this.pais = pais;
        this.valor = valor;
    }

    public abstract double converterParaReal();

    @Override
    public String toString() {
        return String.format("%s - Valor: %.2f", pais, valor);
    }
}