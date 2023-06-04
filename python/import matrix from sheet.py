import os
import pandas as pd

def excel_to_matrix(file_name):
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the file path using the script directory and file name
    file_path = os.path.join(script_dir, file_name)

    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Convert the DataFrame to a matrix (list of lists)
    matrix = df.values.tolist()

    return matrix

# Example usage
file_name = 'test.xlsx'
matrix = excel_to_matrix(file_name)
print(matrix)
