from PIL import Image
import glob

print(glob.glob("*.png"))

for file in glob.glob("*.png"):
    image = Image.open(file)
    rgb_image = image.convert("RGB")
    rgb_image.save(file.replace("png", "jpg"), quality=100)
