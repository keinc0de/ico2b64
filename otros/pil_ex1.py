import base64
from PIL import Image
from io import BytesIO


img1 = 'mas_20p_v2.ico'
img1 = 'lupa_20p.jpg'
# OPCION 1 ico
with open(img1, 'rb') as image_file:
    data = base64.b64encode(image_file.read())
    texto = data.decode('utf-8')
    print(texto)

#OPCION 2
