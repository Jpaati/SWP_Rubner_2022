package ProxyPattern;

public class ColorDrucker implements Drucker{

    private String druckerName;

    public ColorDrucker(String druckerName){
        this.druckerName = druckerName;
    }

    @Override
    public void print(String doc) {
        System.out.println("Printing the document: " + doc + " on " + druckerName);
    }

    @Override
    public void scannen(String email) {
        System.out.println("Scanning the document on " + druckerName + " and sending to: " + email);
    }
}
