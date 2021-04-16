from PIL import Image, ImageFilter
import os

pic_name = "cat.jpg"

image_folder = os.path.dirname(os.path.abspath(__file__))
cat_file = os.path.join(image_folder, pic_name)

try:
  cat = Image.open(cat_file)
except IOError:
  print("Can't open the picture file")
  quit()

blurred = cat.filter(ImageFilter.BLUR)
gray_cat = cat.convert("L")

# gray_cat.show()
# blurred.show()
# cat.show()

gray_cat.save(os.path.join(image_folder, "gray_cat.jpg"))
