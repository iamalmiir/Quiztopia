import tkinter as tk


class Page(tk.Frame):
    MAIN_WINDOW_SIZE = "1200x700"
    YELLOW = "#FFDE00"
    DANGER_COLOR = "#E94560"
    BG_COLOR = "#16213E"
    FG_COLOR = "#533483"
    TITLE_FONT = "Comic Sans MS"

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.configure(bg=self.BG_COLOR)

    def create_label(self, text, xx, yy, font, fg=FG_COLOR):
        label = tk.Label(
            self,
            text=text,
            font=font,
            foreground=fg,
            background=self.BG_COLOR,
        )
        label.place(x=xx, y=yy)
        return label

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.create_label(
            text="Quizzler", xx=200, yy=20, font=("Comic Sans MS", 67), fg=self.YELLOW
        )


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        # b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        # b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        # b1.pack(side="left")
        # b2.pack(side="left")
        # b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    MAIN_WINDOW_SIZE = "1200x700"
    root = tk.Tk()
    root.title("Quizzler")
    root.geometry(MAIN_WINDOW_SIZE)
    root.resizable(False, False)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(MAIN_WINDOW_SIZE)
    root.mainloop()
