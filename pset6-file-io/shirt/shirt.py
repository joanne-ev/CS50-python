import sys
import os
from PIL import Image, ImageOps

def main():
    input_img, output_img = image_file_check()
    shirt(input_img, output_img)

def image_file_check():
    # Command line argument check
    if len(sys.argv) < 3:
        sys.exit('Too few arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many arguments')
    else:
        input_img = sys.argv[1].strip().lower()
        output_img = sys.argv[2].strip().lower()

    # Extension check
    valid_ext = ('.jpg', '.jpeg', '.png')
    input_ext = os.path.splitext(input_img)[1]
    output_ext = os.path.splitext(output_img)[1]

    if input_ext not in valid_ext:
        sys.exit('Invalid input')

    if output_ext not in valid_ext:
        sys.exit('Invalid output')

    if input_ext != output_ext:
        sys.exit('Input and output files do not have the same extensions')

    return input_img, output_img


def shirt(input_img, output_img):
    # Open input image
    try:
        image = Image.open(input_img)
    except FileNotFoundError:
        sys.exit('Input does not exist')

    # Open shirt image
    try:
        shirt = Image.open('shirt.png')
    except FileNotFoundError:
        sys.exit('Shirt picture does not exist')

    # Resizing
    image_cropped = ImageOps.fit(image=image, size=(500, 500))
    shirt_resized = ImageOps.fit(image=shirt, size=(500, 500))

    # Overlaying the shirt over the input image
    image_cropped.paste(shirt_resized, shirt_resized)

    # Saving new image
    return image_cropped.save(f'{output_img}')


if __name__ == "__main__":
    main()
