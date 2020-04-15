


import csv
import os
# import numpy
# import random

#dir(csv)

# Name data files
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_results.txt")

# Setup variables
Total_Votes = 0

## Declare the empty lists
Candidate_options = []
County_options = []

## Declare the empty dictionary
Candidate_votes = {}

with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)


    # setup for loop to go through data in csv file
    for row in file_reader:
        
        # Count each vote in the CSV file
        Total_Votes += 1
        
        # Extract the candidate name from the csv file
        candidate_name = row[2]
        
        # Add only names to the options list that are not already in the list
        if candidate_name not in Candidate_options:
            Candidate_options.append(candidate_name)

            #start candidate vote counter to zero to start off to begin tracking the candidate's vote count
            Candidate_votes[candidate_name] = 0
            
        else:

            Candidate_votes[candidate_name] +=1

        # Count Votes for each Candidate
        #f candidate_name is Candidate_options

        # Extract the county names from the csv file
        county_names = row[1]

        #Add only county name that are not already on the list
        if county_names not in County_options:
            County_options.append(county_names)

for named_Candidate in Candidate_options:
    vote_percentage = Candidate_votes[named_Candidate]/Total_Votes * 100
    print(f'The candidate {named_Candidate} recieved {vote_percentage:.1f}% of the votes')



# Print total votes
print(f'The total number of votes was:  {Total_Votes}')

    


    # To do:  read and analyze the data here

    # Write down the names of all the candidates.

    # Add a vote count for each candidate.

    # Get the total votes for each candidate.

    # Get the total votes cast for the election.



# # Open the output file

# with open(file_to_save,"w") as outputfile: 

#     #write to outputfile
#     outputfile.write("Counties in the election\n-------------------------\n")
#     outputfile.write("Arapahoe\nDenver\nJefferson")

#     # Output:
#     # Total number of votes cast
#     # A complete list of candidates who received votes
#     # Total number of votes each candidate received
#     # Percentage of votes each candidate won
#     # The winner of the election based on popular vote





# # Close the output file
# outputfile.close

