import tkinter as tk
from tkinter import ttk
from operaciones import MiIcono
from pprint import pprint


class Pagina1(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super(Pagina1, self).__init__(parent, **kwargs)
        self.parent = parent
        
        # self.columnconfigure(0, weight=1)
        fm1 = tk.Frame(self, bg='red')
        fm1.grid(row=0, column=0, sticky='wen')
        fm1.columnconfigure(1, weight=4)
        # fm1.columnconfigure(1, weight=4)

        #CONTENIDO FM1
        self.lb1 = tk.Label(fm1, text='ESCALA:', anchor='center')
        self.lb1.grid(row=0, column=0)
        #CONTENIDO FM1
        self.escala = tk.IntVar()
        self.scala = tk.Scale(
            fm1, orient='horizontal', variable=self.escala,
            from_=12, to=60, showvalue=False, resolution=4
            # showvalue=True, tickinterval=20
        )
        self.scala.bind('<ButtonRelease-1>', self._escala_muestra_valor)
        self.scala.grid(row=0, column=1, sticky='we')
        self.escala_str = tk.StringVar()
        self.en_escala = ttk.Entry(
            fm1, width=3, justify='center', textvariable=self.escala_str
        )
        self.en_escala.grid(row=0, column=2)
        self.en_escala.bind('<Return>', self._imagen_en_px)
        self.bt_cver = ttk.Button(fm1, text='CVER', width=8, command=self.guarda_imagen_temporal)
        self.bt_cver.grid(row=0, column=3, sticky='we')

        # contenido frame izquierdo
        self.fmm = tk.Frame(self, bg='blue')
        self.fmm.grid(row=1, column=0, sticky='wens')
        self.lb_visor = tk.Label(
            self.fmm, text='VISOR', background='skyblue', anchor='center'
        )
        self.lb_visor.grid(row=0, column=0, sticky='wens')
        self.out_b64 = tk.Text(self.fmm, bg='yellow', height=6, width=12)
        self.out_b64.grid(row=0, column=1, sticky='wens')
        self.fmm.columnconfigure([0,1], weight=1)
        # self.fmm.columnconfigure(0, weight=1)
        self.fmm.rowconfigure(0, weight=1)
        # self.fmm.columnconfigure(1, weight=2)
        # contenido frame izquierdo

        # contenido frame bottom
        fmb = tk.Frame(self, bg='orange')
        fmb.grid(row=2, column=0, sticky='we')
        fmb.columnconfigure([0,1], weight=1)
        fmb.rowconfigure(0, weight=1, minsize=23)
        self.bt_save = ttk.Button(fmb, text='S', width=3, command=self.guarda_json)
        self.bt_save.grid(row=0, column=0, sticky='w')
        self.bt_clip = ttk.Button(fmb, text='COPIAR', command=lambda:self.copiar_texto())
        self.bt_clip.grid(row=0, column=1, sticky='e')
        self.bt_conv = ttk.Button(fmb, text='A BASE64', command=self.convertir_a_base64)
        self.bt_conv.grid(row=0, column=2, sticky='e')
        # contenido frame bottom

        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=6, minsize=100)
        # self.columnconfigure(1, weight=6)

        self._valores_iniciales()

    def _escala_muestra_valor(self, e):
        # print('escala:  ', self.escala.get())
        px = self.escala.get()
        self.escala_str.set(str(px))
        if self.imagen is not None:
            ico = self.mi_icono.para_tk(int(px))
            self.lb_visor.config(image=ico)
            self.lb_visor.update()

    def _imagen_en_px(self, e=None):
        if self.imagen is not None:
            px = int(self.escala_str.get())
            ico = self.mi_icono.para_tk(px)
            self.lb_visor.config(image=ico)
            self.lb_visor.update()


    def _valores_iniciales(self):
        escala = 16
        self.escala.set(16)
        self.escala_str.set(str(escala))
        self.imagen = None
        self.icono = None
        self.texto_clip = None

    def asigna_imagen(self, ruta_img):
        self.imagen = ruta_img
        self.mi_icono = MiIcono(self.imagen)
        self.ico_tk16 = self.mi_icono.para_tk(16)
        self.bt_cver.config(image=self.ico_tk16, compound='left')
        self.bt_cver.update()
        self.ico_tk = self.mi_icono.para_tk(int(self.escala_str.get()))
        self.lb_visor.config(image=self.ico_tk)
        self.lb_visor.update()
    
    def guarda_imagen_temporal(self):
        if self.imagen is not None:
            px = int(self.escala_str.get())
            self.mi_icono.redimensiona_y_guarda(px)
            pprint(self.mi_icono.obten_data())

    def convertir_a_base64(self):
        if self.imagen is not None:
            # px = int(self.escala_str.get())
            img_b64 = self.mi_icono.en_base64()
            self.out_b64.delete(1.0, tk.END)
            self.out_b64.insert(tk.END, img_b64)
            self.out_b64.see(tk.END)
            print('salida')
            self.texto_clip = img_b64

    def copiar_texto(self):
        self.out_b64.tag_add('start', '1.0', 'end')
        self.out_b64.tag_config('start', background='gray10', foreground='yellow')
        print('copiando..')
        self.texto_clip = self.out_b64.get('1.0', 'end')

        # self.out_b64.
        # self.texto_clip = self.out_b64.selection_get()
        self.clipboard_append('nada')
        self.clipboard_clear()
        self.clipboard_append(self.texto_clip)
        print(self.texto_clip)
        # self.out_b64.update()

    def guarda_json(self):
        if self.texto_clip is not None:
            self.mi_icono.json_escribe(self.texto_clip)

    


if __name__=="__main__":
    app = tk.Tk()
    p1 = Pagina1(bg='green')
    p1.grid(row=0, column=0, sticky='wens')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    # app.rowconfigure([0,1,2], weight=1)
    app.geometry('280x150')
    app.mainloop()