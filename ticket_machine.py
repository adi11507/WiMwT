try:
    import Tkinter as Tk
except ImportError:
    import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Biletomat")
        self.geometry("1080x680")
        self.title_font = tkfont.Font(family='Helvetica', size=20, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (StartPage, Ticket, Card, SeasonTicket):
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

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=3, sticky="news")

        label = tk.Label(self, text="Biletomat", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        image_pl = Image.open("poland.png")
        photo_pl = ImageTk.PhotoImage(image_pl)
        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        image_en = Image.open("england.png")
        photo_en = ImageTk.PhotoImage(image_en)
        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        button1 = tk.Button(self, text="Bilety jednorazowe", height=5, width=25, font=('Times New Roman', 20, "bold"),
                            bg='gold', command=lambda: controller.show_frame("Ticket"))

        button2 = tk.Button(self, text="Bilety okresowe", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: controller.show_frame("SeasonTicket"))

        button3 = tk.Button(self, text="Doładuj kartę miejską", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"), command=lambda: controller.show_frame("Card"))

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=2, pady=5, padx=40, sticky='se')

        label_karta = tk.Label(self, text="Jeżeli chcesz załadować\n bilet przyłóż kartę do czytnika ->",
                               font=('Times New Roman', 20, "bold"),
                               height=5, width=25, fg='white', bg='blue')

        button1.grid(row=1, pady=30, padx=5, sticky='s')
        button2.grid(row=2, pady=30, padx=5)
        label_karta.grid(row=1, column=2, pady=30, padx=5, sticky='s')
        button3.grid(row=2, column=2, pady=30, padx=5)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


class Ticket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet jednorazowy", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        image_pl = Image.open("poland.png")
        photo_pl = ImageTk.PhotoImage(image_pl)
        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        image_en = Image.open("england.png")
        photo_en = ImageTk.PhotoImage(image_en)
        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button1_1 = tk.Button(self, text="1-przejazd\n linie zwykłe", height=5, width=15, bg='gold',
                              font=('Times New Roman', 20, "bold"))
        button1_2 = tk.Button(self, text="1-godzinny\n linie zwykłe", height=5, width=15, bg='gold',
                              font=('Times New Roman', 20, "bold"))
        button1_3 = tk.Button(self, text="1-godzinny\n linie nocne\n pospieszne", height=5, width=15, bg='gold',
                              font=('Times New Roman', 20, "bold"))
        button1_4 = tk.Button(self, text="24-godzinny\n linie nocne\n pospieszne, zwykłe", height=5, width=15,
                              bg='gold', font=('Times New Roman', 20, "bold"))

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=3, columnspan=2, pady=5)
        button1_1.grid(row=1, column=0, pady=30, padx=50,  sticky='es')
        button1_2.grid(row=2, column=0, pady=30, padx=50, sticky='e')
        button1_3.grid(row=1, column=1, pady=30, padx=50, sticky='ws')
        button1_4.grid(row=2, column=1, pady=30, padx=50, sticky='w')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)

        """
        counter_reduced = 0
        counter_regular = 0

        def on_click_up_reduced():
            global counter_reduced
            counter_reduced += 1
            label_reduced_l.config(text=str(counter_reduced), )

        def on_click_down_reduced():
            global counter_reduced
            if counter_reduced - 1 is not -1:
                counter_reduced -= 1
                label_reduced_l.config(text=str(counter_reduced), )

        label_reduced = tk.Label(self, text='Bilet 1-godzinny ulgowy: ', height=3, width=20, bg='yellow')
        label_reduced.grid(row=1, column=0, columnspan=3, pady=5, padx=5)

        label_reduced_l = tk.Label(self, text=str(counter_reduced), height=3, width=4, bg='yellow')
        label_reduced_l.grid(row=1, column=1, columnspan=2, pady=5)

        btn_reduced_up = tk.Button(self, text="+", command=on_click_up_reduced, height=3, width=4)
        btn_reduced_up.grid(row=1, column=1, columnspan=3, pady=5)

        btn_reduced_down = tk.Button(self, text="-", command=on_click_down_reduced, height=3, width=4)
        btn_reduced_down.grid(row=1, column=2, columnspan=3, pady=5)

        def on_click_up_regular():
            global counter_regular
            counter_regular += 1
            label_regular.config(text='Bilet 1-godzinny normalny:   ' + str(counter_regular))

        def on_click_down_regular():
            global counter_regular
            if counter_regular - 1 is not -1:
                counter_regular -= 1
                label_regular.config(text='Bilet normalny:   ' + str(counter_regular), )

        label_regular = tk.Label(self, text='Bilet normalny:   ' + str(counter_reduced), height=2, width=20,
                                 bg='yellow')
        label_regular.grid(row=2, column=0, pady=5)

        btn_regular_up = tk.Button(self, text="+", command=on_click_up_regular, height=2, width=2)
        btn_regular_up.grid(row=2, column=1, pady=5)

        btn_regular_down = tk.Button(self, text="-", command=on_click_down_regular, height=2, width=2)
        btn_regular_down.grid(row=2, column=2, pady=5)

        button = tk.Button(self, text="Cofnij", height=2, width=25,
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=3, pady=5)

        """


class SeasonTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet okresowy", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        image_pl = Image.open("poland.png")
        photo_pl = ImageTk.PhotoImage(image_pl)
        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        image_en = Image.open("england.png")
        photo_en = ImageTk.PhotoImage(image_en)
        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=3, columnspan=2, pady=5)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


class Card(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Doładuj kartę miejską", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        image_pl = Image.open("poland.png")
        photo_pl = ImageTk.PhotoImage(image_pl)
        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        image_en = Image.open("england.png")
        photo_en = ImageTk.PhotoImage(image_en)
        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=3, columnspan=2, pady=5)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
