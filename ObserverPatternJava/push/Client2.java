package ObserverPatternJava.push;

public class Client2 implements Observer{

    @Override
    public void update(int temp, int humidity) {
        System.out.println("Client2 got notified:" + temp +  " " + humidity);
    }
    
}
