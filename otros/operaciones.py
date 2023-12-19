from pathlib import Path
import base64
from PIL import ImageTk, Image
import json

class MiIcono:
    def __init__(self, img_ruta):
        self.img = Image.open(img_ruta)
        # self.icono = None
        self.data = {'ruta': img_ruta}

    def size(self, wh):
        if self.img is not None:
            # self.icono = ImageTk.PhotoImage(self.img.resize((wh, wh), Image.LANCZOS))
            img_r = self.img.resize((wh, wh), Image.LANCZOS)
            self.data['img r'] = img_r
            self.data['px'] = wh
            return img_r
        
    def para_tk(self, px=16):
        imgtk = ImageTk.PhotoImage(self.size(px))
        self.data['img tk'] = imgtk
        return imgtk
    
    def redimensiona_y_guarda(self, wh, nombre='img-temporal.png'):
        img = self.size(wh)
        img.save(nombre)

    def en_base64(self, file_temporal='img-temporal.png'):
        if Path(file_temporal).exists():
            with open(file_temporal, 'rb') as img:
                data = base64.b64encode(img.read())
                return data.decode('utf-8')
        else:
            return 'None...'


    

    # def en_base64(self, px=16):
    #     img_bin = self.img.tobytes()
    #     b64_byte = base64.b64encode(img_bin) 
    #     b64_str = b64_byte.decode()
    #     return b64_str
        # print(type(b64_byte), ':tipo::', b64_str)
        # img_str = base64.b64encode(img_bin.getvalue())


        # texto_b64 = base64.b64encode(img_bin.read())
        # self.data['b64'] = texto_b64
        # return texto_b64
    

        # with open(self.size(px), 'rb') as img:
        #     texto_b64 = base64.b64encode(img.read())
        #     self.data['b64'] = texto_b64
        #     return texto_b64
        
    def obten_data(self):
        return self.data
    
    def json_escribe(self, texto):
        d = self.obten_data()
        nom = Path(d.get('ruta')).stem
        px = d.get('px')
        archivo = f"{nom}_{px}px.json"
        contenido = {
            'tipo':'ICONO-B64',
            'resolusion':f"{px}x{px}",
            'len':len(texto),
            'b64':texto
        }
        with open(archivo, 'w') as file:
            json.dump(contenido, file, indent=4)

