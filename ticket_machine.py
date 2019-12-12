#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        self.counter_reduced = 0
        self.counter_regular = 0
        self.sum = 0

        self.frames = {}
        for F in (StartPage, Ticket, Card, SeasonTicket, OrdinaryOneTicket, OrdinaryHourTicket,
                  HourOrNight, TwentyForHours, ForPay):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def on_click_up(self, label):
        self.counter_reduced += 1
        label.configure(text=str(self.counter_reduced))

    def on_click_down(self, label):
        if (self.counter_reduced-1) is not -1:
            self.counter_reduced -= 1
            label.configure(text=str(self.counter_reduced))

    def on_click_up_r(self, label):
        self.counter_regular += 1
        label.configure(text=str(self.counter_regular))

    def on_click_down_r(self, label):
        if (self.counter_regular - 1) is not -1:
            self.counter_regular -= 1
            label.configure(text=str(self.counter_regular))

    def calculate_sum(self):
        self.sum += self.counter_regular * 3.8 + self.counter_reduced * 1.9
        print(self.sum)


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

        label_karta = tk.Label(self, text="Jeżeli chcesz załadować\n bilet na kartę\n przyłóż ją do czytnika ->",
                               font=('Times New Roman', 20, "bold"),
                               height=5, width=30, fg='white', bg='blue')

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

        button1_1 = tk.Button(self, text="1-przejazd\n linie zwykłe", height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("OrdinaryOneTicket"))
        button1_2 = tk.Button(self, text="1-godzinny\n linie zwykłe", height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("OrdinaryHourTicket"))
        button1_3 = tk.Button(self, text="1-godzinny\n lub jednoprzejazdowy\n linie nocne,\n pospieszne",
                              height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("HourOrNight"))
        button1_4 = tk.Button(self, text="24-godzinny\n linie nocne,\n pospieszne, zwykłe", height=6, width=20,
                              bg='gold', font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("TwentyForHours"))

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=3, columnspan=2, pady=5)
        button1_1.grid(row=1, column=0, pady=30, padx=50, sticky='es')
        button1_2.grid(row=2, column=0, pady=30, padx=50, sticky='e')
        button1_3.grid(row=1, column=1, pady=30, padx=50, sticky='ws')
        button1_4.grid(row=2, column=1, pady=30, padx=50, sticky='w')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


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


class OrdinaryOneTicket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
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
                                command=lambda: controller.show_frame("Ticket"))

        button_back.grid(row=3, columnspan=2, pady=5)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


class OrdinaryHourTicket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
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
                                command=lambda: controller.show_frame("Ticket"))

        label_reduced = tk.Label(self, text='Bilet Ulgowy: ', height=3, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        label_reduced.grid(row=1, column=0, padx=70, pady=5, sticky='es')

        label_reduced_l = tk.Label(self, text=controller.counter_reduced, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_reduced_l.grid(row=1, column=0, padx=5, pady=5, sticky='es')

        btn_reduced_up = tk.Button(self, text="+", command=lambda: controller.on_click_up(label_reduced_l),
                                   height=2, width=3,
                                   font=('Times New Roman', 30, 'bold'))
        btn_reduced_up.grid(row=1, column=1, padx=50, pady=5, sticky='ws')

        btn_reduced_down = tk.Button(self, text="-", command=lambda: controller.on_click_down(label_reduced_l),
                                     height=2, width=3,
                                     font=('Times New Roman', 30, 'bold'))
        btn_reduced_down.grid(row=1, column=1, padx=150, pady=5, sticky="ws")

        label_regular = tk.Label(self, text='Bilet normalny: ', height=3, width=20,
                                 font=('Times New Roman', 20, 'bold'), bg='gold')
        label_regular.grid(row=2, column=0, padx=70, pady=120, sticky='en')

        label_regular_l = tk.Label(self, text=controller.counter_regular, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_regular_l.grid(row=2, column=0, padx=5, pady=120, sticky='en')

        btn_regular_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up_r(label_regular_l))
        btn_regular_up.grid(row=2, column=1, padx=50, pady=120, sticky='wn')

        btn_regular_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down_r(label_regular_l))
        btn_regular_down.grid(row=2, column=1, padx=150, pady=120, sticky='wn')

        btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                               command=lambda: [controller.show_frame("ForPay"), controller.calculate_sum()],
                               font=('Times New Roman', 20, 'bold'))

        btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

        button_back.grid(row=3, columnspan=2, pady=5)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


class ForPay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj płatności", font=controller.title_font, fg='white', bg='blue')
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
                                command=lambda: controller.show_frame("OrdinaryHourTicket"))

        label_pay = tk.Label(self, text='Do zapłaty\n pozostało', height=3, width=20,
                             font=('Times New Roman', 20, 'bold'), bg='gold')
        label_pay.grid(row=2, column=0, padx=70, pady=120, sticky='en')

        label_pay_sum = tk.Label(self, text=str(controller.sum),
                                 height=3, width=5,
                                 bg='white', font=('Times New Roman', 20, 'bold'))
        label_pay_sum.grid(row=2, column=0, padx=5, pady=120, sticky='en')

        button_back.grid(row=3, columnspan=2, pady=5)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


class HourOrNight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
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
                                command=lambda: controller.show_frame("Ticket"))

        button_back.grid(row=3, columnspan=2, pady=5)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)


class TwentyForHours(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        image = Image.open("example2.jpg")
        photo_image = ImageTk.PhotoImage(image)
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
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
                                command=lambda: controller.show_frame("Ticket"))

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