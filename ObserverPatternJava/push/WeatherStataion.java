package ObserverPatternJava.push;

import java.util.ArrayList;

public class WeatherStataion implements Obserable{
    private int temp;
    private int humidity;

    private ArrayList<Observer> observers;

    public WeatherStataion(){
        observers = new ArrayList<Observer>();
    }

    @Override
    public void update(int temp, int humidity) {
        this.temp = temp;
        this.humidity = humidity;
    }

    @Override
    public void addObserver(Observer obs) {
        this.observers.add(obs);
    }

    //push Variante
    @Override
    public void notifyObserver() {
        for (Observer observer : observers) {
            observer.update(temp, humidity);
        }
    }
    
}
