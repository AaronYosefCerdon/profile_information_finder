#Define a variable for the information needed.
identify_fullname = input("Please enter a full name to find information: ")
#Declare a variable to track if the input is found in the txt file.
found = False

#Use read and write to display the information of the name chosen.
with open("./profile_list.txt","r") as profile_finder:
	information = profile_finder.read( )
	lines = information.split("\n\n" )  
        # Use a for loop to find the needed name.
        for line in lines:
            if identify_full_name in line:
                # Print the information.
                print("Required Information has been found.")
                print(line.strip( ))
                found = True
                break
# Use an if statement to display an error message when no input is found.
    if not found:
        print(f"No corresponding profile found for {identify_full_name}.")
    
    # Define a variable to ask user to search again.
    another_find = input("\nDo you want to try searching with another name? (yes/no): ")
    
    # Use an if statement to end the search.
    if another_find.lower() == "no":
        print("Thank you for using the profile finder.")
        
		    

