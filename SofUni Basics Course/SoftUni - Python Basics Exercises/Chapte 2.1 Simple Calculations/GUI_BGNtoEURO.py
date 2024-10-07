import tkinter as tk

class Application(tk. Frame):
    def init_(self, master=None):
        super()._init_(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self) :
        self.label = tk.Label(text="Value Converter") # create widgets
        self. numberEntry = tk.Entry()
        self.convertButton = tk.Button(text="Convert", command=self.convert)
        self.output = tk.Label()


def convert(self):
    entry = self.numberEntry.get()

    try:
        value = float(entry)
        result = round(value * 1.96, 2)
        self.output.config(
            text=str(value) + ' BGN = ' + str(result) + ' EUR',
            bg="green", fg="white")
    except ValueError:
        self.output.config(
            text="That's not a number!",
            bg="red", fg="black")

  # create the application
    app = Application()
    app.master.title("BGN to EUR Converter")

    # start the program
    app.mainloop()