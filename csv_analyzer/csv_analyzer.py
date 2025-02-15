import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """Read a csv file and return a dataframe."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"

def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a statistical summary of the dataframe."""
    analyz = df.describe()
    return analyz

def write_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """Write a dataframe to a csv file"""
    try:
        df.to_csv(file_path, index=False)
        print(f"Data saved in {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Read a csv file, analyze the data and save the results in a new csv file."""
    file_path = "data_1.csv"
    df = read_csv(file_path)
    analyz = describe_data(df)
    print (analyz)
    write_to_csv(analyz, "data_2.csv")
    
if __name__ == "__main__":
    main()
    


