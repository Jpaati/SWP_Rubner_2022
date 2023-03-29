package ProxyPattern;

//Proxy-Element ist Schnittstelle zwischen echter Drucker und Main
// Dient als Türsteher, der etweilige kriterien übrprüft.

public class DruckProxy implements Drucker{

    private Drucker drucker;
    private String druckerName;

    public DruckProxy(String druckerName){
        this.druckerName = druckerName;
    }

    @Override
    public void print(String doc) {
        if(druckerName == "SW" && drucker == null){
            drucker = new SWDrucker(druckerName);
        }else if(druckerName == "CO" && drucker == null){
            drucker = new ColorDrucker(druckerName);
        }
        drucker.print(doc);
    }

    @Override
    public void scannen(String email) {
        if(druckerName == "SW" && drucker == null){
            drucker = new SWDrucker(druckerName);
        }else if(druckerName == "CO" && drucker == null){
            drucker = new ColorDrucker(druckerName);
        }
        drucker.scannen(email);
    }
    
}
