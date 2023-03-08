package FactoryPattern;

public class Main {
    public static void main(String[] args) {
        PizzeriaFactory pb = new PizzeriaBerlin();
        PizzeriaFactory pv = new PizzeriaVipiteno();

        Pizza p1 = pb.createPizza("Salami", 16);
        Pizza p2 = pv.createPizza("Diavola", 18);
    }
}
