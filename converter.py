from PIL import Image
import numpy as np

# Function to convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Function to create an image with embedded binary data
def create_image_with_text_data(text, output_image_path):
    # Convert text to binary
    binary_data = text_to_binary(text)
    
    # Calculate required dimensions for the image
    length = len(binary_data)
    width = int(np.ceil(length ** 0.5))  # Square root for roughly equal width and height
    height = int(np.ceil(length / width))  # Calculate height based on width

    # Create an array for the image with optimized size
    img_array = np.zeros((height, width, 3), dtype=np.uint8)

    # Embed binary data into pixels
    for i in range(length):
        if binary_data[i] == '1':
            img_array[i // width, i % width] = [255, 255, 255]  # White for '1'
        else:
            img_array[i // width, i % width] = [0, 0, 0]        # Black for '0'

    # Create and save the image as PNG
    img = Image.fromarray(img_array)
    img.save(output_image_path)

# Read the content of the text file
with open('input.txt', 'r') as file:
    text_content = file.read()

# Create an image with embedded text data
create_image_with_text_data(text_content, 'output.png')