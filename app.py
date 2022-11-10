import os
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv

load_dotenv()


url = os.getenv("URL")
headers = {
    "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": os.getenv("X-RapidAPI-Host"),
}


class MainApp(tk.Tk):
    SIZE = "1200x800"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Quizller")
        self.geometry(self.SIZE)
        self.resizable(False, False)
        self.config(bg="#000")


app = MainApp()
app.mainloop()
