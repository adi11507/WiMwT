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


def open_images():
    image = Image.open("gdynia.jpg")
    photo_image = ImageTk.PhotoImage(image)
    image_pl = Image.open("poland.png")
    photo_pl = ImageTk.PhotoImage(image_pl)
    image_en = Image.open("england.png")
    photo_en = ImageTk.PhotoImage(image_en)
    card = Image.open("card.jpg")
    card_image = ImageTk.PhotoImage(card)
    return photo_image, photo_pl, photo_en, card_image


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
        self.price = 0
        self.frames = {}

        for F in (StartPage, Ticket, Card, SeasonTicket, ForPay, Metro, Info):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update(self):
        self.counter_regular = 0
        self.counter_reduced = 0
        self.sum = 0
        self.price = 0


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en, card_image = open_images()
        background_label = Label(self, image=photo_image)
        background_label.image = photo_image
        background_label.grid(rowspan=4, columnspan=3, sticky="news")

        label = tk.Label(self, text="Biletomat", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))
        btn_info.grid(row=0, column=2, pady=5, padx=40, sticky='es')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        button1 = tk.Button(self, text="Bilety jednorazowe", height=5, width=25, font=('Times New Roman', 20, "bold"),
                            bg='gold', command=lambda: [controller.show_frame("Ticket"), controller.update()])

        button2 = tk.Button(self, text="Bilety okresowe", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("SeasonTicket"), controller.update()])

        button3 = tk.Button(self, text="Doładuj kartę miejską", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("Card"), controller.update()])

        button4 = tk.Button(self, text="Bilety Metropolitalne", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("Metro"), controller.update()])

        button1.grid(row=1, pady=30, padx=5, sticky='s')
        button2.grid(row=2, pady=30, padx=5)
        button3.grid(row=2, column=2, pady=30, padx=5)
        button4.grid(row=1, column=2, pady=30, padx=5, sticky='s')

        self.rowconfigure(1, weight=1)


class Ticket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.price = controller.price
        self.controller.sum = controller.sum
        self.controller.counter_regular = controller.counter_regular
        self.controller.counter_reduced = controller.counter_reduced

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet jednorazowy", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        self.button1_1 = tk.Button(self, text="1-przejazd\n linie zwykłe", height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__set__(controller.price, 1.6), self.check_relief()])
        self.button1_2 = tk.Button(self, text="1-godzinny\n linie zwykłe", height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__set__(controller.price, 1.9), self.check_relief()])
        self.button1_3 = tk.Button(self, text="1-godzinny\n lub jednoprzejazdowy\n linie nocne,\n pospieszne",
                                   height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__set__(controller.price, 2.1), self.check_relief()])
        self.button1_4 = tk.Button(self, text="24-godzinny\n linie nocne,\n pospieszne, zwykłe", height=6, width=20,
                                   bg='gold', font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__set__(controller.price, 6.5), self.check_relief()])

        self.frame = tk.Frame(self, bg='blue', bd=4)
        self.label_reduced = tk.Label(self.frame, text='Bilet Ulgowy\n', height=9, width=20, bg='gold',
                                      font=('Times New Roman', 20, 'bold'))
        self.label_reduced_l = tk.Label(self.frame, text=controller.counter_reduced, height=2, width=3, bg='white',
                                        font=('Times New Roman', 30, 'bold'))
        self.btn_reduced_up = tk.Button(self.frame, text="+", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                        command=lambda: self.on_click_up(controller.price))
        self.btn_reduced_down = tk.Button(self.frame, text="-", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                          command=lambda: self.on_click_down(controller.price))

        self.frame_reg = tk.Frame(self, bg='blue', bd=4)
        self.label_regular = tk.Label(self.frame_reg, text='Bilet Normalny', height=9, width=20,
                                      font=('Times New Roman', 20, 'bold'), bg='gold')
        self.label_regular_l = tk.Label(self.frame_reg, text=controller.counter_regular, height=2, width=3, bg='white',
                                        font=('Times New Roman', 30, 'bold'))

        self.btn_regular_up = tk.Button(self.frame_reg, text="+", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                        command=lambda: self.on_click_up_r(controller.price * 2))

        self.btn_regular_down = tk.Button(self.frame_reg, text="-", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                          command=lambda: self.on_click_down_r(controller.price * 2))

        self.label_zl = tk.Label(self.frame, text=str(self.controller.price) + ' zł', height=1, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        self.label_zl_reg = tk.Label(self.frame_reg, text=str(self.controller.price*2) + ' zł', height=1,
                                     width=20, bg='gold', font=('Times New Roman', 20, 'bold'))

        self.frame_pay = tk.Frame(self, bg='blue', bd=1)
        self.label_pay = tk.Label(self.frame_pay, text='Do zapłaty: ', height=5, width=20,
                                  font=('Times New Roman', 20, 'bold'), bg='gold')

        self.label_pay_sum = tk.Label(self.frame_pay, text=str(controller.sum), height=1, width=13,
                                      bg='white', font=('Times New Roman', 30, 'bold'))

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))
        btn_info.grid(row=0, column=1, pady=5, padx=175, sticky='se')

        self.button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                     font=('Times New Roman', 20, "bold"),
                                     command=lambda: [self.update(), controller.update(),
                                                      controller.show_frame("StartPage")])
        self.button_back_1 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                       font=('Times New Roman', 20, "bold"),
                                       command=lambda: [self.back_to_normal(), self.update(), controller.update()])

        self.btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                                    command=lambda: [controller.show_frame("ForPay"), self.__set__1(self.controller.sum)],
                                    font=('Times New Roman', 20, 'bold'))

        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.button1_1.grid(row=1, column=0, pady=30, padx=70, sticky='es')
        self.button1_2.grid(row=2, column=0, pady=30, padx=70, sticky='e')
        self.button1_3.grid(row=1, column=1, pady=30, padx=70, sticky='ws')
        self.button1_4.grid(row=2, column=1, pady=30, padx=70, sticky='w')

        self.rowconfigure(1, weight=1)

    def __set__(self, instance, value):
        self.controller.price = value

    def __set__1(self, value):
        self.controller.sum = value

    def check_relief(self):
        self.button1_1.grid_remove()
        self.button1_2.grid_remove()
        self.button1_3.grid_remove()
        self.button1_4.grid_remove()
        self.button_back.grid_remove()
        self.frame.grid(row=1, column=0, padx=50, pady=5, sticky='w')
        self.label_reduced.grid(row=1, column=0, padx=0, pady=5, sticky='')
        self.label_reduced_l.grid(row=2, column=0, padx=0, pady=0, sticky='')
        self.btn_reduced_up.grid(row=2, column=0, padx=0, pady=0, sticky='e')
        self.btn_reduced_down.grid(row=2, column=0, padx=0, pady=0, sticky='w')
        self.label_zl.grid(row=1, column=0, padx=0, pady=10, sticky='s')
        self.label_zl.configure(text=str(self.controller.price) + ' zł')

        self.frame_reg.grid(row=1, columnspan=2, padx=0, pady=5, sticky='')
        self.label_regular.grid(row=1, column=1, padx=0, pady=5, sticky='')
        self.label_regular_l.grid(row=2, column=1, padx=0, pady=0, sticky='')
        self.btn_regular_up.grid(row=2, column=1, padx=0, pady=0, sticky='e')
        self.btn_regular_down.grid(row=2, column=1, padx=0, pady=0, sticky='w')
        self.label_zl_reg.grid(row=1, column=1, padx=0, pady=10, sticky='s')
        self.label_zl_reg.configure(text=str(self.controller.price*2) + ' zł')

        self.frame_pay.grid(row=1, column=1, padx=50, sticky='e')
        self.label_pay.grid(row=1, column=1, padx=5, pady=5, sticky='')
        self.label_pay_sum.grid(row=1, column=1, padx=5, pady=5, sticky='s')
        self.btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')
        self.button_back_1.grid(row=0, column=1, pady=5, padx=10, sticky='se')

    def back_to_normal(self):
        self.button1_1.grid(row=1, column=0, pady=30, padx=70, sticky='es')
        self.button1_2.grid(row=2, column=0, pady=30, padx=70, sticky='e')
        self.button1_3.grid(row=1, column=1, pady=30, padx=70, sticky='ws')
        self.button1_4.grid(row=2, column=1, pady=30, padx=70, sticky='w')
        self.frame.grid_remove()
        self.frame_reg.grid_remove()
        self.frame_pay.grid_remove()
        self.btn_accept.grid_remove()
        self.button_back_1.grid_remove()
        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')

    def on_click_up(self, price):
        self.controller.counter_reduced += 1
        self.label_reduced_l.configure(text=str(self.controller.counter_reduced))
        self.controller.sum += price
        if self.controller.sum <= 0:
            self.controller.sum = 0
        self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def on_click_down(self, price):
        if (self.controller.counter_reduced - 1) != -1:
            self.controller.counter_reduced -= 1
            self.label_reduced_l.configure(text=str(self.controller.counter_reduced))
            self.controller.sum -= price
            if self.controller.sum <= 0:
                self.controller.sum = 0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def on_click_up_r(self, price):
        self.controller.counter_regular += 1
        self.label_regular_l.configure(text=str(self.controller.counter_regular))
        self.controller.sum += price
        if self.controller.sum <= 0:
            self.controller.sum = 0
        self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def on_click_down_r(self, price):
        if (self.controller.counter_regular - 1) is not -1:
            self.controller.counter_regular -= 1
            self.label_regular_l.configure(text=str(self.controller.counter_regular))
            self.controller.sum -= price
            if self.controller.sum <= 0:
                self.controller.sum = 0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def update(self):
        self.label_regular_l.configure(text="0")
        self.label_reduced_l.configure(text="0")
        self.label_pay_sum.configure(text="0")


class SeasonTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en, card_image = open_images()
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

        tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                  command=lambda: controller.show_frame("Info")).grid(row=0, column=1, pady=5, padx=175,
                                                                      sticky='se')

        tk.Button(self, text="Cofnij", width=10, bg='gold', font=('Times New Roman', 20, "bold"),
                  command=lambda: controller.show_frame("StartPage")).grid(row=0, column=1, pady=5,
                                                                           padx=10, sticky='se')

        self.rowconfigure(1, weight=1)


class Card(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Doładuj kartę miejską", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))
        btn_info.grid(row=0, column=1, pady=5, padx=175, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')

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

        self.rowconfigure(1, weight=1)

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


class ForPay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.value = 0
        self.controller.sum = controller.sum
        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz rodzaj płatności", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))
        btn_info.grid(row=0, column=1, pady=5, padx=175, sticky='se')

        self.button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                     font=('Times New Roman', 20, "bold"),
                                     command=lambda: [controller.show_frame("Ticket"),
                                                      self.__set__(self.controller.value, 1)])

        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')

        self.button_cash = tk.Button(self, text="Gotówka", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'), command=self.show_money)

        self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
        self.button_card = tk.Button(self, text="Karta", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'),
                                     command=self.run_progressbar)
        self.button_card.grid(row=1, column=1, padx=5, sticky='')

        self.card_label = tk.Label(self, image=card_image)
        self.card_label.image = card_image

        self.label_pay_sum = tk.Label(self, text=str(controller.sum), height=1, width=13,
                                      bg='white', font=('Times New Roman', 30, 'bold'))

        self.s1 = ttk.Style()
        self.s1.configure("colour.Horizontal.TProgressbar", foreground="white", background="green")
        self.progress_bar = Progressbar(self, style="colour.Horizontal.TProgressbar",
                                        orient=VERTICAL, length=281, mode='determinate')

        self.frame = tk.Frame(self, bg='blue', bd=4)
        self.label_1 = tk.Label(self.frame, text="Postępuj zgodnie z poleceniami na terminalu!",
                                height=3, width=50, bg='gold',
                                font=('Times New Roman', 18, 'bold'))
        self.label1 = tk.Label(self.frame, text="Zapłacono. Odbierz bilety!", height=3, width=50, bg='gold',
                               font=('Times New Roman', 18, 'bold'))

        self.rowconfigure(1, weight=1)

    def run_progressbar(self):
        self.progress_bar.grid(row=1, column=1, padx=150, sticky='e')
        self.progress_bar["maximum"] = 100
        self.show_card()

        for i in range(101):
            time.sleep(0.055)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            if self.controller.value == 1:
                self.progress_bar["value"] = 0
                self.progress_bar.update()
                self.progress_bar.grid_remove()
                self.frame.grid_remove()
                self.label_1.grid_remove()
                self.card_label.grid_remove()
                self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
                self.button_card.grid(row=1, column=1, padx=5, sticky='')
                break
        self.controller.value = 0
        if self.progress_bar["maximum"] == self.progress_bar["value"]:
            self.label_1.grid_remove()
            self.progress_bar.after(1, self.progress_bar.grid_remove)
            self.label1.grid()
            self.label1.update()
            time.sleep(3)
            self.label1.grid_remove()
            self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
            self.frame.grid_remove()
            self.card_label.grid_remove()
            self.controller.show_frame("StartPage")

    def show_card(self):
        self.frame.grid(row=1, columnspan=2, pady=25, sticky='n')
        self.label_1.grid()
        self.button_cash.grid_remove()
        self.card_label.grid(row=1, column=0, padx=5, sticky='e')

    def __set__(self, instance, value):
        self.controller.value = 1

    def show_money(self):
        self.button_card.grid_remove()
        self.label_pay_sum.grid(row=1, column=1)


class Metro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = tk.Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Wybierz bilet metropolitalny", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))
        btn_info.grid(row=0, column=1, pady=5, padx=175, sticky='se')

        button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')

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

        button1_1.grid(row=1, column=0, pady=30, padx=70, sticky='es')
        button1_2.grid(row=2, column=0, pady=30, padx=70, sticky='e')
        button1_3.grid(row=1, column=1, pady=30, padx=70, sticky='ws')
        button1_4.grid(row=2, column=1, pady=30, padx=70, sticky='w')

        self.rowconfigure(1, weight=1)


class Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        label = tk.Label(self, text="Informacje", font=controller.title_font, fg='white', bg='blue')
        label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=40)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=100, sticky='w')

        self.label1 = tk.Label(self, text=" Ceny i rodzaje biletów", anchor='w', width=75, height=2,
                               font=('Times New Roman', 18, "bold")).grid(row=2, columnspan=2, sticky='n')
        self.label2 = tk.Label(self, text=" Karta miejska", width=75, height=2, anchor='w',
                               font=('Times New Roman', 18, "bold")).grid(row=2, columnspan=2, sticky='n', pady=65)
        self.label3 = tk.Label(self, text=" Kontrola Biletowa", width=75, height=2, anchor='w',
                               font=('Times New Roman', 18, "bold")).grid(row=2, columnspan=2, sticky='n', pady=130)
        self.label4 = tk.Label(self, text=" Przepisy w ZKM Gdynia", width=75, height=2, anchor='w',
                               font=('Times New Roman', 18, "bold")).grid(row=2, columnspan=2, sticky='n', pady=195)
        self.label5 = tk.Label(self, text=" Kontakt", width=75, height=2, anchor='w',
                               font=('Times New Roman', 18, "bold")).grid(row=2, columnspan=2, sticky="n", pady=260)

        button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                font=('Times New Roman', 20, "bold"),
                                command=lambda: controller.show_frame("StartPage"))

        button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.rowconfigure(1, weight=1)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
