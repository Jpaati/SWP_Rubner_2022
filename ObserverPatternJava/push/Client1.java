package ObserverPatternJava.push;

public class Client1 implements Observer{

    @Override
    public void update(int temp, int humidity) {
        System.out.println("Client1 got notified: " + temp + " " + humidity);
    }
    
}
