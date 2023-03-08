package FactoryPattern;

public abstract class PizzeriaFactory {
    
    public Pizza makePizza(String type, double price){
        Pizza p = createPizza(type, price);
        p.prepare();
        p.cutting();
        p.packing();
        System.out.println("ICH BIN FERTIG");
        return p;
    }
    abstract Pizza createPizza(String type, double price);
}
