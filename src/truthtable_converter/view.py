"""
The basic view for the app
"""
import tkinter as tk
from tkinter import filedialog
import converter_tex as ct
import converter_logism as cl


class GUI:
    showPath = None
    filepath = None

    def __init__(self):
        # set up window
        root = tk.Tk()
        self.showPath = tk.StringVar()
        self.showPath.set("file path")

        root.title("Truth Table Converter")
        root.minsize(300, 300)
        root.geometry("300x300")

        # label
        tk.Label(root, text="").grid(row=0, column=0, padx=0, pady=10)  # spacer
        text = tk.Label(root, text="Select your file to convert.")
        text.grid(row=1, column=0, padx=70, pady=0)
        tk.Label(root, text="").grid(row=2, column=0, padx=0, pady=5)  # spacer

        button = tk.Button(root, text='Open File', command=self.uploadFile)
        button.grid(row=3, column=0, padx=0, pady=0)
        text2 = tk.Label(root, textvariable=self.showPath)
        text2.grid(row=4, column=0, padx=0, pady=0)
        tk.Label(root, text="").grid(row=5, column=0, padx=0, pady=5)  # spacer

        button = tk.Button(root, text='Convert from logism format', command=self.convertFileLogism)
        button.grid(row=6, column=0, padx=0, pady=0)
        button = tk.Button(root, text='Convert from tex format', command=self.convertFileTex)
        button.grid(row=7, column=0, padx=0, pady=0)
        tk.Label(root, text="").grid(row=8, column=0, padx=0, pady=5)  # spacer
        root.mainloop()

    def uploadFile(self):
        self.filepath = filedialog.askopenfilename()
        self.showPath.set("... " + self.filepath[-30:])

    def convertFileLogism(self):
        cl.convert(self.filepath)

    def convertFileTex(self):
        ct.convert(self.filepath)


class MessageBox:
    def __init__(self, message: str):
        root = tk.Tk()

        root.title("Message")
        root.minsize(100, 50)
        root.maxsize(500, 500)
        root.geometry("300x100")

        # label
        tk.Label(root, text="").pack()  # spacer
        tk.Label(root, text="").pack()  # spacer
        text = tk.Label(root, text=message)
        text.pack()
