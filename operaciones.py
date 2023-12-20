from pathlib import Path
import base64
from PIL import ImageTk, Image
# import json


class MiIcono:
    def __init__(self, img_ruta):
        img_ruta = Path(img_ruta).as_posix()
        self.img = Image.open(img_ruta)
        self.data = {'ruta': img_ruta, 'nombre':Path(img_ruta).name}

    def size(self, wh):
        if self.img is not None:
            img_r = self.img.resize((wh, wh), Image.LANCZOS)
            self.data['img r'] = img_r
            self.data['resolusion'] = f"{wh}x{wh}"
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
                icono64 = data.decode('utf-8')
                self.data['icono64'] = icono64
                self.data['resumen64'] = f"{icono64[:6]}...{icono64[-6:]}"
                self.data['long'] = len(icono64)
                return icono64
        else:
            self.data['icono64'] = None
            return 'None...'
        
    def convertir_a_base64(self, img_archivo, wh):
        return self.en_base64()
        
    def obten_data(self):
        return self.data
    
    # def json_escribe(self, texto):
    #     d = self.obten_data()
    #     nom = Path(d.get('ruta')).stem
    #     px = d.get('px')
    #     archivo = f"{nom}_{px}px.json"
    #     contenido = {
    #         'tipo':'ICONO-B64',
    #         'resolusion':f"{px}x{px}",
    #         'len':len(texto),
    #         'b64':texto
    #     }
    #     with open(archivo, 'w') as file:
    #         json.dump(contenido, file, indent=4)

