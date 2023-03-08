package FactoryPattern;

public class PizzeriaVipiteno extends PizzeriaFactory{
    private String place = "Vipiteno";

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
