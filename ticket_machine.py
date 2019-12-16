#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import Tkinter as Tk
except ImportError:
    import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font as tkfont
import time
from tkinter.ttk import *
import tkinter.ttk as ttk


def update_labels(label1, label2, label3):
    label1.configure(text="0")
    label2.configure(text="0")
    label3.configure(text="0")


def open_images():
    image = Image.open("gdynia.jpg")
    photo_image = ImageTk.PhotoImage(image)
    image_pl = Image.open("poland.png")
    photo_pl = ImageTk.PhotoImage(image_pl)
    image_en = Image.open("england.png")
    photo_en = ImageTk.PhotoImage(image_en)
    return photo_image, photo_pl, photo_en


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
                  HourOrNight, TwentyForHours, ForPay, Metro):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def on_click_up(self, label1, label2, count):
        self.counter_reduced += 1
        label1.configure(text=str(self.counter_reduced))
        self.sum += count
        if self.sum <= 0:
            self.sum = 0
        label2.configure(text=str("{0:.2f}".format(self.sum)))

    def on_click_down(self, label1, label2, count):
        if (self.counter_reduced-1) != -1:
            self.counter_reduced -= 1
            label1.configure(text=str(self.counter_reduced))
            self.sum -= count
            if self.sum <= 0:
                self.sum = 0
            label2.configure(text=str("{0:.2f}".format(self.sum)))

    def on_click_up_r(self, label1, label2, count):
        self.counter_regular += 1
        label1.configure(text=str(self.counter_regular))
        self.sum += count
        if self.sum <= 0:
            self.sum = 0
        label2.configure(text=str("{0:.2f}".format(self.sum)))

    def on_click_down_r(self, label1, label2, count):
        if (self.counter_regular - 1) is not -1:
            self.counter_regular -= 1
            label1.configure(text=str(self.counter_regular))
            self.sum -= count
            if self.sum <= 0:
                self.sum = 0
            label2.configure(text=str("{0:.2f}".format(self.sum)))

    def update_variables(self):
        self.counter_regular = 0
        self.counter_reduced = 0
        self.sum = 0


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en = open_images()
        background_label = Label(self, image=photo_image)
        background_label.image = photo_image
        background_label.grid(rowspan=4, columnspan=3, sticky="news")

        label = tk.Label(self, text="Biletomat", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=2, pady=5, padx=40, sticky='se')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        button1 = tk.Button(self, text="Bilety jednorazowe", height=5, width=25, font=('Times New Roman', 20, "bold"),
                            bg='gold', command=lambda: [controller.show_frame("Ticket"), controller.update_variables()])

        button2 = tk.Button(self, text="Bilety okresowe", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("SeasonTicket"), controller.update_variables()])

        button3 = tk.Button(self, text="Doładuj kartę miejską", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("Card"), controller.update_variables()])

        button4 = tk.Button(self, text="Bilety Metropolitalne", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("Metro"), controller.update_variables()])

        button1.grid(row=1, pady=30, padx=5, sticky='s')
        button2.grid(row=2, pady=30, padx=5)
        button3.grid(row=2, column=2, pady=30, padx=5)
        button4.grid(row=1, column=2, pady=30, padx=5, sticky='s')

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

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet jednorazowy", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

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

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet okresowy", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

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

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Doładuj kartę miejską", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=3, columnspan=2, pady=5)

        self.s = ttk.Style()
        self.s.configure("colour.Horizontal.TProgressbar", foreground="white", background="green")

        self.progress_bar = Progressbar(self, style="colour.Horizontal.TProgressbar",
                                        orient=HORIZONTAL, length=1000, mode='determinate')
        self.progress_bar.grid(row=2, columnspan=2, pady=10)

        label_karta = tk.Button(self, text="Przyłóż kartę do czytnika ->", font=('Times New Roman', 18, 'bold'),
                                height=5, width=30, fg='white', bg='blue', command=self.run_progressbar)

        label_karta.grid(row=1, columnspan=2, pady=30, padx=5)

        self.label_load = tk.Label(self, text="Karta doładowana", height=3, width=30, fg='white', bg='blue',
                                   font=('Times New Roman', 18, 'bold'))

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100

        for i in range(101):
            time.sleep(0.025)
            self.progress_bar["value"] = i
            self.progress_bar.update()

        if self.progress_bar["value"] == self.progress_bar["maximum"]:
            self.label_load.grid(row=1, columnspan=2, sticky='s', pady=10)
            self.label_load.after(3000, self.label_load.grid_remove)
            self.progress_bar["value"] = 0


class OrdinaryOneTicket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = tk.Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        self.label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
        self.label.grid(row=0, columnspan=3, sticky='nwse')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: [controller.show_frame("Ticket"), controller.update_variables(),
                                                 update_labels(label_reduced_l, label_regular_l, label_pay_sum)])

        button_back.grid(row=3, columnspan=2, pady=5)

        label_reduced = tk.Label(self, text='Bilet Ulgowy: ', height=3, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        label_reduced.grid(row=1, column=0, padx=50, pady=5, sticky='ws')

        label_reduced_l = tk.Label(self, text=controller.counter_reduced, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_reduced_l.grid(row=1, column=0, padx=200, pady=5, sticky='es')

        btn_reduced_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up(label_reduced_l, label_pay_sum, 1.6))
        btn_reduced_up.grid(row=1, column=0, padx=110, pady=5, sticky='es')

        btn_reduced_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down(label_reduced_l, label_pay_sum, 1.6))
        btn_reduced_down.grid(row=1, column=0, padx=20, pady=5, sticky="es")

        label_regular = tk.Label(self, text='Bilet normalny: ', height=3, width=20,
                                 font=('Times New Roman', 20, 'bold'), bg='gold')
        label_regular.grid(row=2, column=0, padx=50, pady=60, sticky='wn')

        label_regular_l = tk.Label(self, text=controller.counter_regular, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_regular_l.grid(row=2, column=0, padx=200, pady=60, sticky='en')

        btn_regular_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up_r(label_regular_l, label_pay_sum, 3.2))
        btn_regular_up.grid(row=2, column=0, padx=110, pady=60, sticky='en')

        btn_regular_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down_r(label_regular_l, label_pay_sum, 3.2))
        btn_regular_down.grid(row=2, column=0, padx=20, pady=60, sticky='en')

        btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                               command=lambda: controller.show_frame("ForPay"),
                               font=('Times New Roman', 20, 'bold'))
        btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

        label_pay = tk.Label(self, text='Do zapłaty: ', height=3, width=20,
                             font=('Times New Roman', 20, 'bold'), bg='gold')
        label_pay.grid(row=2, column=1, padx=70, pady=5, sticky='n')

        label_pay_sum = tk.Label(self, text=str(controller.sum),
                                 height=3, width=5,
                                 bg='white', font=('Times New Roman', 20, 'bold'))
        label_pay_sum.grid(row=2, column=1, padx=55, pady=5, sticky='ne')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)


class OrdinaryHourTicket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: [controller.show_frame("Ticket"), controller.update_variables(),
                                                 update_labels(label_reduced_l, label_regular_l, label_pay_sum)])
        button_back.grid(row=3, columnspan=2, pady=5)

        label_reduced = tk.Label(self, text='Bilet Ulgowy: ', height=3, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        label_reduced.grid(row=1, column=0, padx=50, pady=5, sticky='ws')

        label_reduced_l = tk.Label(self, text=controller.counter_reduced, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_reduced_l.grid(row=1, column=0, padx=200, pady=5, sticky='es')

        btn_reduced_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up(label_reduced_l, label_pay_sum, 1.9))
        btn_reduced_up.grid(row=1, column=0, padx=110, pady=5, sticky='es')

        btn_reduced_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down(label_reduced_l, label_pay_sum, 1.9))
        btn_reduced_down.grid(row=1, column=0, padx=20, pady=5, sticky="es")

        label_regular = tk.Label(self, text='Bilet normalny: ', height=3, width=20,
                                 font=('Times New Roman', 20, 'bold'), bg='gold')
        label_regular.grid(row=2, column=0, padx=50, pady=60, sticky='wn')

        label_regular_l = tk.Label(self, text=controller.counter_regular, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_regular_l.grid(row=2, column=0, padx=200, pady=60, sticky='en')

        btn_regular_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up_r(label_regular_l, label_pay_sum, 3.8))
        btn_regular_up.grid(row=2, column=0, padx=110, pady=60, sticky='en')

        btn_regular_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down_r(label_regular_l, label_pay_sum, 3.8))
        btn_regular_down.grid(row=2, column=0, padx=20, pady=60, sticky='en')

        btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                               command=lambda: controller.show_frame("ForPay"),
                               font=('Times New Roman', 20, 'bold'))
        btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

        label_pay = tk.Label(self, text='Do zapłaty: ', height=3, width=20,
                             font=('Times New Roman', 20, 'bold'), bg='gold')
        label_pay.grid(row=2, column=1, padx=70, pady=5, sticky='n')

        label_pay_sum = tk.Label(self, text=str(controller.sum),
                                 height=3, width=5,
                                 bg='white', font=('Times New Roman', 20, 'bold'))
        label_pay_sum.grid(row=2, column=1, padx=55, pady=5, sticky='ne')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)


class ForPay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj płatności", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("OrdinaryHourTicket"))

        button_cash = tk.Button(self, text="Gotówka", bg='gold', height=7, width=15,
                                font=('Times New Roman', 25, 'bold'))
        button_cash.grid(row=1, column=0, padx=20, pady=5, sticky='e')
        button_card = tk.Button(self, text="Karta", bg='gold', height=7, width=15,
                                font=('Times New Roman', 25, 'bold'))
        button_card.grid(row=1, column=1, padx=20, pady=5, sticky='w')

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

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj ulgi", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=15, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: [controller.show_frame("Ticket"), controller.update_variables(),
                                                 update_labels(label_reduced_l, label_regular_l, label_pay_sum)])
        button_back.grid(row=3, columnspan=2, pady=5)

        label_reduced = tk.Label(self, text='Bilet Ulgowy: ', height=3, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        label_reduced.grid(row=1, column=0, padx=50, pady=5, sticky='ws')

        label_reduced_l = tk.Label(self, text=controller.counter_reduced, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_reduced_l.grid(row=1, column=0, padx=200, pady=5, sticky='es')

        btn_reduced_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up(label_reduced_l, label_pay_sum, 2.1))
        btn_reduced_up.grid(row=1, column=0, padx=110, pady=5, sticky='es')

        btn_reduced_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down(label_reduced_l, label_pay_sum, 2.1))
        btn_reduced_down.grid(row=1, column=0, padx=20, pady=5, sticky="es")

        label_regular = tk.Label(self, text='Bilet normalny: ', height=3, width=20,
                                 font=('Times New Roman', 20, 'bold'), bg='gold')
        label_regular.grid(row=2, column=0, padx=50, pady=60, sticky='wn')

        label_regular_l = tk.Label(self, text=controller.counter_regular, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_regular_l.grid(row=2, column=0, padx=200, pady=60, sticky='en')

        btn_regular_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up_r(label_regular_l, label_pay_sum, 4.2))
        btn_regular_up.grid(row=2, column=0, padx=110, pady=60, sticky='en')

        btn_regular_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down_r(label_regular_l, label_pay_sum, 4.2))
        btn_regular_down.grid(row=2, column=0, padx=20, pady=60, sticky='en')

        btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                               command=lambda: controller.show_frame("ForPay"),
                               font=('Times New Roman', 20, 'bold'))
        btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

        label_pay = tk.Label(self, text='Do zapłaty: ', height=3, width=20,
                             font=('Times New Roman', 20, 'bold'), bg='gold')
        label_pay.grid(row=2, column=1, padx=70, pady=5, sticky='n')

        label_pay_sum = tk.Label(self, text=str(controller.sum),
                                 height=3, width=5,
                                 bg='white', font=('Times New Roman', 20, 'bold'))
        label_pay_sum.grid(row=2, column=1, padx=55, pady=5, sticky='ne')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
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
                                command=lambda: [controller.show_frame("Ticket"), controller.update_variables(),
                                                 update_labels(label_reduced_l, label_regular_l, label_pay_sum)])
        button_back.grid(row=3, columnspan=2, pady=5)

        label_reduced = tk.Label(self, text='Bilet Ulgowy: ', height=3, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        label_reduced.grid(row=1, column=0, padx=50, pady=5, sticky='ws')

        label_reduced_l = tk.Label(self, text=controller.counter_reduced, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_reduced_l.grid(row=1, column=0, padx=200, pady=5, sticky='es')

        btn_reduced_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up(label_reduced_l, label_pay_sum, 6.5))
        btn_reduced_up.grid(row=1, column=0, padx=110, pady=5, sticky='es')

        btn_reduced_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down(label_reduced_l, label_pay_sum, 6.5))
        btn_reduced_down.grid(row=1, column=0, padx=20, pady=5, sticky="es")

        label_regular = tk.Label(self, text='Bilet normalny: ', height=3, width=20,
                                 font=('Times New Roman', 20, 'bold'), bg='gold')
        label_regular.grid(row=2, column=0, padx=50, pady=60, sticky='wn')

        label_regular_l = tk.Label(self, text=controller.counter_regular, height=3, width=5, bg='white',
                                   font=('Times New Roman', 20, 'bold'))
        label_regular_l.grid(row=2, column=0, padx=200, pady=60, sticky='en')

        btn_regular_up = tk.Button(self, text="+", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                   command=lambda: controller.on_click_up_r(label_regular_l, label_pay_sum, 13))
        btn_regular_up.grid(row=2, column=0, padx=110, pady=60, sticky='en')

        btn_regular_down = tk.Button(self, text="-", height=2, width=3, font=('Times New Roman', 30, 'bold'),
                                     command=lambda: controller.on_click_down_r(label_regular_l, label_pay_sum, 13))
        btn_regular_down.grid(row=2, column=0, padx=20, pady=60, sticky='en')

        btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                               command=lambda: controller.show_frame("ForPay"),
                               font=('Times New Roman', 20, 'bold'))
        btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

        label_pay = tk.Label(self, text='Do zapłaty: ', height=3, width=20,
                             font=('Times New Roman', 20, 'bold'), bg='gold')
        label_pay.grid(row=2, column=1, padx=70, pady=5, sticky='n')

        label_pay_sum = tk.Label(self, text=str(controller.sum),
                                 height=3, width=5,
                                 bg='white', font=('Times New Roman', 20, 'bold'))
        label_pay_sum.grid(row=2, column=1, padx=55, pady=5, sticky='ne')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)


class Metro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet metropolitalny", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        label_info = tk.Label(self, text="INFO", bg='gold', height=1, width=5, font=('Times New Roman', 18, 'bold'))
        label_info.grid(row=0, column=1, pady=5, padx=40, sticky='se')

        button1_1 = tk.Button(self, text="1-przejazd\n linie zwykłe\n ", height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("OrdinaryOneTicket"))
        button1_2 = tk.Button(self, text="1-przejazd\n linie pospieszne\n i nocne\n (ZTM+ZKM+MZK)",
                              height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("OrdinaryHourTicket"))
        button1_3 = tk.Button(self, text="24-godzinny Komunalny\n (ZTM+ZKM+MZK)",
                              height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, "bold"),
                              command=lambda: controller.show_frame("HourOrNight"))
        button1_4 = tk.Button(self, text="72-godzinny\n (ZTM+ZKM+MZK)", height=6, width=20,
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


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
