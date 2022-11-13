from classes.Page import Page
import tkinter as tk


class StartPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.create_label("Quzzler", 0, 0, 100, 50, 54, justify="center", fg=self.YELLOW)
        self.create_label("Levels", 1, 0, 100, 50, 24, justify="center")
        space_between_buttons = 150
        for level in ["Easy", "Medium", "Hard"]:
            self.create_button(
                text=level,
                x=space_between_buttons,
                y=280,
                font_size=12,
                command=lambda: self.quit(),
                fg=level == "Easy"
                and self.SUCCESS_COLOR
                or level == "Medium"
                and self.YELLOW
                or self.DANGER_COLOR,
            )
            space_between_buttons += 150

        self.create_label("Categories", 2, 0, 100, 50, 24, justify="center")


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = StartPage(self)
        # p2 = Page2(self)
        # p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

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
