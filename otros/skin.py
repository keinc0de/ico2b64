import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from pathlib import Path
from PIL import ImageTk, Image

# operaciones:
# https://stackoverflow.com/questions/42174987/how-do-i-use-the-base64-encoded-image-string-in-tkinter-label


class Skin(TkinterDnD.Tk):
    def __init__(self):
        super(Skin, self).__init__()
        self.geometry('220x360')
        # s = ttk.Style()
        # s.theme_use('winnative')
        # print(s.theme_names())
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tabs = ttk.Notebook()
        pag1 = ttk.Frame(self.tabs, relief='sunken')
        pag2 = ttk.Frame(self.tabs)
        pag1.columnconfigure(1, weight=1)
        pag1.rowconfigure(1, weight=1)
        # pag1.rowconfigure(2, weight=1)

        self.tabs.add(pag1, text='ico a base64', sticky='wens')
        self.tabs.add(pag2, text='base64 ver', sticky='wens')
        self.tabs.grid(row=0, column=0, sticky='wens')
        self.escala = tk.StringVar()
        self.escala.set(str(16))
        self.en_escala = ttk.Entry(pag1, width=3, textvariable=self.escala, justify='right')
        self.en_escala.grid(row=0, column=0)
        self.lb_texto = ttk.Label(pag1, text='nombre icono')
        self.lb_texto.grid(row=0, column=1, sticky='we')
        self.bt_muestra = ttk.Button(pag1, text='a B64', width=12)
        self.bt_muestra.grid(row=0, column=2)
        self.lb_vista = ttk.Label(pag1, background='white', anchor='center')
        self.lb_vista.grid(row=1, column=0, columnspan=3, sticky='wens')
        self.wtexto = tk.Text(pag1, height=6)
        self.wtexto.grid(row=2, column=0, columnspan=3, sticky='wens')

        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop_archivo)

        self._valores()

    def _valores(self):
        self.img = None

    def drop_archivo(self, event):
        e = event.data
        nom = Path(e).name
        self.lb_texto.config(text=nom)
        img = Image.open(e)
        escala = int(self.escala.get())
        img20 = img.resize((escala,escala), Image.LANCZOS)
        self.icono_bt = ImageTk.PhotoImage(img20)
        self.icono_lb = ImageTk.PhotoImage(img.resize((40,40), Image.LANCZOS))
        self.bt_muestra.config(image=self.icono_bt, compound='left')
        self.lb_vista.config(image=self.icono_lb)
        print("eee: ", e)
        # self.refresh()
        # self.bt_muestra.update()
        self.update()

    def refresh(self):
        self.destroy()
        self.__init__()



if __name__=="__main__":
    app = Skin()
    app.mainloop()