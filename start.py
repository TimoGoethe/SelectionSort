import tkinter as tk
from sort import Sort

class Start(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label1 = tk.Label(self, text="Deine Liste:")
        self.label1.grid()
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row= 0, column=1)
        self.button1 = tk.Button(self, text="Confirm", command=self.confirm)
        self.button1.grid(row=1)

        self.mainloop()

    def confirm(self):
        self.values = self.entry1.get()
        Sort(self.values)

