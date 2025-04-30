package Cofrinho;
public class Dolar extends Moeda {
    public Dolar(double valor) {
        super("Estados Unidos", valor);
    }

    @Override
    public double converterParaReal() {
        // Supondo uma taxa de conversão fixa de 5.14 para 1 Dólar
        return valor * 5.14;
    }
}