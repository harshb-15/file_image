from PIL import Image
import numpy as np

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Extract binary data from pixels (assuming same embedding method)
    binary_data = ''
    
    for row in img_array:
        for pixel in row:
            # Check if pixel is white or black based on our encoding
            if np.array_equal(pixel[:3], [255, 255, 255]):  # White pixel represents '1'
                binary_data += '1'
            elif np.array_equal(pixel[:3], [0, 0, 0]):      # Black pixel represents '0'
                binary_data += '0'

    # Convert binary back to text
    chars = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
    
    # Filter out any incomplete bytes at the end and convert to characters
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)

# Extract and print the text from the PNG
extracted_text = extract_text_from_image('output.png')
print(extracted_text)  # This should output the original text content