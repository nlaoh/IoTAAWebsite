import os

def get_image_filenames(folder_path, extensions=['.jpg', '.png', '.jpeg']):
    image_filenames = []
    
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter for files with allowed extensions
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in extensions]
    
    return image_files

folder_path = r'C:\Users\nlaoh\Desktop\RMIT-PC\HTML_Projects\IOTAA_Volunteering\logo_images\Logos'
image_filenames = get_image_filenames(folder_path)
image_filenames = [string.replace(" ", "_") for string in image_filenames] #This removes whitespace

for filename in image_filenames:
    print(r'<div class="col-xs-4 col-sm-3 col-md-2 mbottom-15 generalUse4-item"> <a href="/"><img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" alt="/" class="img-responsive" /></a> </div>'.format(filename.lower()))