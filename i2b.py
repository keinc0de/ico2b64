from interfaz_i2b import Interfaz
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk


class Ico2B64(TkinterDnD.Tk):
    def __init__(self):
        super(Ico2B64, self).__init__()
        self.geometry("350x180")
        self.iz = Interfaz(self)
        self.iz.pack(fill='both', expand=1)
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop_archivo)

        self.title('IMG A ICONO(b64)')
        ico = '''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADcklEQVR4nCXO3U9bZQDA4d97zmnpaWmhdIKwIjhAPuZ
        08WPEdcgYwiAQTLboxYLeaFxM0GSJF8Y4jUbjst0sG9GQuDmN4UaTZcapTASmARctjIKjiQ4GdY6vDjZaaE8557xe8A88ecTacvR
        s2jC6FEVFVRWSyXW83mwAFEUhnU6zuWmi6zoej45hZIjHV/B4dLYF8rqxUjH52itHZN/3X8vhoYvS5/PKcz2npLkxJ1cXb8i60B7
        Z2BCSmeQtGQn/LJ+pfUIGg0WysmKH/PHSV1KxbZtEIoll2SzHVyguLmJgcBjDMAiPRrAsC4/HTSqV5s1jx2l6rp6Zf/6g73IvObk
        +FABN01DUre6zoVocDgeRyBThsQlamvcTCPiJRKZQVYX33z1Gz2fnOPPpeVyurC1ACIFAYEtwubJoaqzjoxNnmJ6JUbvnSZLJDfz
        +HJbjK8zO/ktpeRnXro3Sd2UIRQhBMplEShNpmywsLtHe1sQPPw3wULCQkuJC5mK3qazcQWNDiNaOlxi7fgOnQ0PXdTTDyNDW1kq
        Ov4AsPYfDz7fg9nro/fI05RXVmGh0He0klUpz4uN3qK5+hP6B36nZuZOO9ma0xNo6V67rnPx2HCklhxtKaE0lIbuGzvfCWLbN0UM
        1CCS2ZXLgwEF6+rMpL81ne2EARVUF0ZsLhHbl8nJLkNO9ESanFvige5h9jwd4u7OKUxfCTMfuoesaX3wzxtjoTWZjdzA3TTQAVVX
        JD+jsrvCT5VRYSxg4HQ7cuoMX2qpori8nL9fFbGyVyyPzaB4XWQ4NIQSabUvcusbV0UUGw4vseyyfitI8nA7BxcEY3/16m72PBjj
        /SSP9IzGW7m4QDDgxTImUcmsAYEvI8zpYWcuQXM+wnrJoryuipMDDh59P8FZ0gUtDMV7tKCM6t4a0we12oimKYCNt0hQq5lD9dpq
        7fmE8uoSmCR7M97KrzMsDuS7+nJzn6tgiTqfKzHwaaVuEJ+6gSblVWV5N83csgWnauF0aQkDsv/s4sVhNZCgu9HH89aeJr24wOX0
        P3aEAoAmhUlyQzfBEnJGJZY4cfJjm/eWsbNicvPAXv43HeePFKhr2ltGW7QRspm/dxe9z8dTuIOL+UvRsOmN1GRkLiSTP5wShoCq
        wumZg25JtuS4ypiSzaSEEGBkbVVXI0kT3/9lGgiOBDO3wAAAAAElFTkSuQmCC'''
        self.iconphoto(True, tk.PhotoImage(data=ico))

    def drop_archivo(self, event):
        self.iz.asigna_imagen(event.data)


if __name__=="__main__":
    app = Ico2B64()
    app.mainloop()