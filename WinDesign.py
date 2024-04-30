from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Entry

from tkinter.font import Font
from tkinter.ttk import Notebook

class Window:
    FF = "Fira Code"

    def __init__(self) -> None:
        self.__init_tk__()
        self.__init_notebook__()
        self.__init_nb_p1__()
        self.__init_nb_p2__()
        self.__config_btn_setups__()

    def __init_tk__(self):
        self.win = Tk("TKWinRA")
        self.win.title("Cams Recipe App")
        self.win.geometry("500x500")

        ph = PhotoImage(file="./Assets/Pizza_Icon.png")
        self.win.iconphoto(False, ph)

    def __init_notebook__(self):
        self.nb = Notebook(self.win)
        self.nb.place(x=0, y=0, relwidth=1, relheight=1)

        self.nb_p1 = Frame(self.win)
        self.nb_p1.place(x=0, y=0, relwidth=1, relheight=1)

        self.nb_p2 = Frame(self.win)
        self.nb_p2.place(x=0, y=0, relwidth=1, relheight=1)

        self.nb_p3 = Frame(self.win)
        self.nb_p3.place(x=0, y=0, relwidth=1, relheight=1)

        self.nb.add(self.nb_p1, text="Page 1")
        self.nb.add(self.nb_p2, text="Page 2")
        self.nb.add(self.nb_p3, text="Page 3")

    def __init_nb_p1__(self):
        self.lbl_p1_welcome = Label(self.nb_p1, text="Welcome to the Online Recipe App!", font=self.__set_font__(10),)
        self.lbl_p1_welcome.place(x=120, y=10)

        self.btn_p1_login = Button(self.nb_p1, text="Log In", width=20, height=1, font=self.__set_font__(10), cursor="hand2")
        self.btn_p1_login.place(x=150, y=40)

        self.btn_p1_signup = Button(self.nb_p1, text="Sign Up", width=20, height=1, font=self.__set_font__(10), cursor="hand2")
        self.btn_p1_signup.place(x=150, y=70)

    def __init_nb_p2__(self):
        self.lbl_p2_username = Label(self.nb_p2, text="Enter your username", width=30, height=1, font=self.__set_font__(10))
        self.lbl_p2_username.place(x=100, y=10)

        self.ent_p2_username = Entry(self.nb_p2, width=20, font=self.__set_font__(10))
        self.ent_p2_username.place(x=150, y=40)

        self.lbl_p2_password = Label(self.nb_p2, text="Please enter your password", width=30, height=1, font=self.__set_font__(10))
        self.lbl_p2_password.place(x=100, y=70)

        self.ent_p2_password = Entry(self.nb_p2, width=20, font=self.__set_font__(10), show='*')
        self.ent_p2_password.place(x=150, y=100)

        self.btn_p2_login = Button(self.nb_p2, width=20, height=1, font=self.__set_font__(10), text="Login")
        self.btn_p2_login.place(x=150, y=130)
        
        self.btn_p2_forgotpassword = Button(self.nb_p2, width=20, height=1, font=self.__set_font__(10), text="Forgot Password")
        self.btn_p2_forgotpassword.place(x=150, y=160)

        self.btn_p2_back = Button(self.nb_p2, width=20, height=1, font=self.__set_font__(10), text="<< Back")
        self.btn_p2_back.place(x=150, y=190)

    def __set_font__(self, size: int) -> Font:
        return Font(size=size, family="Fira Code")
    
    def __config_btn_setups__(self) -> None:
        self.btn_p1_login.configure(command=self.__btn_p1_login_click__)
        self.btn_p1_signup.configure(command=self.__btn_p1_signup_click__)

    def run(self):
        self.win.mainloop()