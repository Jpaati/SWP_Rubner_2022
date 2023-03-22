package ObserverPatternJava.pull;

public class Client2 implements Observer{

    @Override
    public void update(WeatherStataion s) {
        System.out.println("Client2 got notified:" + s.getTemp());
    }
    
}
