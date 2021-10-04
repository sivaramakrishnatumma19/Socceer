
import sys, getopt
import os
import pandas as pd


 
""" 
Main function will read the command line arguments and return the filename
return the filename passed as arguments
"""
def main(argv):
   
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('soccer.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('soccer.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg

   return inputfile

"""
it will verify the input file and read the file using pandas
return the dataframe
"""
def read_csv(inputfile):
   try:
       name, extension = os.path.splitext(inputfile)
       if(extension != '.csv'):
          print('Note: we support only csv files.')
          sys.exit()
       df = pd.read_csv(inputfile)
       return df
   except pd.errors.EmptyDataError:
       print('Note: filename.csv was empty. Skipping.')
       sys.exit()
     
"""
It will read the dataframe and provide the required anlytics
"""
def analytics(df):
    goal_diff = []
    top_10 = pd.DataFrame()
    most_draws = []
    #The team with the smallest difference in 'for' and 'against' goals.
    df['diff'] = df['Goals'] - df['Goals Allowed']
    a = df['diff'].idxmin()
    goal_diff = df.iloc[a,:].tolist()

    #List the top 10 teams with the highest win percentage
    top_10 = df.nlargest(10,'Wins')

    #Full stats for team with the most draws (include all columns available in CSV file)
    b= df['Draws'].idxmax()
    most_draws = df.iloc[b,:].tolist()

    return goal_diff,top_10,most_draws


if __name__ == "__main__":
   filename = main(sys.argv[1:])
   df = read_csv(filename)
   goal_diff,top_10,most_draws = analytics(df)
   print("-"*100)
   print("The team with the smallest difference in 'for' and 'against' goals.")
   print("-"*100)
   print(goal_diff)
   print("-"*100)
   print("The top 10 teams with the highest win percentage")
   print("-"*100)
   print(top_10)
   print("-"*100)
   print("Full stats for team with the most draws")
   print("-"*100)
   print(most_draws)
   print("*"*100)