package FactoryPattern;

public class Salami extends Pizza{

    private int _price;
    private String _place;

    public Salami (int price, String place){
        this._place = place;
        this._price = price;
    }

    @Override
    public int getPrice() {
        return this._price;
    }

    @Override
    public String getName() {
        return this._place;
    }

}