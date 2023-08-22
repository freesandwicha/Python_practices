# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 22/8/2023 12:10 pm

import os
import requests

#Check if is a true picture file.
def get_extension(image_url: str) -> str | None :
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
    for ext in extensions:
        if ext in image_url:
        # Whether the current extension ext (from our extensions list) is present in the image_url.
        # The right extensions of pictures should be in the extensions list.
            return ext

    return 'Wrong extensions about this picture...'


def download_image(image_url: str, name: str, folder: str = None):
    if ext:= get_extension(image_url):
        #This uses the walrus operator (:=) to both call the get_extension function and assign its result to the ext variable in a single line
        #This line checks the extension of the image URL:
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception("Image extension could not be located...")

   #Check if name already exists
    if os.path.isfile(image_name):
        raise Exception("The file name already exists...")

    # Download and save images.
    try:
        image_content: bytes = requests.get(image_url).content
        # Download the image
        #.content is  useful because images are binary files, so when we download them, we want the raw bytes and not a string representation.
        with open(image_name, 'wb') as handler:
        #This opens (or creates if it doesn't exist) a file in "binary write" mode.
        #Since images are binary files, we need to open the file in binary mode to write to it. 'wb'=write binary .
        #with makes sure the file is properly closed after it's been written to.
            handler.write(image_content)
        #This writes the downloaded image content (in bytes) to the file.
            print(f'Download: {image_name} successfully!')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_url: str = input('Enter a url: ')
    input_name: str = input('What would you like to name it?')

    print("Downloading...")
    download_image(input_url, input_name, folder='images')
