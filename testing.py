from PIL import Image
import numpy as np
import math

def zip_to_binary(zip_file_path):
    """Convert a ZIP file to a binary string."""
    with open(zip_file_path, 'rb') as file:
        binary_data = file.read()
    # Convert each byte to its 8-bit binary representation
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string

def create_image_with_zip(zip_path, output_image_path):
    """Create an image from a ZIP file's binary representation."""
    # Convert ZIP file to binary string
    binary_data = zip_to_binary(zip_path)
    
    # Calculate required dimensions for the image
    length = len(binary_data)
    width = int(math.ceil(length ** 0.5))  # Square root for roughly equal width and height
    height = int(math.ceil(length / width))  # Calculate height based on width

    # Create an array for the image with optimized size
    img_array = np.zeros((height, width, 3), dtype=np.uint8)

    # Embed binary data into pixels
    for i in range(length):
        if binary_data[i] == '1':
            img_array[i // width, i % width] = [255, 255, 255]  # White for '1'
        else:
            img_array[i // width, i % width] = [0, 0, 0]        # Black for '0'

    # Create and save the image as PNG (lossless)
    img = Image.fromarray(img_array)
    img.save(output_image_path)
    
    return binary_data

def extract_binary_string_from_image(image_path):
    """Extract a binary string from an image."""
    img = Image.open(image_path)
    img_array = np.array(img)

    binary_data = ''
    
    for row in img_array:
        for pixel in row:
            if np.array_equal(pixel[:3], [255, 255, 255]): 
                binary_data += '1'
            elif np.array_equal(pixel[:3], [0, 0, 0]):    
                binary_data += '0'
    
    return binary_data

def binary_string_to_zip(binary_string, output_zip_path):
    """Convert a binary string back to a ZIP file."""
    # Split the binary string into chunks of 8 bits
    byte_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    
    # Convert each chunk from binary string to an integer and create a bytearray
    byte_array = bytearray(int(chunk, 2) for chunk in byte_chunks)
    
    # Write bytes back to a ZIP file
    with open(output_zip_path, 'wb') as file:
        file.write(byte_array)

# Example usage
if __name__ == "__main__":
    zip_file_path = 'testing.zip'           # Path to your ZIP file
    output_image_path = 'output1.png'        # Path where you want to save the image
    output_zip_path = 'output.zip'        # Path where you want to save the restored ZIP file

    # Step 1: Create an image from ZIP file
    binary_data_created = create_image_with_zip(zip_file_path, output_image_path)

    # Step 2: Extract binary string from the created image
    binary_data_extracted = extract_binary_string_from_image(output_image_path)

    # Step 3: Convert extracted binary string back to ZIP file
    binary_string_to_zip(binary_data_extracted, output_zip_path)

    # Verify that the original and restored ZIP files are identical
    with open(zip_file_path, 'rb') as original_file:
        original_zip_data = original_file.read()

    with open(output_zip_path, 'rb') as restored_file:
        restored_zip_data = restored_file.read()

    if original_zip_data == restored_zip_data:
        print("The extracted ZIP file matches the original.")
    else:
        print("Mismatch between original and restored ZIP files.")