import os

def generate_html_links(directory_path, prefix):
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    
    # Get a list of files in the directory with modification times
    files_with_times = [(filename, os.path.getmtime(os.path.join(directory_path, filename))) for filename in os.listdir(directory_path) if filename.lower().endswith(".pdf")]
    
    # Sort the files based on modification times
    sorted_files = sorted(files_with_times, key=lambda x: x[1], reverse=False)
    
    # Iterate through sorted files
    for filename, _ in sorted_files:
        # Replace whitespaces with underscores and cut the filename (excluding ".pdf") at the 28th character
        shortened_filename = filename.replace(" ", "_")[:-4][:28] + ".pdf"
        display_filename = filename[:-4]

        full_filename = prefix + shortened_filename

        # Generate and print the HTML code
        link = f'<a href="{full_filename}" target="_blank">{display_filename}</a>'
        print(link)

# Replace 'your_directory_path' with the path to your chosen directory
your_directory_path = r'D:\GIT_REPOS\personalprojects\IoTAAWebsite\learn_page\Advocacy\water'
resource_manager_path = r'/resource/resmgr/workstream_files/water/'
generate_html_links(your_directory_path, resource_manager_path)
print(resource_manager_path)
