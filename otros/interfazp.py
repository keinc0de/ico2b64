import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from pathlib import Path
from operaciones import MiIcono
from pagina1 import Pagina1


class InterfazP(TkinterDnD.Tk):
    def __init__(self):
        super(InterfazP, self).__init__()
        self.geometry('320x250')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tabs = ttk.Notebook()
        pag1 = ttk.Frame(self.tabs, relief='flat')
        pag2 = ttk.Frame(self.tabs, relief='flat')
        self.tabs.add(pag1, text='img a base64', sticky='wens')
        self.tabs.add(pag2, text='base64 a img', sticky='wens')
        self.tabs.grid(row=0, column=0, sticky='wens')


        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop_archivo)

        # AGREGA PAGINA 1
        self.fm_img2b64 = Pagina1(pag1)
        self.fm_img2b64.grid(row=0, column=0, sticky='wens')
        pag1.columnconfigure(0, weight=1)
        # AGREGA PAGINA 1

    def drop_archivo(self, event):
        ruta_img = event.data
        print('r img:: ', ruta_img)
        nom = Path(ruta_img).name
        # self.mi_ico = MiIcono(ruta_img)
        self.title(nom)
        if ruta_img.startswith('{'):
            ruta_img = ruta_img[1:]
        if ruta_img.endswith('}'):
            ruta_img = ruta_img[:-1]
        print(ruta_img)
        self.fm_img2b64.asigna_imagen(Path(ruta_img).as_posix())
    


if __name__=="__main__":
    app = InterfazP()
    app.mainloop()

    