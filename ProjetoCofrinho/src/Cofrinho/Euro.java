package Cofrinho;
public class Euro extends Moeda {
    public Euro(double valor) {
        super("União Europeia", valor);
    }

    @Override
    public double converterParaReal() {
        // Supondo uma taxa de conversão fixa de 5.54 para 1 Euro
        return valor * 5.54;
    }
}