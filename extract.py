from PIL import Image
import random

# B1 - Same configuration (must match embed.py exactly)
key = 2026
colour_plane = 2   # must be identical
bit_position = 6   # must be identical

stego_image = 'steg_lab/stego-image.bmp'

# B2 - Open stego image
img = Image.open(stego_image)
width, height = img.size
pixels = img.load()

# B3 - Rebuild shuffled pixel order
indexes = list(range(width * height))
random.seed(key)
random.shuffle(indexes)

# B4 - Read embedded bits
bits = ''

for i in range(width * height):
    pixel_index = indexes[i]

    x = pixel_index % width
    y = pixel_index // width

    pixel = pixels[x, y]
    channel_value = pixel[colour_plane]

    binary = format(channel_value, '08b')
    bits += binary[bit_position]

# B5 - Recover message length (first 14 bits)
length_bits = bits[:14]
message_length = int(length_bits, 2)

# B6 - Decode message (7-bit ASCII)
message_bits = bits[14:14 + (message_length * 7)]

message = ''

for i in range(0, len(message_bits), 7):
    char_bits = message_bits[i:i+7]
    message += chr(int(char_bits, 2))

print("Recovered message:")
print(message)