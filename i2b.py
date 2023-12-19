from interfaz_i2b import Interfaz
from tkinterdnd2 import DND_FILES, TkinterDnD


class Ico2B64(TkinterDnD.Tk):
    def __init__(self):
        super(Ico2B64, self).__init__()
        self.geometry("320x160")
        self.iz = Interfaz(self)
        self.iz.pack(fill='both', expand=1)
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop_archivo)

    def drop_archivo(self, event):
        self.iz.asigna_imagen(event.data)


if __name__=="__main__":
    app = Ico2B64()
    app.mainloop()