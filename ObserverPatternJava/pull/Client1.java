package ObserverPatternJava.pull;

public class Client1 implements Observer{

    @Override
    public void update(WeatherStataion s) {
        System.out.println("Client1 got notified: " + s.getHumidity());
    }
    
}
