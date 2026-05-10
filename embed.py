from PIL import Image
import random

# Shared configuration
key = 2026
colour_plane = 1
bit_position = 7

cover_image = 'img/flowers.bmp'
secret_file = 'secret.txt'
output_image = 'stego-image.bmp'

# Open image
img = Image.open(cover_image)

width, height = img.size

pixels = img.load()

# Read secret message
with open(secret_file, 'r') as f:
    secret = f.read()

# Convert message to 7-bit binary
message_bits = ''

for char in secret:
    binary = format(ord(char), '07b')
    message_bits += binary

# Create 14-bit length header
length = len(secret)

length_bits = format(length, '014b')

# Final message bits
full_message = length_bits + message_bits