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


def cofactor(matrix, i, j):
    # Returns the matrix without the i-th row and j-th column
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinant(matrix):
    # Base case: If the matrix is 2x2, return the determinant directly
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    # Iterate over the first row to calculate the determinant
    for j in range(len(matrix)):
        det += ((-1) ** j) * matrix[0][j] * determinant(cofactor(matrix, 0, j))
    
    return det

# Example usage
#matrix = [
#    [4, -3, 5],
#    [1, 0, 3],
#    [-1, 5, 2]
#]

det = determinant(matrix)
print("Determinant:", det)
