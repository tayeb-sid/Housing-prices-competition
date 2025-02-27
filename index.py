import pandas as pd 

def calculer():
    # Load the datasets
    a = pd.read_csv("./home-data-for-ml-course/sample_submission.csv")
    b = pd.read_csv("./Sumb_Final_Data.csv")

    # Check if the 'SalePrice' column exists in both dataframes
    if 'SalePrice' in a.columns and 'SalePrice' in b.columns:
        # Calculate the absolute differences
        differences = abs(a['SalePrice'] - b['SalePrice'])

        # Count the number of differences greater than 20,000
        count = (differences < 3000).sum()

        # Display the count
        print(f"Count of SalePrice values with a difference greater than 20,000: {count}")
    else:
        print("SalePrice column not found in one or both files.")

# Call the function
calculer()
