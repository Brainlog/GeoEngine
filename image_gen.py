from PIL import Image
import numpy as np
import os
import random

# Output directory to save the generated images
output_directory = "Dataset"
os.makedirs(output_directory, exist_ok=True)

# Number of images to generate
num_images = 1000

# Image size (width x height)
image_size = (512, 512)

for i in range(num_images):
    random_pixels = np.random.randint(0, 256, size=(image_size[1], image_size[0], 3), dtype=np.uint8)
    random_image = Image.fromarray(random_pixels)
    image_filename = os.path.join(output_directory, f"random_image_{i}.png")
    random_image.save(image_filename)

print(f"{num_images} random images have been generated and saved in the '{output_directory}' directory.")
