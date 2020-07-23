# convert image into black-white version
from PIL import Image

img = Image.open('rose.jpg')
contobw = img.convert('L')
contobw.save('rose-bw.jpg')
contobw.show()
