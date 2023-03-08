# csv_writer = csv.writer(f)
# csv_writer.writerows(data)
# fieldnames = ['Name', 'Age', 'Gender']
import csv

data = [
    {'Name': 'John', 'Age': 25, 'Gender': 'Male'},
    {'Name': 'Jane', 'Age': 30, 'Gender': 'Female'}
]

# Open the CSV file in write mode
with open('testcsv.csv', 'w', newline='') as file:
    # Define the field names for the CSV file
    fieldnames = ['Name', 'Age', 'Gender']

    # Create a CSV writer object
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row to the CSV file
    csv_writer.writeheader()

    # Write the data to the CSV file
    csv_writer.writerows(data)
