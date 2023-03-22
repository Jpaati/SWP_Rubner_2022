package ObserverPatternJava.pull;

public interface Obserable{
    public void update(int temp, int humidity);
    public void addObserver(Observer obs);
    public void notifyObserver();
    public int getTemp();
    public int getHumidity();
}