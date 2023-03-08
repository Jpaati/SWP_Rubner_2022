package FactoryPattern;

public abstract class Pizza{
    public void prepare(){
        System.out.println("Preparing the Pizza");
    }
    public void cutting(){
        System.out.println("Cutting the Pizza");
    }
    public void packing(){
        System.out.println("Packing the Pizza");
    }

    public abstract int getPrice();
    public abstract String getName();
}
