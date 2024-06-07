import pandas as pd

# Function to read a CSV file
def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to calculate the average of a column
def calculate_average(data, column_name):
    return data[column_name].mean()

# Function to write results to a CSV file
def write_csv(file_path, data):
    data.to_csv(file_path, index=False)

# Main function
def main(input_file, output_file, column_name):
    # Read the data
    data = read_csv(input_file)
    
    # Calculate the average
    average = calculate_average(data, column_name)
    
    # Prepare the result
    result = pd.DataFrame({column_name: [average]})
    
    # Write the result to a CSV file
    write_csv(output_file, result)
    
    print(f"The average of the column '{column_name}' is: {average}")

# Execute the main function
if __name__ == "__main__":
    # Define input and output file paths
    input_file = "input_data.csv"  # Replace with your input file path
    output_file = "output_data.csv"  # Replace with your output file path
    column_name = "numeric_column"  # Replace with your column name

    main(input_file, output_file, column_name)
