package Cofrinho;
public class Real extends Moeda {
    public Real(double valor) {
        super("Brasil", valor);
    }

    @Override
    public double converterParaReal() {
        // A moeda Real já está em Reais, então não precisa converter
        return valor;
    }
}