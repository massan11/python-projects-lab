import pandas as pd
import argparse

def get_file_path() -> str:
    """Get the file path from the command line."""
    parser = argparse.ArgumentParser(description="Analyze a csv file")
    parser.add_argument("file_path", type=str, help="The path to the csv file")
    args = parser.parse_args()
    return args.file_path

def read_csv(file_path: str) -> pd.DataFrame:
    """Read a csv file and return a dataframe."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"
    
def basic_statistics(df: pd.DataFrame) -> None:
    """Print basic statistics of the dataset."""
    print("\n📊 **Dataset Overview**")
    print(f"Total Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")
    print("\n📝 Column Names and Types:")
    print(df.dtypes)
    
def summarize_numeric_columns(df: pd.DataFrame) -> None:
    """Print summary statistics of numeric columns."""
    print("\n📈 **Numeric Columns Summary:**")
    print(df.describe())

def main():
    file_path = get_file_path()
    df = read_csv(file_path)
    basic_statistics(df)
    summarize_numeric_columns(df)
    
    save_file = input("\n💾 Do you want to save the processed data? (y/n): ")
    if save_file.lower() == "y":
        output_filename = "processed_" + file_path
        df.to_csv(output_filename, index=False)
        print(f"✅ Processed data saved as {output_filename}")
    
if __name__ == "__main__":
    main()
    

    


