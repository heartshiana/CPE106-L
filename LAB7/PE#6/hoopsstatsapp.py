from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(dataframe):
    for column in ['FG', '3PT', 'FT']:
        # Split the column into makes and attempts
        makes_attempts = dataframe[column].str.split('-', expand=True)
        makes_attempts.columns = [f"{column}M", f"{column}A"]
        
        # Insert new columns into the dataframe
        dataframe = pd.concat([dataframe, makes_attempts], axis=1)
        
        # Remove the original column
        dataframe.drop(column, axis=1, inplace=True)
        
    return dataframe

def main():
    """Loads the data frame, cleans it, prints it, creates the view, and starts the app."""
    # Load the data frame from the CSV file
    frame = pd.read_csv("cleanbrogdonstats.csv")
    
    # Clean the data frame
    cleaned_frame = cleanStats(frame)
    
    # Print the cleaned data frame
    print("Cleaned DataFrame:")
    print(cleaned_frame)
    
    # Create the HoopStatsView with the cleaned data frame
    HoopStatsView(cleaned_frame)

if __name__ == "__main__":
    main()


