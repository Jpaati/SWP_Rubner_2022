package FactoryPattern;

public class PizzeriaBerlin extends PizzeriaFactory{
    private String place = "Berlin";

    @Override
    Pizza createPizza(String type, double price){
        switch(type){
            case "Salami": return new Salami(18, place);
            case "Diavola": return new Diavola(20, place);
            case "Funghi": return new Funghi(19, place);
            case "Calzone": return new Calzone(22, place);
        }
        return null;
    }
}
