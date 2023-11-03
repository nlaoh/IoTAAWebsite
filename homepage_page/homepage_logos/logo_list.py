import os
import random
from PIL import Image #Used to access image size

def get_image_filenames(folder_path, extensions=['.jpg', '.png', '.jpeg']):
    image_filenames = []
    
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter for files with allowed extensions
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in extensions]
    random.shuffle(image_files)

    return image_files


# Provide the path to the folder containing images
folder_path = r'C:\Users\nlaoh\Desktop\RMIT-PC\HTML_Projects\IOTAA_Volunteering\logo_images\Logos'

# Get image filenames
image_filenames = get_image_filenames(folder_path)
image_paths = []
for filename in image_filenames:
    image_paths.append(os.path.join(folder_path, filename)) #This needs to go before the whitespace is removed
image_filenames = [string.replace(" ", "_") for string in image_filenames] #This removes whitespace

# # Print the list of image filenames (FOR TESTING)
# for filename in image_filenames:
#     print(filename)

"""
This is the code to copy the list of html elements in the rotator.
"""
# There are 4 tabs at the start for indentation in the rotator code, change as you like.

# def check_width_greater_than(image_path, max_width):
#     try:
#         image = Image.open(image_path)
#         width, height = image.size
        
#         if width > max_width:
#             return True
#         else:
#             return False
#     except Exception as e:
#         return "Error:", e
    
# def check_height_greater_than(image_path, max_height):
#     try:
#         image = Image.open(image_path)
#         width, height = image.size
        
#         if height > max_height:
#             return True
#         else:
#             return False
#     except Exception as e:
#         return "Error:", e
# for filename in image_filenames:
#     print(r'                <li class="slide"><a href="#"><img alt="" src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" /></a></li>'.format(filename.lower()))

# for filename, image_path in zip(image_filenames, image_paths):
#     max_width = 180  # maximum width
#     max_height = 130  # maximum height
#     width_check = check_width_greater_than(image_path, max_width)
#     height_check = check_height_greater_than(image_path, max_height)
    
#     if width_check and height_check: #width and height exceeds max
#         print(r'                <li class="slide"><a href="#"><img alt="" src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" style="width: 150px;"/></a></li>'.format(filename.lower()))
#     elif width_check: #width exceeds max
#         print(r'                <li class="slide"><a href="#"><img alt="" src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" style="width: 150px;"/></a></li>'.format(filename.lower()))
#     elif height_check: #height exceeds max
#         print(r'                <li class="slide"><a href="#"><img alt="" src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" style="height: 130px;"/></a></li>'.format(filename.lower()))
#     else: #width and height below max
#         print(r'                <li class="slide"><a href="#"><img alt="" src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" /></a></li>'.format(filename.lower()))


"""
This is the code for the flexible image layout implementation.
"""
# 
# for filename in image_filenames:
#     print(r'    <div class="logo">')
#     print(r'        <a href="#"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" alt="{}"></a>'.format(filename.lower(), filename.lower()))
#     print(r'    </div>')

"""
This is the code for the masonry grid image layout implementation.
"""
# 
# for filename in image_filenames:
#     print(r'        <div class="masonry-item"><a href="#"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/{}" alt="{}"></a></div>'.format(filename.lower(), filename.lower()))