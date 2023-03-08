package FactoryPattern;

public class Calzone extends Pizza{
    private int _price;
    private String _place;

    public Calzone (int price, String place){
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
