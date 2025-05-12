import java.util.ArrayList;
import java.util.Scanner;
import java.lang.StringIndexOutOfBoundsException;
import java.util.InputMismatchException;

/*
 * Rescue animal program that allows users to view lists of rescue animals,
 * reserve animals, or register a new rescue animal.
 */
public class Driver {
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();
    
    public static void main(String[] args) {
        initializeDogList();
        initializeMonkeyList();
        boolean menuLoop = true;
        Scanner scrn = new Scanner(System.in);
        
        // Loop to get user input
        while (menuLoop) {
            displayMenu();
            char choice = getChar(scrn);
            // Using System.out.println() as Blank lines for readability
            System.out.println();
            switch(choice){
                case '1':
                    System.out.println("Adding new dog to the system.");
                    enterToContinue(scrn);
                    intakeNewDog(scrn);
                    break;
                case '2':
                    System.out.println("Adding new monkey to the system.");
                    enterToContinue(scrn);
                    intakeNewMonkey(scrn);
                    break;
                case '3':
                    System.out.println("Reserving an animal.");
                    enterToContinue(scrn);
                    reserveAnimal(scrn);
                    break;
                case '4':
                    System.out.println("Showing all dogs in the system.");
                    enterToContinue(scrn);
                    printAnimals(dogList,scrn);
                    break;
                case '5':
                    System.out.println("Showing all monkeys in the system.");
                    enterToContinue(scrn);
                    printAnimals(monkeyList,scrn);
                    break;
                case '6':
                    System.out.println("Showing non reserved in service animals.");
                    enterToContinue(scrn);
                    printAnimals(getAvailableList(),scrn);
                    break;
                case 'q':
                    menuLoop = false;
                    scrn.close();
                    System.out.println("Exiting menu");
                    break;
                default:
                    System.out.println("Invalid option");
                    enterToContinue(scrn);
            }
        }
    }

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "male", 1, 25.6, "05-12-2019", "United States", "intake", false, "United States", "German Shepherd");
        Dog dog2 = new Dog("Rex", "male", 3, 35.2, "02-03-2020", "United States", "Phase I", false, "United States", "Great Dane");
        Dog dog3 = new Dog("Bella", "female", 4, 25.6, "12-12-2019", "Canada", "in service", true, "Canada", "Chihuahua");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }

    // Adds monkeys to a list for testing
    public static void initializeMonkeyList() {
        Monkey monkey1 = new Monkey("Andross", "male", 5, 25.6, "05-12-2019", "United States", "intake", false, "United States", "Tamarin", 10.1, 4.5, 19.1);
        Monkey monkey2 = new Monkey("Goku", "male", 6, 35.2, "02-03-2020", "Japan", "in service", false, "United States","Macaque", 12.2, 3.3, 22.1);
        
        monkeyList.add(monkey1);
        monkeyList.add(monkey2);
    }

    // Checks name of new dog to see if it is a duplicate, if not then asks intake questions
    public static void intakeNewDog(Scanner scanner) {
        
    	String prompt = "What is the dog's name?";
        String name = getResponse(scanner, prompt);
       
        if(checkDogName(name) != null) {
            System.out.println("\n\nThis dog is already in our system\n\n");
            enterToContinue(scanner);
            return; //returns to menu
        }
        
        // Ask questions then add dog to list. 
        intakeQuestions("dog", name, scanner);   
    }

    // Checks name of new monkey to see if it is a duplicate, if not then asks intake questions
    public static void intakeNewMonkey(Scanner scanner) {
        String prompt = "What is the monkey's name?";
        String name = getResponse(scanner, prompt);
        
    	if (checkMonkeyName(name) != null){
            System.out.println("\n\nThis monkey is already in our system\n\n");
            enterToContinue(scanner);
            return; //returns to menu
        }
    	
    	// Ask questions then add monkey to list. 
        intakeQuestions("monkey", name, scanner);    
    }
    

    // Creates a list of animals given animal type, and in service country.
    // Then attempt to reserve the first animal given.
    public static void reserveAnimal(Scanner scanner) {
    	String animalName = null;
    	String prompt;
    	String type = "";
    	
    	
        System.out.println("Would you like to reserve a monkey or a dog? (Enter 1 for monkey or 2 for dog)");

        char choiceType = getChar(scanner);
        if (choiceType == '1' || choiceType == '2') {
        	prompt = "Please select your service country.";
        	String choiceCountry = getResponse(scanner, prompt);
        	System.out.println();
        	
        	// Monkeys only search
        	if(choiceType == '1') {
        		type = "monkeys";
        		for (Monkey monkey: monkeyList) {
        			// Take the first available to reserve so long as they in service
            		if (monkey.getInServiceLocation().equalsIgnoreCase(choiceCountry) && monkey.getTrainingStatus().equalsIgnoreCase("in service")) {
                        monkey.setReserved(true);
                        animalName = monkey.getName();
            			break;
            		}
            	}
        	}
        	// Dog only search
        	else {
        		for (Dog dog: dogList) {
        			type = "dogs";
        			// Take the first available to reserve so long as they are in service
        			if (dog.getInServiceLocation().equalsIgnoreCase(choiceCountry) && dog.getTrainingStatus().equalsIgnoreCase("in service")) {
        				dog.setReserved(true);
                        animalName = dog.getName();
            			break;
            		}
            	}
			}
        	
            // If we found an animal output that it has been reserved
            if(animalName != null) {
            	System.out.println(animalName + " has been reserved.");
            }
            
            // In case there are no available animals.
        	else {System.out.println("Sorry there are no in service "+ type + " in the country " + choiceCountry + "." );}
            
        }
        // If user does not select a valid animal type
        else {
        	System.out.println("Invalid animal type " + choiceType + " selected.");
        }
        
        // Exiting reserve system.
        System.out.println();
        System.out.println("returning to main menu.");
        enterToContinue(scanner);
    }

    // Include the animal name, status, acquisition country and if the animal is reserved.
    // based on the listType parameter
    // dog - prints the list of dogs
    // monkey - prints the list of monkeys
    // available - prints a combined list of all animals that are
    // fully trained ("in service") but not reserved 
    public static void printAnimals(ArrayList<?> list, Scanner scanner) {
    	String reserved;
    	
    	for(Object animal:list) {
    		String name = ((RescueAnimal) animal).getName();
    		String status = ((RescueAnimal) animal).getTrainingStatus();
    		// Convert boolean reserved value to string for user to read.
    		if (((RescueAnimal) animal).getReserved() == true) {reserved = "Yes";}
    		else {reserved = "No";}
    		String serviceCountry = ((RescueAnimal) animal).getInServiceLocation();
    		
    		// Output info with new lines after each value
    		System.out.println("Name: " + name + "\nStatus: " + status
    							+ "\nReserved: " + reserved + "\nService Country: " + serviceCountry);
    		System.out.println("------------");
    	}
    	enterToContinue(scanner);
    }


    // Determines if animal is a dog or monkey then asks questions based on species
    private static void intakeQuestions(String type, String name, Scanner scanner){
        // Placeholder variables
    	boolean reserved;
        String gender;
        String acquisitionDate;
        String acquisitionCountry;
        String status;        
        String serviceCountry;
        String prompt;
        int age;
        double weight;
        // Validation lists
        String[] validSpecies = {"capuchin", "quenon", "macaque", "marmoset",
                "squirrel monkey", "tamarin"};
        String[] validStatuses = {"Intake", "Phase I", "Phase II", "Phase III",
                "Phase IV", "Phase V", "In Service", "Farm"};
       
        // Print line for readability
        System.out.println();
        
        prompt = "What is " + name + "'s gender? ";
        gender = getResponse(scanner, prompt);

        System.out.println();
        
        prompt = "When was " + name + "'s acquisition date? ";
        acquisitionDate = getResponse(scanner, prompt);
        
        System.out.println();

        prompt = "What country was " + name + " accuried in? ";
        acquisitionCountry = getResponse(scanner, prompt);
        
        System.out.println();

        prompt = "What is " + name + "'s training status? ";
        // Loop to check if status is correct
        do {status = getResponse(scanner, prompt);}
        while (validate(status, validStatuses) == false);
        
        System.out.println();

        System.out.println("Is " + name + " reserved? (Enter y for yes). ");
        // Take the first character of next input. If it is y then mark as reserved
        // Otherwise assume it is not.
        if (getChar(scanner) == 'y') {
            reserved = true;
            System.out.println(name + " is now reserved.");
        }
        else {
            reserved = false;
            System.out.println(name + " will not be reserved.");
        }
        
        System.out.println();
        
        prompt = "What counrty is " + name + " in service? ";
        serviceCountry = getResponse(scanner, prompt);
        
        prompt = "What is " + name + "'s age? (Rounds down to whole year)";
        do{
        	System.out.println();
        	age = (int)Math.floor(getPositiveNumber(prompt, scanner));
        	// invalid input message
        	if(age < 1) {
        		System.out.println(name + "'s age must be at least 1.");
        	}
        }
        while(age < 1);
        System.out.println(name + "'s age is " + age);
        System.out.println();

        prompt ="What is " + name + "'s weight? ";
        weight = getPositiveNumber(prompt, scanner);
        
        System.out.println();

        // Ask dog specific questions then create and add new dog
        if (type.equals("dog")) {
        	prompt = "What is "+ name + "'s breed? ";
            String breed = getResponse(scanner, prompt);

            // Create Dog object and add to dog list.
            Dog newDog = new Dog(name, gender, age, weight, acquisitionDate,
                acquisitionCountry, status, reserved, serviceCountry, breed);
            dogList.add(newDog);
        }
        
        // Ask monkey specific questions then create and add new monkey
        else {
            // Monkey specific variables
            double tailLength;
            double height;
            double bodyLength;
            String species;        

            prompt = "What is "+ name + "'s species? ";
            
            // Loop to check if status is correct
            do {species = getResponse(scanner, prompt);}
            while (validate(species, validSpecies) == false);
            
            System.out.println();

            prompt = "What is " + name + "'s body length? ";
            bodyLength = getPositiveNumber(prompt, scanner);
            
            System.out.println();

            prompt = "What is " + name + "'s tail length? ";
            tailLength = getPositiveNumber(prompt, scanner);
            
            System.out.println();

            prompt = "What is " + name + "'s height? ";
            height = getPositiveNumber(prompt, scanner);

            // To reset scanner 
            // scanner.nextLine();
            
            // Create new monkey object and add to monkey list
            Monkey newMonkey = new Monkey(name, gender, age, weight, acquisitionDate,
                   acquisitionCountry, status, reserved, serviceCountry, species,
                   bodyLength, tailLength, height);
            monkeyList.add(newMonkey);
        }
        
        // Successful intake screen
        System.out.println();
        System.out.println(name + " successfully added to the " + type + " list");
        enterToContinue(scanner);
    }
    
    // Check to see if the user provided a valid training status or species
    private static boolean validate(String status, String[] list){

        // Check each species if we get a match the leave loop as true
        for (String validStatus : list) {
            if (status.equalsIgnoreCase(validStatus)) {
                return true;
            }
        }
        // If we get here then given statues did not match show valid statuses and allow user to try again
        System.out.println(status + " is an invalid input.");
        System.out.println();
        System.out.println("Valid inputs are...");
        for (String validInput : list) {
            System.out.print("\"" + validInput + "\", ");
        }
        System.out.println();
        System.out.println("Please enter a valid input.");
        return false;
    }
    
    // Creates a temp list of available animals
    private static ArrayList<RescueAnimal> getAvailableList() {
    	ArrayList<RescueAnimal> templist = new ArrayList<RescueAnimal>();
    	
    	// Check then add available monkeys that are in service
    	for(RescueAnimal animal:monkeyList) {
    		if (animal.getReserved() == false && animal.getTrainingStatus().equalsIgnoreCase("in service")) {
    			templist.add(animal);
    		}
    	}
    	// Repeat for available Dogs that are in service
    	for(RescueAnimal animal:dogList) {
    		if (animal.getReserved() == false && animal.getTrainingStatus().equalsIgnoreCase("in service")) {
    			templist.add(animal);
    		}
    	}
    
    	return templist;
    }
    	
    
    // Pause screen for allowing user to read output
    private static void enterToContinue(Scanner scanner) {
        System.out.println("Press enter to continue.");
        scanner.nextLine();
    }

    // Name checking for duplicates. If we find the animal return the animal object.
    private static Dog checkDogName(String name) {
        for(Dog dog:dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                return dog; // If we find the name
            }
        }
        return null; // If we don't find the name
	}
        
    private static Monkey checkMonkeyName(String name) {
        for(Monkey monkey:monkeyList) {
            if(monkey.getName().equalsIgnoreCase(name)) {
                return monkey; // If we find the name
            }
        }
        return null; // If we don't find the name
	}
       
    // Gets a char input from user
    // If nothing is entered, return an invalid menu choice
    private static char getChar(Scanner scanner) {
	  // Preset choice as an invalid menu choice
	  char choice = 'z';
	  
	  try {
		  choice = scanner.nextLine().charAt(0);
  		
		} catch (StringIndexOutOfBoundsException e) {
			// Stops error from user leaving an empty input
			// error messages handled in the methods that call this
		}
	  
	  return choice;
    }
    
    // Ensures the user does not leave a question blank
    private static String getResponse(Scanner scanner, String prompt) {
	  // Preset choice as an invalid menu choice
	  String response = "";
	  
	  while(response.equals("")) {
		  System.out.println(prompt);
		  response = scanner.nextLine();
		  
		  // incase the user leaves the line blank
		  if(response.strip().equals("")) {
			  System.out.println("Please answer the question.");
			  System.out.println();
		  }
	  }
	  
	  return response;
    }
 
    // Ensures that that the user inputs a number above zero
    private static double getPositiveNumber(String prompt, Scanner scanner) {

	    double input = -1.0;
	
		  do {
			try {
				System.out.println(prompt);
				input = scanner.nextDouble();
				
				if(Double.compare(input, 0.01) < 0) {
					System.out.println("Number must be larger than 0");
				}
				
			} catch (InputMismatchException e) {
				// If the user does not enter in a number
				System.out.println("Please enter a number.");
				System.out.println();
				
			} finally {
				// Always clear the scanner for the next input 
				scanner.nextLine();
			}
		}
		while(Double.compare(input, 0.01) < 0);
		  return input;
	  }
}