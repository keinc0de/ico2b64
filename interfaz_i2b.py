import tkinter as tk
from tkinter import ttk
from operaciones import MiIcono
from pathlib import Path
from pprint import pprint


class Interfaz(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        super(Interfaz, self).__init__(parent, **kwargs)
        self.parent = parent

        ttks = ttk.Style()
        ttks.theme_use('clam')
        w1 = 'white'
        b1 = '#0E0718'
        fm1 = tk.Frame(self, bg=b1)
        fm1.grid(row=0, column=0, sticky='wen')
        fm1.columnconfigure(1, weight=4)
        #CONTENIDO FM1
        self.lb1 = tk.Label(
            fm1, text='ESCALA:', anchor='center', font=('consolas', 8),
            fg=w1, bg=b1
        )
        self.lb1.grid(row=0, column=0)
        #CONTENIDO FM1
        # self.escala = tk.IntVar()
        self.escala_str = tk.StringVar()
        self.scala = tk.Scale(
            fm1, orient='horizontal', variable=self.escala_str,
            from_=12, to=60, showvalue=False, resolution=1,
            command=self.recorre_escala,
            troughcolor='#686562', bd=0, relief='flat', fg='red', bg='#F0EAD6',
            sliderrelief='flat', borderwidth=0,
            highlightcolor=b1, highlightbackground='#686562', highlightthickness=0,
        )
        # self.scala = ttk.Scale(
        #     fm1, orient='horizontal', variable=self.escala_str,
        #     from_=12, to=60,
        #     command=self.recorre_escala
            # showvalue=True, tickinterval=20
        # )

        # self.scala.bind('<ButtonRelease-1>', self._escala_muestra_valor)
        self.scala.grid(row=0, column=1, sticky='we')
        self.en_escala = tk.Entry(
            fm1, width=3, justify='center', textvariable=self.escala_str,
            background=b1, foreground=w1, relief='flat'
        )
        self.en_escala.grid(row=0, column=2)
        self.en_escala.bind('<Return>', self._imagen_en_px)
        # self.bt_cver = ttk.Button(fm1, text='CVER', width=8, command=self.guarda_imagen_temporal)
        # self.bt_cver.grid(row=0, column=3, sticky='we')

        # contenido frame izquierdo
        self.fmm = tk.Frame(self, bg=w1)
        self.fmm.grid(row=1, column=0, sticky='wens')
        self.lb_visor = tk.Label(
            self.fmm, text='VISOR', bg=b1, anchor='center',
            relief='flat', border=0
        )
        self.lb_visor.grid(row=0, column=0, sticky='wens')
        self.out_b64 = tk.Text(
            self.fmm, height=6, width=12,
            font=('Segoe UI', 10),
            fg='white', bg=b1, relief='flat'
        )
        self.out_b64.grid(row=0, column=1, sticky='wens')
        self.fmm.columnconfigure([0,1], weight=1)
        self.fmm.rowconfigure(0, weight=1)
        # contenido frame izquierdo

        # contenido frame bottom
        fmb = tk.Frame(self, bg=b1)
        fmb.grid(row=2, column=0, sticky='we')
        fmb.columnconfigure([0,1], weight=1)
        fmb.rowconfigure(0, weight=1, minsize=23)
        # self.bt_save = ttk.Button(fmb, text='S', width=3, command=self.guarda_json)
        # self.bt_save.grid(row=0, column=0, sticky='w')
        self.btc = ttk.Button(fmb, text='BN', width=4, padding=0, command=self._cambia_bg)
        self.btc.grid(row=0, column=0, sticky='nw')
        self.bt_conv = ttk.Button(fmb, text='A BASE64', command=self.convertir_a_base64)
        self.bt_conv.grid(row=0, column=1, sticky='e')
        self.bt_conv.config(width=16)
        # self.bt_clip = ttk.Button(fmb, text='COPIAR', command=lambda:self.copiar_texto())
        self.bt_clip = ttk.Button(fmb, text='COPIAR', command=self.copiar_texto_con_limite)
        self.bt_clip.grid(row=0, column=2, sticky='e')
        self.bt_conv.configure(padding=0)
        self.bt_clip.configure(padding=0)
        # contenido frame bottom

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=6, minsize=100)
        self._valores_iniciales()

    def escribe(self, texto, tag, **kwargs):
        self.out_b64.insert('end', texto, tag)
        self.out_b64.tag_config(tag, **kwargs)

    def recorre_escala(self, v=None):
        if self.imagen is not None:
            ico = self.mi_icono.para_tk(int(self.escala_str.get()))
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
        self.escala_str.set(str(escala))
        self.imagen = None
        self.icono = None
        self.texto_clip = None
        self.bg_visor = 'black'
        self.colores = []

    def asigna_imagen(self, ruta_img):
        ruta_img = Path(ruta_img).as_posix()
        if ruta_img.startswith('{'):ruta_img = ruta_img[1:]
        if ruta_img.endswith('}'):ruta_img = ruta_img[:-1]
        self.imagen = ruta_img
        s = {'font':('Consolas', 8), 'foreground':'#F3CC4A'}
        self.escribe(f"{Path(self.imagen).name}\n", tag='a1', **s)
        self.mi_icono = MiIcono(self.imagen)
        self.ico_tk16 = self.mi_icono.para_tk(16)
        self.bt_conv.config(image=self.ico_tk16, compound='left')
        # self.bt_conv.update()
        self.ico_tk = self.mi_icono.para_tk(int(self.escala_str.get()))
        self.lb_visor.config(image=self.ico_tk)
        # self.lb_visor.update()
    
    def guarda_imagen_temporal(self):
        if self.imagen is not None:
            px = int(self.escala_str.get())
            self.mi_icono.redimensiona_y_guarda(px)
            # pprint(self.mi_icono.obten_data())

    def convertir_a_base64(self):
        if self.imagen is not None:
            px = int(self.escala_str.get())
            # img_b64 = self.mi_icono.en_base64()
            self.guarda_imagen_temporal()
            img_b64 = self.mi_icono.convertir_a_base64(self.imagen, px)

            self.out_b64.delete(1.0, tk.END)
            data = self.mi_icono.obten_data()
            s1 = {
                'font':('Consolas', 8, 'bold'),
                'foreground':'#83A696'
            }
            s2 = {
                'font':('segoe UI', 8, 'bold'),
                'foreground':'#EDDEC4'
            }
            # self.escribe('RESOLUSION: ', 'res', foreground='#F4CA16')
            self.escribe(data.get('nombre')+"\n", 'nom', **s2)
            self.escribe('RESOLUSION: ', 'res', **s1)
            self.escribe(f"{data.get('resolusion')} px\n", 'res_', **s2)
            self.escribe('LONGITUD: ', 'lon', **s1)
            self.escribe(f"{data.get('long')}\n", 'lon_', **s2)
            self.escribe('IMG 64: ', 'i64', **s1)
            self.escribe(f"{data.get('resumen64')}\n", 'i64_', **s2)
            self.out_b64.see(tk.END)
            self.copiar_texto()
            # self.texto_clip = img_b64

    def copiar_texto(self):
        if self.imagen is not None:
            img64 = self.mi_icono.data['icono64']
            n = len(img64)
            lineas = []
            valor = 100
            i = 0
            for x in range(int(n/valor)):
                lineas.append(img64[i:i+valor]+"\n")
                i+=100
            if i<n:
                lineas.append(img64[i:])
            self.parent.clipboard_clear()
            # self.parent.clipboard_append(img64)
            self.parent.clipboard_append(''.join(lineas))
            s = {'font':('Consolas', 8), 'foreground':'#C3E734'}
            self.escribe('icono en base64 - copiado al portapapeles\n', 'msg1', **s)

    def copiar_texto_con_limite(self, chars=100):
        if self.imagen is not None:
            img64 = self.mi_icono.data['icono64']
            limite = len(img64)
            # indice = 0
            lm = int(limite/chars)
            lineas = []
            # lineas = [img64[i*chars:(i*chars)+chars]+"\n" for i in int(limite/chars)]
            for i in range(lm):
                lineas.append(img64[i*chars:(i*chars)+chars]+"\n")
            if i<limite:
                lineas.append(img64[i*chars+chars:])

            self.parent.clipboard_clear()
            self.parent.clipboard_append(''.join(lineas))
            s = {'font':('Consolas', 8), 'foreground':'#C3E734'}
            self.escribe('icono en base64 - copiado al portapapeles\n', 'msg1', **s)


    def guarda_json(self):
        if self.texto_clip is not None:
            self.mi_icono.json_escribe(self.texto_clip)

    def _cambia_bg(self):
        self.bg_visor = 'white' if self.bg_visor=='black' else 'black'
        self.lb_visor.config(bg=self.bg_visor)
    


if __name__=="__main__":
    app = tk.Tk()
    p1 = Pagina1(bg='green')
    p1.grid(row=0, column=0, sticky='wens')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    # app.rowconfigure([0,1,2], weight=1)
    app.geometry('280x150')
    app.mainloop()