package ObserverPatternJava;

public interface Obserable{
    public void update(int temp, int humidity);
    public void addObserver(Observer obs);
    public void notifyObserver();
}