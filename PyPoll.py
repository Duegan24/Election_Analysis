


import csv
import os
# import numpy
# import random

#dir(csv)

# Name data files
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_results.txt")

with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file
    # for row in file_reader:

    #     print(row)


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

