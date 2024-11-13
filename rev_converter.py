from PIL import Image
import numpy as np

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    binary_data = ''
    
    for row in img_array:
        for pixel in row:
            if np.array_equal(pixel[:3], [255, 255, 255]): 
                binary_data += '1'
            elif np.array_equal(pixel[:3], [0, 0, 0]):    
                binary_data += '0'

    chars = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
    
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)

extracted_text = extract_text_from_image('output.png')
print(extracted_text)  