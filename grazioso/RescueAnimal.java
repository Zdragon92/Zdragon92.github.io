

import java.lang.String;

public class RescueAnimal {

    // Instance variables
    private String name;
    private String animalType;
    private String gender;
    // Changed age to int for age in years
    private int age;
    // Changed weight to double
    private double weight;
    private String acquisitionDate;
    private String acquisitionCountry;
    private String trainingStatus;
    private boolean reserved;
    private String inServiceCountry;


    // Constructor
    public RescueAnimal() {
    }


    public String getName() {
        return name;
    }


    public void setName(String name) {
        this.name = name;
    }


    public String getAnimalType() {
        return animalType;
    }


    public void setAnimalType(String animalType) {
        this.animalType = animalType;
    }


    public String getGender() {
        return gender;
    }


    public void setGender(String gender) {
        this.gender = gender;
    }


    public int getAge() {
        return age;
    }


    public void setAge(int age) {
        this.age = age;
    }


    public double getWeight() {
        return weight;
    }


    public void setWeight(double weight) {
        this.weight = weight;
    }


    public String getAcquisitionDate() {
        return acquisitionDate;
    }


    public void setAcquisitionDate(String acquisitionDate) {
        this.acquisitionDate = acquisitionDate;
    }


    public String getAcquisitionLocation() {
        return acquisitionCountry;
    }


    public void setAcquisitionLocation(String acquisitionCountry) {
        this.acquisitionCountry = acquisitionCountry;
    }


    public boolean getReserved() {
        return reserved;
    }


    public void setReserved(boolean reserved) {
        this.reserved = reserved;
    }


    public String getInServiceLocation() {
        return inServiceCountry;
    }


    public void setInServiceCountry(String inServiceCountry) {
        this.inServiceCountry = inServiceCountry;
    }


    public String getTrainingStatus() {
        return trainingStatus;
    }


    public void setTrainingStatus(String trainingStatus) {
        this.trainingStatus = trainingStatus;
    }
}
