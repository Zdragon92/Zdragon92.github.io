
public class Dog extends RescueAnimal {

    // Instance variable
    private String breed;

    // Constructor reordered to ask for unique identifiers last
    public Dog(String name, String gender, int age, double weight,
    String acquisitionDate, String acquisitionCountry, String trainingStatus,
    boolean reserved, String inServiceCountry, String breed) {
        setName(name);
        setBreed(breed);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);

    }

    // Accessor Method
    public String getBreed() {
        return breed;
    }

    // Mutator Method
    public void setBreed(String dogBreed) {
        breed = dogBreed;
    }

}
