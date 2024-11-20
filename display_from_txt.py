#Define a variable for the information needed.
identify_fullname = input("Please enter a full name to find information: ")

#Use read and write to display the information of the name chosen.
with open("./profile_list.txt","r") as profile_finder:
	information = profile_finder.read( )
  
#Print the information.

#Display error message when no information is found.
