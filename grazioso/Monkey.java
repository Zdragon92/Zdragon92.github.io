public class Monkey extends RescueAnimal {
    
    // Monkey specific variables
    private double tailLength;
    private double bodyLength;
    private double height;
    private String species;
    
    
    public Monkey(String name, String gender, int age,
    double weight, String acquisitionDate, String acquisitionCountry,
    String trainingStatus, boolean reserved, String inServiceCountry,
    String species, double bodyLength, double tailLength, double height) {
        setName(name);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);
        setSpecies(species);
        setBodyLength(bodyLength);
        setTailLength(tailLength);
        setHeight(height);
    }
    
    // Getters and Setters
    public String getSpecies() {
        return species;
    }
    
    public void setSpecies(String monkeySpecies) {
        species = monkeySpecies;
    }

    public double getTailLength() {
        return tailLength;
    }
    
    public void setTailLength(double monkeyTailLenght) {
        tailLength = monkeyTailLenght;
    }

    public double getBodyLength() {
        return bodyLength;
    }
    
    public void setBodyLength(double monkeyBodyLength) {
        bodyLength = monkeyBodyLength;
    }    

    public double getHeight() {
        return height;
    }
    
    public void setHeight(double monkeyHeight) {
        height = monkeyHeight;
    }
}
