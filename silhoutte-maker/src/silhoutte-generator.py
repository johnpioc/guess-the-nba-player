import os
from PIL import Image, ImageOps

input_folder = "raw_player_images"
output_folder = "silhouttes"

os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    if (file_name.endswith(".jpg")):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path).convert("L")

        silhouette = img.point(lambda p: 0 if p < 255 else 255)
        silhouette.save(os.path.join(output_folder, file_name))