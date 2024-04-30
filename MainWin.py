from WinDesign import Window

class MainWin(Window):
    def __init__(self) -> None:
        super().__init__()
        self.__config_btn_setups__()

    def __btn_p1_login_click__(self) -> None:
        self.nb.select(self.nb_p2)

    def __btn_p1_signup_click__(self) -> None:
        self.nb.select(self.nb_p3)