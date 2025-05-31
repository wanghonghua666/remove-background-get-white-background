from rembg import remove
from PIL import Image
import os

# 設定模型為高精度版
os.environ["REMBG_MODEL"] = "isnet-general-use"

input_folder = 'input_images'
output_folder = 'output_images'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.png')):
        with open(os.path.join(input_folder, filename), 'rb') as i:
            input_data = i.read()
            output_data = remove(input_data)
        
        with open('temp.png', 'wb') as o:
            o.write(output_data)

        img = Image.open('temp.png').convert("RGBA")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])

        bg.save(os.path.join(output_folder, filename))
