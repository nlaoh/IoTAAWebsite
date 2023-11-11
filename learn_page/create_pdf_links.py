import os

def generate_html_links(directory_path):
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return
    
    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a PDF
        if filename.lower().endswith(".pdf"):
            # Replace whitespaces with underscores and cut the filename (excluding ".pdf") at the 28th character
            display_filename = filename.replace(" ", "_")[:-4][:28] + ".pdf"
            
            # Generate and print the HTML code
            link = f'<a href="{display_filename}" target="_blank">{display_filename}</a>\n<br>'
            print(link)

# Replace 'your_directory_path' with the path to your chosen directory
your_directory_path = r'D:\GIT_REPOS\personalprojects\IoTAAWebsite\learn_page\Advocacy'
generate_html_links(your_directory_path)
