package ObserverPatternJava.pull;

public class Main {

    public static void main(String[] args) {
        WeatherStataion wStataion = new WeatherStataion();
        wStataion.addObserver(new Client1());
        wStataion.addObserver(new Client2());
        wStataion.update(100, 20);
        wStataion.notifyObserver();
    }
    }
   
