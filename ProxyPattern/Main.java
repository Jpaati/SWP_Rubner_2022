package ProxyPattern;

public class Main {
    public static void main(String[] args) {
        Drucker sw = new DruckProxy("SW");
        sw.scannen("test@test.at");
        sw.print("Diplomarbeit");

        System.out.println("-------------------------------------");

        Drucker color = new DruckProxy("CO");
        color.scannen("test@test.at");
        color.print("Diplomarbeit");
    }
}
