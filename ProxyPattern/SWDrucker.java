package ProxyPattern;

public class SWDrucker implements Drucker{

    private String druckerName;

    public SWDrucker(String druckerName){
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
