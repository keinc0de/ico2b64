import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.slider = tk.Scale(self.root, from_=0, to=256, 
                               orient="horizontal")
        self.slider.bind("<ButtonRelease-1>", self.updateValue)
        self.slider.pack()
        self.root.mainloop()

    def updateValue(self, event):
        print(self.slider.get())

app=App()