from tkinter import Tk
from tkinter import PhotoImage

from tkinter.ttk import Notebook

class Window:
    def __init__(self) -> None:
        self.__init_tk__()
        self.__init_notebook__()
        self.__init_nb_p1__()

    def __init_tk__(self):
        self.tk = Tk("TKWinRA")
        self.tk.title("Cams Recipe App")
        self.tk.geometry("500x500")

        ph = PhotoImage(file="./Assets/Pizza_Icon.png")
        self.tk.iconphoto(False, ph)

    def __init_notebook__(self):
        self.nb = Notebook(self.tk)
        self.nb.place(relx=1, rely=1)

    def __init_nb_p1__(self):
        pass

    def run(self):
        self.tk.mainloop()