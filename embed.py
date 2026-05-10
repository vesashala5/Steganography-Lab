from PIL import Image
import random

# A1 - Shared configuration
key = 2026
colour_plane = 2  # 0=red, 1=green, 2=blue
bit_position = 0   # LSB style

cover_image = 'steg_lab/img/dice.bmp'
secret_file = 'steg_lab/secret.txt'
output_image = 'steg_lab/stego-image.bmp'

# A2 - Open image
img = Image.open(cover_image)
width, height = img.size
pixels = img.load()

# A3 - Create repeatable pixel order
indexes = list(range(width * height))
random.seed(key)
random.shuffle(indexes)

# A4 - Read secret and convert to bits
with open(secret_file, 'r') as f:
    secret = f.read()

# 14-bit length header
length_bits = format(len(secret), '014b')

# 7-bit ASCII encoding
message_bits = ''
for char in secret:
    message_bits += format(ord(char), '07b')

full_message = length_bits + message_bits

# A5 - Embed one bit per pixel
for i in range(len(full_message)):
    pixel_index = indexes[i]

    x = pixel_index % width
    y = pixel_index // width

    pixel = list(pixels[x, y])

    channel_value = pixel[colour_plane]
    binary = format(channel_value, '08b')

    # Replace selected bit
    binary_list = list(binary)
    binary_list[bit_position] = full_message[i]

    new_value = int(''.join(binary_list), 2)
    pixel[colour_plane] = new_value

    pixels[x, y] = tuple(pixel)

# A6 - Save stego image
img.save(output_image)

print("Embedding completed. Stego-image created successfully.")