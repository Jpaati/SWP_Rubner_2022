package ProxyPattern;

public class Main {
    public static void main(String[] args) {
        Drucker SWDrucker = new DruckProxy("SW");
        SWDrucker.scannen("meine@test.at");
        SWDrucker.print("Diplomarbeit");

        System.out.println("-------------------------------------------------------");

        Drucker ColorDrucker = new DruckProxy("CO");
        ColorDrucker.scannen("test@test.at");
        ColorDrucker.print("Diplomarbeit");
    }
}