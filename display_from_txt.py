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
 
#Display error message when no information is found.
		    
#Ask the user if they want to repeat.
