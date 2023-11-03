import os

# Define the target directory
target_directory = "html_versions"

# Define the starting directory path
starting_directory = r'C:\Users\nlaoh\Desktop\RMIT-PC\HTML_Projects\IOTAA_Volunteering\programs_and_workstreams\workstreams'

# Read the HTML content from the template.html file
with open('foundation_html_template.html', 'r') as template_file:
    initial_html_content = template_file.read()

# Walk through all directories starting from the specified path
for root, dirs, files in os.walk(starting_directory):
    if target_directory in dirs:
        # The target directory already exists in this directory
        target_dir = os.path.join(root, target_directory)
        html_file_path = os.path.join(target_dir, 'v1_default.html')

        # Extract the directory name from the path
        directory_name = os.path.basename(root)

        # Replace underscores with spaces in the directory name
        directory_name = directory_name.replace('_', ' ')

        # Create a copy of the initial HTML content
        html_content = initial_html_content

        # Replace [Placeholder] with the directory name in the HTML content
        html_content = html_content.replace('[Placeholder]', directory_name)

        with open(html_file_path, 'w') as html_file:
            html_file.write(html_content)

print("v1_default.html files added to existing directories in html_versions")
