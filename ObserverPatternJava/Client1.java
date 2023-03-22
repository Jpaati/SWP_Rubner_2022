package ObserverPatternJava;

public class Client1 implements Observer{

    @Override
    public void notifyObservers(int temp, int humidity) {
        System.out.println("Client1 got notified: " + temp + humidity);
    }
    
}
