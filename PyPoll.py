import csv
import os

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
County_votes = {}

# Open the election data file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Headers
    Headers = next(file_reader)
        
    # setup for loop to go through data in csv file
    for row in file_reader:
 
        # Count each vote in the CSV file
        Total_Votes += 1
        
        # Extract the candidate and county name from the csv file
        candidate_name = row[2]
        county_name = row[1]
        
        # Add only names to the options list that are not already in the list
        if candidate_name not in Candidate_options:
            Candidate_options.append(candidate_name)

            #start candidate vote counter to zero to begin tracking the candidate's vote count
            Candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        Candidate_votes[candidate_name] +=1

        # Add only county names to the options list that are not in the list
        if county_name not in County_options:
            County_options.append(county_name)

            # Start County vote counter to zero to begin tracking the candidate's vote count
            County_votes[county_name] = 0
        
        # Add a vote to the appropriate county
        County_votes[county_name] +=1

#Winning Candidate and Winning Count Tracker Initialization
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results file to place the outputs from the analysis
with open(file_to_save, "w") as election_results_output:

    # Compose Election result string
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {Total_Votes:,}\n"
        f"-------------------------\n")
    
    #Print to terminal
    print(election_results, end="")
    
    # Save to the output file
    election_results_output.write(election_results)

    for candidate in Candidate_votes:
        
        # Retrieve vote count of a candidate
        votes = Candidate_votes[candidate]
        
        # Calculate the percentage of votes
        vote_percentage = float(votes / Total_Votes * 100)
        
        # Print out each candidate's name, vote count, and percentage
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')

        # Votes to terminal
        print(candidate_results)

        # Results saved to output file
        election_results_output.write(candidate_results)

        # Determine the winning vote count and candidate
        # Determine if the vote is great than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If True then set winning_count = votes and winning percent
            winning_count = votes
            winning_candidate = candidate

            #And set the winning_candidate equal to the candidate's name
            winning_percentage = vote_percentage


    # Print winning results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save winning results to output file
    election_results_output.write(winning_candidate_summary)
    
