import tkinter as tk
from time import sleep

class Sort(tk.Tk):
    def __init__(self, values):
        tk.Tk.__init__(self)
        self.values = values
        self.new_tokens = edit_string(self.values)
        self.all_labels = []
        for i in range(len(self.new_tokens)):
            self.all_labels.append(tk.Label(self, text=self.new_tokens[i]))
            self.all_labels[i].grid(row = 0, column = i)
        self.min_index = 0
        self.min_value = 99999999
        for i in range(len(self.new_tokens)):
            for j in range(i, len(self.new_tokens)):
                if self.new_tokens[j] < self.min_value:
                    self.min_value = self.new_tokens[j]
                    self.min_index = j
                #exchange new_tokens[i] and new_tokens[min_index]
            sleep(1)
            for k in range(len(self.new_tokens)):
                print("jo", k)
                self.all_labels[k].configure(bg="white")
            self.all_labels[i].configure(bg="red")
            self.all_labels[self.min_index].configure(bg="red")
            temp = self.new_tokens[i]
            self.new_tokens[i] = self.new_tokens[self.min_index]
            self.new_tokens[self.min_index] = temp
            print("sorted:", self.new_tokens)
            self.all_labels = []
            for k in range(len(self.new_tokens)):
                self.all_labels.append(tk.Label(self, text=self.new_tokens[k]))
                self.all_labels[k].grid(row=0, column=i)
            print("dooooone")






        self.mainloop()

def edit_string(tokens):
    output = []
    add = ""
    for i in range(len(tokens)):
        if tokens[i] != ",":
            add += tokens[i]
        elif tokens[i] == ",":
            output.append(int(add))
            add = ""
    return output



