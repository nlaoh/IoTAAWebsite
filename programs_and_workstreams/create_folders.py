import os

# Define the target directory
target_directory = "html_versions"
subdirectories = ["Advocacy", "Practice", "Useful_Links", "Presentations"]
file_to_add = "placeholder.txt"

# Define the starting directory path
starting_directory = r'D:\GIT_REPOS\personalprojects\IoTAAWebsite\programs_and_workstreams\programs'

# Walk through the 'workstreams' directory
for root, dirs, files in os.walk(starting_directory):
    if root == starting_directory:  # This condition ensures we start at the 'workstreams' directory
        for dir in dirs:
            # Iterate through the subdirectories of 'workstreams'
            for subdirectory in subdirectories:
                new_directory_path = os.path.join(root, dir, subdirectory)
                if not os.path.exists(new_directory_path):
                    os.makedirs(new_directory_path)
                # Create a file in the new directory (e.g., placeholder.txt)
                with open(os.path.join(new_directory_path, file_to_add), 'w') as new_file:
                    new_file.write("This file is a placeholder so that the folder is shown on git.")

print("Placeholder files (placeholder.txt) added to new directories in 'workstreams'.")
