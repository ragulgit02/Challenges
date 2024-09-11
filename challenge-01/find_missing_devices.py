import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file/table_data.xlsx'  # Update with the actual path to your file

# Read the worksheets from the Excel file
employees_df = pd.read_excel(file_path, sheet_name='Employees')
devices_df = pd.read_excel(file_path, sheet_name='Devices')

# Merge data to find employees without a device
merged_df = pd.merge(employees_df, devices_df, left_on='id', right_on='employee_id', how='left', indicator=True)

# Filter employees without a device record
employees_without_device = merged_df[merged_df['_merge'] == 'left_only'][['first_name', 'last_name']]

# Print the output
print("Employees without a recorded device:")
print(employees_without_device)