import csv

# Define the path to your CSV file (modify as needed)
csv_file_path = "D:\project\data\HOst.csv"

# Open the CSV file in read mode
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Generate HTML table header
    html_content = '<table>\n'
    html_content += '<tr>\n'
    html_content += '<th>Hospital Name</th>\n'
    html_content += '<th>Doctor Name</th>\n'
    html_content += '<th>Specialization</th>\n'
    html_content += '<th>Experience</th>\n'
    html_content += '<th>Slot URL</th>\n'
    html_content += '</tr>\n'

    # Process each row in the CSV file
    for row in reader:
        hospital_name = row['Hospital Name']
        doctor_name = row['Doctor Name']
        specialization = row['Specialization']
        experience = row['Experience']
        slot_url = row['Slot URL']

        # Generate HTML table row with hyperlink
        html_content += f'<tr>\n'
        html_content += f'<td>{hospital_name}</td>\n'
        html_content += f'<td><a href="{slot_url}">{doctor_name}</a></td>\n'
        html_content += f'<td>{specialization}</td>\n'
        html_content += f'<td>{experience}</td>\n'
        html_content += f'<td>{slot_url}</td>\n'
        html_content += '</tr>\n'

    # Close the HTML table
    html_content += '</table>'

# Write the HTML content to a file
html_file_path = "output.html"
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

# Print a message indicating where the HTML file is saved
print(f"HTML content saved to: {html_file_path}")
