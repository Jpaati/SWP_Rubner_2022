package ObserverPatternJava;

public class Client2 implements Observer{

    @Override
    public void notifyObservers(int temp, int humidity) {
        System.out.println("Client2 got notified:" + temp + humidity);
    }
    
}
