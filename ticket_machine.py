import tkinter as tk
from tkinter import font as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Biletomat")
        self.geometry("1080x680")
        self.configure(background='white')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Ticket, Card):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Biletomat", font=controller.title_font, fg='white', bg='blue')
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Kup bilet", height=10, width=65,
                            command=lambda: controller.show_frame("Ticket"))
        button2 = tk.Button(self, text="Doładuj kartę", height=10, width=65,
                            command=lambda: controller.show_frame("Card"))
        button1.pack(side="left", padx="20", pady="10")
        button2.pack(side="right", padx="20", pady="10")


class Ticket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Wybierz bilet", font=controller.title_font, fg='white', bg='blue')
        label.pack(side="top", fill="x", pady=10)

        global counter_reduced, counter_regular
        counter_reduced = 0
        counter_regular = 0

        def on_click_up_reduced():
            global counter_reduced
            counter_reduced += 1
            label_reduced.config(text='Bilet ulgowy:   ' + str(counter_reduced),)

        def on_click_down_reduced():
            global counter_reduced
            if counter_reduced - 1 is not -1:
                counter_reduced -= 1
                label_reduced.config(text='Bilet ulgowy:   ' + str(counter_reduced),)

        label_reduced = tk.Label(self, text='Bilet ulgowy:   ' + str(counter_reduced), height=2, width=20)
        label_reduced.pack(side="top", padx=20)

        btn_reduced_up = tk.Button(self, text="+", command=on_click_up_reduced, height=2, width=2)
        btn_reduced_up.pack(side="top")
        btn_reduced_down = tk.Button(self, text="-", command=on_click_down_reduced, height=2, width=2)
        btn_reduced_down.pack()

        def on_click_up_regular():
            global counter_regular
            counter_regular += 1
            label_regular.config(text='Bilet normalny:   ' + str(counter_regular))

        def on_click_down_regular():
            global counter_regular
            if counter_regular-1 is not -1:
                counter_regular -= 1
                label_regular.config(text='Bilet normalny:   ' + str(counter_regular),)

        label_regular = tk.Label(self, text='Bilet normalny:   ' + str(counter_reduced), height=2, width=20)
        label_regular.pack(side="top", padx=20)

        btn_regular_up = tk.Button(self, text="+", command=on_click_up_regular, height=2, width=2)
        btn_regular_up.pack(side="top")
        btn_regular_down = tk.Button(self, text="-", command=on_click_down_regular, height=2, width=2)
        btn_regular_down.pack()

        button = tk.Button(self, text="Cofnij", height=2, width=25,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="bottom", pady=10)


class Card(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Doładuj kartę", font=controller.title_font, fg='white', bg='blue')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Cofnij", height=2, width=25,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="bottom", pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
