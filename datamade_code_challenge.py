# author: Janaya Crevier
# date: 11-15-2019
# Spreadsheet manipulation exercise for DataMade code challenge
import pandas as pd

# Read File
us_legislator_file = pd.read_excel("US_Legislators_Original.xlsx", parse_dates=[28])

# Get legislators who are Democrats under age 45
dem_party=['D']
D_under_45 = us_legislator_file[us_legislator_file['party'].isin(dem_party) # filters for Dem reps
& (us_legislator_file["birthdate"] > "11/15/1974")] # filters for under age 45 reps (as of today's date 11-15-2019)

# Output the records
D_under_45.to_excel("D_under_45.xlsx")

# Get legislators who are Republicans with YouTube and Twitter accounts
rep_party=['R']
R_hasYT_hasTwitter = us_legislator_file[us_legislator_file['party'].isin(rep_party) #filters Republican legislators
&(us_legislator_file['youtube_url'].dropna()) #filters those with YouTube accounts (non-null values in the youtube_url field)
&(us_legislator_file['twitter_id'].dropna())] #filters those with Twitter accounts (non-null values in the twitter_id field)

# Output the records
R_hasYT_hasTwitter.to_excel("R_hasYT_hasTwitter.xlsx")


# Written with help from this tutorial from the Towards Data Science blog: https://towardsdatascience.com/intro-to-reading-and-writing-spreadsheets-with-python-b635ae514ab8
# Help also from this run-down of various functions in Python that can be used similar to Excel filtering: https://towardsdatascience.com/replacing-excel-with-python-30aa060d35e
