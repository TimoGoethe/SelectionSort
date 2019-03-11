import tkinter as tk


class Intro():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Eingabe in folgender Form: 4,5,6,2,3")
        self.label.grid()
        self.label1 = tk.Label(self.root, text="Deine Liste:")
        self.label1.grid(row= 1, column=0)
        self.entry1 = tk.Entry(self.root)
        self.entry1.grid(row=1, column=1)
        self.button1 = tk.Button(self.root, text="Confirm", command=self.confirm)
        self.button1.grid(row=2)
        self.root.mainloop()

    def confirm(self):
        self.values = self.entry1.get()
        Sort(self.values)


class Sort():
    def __init__(self, values):
        self.values = values
        self.time = 800
        self.root = tk.Tk()
        self.values2 = []
        self.result = True # show the result just once
        current = ""
        for i in self.values:
            if i == ",":
                try:
                    self.values2.append(int(current))
                    current = ""
                except:
                    print("Eingabe hat falsches Format")
                    current = ""
            else:
                current += i
        try:
            self.values2.append(int(current))
            current = ""
        except:
            print("Eingabe hat falsches Format")
            current = ""

        self.canvas = tk.Canvas(self.root, width = 600, height = 600)
        self.canvas.grid()
        self.size = len(self.values2)
        self.round = 0
        self.show_numbers()


    def show_numbers(self, exchange1=987.43, exchange2=987.46):
        self.width = 600/len(self.values2)
        self.factor = 600/max(self.values2)
        i = 0
        for number in self.values2:
            if number == exchange1 or number == exchange2:
                self.canvas.create_rectangle(i*self.width, 600-number*self.factor, (i+1)*self.width, 600, fill="red")
            else:
                self.canvas.create_rectangle(i * self.width, 600 - number * self.factor, (i + 1) * self.width, 600,
                                             fill="yellow")
            i += 1
        self.root.after(self.time, self.selection_sort) # that's the command you need!!
        self.root.mainloop()


    def selection_sort(self):
        if self.round <= self.size-1:
            min_element = 9999
            min_index = -1
            for j in range(self.round, self.size):
                if self.values2[j] < min_element:
                    min_element = self.values2[j]
                    min_index = j
            temp = self.values2[self.round]
            self.values2[self.round] = min_element
            self.values2[min_index] = temp
            self.round += 1
            self.canvas.delete("all")
            self.show_numbers(min_element, self.values2[min_index])
            self.root.after(self.time, self.show_numbers) # that's the command you need!!
            self.root.mainloop()
        elif self.result:
            self.result = False
            self.show_numbers()


Intro()