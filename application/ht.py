import os

def work():
    # Replace this with the path to your folder containing the images
    image_folder_path = 'D:/FInance Flash/application/templates'

    # This is the path to the HTML file that will be created
    html_file_path = 'D:/FInance Flash/application/templates/res.html'

    # Open the HTML file for writing
    with open(html_file_path, 'w') as html_file:
        # Write the initial part of the HTML file
        html_file.write('<!DOCTYPE html>\n<html>\n<body>\n')

        # Get the list of all image files in the folder
        image_files = [f for f in os.listdir(image_folder_path) if f.endswith(".png")]

        # For each image file, write an HTML <img> tag to the HTML file
        for image_file in image_files:
            html_file.write(f'<img src="{image_file}" width="600px" height="300px">\n')

        # Write the final part of the HTML file
        html_file.write('</body>\n</html>')

work()