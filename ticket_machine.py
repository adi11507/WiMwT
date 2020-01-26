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
        self.price_metro = 0
        self.sum_metro = 0
        self.cnt_ord_red = 0
        self.cnt_ord_reg = 0
        self.cnt_ord_red1 = 0
        self.cnt_ord_reg1 = 0
        self.rest = 0
        self.frames = {}

        for F in (StartPage, Ticket, Card, Metro, Info):
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
        self.price_metro = 0
        self.sum_metro = 0
        self.cnt_ord_red = 0
        self.cnt_ord_reg = 0
        self.cnt_ord_red1 = 0
        self.cnt_ord_reg1 = 0
        self.rest = 0


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

        button3 = tk.Button(self, text="Doładuj kartę miejską", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("Card"), controller.update()])

        button4 = tk.Button(self, text="Bilety Metropolitalne", height=5, width=25, bg='gold',
                            font=('Times New Roman', 20, "bold"),
                            command=lambda: [controller.show_frame("Metro"), controller.update()])
        label_karta = tk.Label(self, text="Jeżeli chcesz doładować kartę\n "
                                          "Włóż kartę do czytnika ->", font=('Times New Roman', 18, 'bold'),
                               height=5, width=30, fg='white', bg='blue')

        button1.grid(row=1, pady=30, padx=5, sticky='s')
        label_karta.grid(row=2, padx=5, pady=30)
        button3.grid(row=2, column=2, pady=30, padx=5)
        button4.grid(row=1, column=2, pady=30, padx=5, sticky='s')

        self.rowconfigure(1, weight=1)


class Ticket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.price = controller.price
        self.controller.sum = controller.sum
        self.controller.value = 0
        self.controller.counter_regular = controller.counter_regular
        self.controller.counter_reduced = controller.counter_reduced
        self.controller.rest = controller.rest

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        self.label = tk.Label(self, text="Wybierz bilet jednorazowy", font=controller.title_font, fg='white', bg='blue')
        self.label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        # checking tickets
        self.button1_1 = tk.Button(self, text="1-przejazd\n linie zwykłe", height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__setitem__(1, 1.6), self.check_relief()])
        self.button1_2 = tk.Button(self, text="1-godzinny\n linie zwykłe", height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__setitem__(1, 1.9), self.check_relief()])
        self.button1_3 = tk.Button(self, text="1-godzinny\n lub jednoprzejazdowy\n linie nocne,\n pospieszne",
                                   height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__setitem__(1, 2.1), self.check_relief()])
        self.button1_4 = tk.Button(self, text="24-godzinny\n linie nocne,\n pospieszne, zwykłe", height=6, width=20,
                                   bg='gold', font=('Times New Roman', 20, "bold"),
                                   command=lambda: [self.__setitem__(1, 6.5), self.check_relief()])

        # checking relief
        # reduced
        self.frame = tk.Frame(self, bg='blue', bd=4)
        self.label_reduced = tk.Label(self.frame, text='Bilet Ulgowy\n', height=9, width=20, bg='gold',
                                      font=('Times New Roman', 20, 'bold'))
        self.label_reduced_l = tk.Label(self.frame, text=controller.counter_reduced, height=2, width=3, bg='white',
                                        font=('Times New Roman', 30, 'bold'))
        self.btn_reduced_up = tk.Button(self.frame, text="+", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                        command=lambda: self.on_click_up(controller.price))
        self.btn_reduced_down = tk.Button(self.frame, text="-", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                          command=lambda: self.on_click_down(controller.price))

        # regular
        self.frame_reg = tk.Frame(self, bg='blue', bd=4)
        self.label_regular = tk.Label(self.frame_reg, text='Bilet Normalny', height=9, width=20,
                                      font=('Times New Roman', 20, 'bold'), bg='gold')
        self.label_regular_l = tk.Label(self.frame_reg, text=controller.counter_regular, height=2, width=3, bg='white',
                                        font=('Times New Roman', 30, 'bold'))

        self.btn_regular_up = tk.Button(self.frame_reg, text="+", height=2, width=4,
                                        font=('Times New Roman', 27, 'bold'),
                                        command=lambda: self.on_click_up_r(controller.price * 2))

        self.btn_regular_down = tk.Button(self.frame_reg, text="-", height=2, width=4,
                                          font=('Times New Roman', 27, 'bold'),
                                          command=lambda: self.on_click_down_r(controller.price * 2))

        # set price of ticket
        self.label_zl = tk.Label(self.frame, text=str(self.controller.price) + ' zł', height=1, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        self.label_zl_reg = tk.Label(self.frame_reg, text=str(self.controller.price * 2) + ' zł', height=1,
                                     width=20, bg='gold', font=('Times New Roman', 20, 'bold'))

        # calculate sum to pay
        self.frame_pay = tk.Frame(self, bg='blue', bd=1)
        self.label_pay = tk.Label(self.frame_pay, text='Do zapłaty: ', height=5, width=20,
                                  font=('Times New Roman', 20, 'bold'), bg='gold')

        self.label_pay_sum = tk.Label(self.frame_pay, text=str(self.controller.sum), height=1, width=13,
                                      bg='white', font=('Times New Roman', 30, 'bold'))

        # payment
        self.button_cash = tk.Button(self, text="Gotówka", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'), command=self.show_money)
        self.button_card = tk.Button(self, text="Karta", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'),
                                     command=self.run_progressbar)

        self.frame_money = tk.Frame(self, bg='blue', bd=1)
        self.ten = tk.Button(self.frame_money, text=" 10 gr", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(0.10)])
        self.twenty = tk.Button(self.frame_money, text=" 20 gr", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_cash(0.20)])
        self.fifty = tk.Button(self.frame_money, text=" 50 gr", font=('Times New Roman', 20, 'bold'),
                               command=lambda: [self.minus_cash(0.50)])
        self.one = tk.Button(self.frame_money, text="  1 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(1)])
        self.two = tk.Button(self.frame_money, text="  2 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(2)])
        self.five = tk.Button(self.frame_money, text="  5 zł  ", font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.minus_cash(5)])
        self.ten_zl = tk.Button(self.frame_money, text=" 10 zł ", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_cash(10)])
        self.twenty_zl = tk.Button(self.frame_money, text=" 20 zł ", font=('Times New Roman', 20, 'bold'),
                                   command=lambda: [self.minus_cash(20)])

        self.card_label = tk.Label(self, image=card_image)
        self.card_label.image = card_image

        self.s1 = ttk.Style()
        self.s1.configure("colour.Horizontal.TProgressbar", foreground="white", background="green")
        self.progress_bar = Progressbar(self, style="colour.Horizontal.TProgressbar",
                                        orient=VERTICAL, length=281, mode='determinate')

        self.frame_payment = tk.Frame(self, bg='blue', bd=4)
        self.label_1 = tk.Label(self.frame_payment, text="Postępuj zgodnie z poleceniami na terminalu!",
                                height=3, width=50, bg='gold',
                                font=('Times New Roman', 18, 'bold'))
        self.label1 = tk.Label(self.frame_payment, text="Zapłacono. Odbierz bilety!", height=3, width=50, bg='gold',
                               font=('Times New Roman', 18, 'bold'))

        self.frame_cash_payment = tk.Frame(self, bg='blue', bd=4)
        self.label2 = tk.Label(self.frame_cash_payment,
                               text="Zapłacono. Odbierz bilety i resztę: " + str(self.controller.rest),
                               height=3, width=50, bg='gold', font=('Times New Roman', 18, 'bold'))

        # additional buttons
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
        self.button_back_2 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                       font=('Times New Roman', 20, "bold"),
                                       command=lambda: self.back_to_checking())
        self.button_back_3 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                       font=('Times New Roman', 20, "bold"),
                                       command=lambda: self.__setitem__(3, 1))

        self.btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                                    command=lambda: self.to_payment(),
                                    font=('Times New Roman', 20, 'bold'))

        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.button1_1.grid(row=1, column=0, pady=30, padx=70, sticky='es')
        self.button1_2.grid(row=2, column=0, pady=30, padx=70, sticky='e')
        self.button1_3.grid(row=1, column=1, pady=30, padx=70, sticky='ws')
        self.button1_4.grid(row=2, column=1, pady=30, padx=70, sticky='w')

        self.rowconfigure(1, weight=1)

    def back_af_cash_pay(self):
        time.sleep(2)
        self.frame_cash_payment.grid_remove(), self.frame_pay.grid_remove(), self.frame_money.grid_remove()
        self.button_back_2.grid_remove(), self.button_cash.grid_remove()
        self.button1_1.grid(row=1, column=0, pady=30, padx=70, sticky='es')
        self.button1_2.grid(row=2, column=0, pady=30, padx=70, sticky='e')
        self.button1_3.grid(row=1, column=1, pady=30, padx=70, sticky='ws')
        self.button1_4.grid(row=2, column=1, pady=30, padx=70, sticky='w')
        self.label.configure(text="Wybierz bilet jednorazowy")
        self.button_back_2.grid_remove(), self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.update(), self.controller.update()
        self.controller.show_frame("StartPage")

    def minus_cash(self, count):
        if self.controller.sum - count < 0.01:
            self.label_pay_sum.configure(text=str(0.00))
            self.controller.rest = self.controller.sum - count
            self.frame_cash_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
            if self.controller.rest < -0.01:
                self.label2.configure(text="Zapłacono. Odbierz bilety i resztę: " +
                                           ("{0:.2f}".format(-self.controller.rest)))
            else:
                self.label2.configure(text="Zapłacono. Odbierz bilety.")

            self.label2.grid(), self.label2.update(), self.back_af_cash_pay()
        else:
            self.controller.sum -= count
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def check_relief(self):
        self.button1_1.grid_remove()
        self.button1_2.grid_remove()
        self.button1_3.grid_remove()
        self.button1_4.grid_remove()
        self.button_back.grid_remove()
        self.label.configure(text="Wybierz ulgę")
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
        self.label_zl_reg.configure(text=str(self.controller.price * 2) + ' zł')

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
        self.label.configure(text="Wybierz bilet jednorazowy")
        self.frame.grid_remove(), self.frame_reg.grid_remove(), self.frame_pay.grid_remove()
        self.btn_accept.grid_remove(), self.button_back_1.grid_remove()
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

    def run_progressbar(self):
        self.progress_bar.grid(row=1, column=1, padx=150, sticky='e')
        self.progress_bar["maximum"] = 100
        self.show_card(), self.button_back_2.grid_remove(), self.label.configure(text="Wybierz sposób płatności")
        self.button_back_3.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        for i in range(101):
            time.sleep(0.055)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            if self.controller.value == 1:
                self.progress_bar["value"] = 0
                self.progress_bar.update()
                self.progress_bar.grid_remove(), self.frame_payment.grid_remove()
                self.label_1.grid_remove(), self.card_label.grid_remove()
                self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
                self.button_card.grid(row=1, column=1, padx=5, sticky='')
                self.button_back_3.grid_remove(), self.button_back_2.grid(row=0, column=1, pady=5, padx=10, sticky='se')
                break

        self.controller.value = 0

        if self.progress_bar["maximum"] == self.progress_bar["value"]:
            self.label_1.grid_remove()
            self.progress_bar.after(1, self.progress_bar.grid_remove)
            self.label1.grid(), self.label1.update()
            time.sleep(3)
            self.label1.grid_remove()
            self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
            self.frame_payment.grid_remove(), self.card_label.grid_remove()
            self.button_cash.grid_remove(), self.button_card.grid_remove()
            self.button1_1.grid(row=1, column=0, pady=30, padx=70, sticky='es')
            self.button1_2.grid(row=2, column=0, pady=30, padx=70, sticky='e')
            self.button1_3.grid(row=1, column=1, pady=30, padx=70, sticky='ws')
            self.button1_4.grid(row=2, column=1, pady=30, padx=70, sticky='w')
            self.label.configure(text="Wybierz bilet jednorazowy")
            self.button_back_3.grid_remove(), self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
            self.update(), self.controller.update()
            self.controller.show_frame("StartPage")

    def show_card(self):
        self.frame_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
        self.label_1.grid(), self.button_cash.grid_remove()
        self.card_label.grid(row=1, column=0, padx=5, sticky='e')

    def show_money(self):
        self.button_card.grid_remove()
        self.frame_pay.grid(row=1, columnspan=2, pady=25, sticky='')
        self.label_pay.configure(text="Do zapłaty\n pozostało:")
        self.frame_money.grid(row=1, columnspan=2)
        self.ten.grid(), self.twenty.grid(), self.fifty.grid(), self.one.grid(), self.two.grid(), self.five.grid(),
        self.ten_zl.grid(), self.twenty_zl.grid()

    def to_payment(self):
        self.frame.grid_remove(), self.frame_pay.grid_remove(), self.frame_reg.grid_remove()
        self.btn_accept.grid_remove(), self.label.configure(text="Wybierz sposób płatności")
        self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
        self.button_card.grid(row=1, column=1, padx=5, sticky='')
        self.button_back_1.grid_remove()
        self.button_back_2.grid(row=0, column=1, pady=5, padx=10, sticky='se')

    def back_to_checking(self):
        self.frame.grid(row=1, column=0, padx=50, pady=5, sticky='w')
        self.frame_reg.grid(row=1, columnspan=2, padx=0, pady=5, sticky='')
        self.frame_pay.grid(row=1, column=1, padx=50, sticky='e')
        self.button_cash.grid_remove(), self.button_card.grid_remove()
        self.button_back_2.grid_remove(), self.frame_money.grid_remove()
        self.label.configure(text="Wybierz ulgę")
        self.button_back_1.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

    def __setitem__(self, key, value):
        if key == 1:
            self.controller.price = value
        elif key == 2:
            self.controller.sum = value
        elif key == 3:
            self.controller.value = 1


class Card(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        self.label = tk.Label(self, text="Wybierz bilet okresowy", font=controller.title_font, fg='white', bg='blue')
        self.label.grid(row=0, columnspan=3, sticky='nwse')

        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        self.frame1 = tk.Frame(self, bg='blue', bd=1)
        self.button1 = tk.Button(self.frame1, text="Bilety okresowe",
                                 height=6, width=20, bg='gold',
                                 font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.choose_option(1), self.open_ticket(0)])
        self.info1 = tk.Label(self.frame1, text='ważne od poniedziałku do piątku',
                              font=('Times New Roman', 16, 'bold italic'), width=26)

        self.frame2 = tk.Frame(self, bg='blue', bd=1)
        self.button2 = tk.Button(self.frame2, text="Bilety okresowe",
                                 height=6, width=20, bg='gold',
                                 font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.choose_option(2), self.open_ticket(0)])
        self.info2 = tk.Label(self.frame2, text='ważne we wszystkie dni tygodnia',
                              font=('Times New Roman', 16, 'bold italic'), width=26)

        self.frame5 = tk.Frame(self, bg='blue', bd=1)
        self.button5 = tk.Button(self.frame5, text="Bilety okresowe \nsemestralne\n 5-miesięczne\n",
                                 height=6, width=23, bg='gold', font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.choose_option(4), self.open_ticket(2)])
        self.info5 = tk.Label(self.frame5, text="0.1.10-31.01 lub 01.02-31.05\n"
                                                "*przysługuje uczniom i studentom do 24 lat",
                              font=('Times New Roman', 14, 'bold italic'), width=36)

        self.frame4 = tk.Frame(self, bg='blue', bd=1)
        self.button4 = tk.Button(self.frame4, text="Bilety okresowe \nsemestralne\n 4-miesięczne\n",
                                 height=6, width=23,
                                 bg='gold', font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.choose_option(3), self.open_ticket(1)])
        self.info4 = tk.Label(self.frame4, text="01.09-31.01 lub 01.02-31.06\n"
                                                "*przysługuje uczniom i studentom do 24 lat",
                              font=('Times New Roman', 14, 'bold italic'), width=36)

        self.frame3 = tk.Frame(self, bg='blue', bd=1)
        self.button3 = tk.Button(self.frame3, text="Bilety okresowe\n metropolitalne", height=6, width=20, bg='gold',
                                 font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.choose_option(5), self.open_metro()])

        self.info3 = tk.Label(self.frame3, text="Komunalne lub łączone",
                              font=('Times New Roman', 16, 'bold italic'), width=26)

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))

        self.frame_month1 = tk.Frame(self, bg='blue', bd=1)
        self.zw1 = tk.Button(self.frame_month1, text='Zwykłe', height=6, width=20, bg='gold',
                             font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.choose_sum(1), self.check_relief(1)])
        self.info_zw1 = tk.Label(self.frame_month1, text='W granicach Gdynii',
                                 font=('Times New Roman', 16, 'bold italic'), width=26)

        self.frame_month2 = tk.Frame(self, bg='blue', bd=1)
        self.npz1 = tk.Button(self.frame_month2, text='Nocne, pospieszne\n i zwykłe',
                              height=6, width=20, bg='gold',
                              font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.choose_sum(2), self.check_relief(1)])
        self.info_npz1 = tk.Label(self.frame_month2, text='W  granicach Gdynii',
                                  font=('Times New Roman', 16, 'bold italic'), width=26)

        self.frame_month3 = tk.Frame(self, bg='blue', bd=1)
        self.npz2 = tk.Button(self.frame_month3, text='Nocne, pospieszne\n i zwykłe',
                              height=5, width=20, bg='gold',
                              font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.choose_sum(3), self.check_relief(1)])
        self.info_npz2 = tk.Label(self.frame_month3, text='W granicach Sopotu lub Rumi\n lub Gm.Kosakowo'
                                                          ' lub Gm.Żukowo\n lub Gm.Szemud lub Gm.Wejherowo',
                                  font=('Times New Roman', 14, 'bold italic'), width=32)

        self.frame_month4 = tk.Frame(self, bg='blue', bd=1)
        self.npz3 = tk.Button(self.frame_month4, text='Nocne, pospieszne\n i zwykłe',
                              height=5, width=20, bg='gold',
                              font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.choose_sum(4), self.check_relief(1)])
        self.info_npz3 = tk.Label(self.frame_month4, text='W granicach Rumi, Redy \n i miasta Wejherowa,\n'
                                                          'albo Gm. Wejherowo i Rumi',
                                  font=('Times New Roman', 16, 'bold italic'), width=26)
        self.frame_month5 = tk.Frame(self, bg='blue', bd=1)
        self.npz4 = tk.Button(self.frame_month5, text='Nocne, pospieszne\n i zwykłe',
                              height=5, width=20, bg='gold',
                              font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.choose_sum(5), self.check_relief(1)])
        self.info_npz4 = tk.Label(self.frame_month5, text='W obrębie sieci komunikacyjnej\n'
                                                          '[w tym linie G, N1, 101, 171]',
                                  font=('Times New Roman', 16, 'bold italic'), width=26)

        self.metro = tk.Frame(self, bg='blue', bd=1)
        self.m1 = tk.Button(self.metro, text='Komunalny',
                            height=5, width=20, bg='gold',
                            font=('Times New Roman', 20, 'bold'),
                            command=lambda: [self.choose_sum(1), self.check_relief(2)])
        self.info_m1 = tk.Label(self.metro, text='ZTM Gdańsk + ZKM Gdynia\n + MZK Wejherowo',
                                font=('Times New Roman', 16, 'bold italic'), width=26)

        self.metro2 = tk.Frame(self, bg='blue', bd=1)
        self.m2 = tk.Button(self.metro2, text='Miesięczny\n Gdańsk-Sopot\n Gdynia-Sopot',
                            height=5, width=20, bg='gold',
                            font=('Times New Roman', 20, 'bold'),
                            command=lambda: [self.choose_sum(2), self.check_relief(2)])
        self.info_m2 = tk.Label(self.metro2, text='wymaga jednoczesnego zakupu\n promocyjnego biletu SKM I PR',
                                font=('Times New Roman', 16, 'bold italic'), width=26)

        self.metro3 = tk.Frame(self, bg='blue', bd=1)
        self.m3 = tk.Button(self.metro3, text='Miesięczny\n Sieciowy jednego\n organizatora',
                            height=5, width=20, bg='gold',
                            font=('Times New Roman', 20, 'bold'),
                            command=lambda: [self.choose_sum(3), self.check_relief(2)])
        self.info_m3 = tk.Label(self.metro3, text='wymaga jednoczesnego zakupu\n promocyjnego biletu SKM I PR\n',
                                font=('Times New Roman', 16, 'bold italic'), width=26)

        self.metro4 = tk.Frame(self, bg='blue', bd=1)
        self.m4 = tk.Button(self.metro4, text='Miesięczny\n na cały obszar\n MZKZG',
                            height=5, width=20, bg='gold',
                            font=('Times New Roman', 20, 'bold'),
                            command=lambda: [self.choose_sum(4), self.check_relief(2)])
        self.info_m4 = tk.Label(self.metro4, text='wymaga jednoczesnego zakupu\n promocyjnego biletu \n'
                                                  'SKM (w tym PKM) I PR',
                                font=('Times New Roman', 16, 'bold italic'), width=26)

        btn_info.grid(row=0, column=1, pady=5, padx=175, sticky='se')

        self.button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                     font=('Times New Roman', 20, "bold"),
                                     command=lambda: controller.show_frame("StartPage"))

        self.btn_to_per = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                    font=('Times New Roman', 20, "bold"),
                                    command=lambda: self.back_to_per(1))
        self.btn_to_per2 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                     font=('Times New Roman', 20, "bold"),
                                     command=lambda: self.back_to_per(2))
        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')

        self.back1 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                               font=('Times New Roman', 20, "bold"),
                               command=lambda: self.back(1))
        self.back2 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                               font=('Times New Roman', 20, "bold"),
                               command=lambda: self.back(2))
        self.button_back_3 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                       font=('Times New Roman', 20, "bold"),
                                       command=lambda: self.__setitem__(3, 1))
        self.s = ttk.Style()
        self.s.configure("colour.Horizontal.TProgressbar", foreground="white", background="green")

        self.progress_bar1 = Progressbar(self, style="colour.Horizontal.TProgressbar",
                                         orient=HORIZONTAL, length=1000, mode='determinate')

        self.label_load = tk.Label(self, text="Ładowanie karty...", height=3, width=30, fg='white', bg='blue',
                                   font=('Times New Roman', 18, 'bold'))

        self.frame = tk.Frame(self, bg='blue', bd=4)
        self.label_reduced = tk.Button(self.frame, text='Bilet Ulgowy', height=9, width=20, bg='gold',
                                       font=('Times New Roman', 20, 'bold'),
                                       command=lambda: [self.confi(1), self.to_payment()])

        # regular
        self.frame_reg = tk.Frame(self, bg='blue', bd=4)
        self.label_regular = tk.Button(self.frame_reg, text='Bilet Normalny', height=9, width=20,
                                       font=('Times New Roman', 20, 'bold'), bg='gold',
                                       command=lambda: [self.confi(2), self.to_payment()])

        # set price of ticket
        self.label_zl = tk.Label(self.frame, text=str(self.controller.price) + ' zł', height=1, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        self.label_zl_reg = tk.Label(self.frame_reg, text=str(self.controller.price * 2) + ' zł', height=1,
                                     width=20, bg='gold', font=('Times New Roman', 20, 'bold'))

        self.zl_f1 = tk.Label(self.frame_month1, text=str(self.controller.price) + ' zł', height=1, width=20, bg='gold',
                              font=('Times New Roman', 20, 'bold'))
        self.zl_f2 = tk.Label(self.frame_month2, text=str(self.controller.price) + ' zł', height=1, width=20,
                              bg='gold',
                              font=('Times New Roman', 20, 'bold'))
        self.zl_f3 = tk.Label(self.frame_month3, text=str(self.controller.price) + ' zł', height=1, width=20,
                              bg='gold',
                              font=('Times New Roman', 20, 'bold'))
        self.zl_f4 = tk.Label(self.frame_month4, text=str(self.controller.price) + ' zł', height=1, width=20,
                              bg='gold',
                              font=('Times New Roman', 20, 'bold'))
        self.zl_f5 = tk.Label(self.frame_month5, text=str(self.controller.price) + ' zł', height=1, width=20,
                              bg='gold',
                              font=('Times New Roman', 20, 'bold'))

        # calculate sum to pay
        self.frame_pay = tk.Frame(self, bg='blue', bd=1)
        self.label_pay = tk.Label(self.frame_pay, text='Do zapłaty: ', height=5, width=20,
                                  font=('Times New Roman', 20, 'bold'), bg='gold')

        self.label_pay_sum = tk.Label(self.frame_pay, text=str(self.controller.sum), height=1, width=13,
                                      bg='white', font=('Times New Roman', 30, 'bold'))

        # payment
        self.button_cash = tk.Button(self, text="Gotówka", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'), command=self.show_money)
        self.button_card = tk.Button(self, text="Karta", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'),
                                     command=self.run_progressbar)

        self.frame_money = tk.Frame(self, bg='blue', bd=1)
        self.ten = tk.Button(self.frame_money, text=" 10 gr", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(0.10)])
        self.twenty = tk.Button(self.frame_money, text=" 20 gr", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_cash(0.20)])
        self.fifty = tk.Button(self.frame_money, text=" 50 gr", font=('Times New Roman', 20, 'bold'),
                               command=lambda: [self.minus_cash(0.50)])
        self.one = tk.Button(self.frame_money, text="  1 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(1)])
        self.two = tk.Button(self.frame_money, text="  2 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(2)])
        self.five = tk.Button(self.frame_money, text="  5 zł  ", font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.minus_cash(5)])
        self.ten_zl = tk.Button(self.frame_money, text=" 10 zł ", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_cash(10)])
        self.twenty_zl = tk.Button(self.frame_money, text=" 20 zł ", font=('Times New Roman', 20, 'bold'),
                                   command=lambda: [self.minus_cash(20)])
        self.fifty_zl = tk.Button(self.frame_money, text=" 50 zł ", font=('Times New Roman', 20, 'bold'),
                                  command=lambda: [self.minus_cash(50)])
        self.hundred_zl = tk.Button(self.frame_money, text="100 zł", font=('Times New Roman', 20, 'bold'),
                                    command=lambda: [self.minus_cash(100)])

        self.frame_cash_payment = tk.Frame(self, bg='blue', bd=4)
        self.label2 = tk.Label(self.frame_cash_payment,
                               text="Zapłacono. Odbierz bilety i resztę: " + str(self.controller.rest),
                               height=3, width=50, bg='gold', font=('Times New Roman', 18, 'bold'))

        self.card_label = tk.Label(self, image=card_image)
        self.card_label.image = card_image

        self.s1 = ttk.Style()
        self.s1.configure("colour.Horizontal.TProgressbar", foreground="white", background="green")
        self.progress_bar = Progressbar(self, style="colour.Horizontal.TProgressbar",
                                        orient=VERTICAL, length=281, mode='determinate')

        self.frame_payment = tk.Frame(self, bg='blue', bd=4)
        self.label_1 = tk.Label(self.frame_payment, text="Postępuj zgodnie z poleceniami na terminalu!",
                                height=3, width=50, bg='gold',
                                font=('Times New Roman', 18, 'bold'))
        self.label1 = tk.Label(self.frame_payment, text="Zapłacono! Odbierz kartę po załadowaniu!"
                               , height=3, width=50, bg='gold',
                               font=('Times New Roman', 18, 'bold'))

        self.frame1.grid(row=1, column=0, pady=50, sticky=''), self.button1.grid(), self.info1.grid()
        self.frame2.grid(row=1, columnspan=2, pady=50), self.button2.grid(), self.info2.grid()
        self.frame5.grid(row=2, column=1, pady=30, sticky=''), self.button5.grid(), self.info5.grid()
        self.frame4.grid(row=2, column=0, pady=30, sticky='e'), self.button4.grid(), self.info4.grid()
        self.frame3.grid(row=1, column=1, pady=50, padx=70, sticky='e'), self.button3.grid(), self.info3.grid()
        self.rowconfigure(1, weight=1)

    def back_af_cash_pay(self):
        self.frame_cash_payment.grid_remove(), self.frame_pay.grid_remove(), self.frame_money.grid_remove()
        self.back1.grid_remove(), self.button_cash.grid_remove()
        time.sleep(2)

        self.card_label.grid(row=1, columnspan=2, padx=5, sticky='')
        self.progress_bar1.grid(row=2, columnspan=2, pady=10)
        self.run_progressbar1()
        self.card_label.grid_remove()
        self.label.configure(text="Wybierz bilet okresowy")
        self.frame1.grid(), self.frame2.grid(), self.frame3.grid(), self.frame4.grid(), self.frame5.grid()
        self.button_back.grid()
        self.update(), self.controller.update()
        self.controller.show_frame("StartPage")

    def minus_cash(self, count):
        if self.controller.sum - count < 0.01:
            self.label_pay_sum.configure(text=str(0.00))
            self.controller.rest = self.controller.sum - count
            self.frame_cash_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
            if self.controller.rest < -0.01:
                self.label2.configure(text="Zapłacono. Odbierz kartę po załadowaniu i resztę: " +
                                           ("{0:.2f}".format(-self.controller.rest)))
            else:
                self.label2.configure(text="Zapłacono. Odbierz kartę po załadowaniu.")

            self.label2.grid(), self.label2.update(), self.back_af_cash_pay()
        else:
            self.controller.sum -= count
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def run_progressbar1(self):
        self.progress_bar1["maximum"] = 100
        self.label_load.grid(row=1, columnspan=2, sticky='s', pady=10)

        for i in range(101):
            time.sleep(0.025)
            self.progress_bar1["value"] = i
            self.progress_bar1.update()

        if self.progress_bar1["value"] == self.progress_bar1["maximum"]:
            self.progress_bar1["value"] = 0

        self.progress_bar1.grid_remove()
        self.label_load.grid_remove()

    def open_ticket(self, key):
        self.label.configure(text='Wybierz bilet okresowy')
        self.frame1.grid_remove(), self.frame2.grid_remove(), self.frame3.grid_remove(), self.frame4.grid_remove(),
        self.frame5.grid_remove()
        self.frame_month1.grid(row=1, column=0, pady=50, sticky=''), self.zw1.grid(), self.info_zw1.grid()
        self.frame_month2.grid(row=1, columnspan=2, pady=50), self.npz1.grid(), self.info_npz1.grid()
        self.frame_month3.grid(row=2, column=1, pady=30, sticky=''), self.npz2.grid(), self.info_npz2.grid()
        self.frame_month4.grid(row=2, column=0, pady=30, sticky='e'), self.npz3.grid(), self.info_npz3.grid()
        self.frame_month5.grid(row=1, column=1, pady=50, padx=70, sticky='e'), self.npz4.grid()
        self.info_npz4.grid(), self.button_back.grid_remove()
        self.btn_to_per.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 1:
            self.zl_f1.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f1.configure(text=str(156.0) + ' zł')
            self.zl_f2.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f2.configure(text=str(179.0) + ' zł')
            self.zl_f3.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f3.configure(text=str(122.0) + ' zł')
            self.zl_f4.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f4.configure(text=str(160.0) + ' zł')
            self.zl_f5.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f5.configure(text=str(198.0) + ' zł')
        if key == 2:
            self.zl_f1.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f1.configure(text=str(195.0) + ' zł')
            self.zl_f2.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f2.configure(text=str(223.0) + ' zł')
            self.zl_f3.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f3.configure(text=str(152.0) + ' zł')
            self.zl_f4.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f4.configure(text=str(200.0) + ' zł')
            self.zl_f5.grid(row=0, padx=0, pady=10, sticky='s')
            self.zl_f5.configure(text=str(247.0) + ' zł')
        else:
            pass

    def open_metro(self):
        self.label.configure(text='Wybierz bilet miesięczny')
        self.frame1.grid_remove(), self.frame2.grid_remove(), self.frame3.grid_remove(), self.frame4.grid_remove(),
        self.frame5.grid_remove()
        self.button_back.grid_remove()
        self.btn_to_per2.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.metro.grid(row=1, column=0, padx=50, pady=50, sticky=''), self.m1.grid(), self.info_m1.grid()
        self.metro2.grid(row=1, column=1, padx=50, pady=50, sticky=''), self.m2.grid(), self.info_m2.grid()
        self.metro3.grid(row=2, column=0, pady=50, sticky=''), self.m3.grid(), self.info_m3.grid()
        self.metro4.grid(row=2, column=1, pady=50, sticky=''), self.m4.grid(), self.info_m4.grid()

    def back_to_per(self, key):
        if key == 1:
            self.frame_month1.grid_remove(), self.frame_month2.grid_remove(), self.frame_month3.grid_remove()
            self.frame_month4.grid_remove(), self.frame_month5.grid_remove(), self.btn_to_per.grid_remove()
            self.zl_f1.grid_remove(), self.zl_f2.grid_remove(), self.zl_f3.grid_remove(), self.zl_f4.grid_remove()
            self.zl_f5.grid_remove()
        if key == 2:
            self.metro.grid_remove(), self.metro2.grid_remove(), self.metro3.grid_remove()
            self.metro4.grid_remove(), self.btn_to_per2.grid_remove()
            self.label.configure(text="Wybierz bilet okresowy")

        self.frame1.grid(), self.frame2.grid(), self.frame3.grid(), self.frame4.grid(), self.frame5.grid(),

        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')

    def back(self, key):
        self.frame.grid_remove(), self.frame_reg.grid_remove(), self.frame_pay.grid_remove()
        if key == 1:
            self.frame_month1.grid(), self.frame_month2.grid(), self.frame_month3.grid(), self.frame_month4.grid(),
            self.frame_month5.grid(), self.back1.grid_remove()
            self.btn_to_per.grid(row=0, column=1, pady=5, padx=10, sticky='se')
            self.card_label.grid_remove(), self.button_card.grid_remove(), self.button_cash.grid_remove()
            self.frame_money.grid_remove()
        if key == 2:
            self.metro.grid(), self.metro2.grid(), self.metro3.grid(), self.metro4.grid(), self.back2.grid_remove(),
            self.card_label.grid_remove(), self.button_card.grid_remove(), self.button_cash.grid_remove(),
            self.frame_money.grid_remove()
            self.btn_to_per2.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.label.configure(text='Wybierz bilet okresowy')

    def choose_option(self, option):
        if option == 1:
            self.controller.option = 1
        if option == 2:
            self.controller.option = 2
        if option == 3:
            self.controller.option = 3
        if option == 4:
            self.controller.option = 4
        if option == 5:
            self.controller.option = 5

    def choose_sum(self, key):
        if self.controller.option == 1 and key == 1:
            self.__setitem__(1, 36.0)
        elif self.controller.option == 1 and key == 2:
            self.__setitem__(1, 43.0)
        elif self.controller.option == 1 and key == 3:
            self.__setitem__(1, 29.0)
        elif self.controller.option == 1 and key == 4:
            self.__setitem__(1, 37.0)
        elif self.controller.option == 1 and key == 5:
            self.__setitem__(1, 48.0)
        elif self.controller.option == 2 and key == 1:
            self.__setitem__(1, 41.0)
        elif self.controller.option == 2 and key == 2:
            self.__setitem__(1, 47.0)
        elif self.controller.option == 2 and key == 3:
            self.__setitem__(1, 32.0)
        elif self.controller.option == 2 and key == 4:
            self.__setitem__(1, 42.0)
        elif self.controller.option == 2 and key == 5:
            self.__setitem__(1, 52.0)
        elif self.controller.option == 3 and key == 1:
            self.__setitem__(2, 156.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 3 and key == 2:
            self.__setitem__(2, 179.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 3 and key == 3:
            self.__setitem__(2, 122.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 3 and key == 4:
            self.__setitem__(2, 160.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 3 and key == 5:
            self.__setitem__(2, 198.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 4 and key == 1:
            self.__setitem__(2, 195.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 4 and key == 2:
            self.__setitem__(2, 223.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 4 and key == 3:
            self.__setitem__(2, 152.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 4 and key == 4:
            self.__setitem__(2, 200.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 4 and key == 5:
            self.__setitem__(2, 247.0), self.label_pay_sum.configure(text=str(self.controller.sum))
        elif self.controller.option == 5 and key == 1:
            self.__setitem__(1, 66.0),
        elif self.controller.option == 5 and key == 2:
            self.__setitem__(1, 35.0)
        elif self.controller.option == 5 and key == 3:
            self.__setitem__(1, 38.0)
        elif self.controller.option == 5 and key == 4:
            self.__setitem__(1, 48.0)

    def confi(self, option):
        if option == 1:
            self.controller.sum = self.controller.price
        if option == 2:
            self.controller.sum = self.controller.price*2
        self.label_pay_sum.configure(text=str(self.controller.sum))

    def check_relief(self, key):
        self.label.configure(text="Wybierz ulgę")
        if key == 1:
            self.frame_month1.grid_remove(), self.frame_month2.grid_remove(), self.frame_month3.grid_remove()
            self.frame_month4.grid_remove(), self.frame_month5.grid_remove(), self.btn_to_per.grid_remove()
            self.back1.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 2:
            self.metro.grid_remove(), self.metro2.grid_remove(), self.metro3.grid_remove()
            self.metro4.grid_remove(), self.btn_to_per2.grid_remove()
            self.back2.grid(row=0, column=1, pady=5, padx=10, sticky='se')

        if self.controller.option == 1 or self.controller.option == 2 or self.controller.option == 5:
            self.frame.grid(row=1, column=0, padx=50, pady=5, sticky='w')
            self.label_reduced.grid(row=1, column=0, padx=0, pady=5, sticky='')
            self.label_zl.grid(row=1, column=0, padx=0, pady=10, sticky='s')
            self.label_zl.configure(text=str(self.controller.price) + ' zł')
            self.frame_reg.grid(row=1, columnspan=2, padx=0, pady=5, sticky='')
            self.label_regular.grid(row=1, column=1, padx=0, pady=5, sticky='')
            self.label_zl_reg.grid(row=1, column=1, padx=0, pady=10, sticky='s')
            self.label_zl_reg.configure(text=str(self.controller.price * 2) + ' zł')

        else:
            self.label.configure(text="Wybierz sposób płatności")
            self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
            self.button_card.grid(row=1, column=1, padx=5, sticky='')
            self.btn_to_per.grid_remove()
            self.back1.grid(row=0, column=1, pady=5, padx=10, sticky='se')

    def update(self):
        self.label_pay_sum.configure(text="0")

    def run_progressbar(self):
        self.progress_bar.grid(row=1, column=1, padx=150, sticky='e')
        self.progress_bar["maximum"] = 100
        self.show_card(), self.label.configure(text="Wybierz sposób płatności"), self.back1.grid_remove()
        self.button_back_3.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        for i in range(101):
            time.sleep(0.055)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            if self.controller.value == 1:
                self.progress_bar["value"] = 0
                self.progress_bar.update()
                self.progress_bar.grid_remove(), self.frame_payment.grid_remove()
                self.label_1.grid_remove(), self.card_label.grid_remove()
                self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
                self.button_card.grid(row=1, column=1, padx=5, sticky='')
                self.button_back_3.grid_remove(), self.back1.grid(row=0, column=1, pady=5, padx=10, sticky='se')
                break

        self.controller.value = 0

        if self.progress_bar["maximum"] == self.progress_bar["value"]:
            self.label_1.grid_remove()
            self.progress_bar.after(1, self.progress_bar.grid_remove)
            self.label1.grid(), self.label1.update()
            time.sleep(3)
            self.label1.grid_remove()
            self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
            self.frame_payment.grid_remove()
            self.button_cash.grid_remove(), self.button_card.grid_remove()
            self.progress_bar1.grid(row=2, columnspan=2, pady=10)
            self.card_label.grid_remove()
            self.card_label.grid(row=1, columnspan=2, sticky='', pady=10)
            self.label_load.grid(row=1, columnspan=2, sticky='s', pady=10)
            self.run_progressbar1()
            self.card_label.grid_remove(), self.button_back_3.grid_remove()

            self.label.configure(text="Wybierz bilet okresowy")
            self.frame1.grid(), self.frame2.grid(), self.frame3.grid(), self.frame4.grid(), self.frame5.grid()
            self.button_back.grid()
            self.update(), self.controller.update()
            self.controller.show_frame("StartPage")

    def show_card(self):
        self.frame_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
        self.label_1.grid(), self.button_cash.grid_remove()
        self.card_label.grid(row=1, column=0, padx=5, sticky='e')

    def show_money(self):
        self.button_card.grid_remove()
        self.frame_pay.grid(row=1, column=1, pady=25, sticky='')
        self.label_pay.grid(row=1, column=1, padx=5, pady=5, sticky='')
        self.label_pay.configure(text="Do zapłaty\n pozostało:")
        self.label_pay_sum.grid(row=1, column=1, padx=5, pady=5, sticky='s')
        self.frame_money.grid(row=1, columnspan=2)

        self.ten.grid(), self.twenty.grid(), self.fifty.grid(), self.one.grid(), self.two.grid(), self.five.grid(),
        self.ten_zl.grid(), self.twenty_zl.grid(), self.fifty_zl.grid(), self.hundred_zl.grid()

    def to_payment(self):
        self.frame_reg.grid_remove(), self.frame.grid_remove()
        self.label.configure(text="Wybierz sposób płatności")
        self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
        self.button_card.grid(row=1, column=1, padx=5, sticky='')

    def __setitem__(self, key, value):
        if key == 1:
            self.controller.price = value
        elif key == 2:
            self.controller.sum = value
        elif key == 3:
            self.controller.value = 1


class Metro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.price_metro = controller.price_metro
        self.controller.sum_metro = controller.sum_metro

        photo_image, photo_pl, photo_en, card_image = open_images()
        self.background_label = tk.Label(self, image=photo_image)
        self.background_label.image = photo_image
        self.background_label.grid(rowspan=4, columnspan=2, sticky="news")

        self.label = tk.Label(self, text="Wybierz bilet metropolitalny", font=controller.title_font,
                              fg='white', bg='blue')
        self.label.grid(row=0, columnspan=3, sticky='nwse')
        self.pl_label = Button(self, image=photo_pl)
        self.pl_label.image = photo_pl
        self.pl_label.grid(row=0, column=0, sticky='w', padx=10)

        self.en_label = Button(self, image=photo_en)
        self.en_label.image = photo_en
        self.en_label.grid(row=0, column=0, pady=5, padx=75, sticky='w')

        btn_info = tk.Button(self, text="Info", bg='gold', height=1, width=5, font=('Times New Roman', 20, 'bold'),
                             command=lambda: controller.show_frame("Info"))
        btn_info.grid(row=0, column=1, pady=5, padx=175, sticky='se')

        self.button1_1 = tk.Button(self, text="1-przejazdowy", height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: self.open_one_pass())
        self.button1_2 = tk.Button(self, text="24-godzinny", height=6, width=20, bg='gold',
                                   font=('Times New Roman', 20, "bold"),
                                   command=lambda: self.open_24_hours())
        self.button1_3 = tk.Button(self, text="72-godzinny", height=6, width=20,
                                   bg='gold', font=('Times New Roman', 20, "bold"),
                                   command=lambda: self.open_72_hours())

        # frame of reduced one pass
        self.frame_one_pass_red = tk.Frame(self, bg='blue', bd=1)
        self.one_pass_red = tk.Button(self.frame_one_pass_red, text='Jeden przejazd\n linie zwykłe', height=6,
                                      width=20, bg='gold', font=('Times New Roman', 20, 'bold'),
                                      command=lambda: [self.__setitem__(1, 1.70), self.check_relief(1)])
        self.info_opr = tk.Label(self.frame_one_pass_red, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                 font=('Times New Roman', 14, ' bold italic'), width=31)

        # frame of reduced one pass night
        self.frame_one_pass_red1 = tk.Frame(self, bg='blue', bd=1)
        self.one_pass_red1 = tk.Button(self.frame_one_pass_red1, text='Jeden przejazd\n linie zwykłe,\n nocne '
                                                                      'i pospieszne', height=6, width=20, bg='gold',
                                       font=('Times New Roman', 20, 'bold'),
                                       command=lambda: [self.__setitem__(1, 2.20), self.check_relief(1)])
        self.info_opr2 = tk.Label(self.frame_one_pass_red1, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 14, 'bold italic'), width=31)

        # back buttons
        self.button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                     font=('Times New Roman', 20, "bold"),
                                     command=lambda: controller.show_frame("StartPage"))
        self.button_to_metro = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                         font=('Times New Roman', 20, "bold"),
                                         command=lambda: [self.controller.update(),
                                                          self.back_to_metro()])
        self.button_to_choice = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                          font=('Times New Roman', 20, "bold"),
                                          command=lambda: [self.back_to_checking(1), self.update(),
                                                           controller.update()])
        self.button_to_choice1 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                           font=('Times New Roman', 20, "bold"),
                                           command=lambda: [self.back_to_checking(2), self.update(),
                                                            controller.update()])
        self.button_to_choice2 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                           font=('Times New Roman', 20, "bold"),
                                           command=lambda: [self.back_to_checking(3), self.update(),
                                                            controller.update()])
        self.button_to_pay = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                       font=('Times New Roman', 20, "bold"),
                                       command=lambda: [self.back_to_pay(1)])
        self.button_to_pay1 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                        font=('Times New Roman', 20, "bold"),
                                        command=lambda: [self.back_to_pay(2)])
        self.button_to_pay2 = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                        font=('Times New Roman', 20, "bold"),
                                        command=lambda: [self.back_to_pay(3)])
        self.back_choice_pay = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                         font=('Times New Roman', 20, "bold"),
                                         command=lambda: self.__setitem__(3, 1))

        self.btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                                    font=('Times New Roman', 20, 'bold'), command=lambda: self.to_payment(1))
        self.btn_accept1 = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                                     font=('Times New Roman', 20, 'bold'), command=lambda: self.to_payment(2))
        self.btn_accept2 = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                                     font=('Times New Roman', 20, 'bold'), command=lambda: self.to_payment(3))

        # button for 24 hours
        self.frame_thf_comunal = tk.Frame(self, bg='blue', bd=1)
        self.thf_comunal = tk.Button(self.frame_thf_comunal, text="24-godzinny\n komunalny", height=6, width=19,
                                     bg='gold', font=('Times New Roman', 20, "bold"),
                                     command=lambda: [self.__setitem__(1, 7.50), self.check_relief(2)])
        self.info_thf1 = tk.Label(self.frame_thf_comunal, width=33, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, ' bold italic'))

        self.frame_thf_comunal_train = tk.Frame(self, bg='blue', bd=1)
        self.thf_comunal_train = tk.Button(self.frame_thf_comunal_train, text="24-godzinny\n kolejowo-komunalny",
                                           height=6, width=20, bg='gold',
                                           font=('Times New Roman', 20, "bold"),
                                           command=lambda: [self.__setitem__(1, 10.0), self.check_relief(2)])
        self.info_thf2 = tk.Label(self.frame_thf_comunal_train, text='Dwóch organizatorów:\n SKM, PR i '
                                                                     'ZKM Gdynia \nalbo ZTM Gdańsk albo MZK Wejherowo ',
                                  font=('Times New Roman', 12, ' bold italic'), width=35)

        self.frame_thf_all = tk.Frame(self, bg='blue', bd=1)
        self.thf_all = tk.Button(self.frame_thf_all, text="24-godzinny\n kolejowo-komunalny", height=6, width=19,
                                 bg='gold', font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.__setitem__(1, 11.50), self.check_relief(2)])
        self.info_thf3 = tk.Label(self.frame_thf_all, text='Wszystkich organizatorów:\n SKM, PR i '
                                                           'ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo ',
                                  font=('Times New Roman', 12, ' bold italic'))

        # buttons for 72 hours
        self.frame_shs_comunal = tk.Frame(self, bg='blue', bd=1)
        self.shs_comunal = tk.Button(self.frame_shs_comunal, text="72-godzinny\n komunalny", height=6, width=19,
                                     bg='gold', font=('Times New Roman', 20, "bold"),
                                     command=lambda: [self.__setitem__(1, 15.0), self.check_relief(3)])
        self.info_shs1 = tk.Label(self.frame_shs_comunal, width=33, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, ' bold italic'))

        self.frame_shs_all = tk.Frame(self, bg='blue', bd=1)
        self.shs_all = tk.Button(self.frame_shs_all, text="72-godzinny\n kolejowo-komunalny", height=6, width=19,
                                 bg='gold', font=('Times New Roman', 20, "bold"),
                                 command=lambda: [self.__setitem__(1, 23.0), self.check_relief(3)])
        self.info_shs3 = tk.Label(self.frame_shs_all, text='Wszystkich organizatorów:\n SKM, PR i '
                                                           'ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo ',
                                  font=('Times New Roman', 12, ' bold italic'))

        self.frame = tk.Frame(self, bg='blue', bd=4)
        self.label_reduced = tk.Label(self.frame, text='Bilet Ulgowy\n', height=9, width=20, bg='gold',
                                      font=('Times New Roman', 20, 'bold'))
        self.label_reduced_l = tk.Label(self.frame, text=controller.counter_reduced, height=2, width=3, bg='white',
                                        font=('Times New Roman', 30, 'bold'))
        self.btn_reduced_up = tk.Button(self.frame, text="+", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                        command=lambda: self.on_click_up(controller.price))
        self.btn_reduced_down = tk.Button(self.frame, text="-", height=2, width=4, font=('Times New Roman', 27, 'bold'),
                                          command=lambda: self.on_click_down(controller.price))

        # regular
        self.frame_reg = tk.Frame(self, bg='blue', bd=4)
        self.label_regular = tk.Label(self.frame_reg, text='Bilet Normalny', height=9, width=20,
                                      font=('Times New Roman', 20, 'bold'), bg='gold')
        self.label_regular_l = tk.Label(self.frame_reg, text=controller.counter_regular, height=2, width=3, bg='white',
                                        font=('Times New Roman', 30, 'bold'))

        self.btn_regular_up = tk.Button(self.frame_reg, text="+", height=2, width=4,
                                        font=('Times New Roman', 27, 'bold'),
                                        command=lambda: self.on_click_up_r(controller.price * 2))

        self.btn_regular_down = tk.Button(self.frame_reg, text="-", height=2, width=4,
                                          font=('Times New Roman', 27, 'bold'),
                                          command=lambda: self.on_click_down_r(controller.price * 2))

        # set price of ticket
        self.label_zl = tk.Label(self.frame, text=str(self.controller.price) + ' zł', height=1, width=20, bg='gold',
                                 font=('Times New Roman', 20, 'bold'))
        self.label_zl_reg = tk.Label(self.frame_reg, text=str(self.controller.price * 2) + ' zł', height=1,
                                     width=20, bg='gold', font=('Times New Roman', 20, 'bold'))

        # calculate sum to pay
        self.frame_pay = tk.Frame(self, bg='blue', bd=1)
        self.label_pay = tk.Label(self.frame_pay, text='Do zapłaty: ', height=5, width=20,
                                  font=('Times New Roman', 20, 'bold'), bg='gold')

        self.label_pay_sum = tk.Label(self.frame_pay, text=str(self.controller.sum), height=1, width=13,
                                      bg='white', font=('Times New Roman', 30, 'bold'))

        # payment
        self.button_cash = tk.Button(self, text="Gotówka", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'), command=self.show_money)
        self.button_card = tk.Button(self, text="Karta", bg='gold', height=7, width=15,
                                     font=('Times New Roman', 25, 'bold'),
                                     command=self.run_progressbar)

        self.frame_money = tk.Frame(self, bg='blue', bd=1)
        self.ten = tk.Button(self.frame_money, text=" 10 gr", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(0.10)])
        self.twenty = tk.Button(self.frame_money, text=" 20 gr", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_cash(0.20)])
        self.fifty = tk.Button(self.frame_money, text=" 50 gr", font=('Times New Roman', 20, 'bold'),
                               command=lambda: [self.minus_cash(0.50)])
        self.one = tk.Button(self.frame_money, text="  1 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(1)])
        self.two = tk.Button(self.frame_money, text="  2 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_cash(2)])
        self.five = tk.Button(self.frame_money, text="  5 zł  ", font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.minus_cash(5)])
        self.ten_zl = tk.Button(self.frame_money, text=" 10 zł ", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_cash(10)])
        self.twenty_zl = tk.Button(self.frame_money, text=" 20 zł ", font=('Times New Roman', 20, 'bold'),
                                   command=lambda: [self.minus_cash(20)])

        self.frame_cash_payment = tk.Frame(self, bg='blue', bd=4)
        self.label2 = tk.Label(self.frame_cash_payment,
                               text="Zapłacono. Odbierz bilety i resztę: " + str(self.controller.rest),
                               height=3, width=50, bg='gold', font=('Times New Roman', 18, 'bold'))

        self.card_label = tk.Label(self, image=card_image)
        self.card_label.image = card_image

        self.s1 = ttk.Style()
        self.s1.configure("colour.Horizontal.TProgressbar", foreground="white", background="green")
        self.progress_bar = Progressbar(self, style="colour.Horizontal.TProgressbar",
                                        orient=VERTICAL, length=281, mode='determinate')

        self.frame_payment = tk.Frame(self, bg='blue', bd=4)
        self.label_1 = tk.Label(self.frame_payment, text="Postępuj zgodnie z poleceniami na terminalu!",
                                height=3, width=50, bg='gold',
                                font=('Times New Roman', 18, 'bold'))
        self.label1 = tk.Label(self.frame_payment, text="Zapłacono. Odbierz bilety!", height=3, width=50, bg='gold',
                               font=('Times New Roman', 18, 'bold'))

        self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.button1_1.grid(row=1, columnspan=2, pady=5, padx=5, sticky='')
        self.button1_2.grid(row=2, column=0, pady=5, padx=80, sticky='n')
        self.button1_3.grid(row=2, column=1, pady=5, padx=5, sticky='n')

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def back_af_cash_pay(self):
        time.sleep(2)
        self.frame_cash_payment.grid_remove(), self.frame_pay.grid_remove(), self.frame_money.grid_remove()
        self.button_to_pay.grid_remove(), self.button_cash.grid_remove()
        self.button1_1.grid(row=1, columnspan=2, pady=5, padx=5, sticky='')
        self.button1_2.grid(row=2, column=0, pady=5, padx=80, sticky='n')
        self.button1_3.grid(row=2, column=1, pady=5, padx=5, sticky='n')
        self.label.configure(text="Wybierz bilet jednorazowy")
        self.button_to_pay.grid_remove(), self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.update(), self.controller.update()
        self.controller.show_frame("StartPage")

    def minus_cash(self, count):
        if self.controller.sum - count < 0.01:
            self.label_pay_sum.configure(text=str(0.00))
            self.controller.rest = self.controller.sum - count
            self.frame_cash_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
            if self.controller.rest < -0.01:
                self.label2.configure(text="Zapłacono. Odbierz bilety i resztę: " +
                                           ("{0:.2f}".format(-self.controller.rest)))
            else:
                self.label2.configure(text="Zapłacono. Odbierz bilety.")

            self.label2.grid(), self.label2.update(), self.back_af_cash_pay()
        else:
            self.controller.sum -= count
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def open_one_pass(self):
        self.button1_1.grid_remove(), self.button1_2.grid_remove(), self.button1_3.grid_remove()
        self.button_back.grid_remove(), self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.frame_one_pass_red.grid(row=1, column=0, padx=5, sticky='e')
        self.frame_one_pass_red1.grid(row=1, column=1, padx=5, sticky='')
        self.info_opr.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.info_opr2.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.one_pass_red.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.one_pass_red1.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.label.configure(text="Wybierz bilet jednorazowy metropolitalny")

    def open_24_hours(self):
        self.button1_1.grid_remove(), self.button1_2.grid_remove(), self.button1_3.grid_remove()
        self.button_back.grid_remove()
        self.label.configure(text="Wybierz bilet 24-godzinny metropolitalny")
        self.frame_thf_comunal_train.grid(row=2, column=0, pady=5, padx=80, sticky='n')
        self.frame_thf_comunal.grid(row=1, columnspan=2, padx=5, sticky='')
        self.frame_thf_all.grid(row=2, column=1, pady=5, padx=5, sticky='n')
        self.thf_all.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.thf_comunal_train.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.thf_comunal.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.info_thf1.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.info_thf2.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.info_thf3.grid(row=1, column=0, padx=0, pady=0, sticky='s')

    def open_72_hours(self):
        self.button1_1.grid_remove(), self.button1_2.grid_remove(), self.button1_3.grid_remove()
        self.button_back.grid_remove(), self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.label.configure(text="Wybierz bilet 72-godzinny metropolitalny")
        self.frame_shs_all.grid(row=1, column=1, padx=5, sticky='')
        self.frame_shs_comunal.grid(row=1, column=0, padx=5, sticky='e')
        self.shs_all.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.shs_comunal.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.info_shs1.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.info_shs3.grid(row=1, column=0, padx=0, pady=0, sticky='s')

    def check_relief(self, key):
        self.label.configure(text="Wybierz ulgę")
        if key == 1:
            self.frame_one_pass_red.grid_remove(), self.frame_one_pass_red1.grid_remove()
            self.button_to_choice.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 2:
            self.frame_thf_comunal.grid_remove(), self.frame_thf_comunal_train.grid_remove(),
            self.frame_thf_all.grid_remove(), self.button_to_choice1.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 3:
            self.frame_shs_all.grid_remove(), self.frame_shs_comunal.grid_remove(),
            self.button_to_choice2.grid(row=0, column=1, pady=5, padx=10, sticky='se')

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
        self.label_zl_reg.configure(text=str(self.controller.price * 2) + ' zł')

        self.frame_pay.grid(row=1, column=1, padx=50, sticky='e')
        self.label_pay.grid(row=1, column=1, padx=5, pady=5, sticky='')
        self.label_pay_sum.grid(row=1, column=1, padx=5, pady=5, sticky='s')
        if key == 1: self.btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')
        if key == 2: self.btn_accept1.grid(row=2, columnspan=2, pady=30, sticky='s')
        if key == 3: self.btn_accept2.grid(row=2, columnspan=2, pady=30, sticky='s')

    def back_to_checking(self, key):
        self.frame.grid_remove(), self.frame_reg.grid_remove(), self.frame_pay.grid_remove()
        self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 1:
            self.button_to_choice.grid_remove(), self.btn_accept.grid_remove()
            self.label.configure(text="Wybierz bilet jednorazowy metropolitalny")
            self.frame_one_pass_red.grid(row=1, column=0, padx=5, sticky='e')
            self.frame_one_pass_red1.grid(row=1, column=1, padx=5, sticky='')
        if key == 2:
            self.button_to_choice1.grid_remove(), self.btn_accept1.grid_remove()
            self.label.configure(text="Wybierz bilet 24-godzinny metropolitalny")
            self.frame_thf_comunal_train.grid(row=2, column=0, pady=5, padx=80, sticky='n')
            self.frame_thf_comunal.grid(row=1, columnspan=2, padx=5, sticky='')
            self.frame_thf_all.grid(row=2, column=1, pady=5, padx=5, sticky='n')
        if key == 3:
            self.button_to_choice2.grid_remove(), self.btn_accept2.grid_remove()
            self.label.configure(text="Wybierz bilet 72-godzinny metropolitalny")
            self.frame_shs_all.grid(row=1, column=1, padx=5, sticky='')
            self.frame_shs_comunal.grid(row=1, column=0, padx=5, sticky='e')

    def back_to_pay(self, key):
        self.label.configure(text="Wybierz ulgę")
        if key == 1:
            self.btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')
            self.button_to_pay.grid_remove()
            self.button_to_choice.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 2:
            self.btn_accept1.grid(row=2, columnspan=2, pady=30, sticky='s')
            self.button_to_pay1.grid_remove(),
            self.button_to_choice1.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 3:
            self.btn_accept2.grid(row=2, columnspan=2, pady=30, sticky='s')
            self.button_to_pay2.grid_remove()
            self.button_to_choice2.grid(row=0, column=1, pady=5, padx=10, sticky='se')

        self.frame.grid(row=1, column=0, padx=50, pady=5, sticky='w')
        self.frame_reg.grid(row=1, columnspan=2, padx=0, pady=5, sticky='')
        self.frame_pay.grid(row=1, column=1, padx=50, sticky='e')
        self.button_cash.grid_remove(), self.button_card.grid_remove()
        self.frame_money.grid_remove()

    def back_to_metro(self):
        self.label.configure(text="Wybierz bilet metropolitalny")
        # self.frame_one_pass_reg1.grid_remove(), self.frame_one_pass_reg.grid_remove()
        self.frame_one_pass_red1.grid_remove(), self.frame_one_pass_red.grid_remove()
        # self.frame_pay.grid_remove(),
        self.frame_thf_all.grid_remove(), self.frame_thf_comunal.grid_remove()
        self.frame_thf_comunal_train.grid_remove(), self.frame_shs_comunal.grid_remove()
        self.frame_shs_all.grid_remove()
        self.button_to_metro.grid_remove(), self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.button1_1.grid(row=1, columnspan=2, pady=5, padx=5, sticky='')
        self.button1_2.grid(row=2, column=0, pady=5, padx=80, sticky='n')
        self.button1_3.grid(row=2, column=1, pady=5, padx=5, sticky='n')
        self.btn_accept.grid_remove()

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

    def run_progressbar(self):
        self.progress_bar.grid(row=1, column=1, padx=150, sticky='e')
        self.progress_bar["maximum"] = 100
        self.show_card(), self.button_to_pay.grid_remove(), self.label.configure(text="Wybierz sposób płatności")
        self.back_choice_pay.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        for i in range(101):
            time.sleep(0.055)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            if self.controller.value == 1:
                self.progress_bar["value"] = 0
                self.progress_bar.update()
                self.progress_bar.grid_remove(), self.frame_payment.grid_remove()
                self.label_1.grid_remove(), self.card_label.grid_remove()
                self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
                self.button_card.grid(row=1, column=1, padx=5, sticky='')
                self.back_choice_pay.grid_remove()
                self.button_to_pay.grid(row=0, column=1, pady=5, padx=10, sticky='se')
                break

        self.controller.value = 0

        if self.progress_bar["maximum"] == self.progress_bar["value"]:
            self.label_1.grid_remove()
            self.progress_bar.after(1, self.progress_bar.grid_remove)
            self.label1.grid(), self.label1.update()
            time.sleep(3)
            self.label1.grid_remove()
            self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
            self.frame_payment.grid_remove(), self.card_label.grid_remove()
            self.button_cash.grid_remove(), self.button_card.grid_remove()

            self.label.configure(text="Wybierz bilet metropolitalny")
            self.back_choice_pay.grid_remove(), self.button_back.grid(row=0, column=1, pady=5, padx=10, sticky='se')
            self.button1_1.grid(row=1, columnspan=2, pady=5, padx=5, sticky='')
            self.button1_2.grid(row=2, column=0, pady=5, padx=80, sticky='n')
            self.button1_3.grid(row=2, column=1, pady=5, padx=5, sticky='n')
            self.update(), self.controller.update()
            self.controller.show_frame("StartPage")

    def show_card(self):
        self.frame_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
        self.label_1.grid(), self.button_cash.grid_remove()
        self.card_label.grid(row=1, column=0, padx=5, sticky='e')

    def show_money(self):
        self.button_card.grid_remove()
        self.frame_pay.grid(row=1, columnspan=2, pady=25, sticky='')
        self.label_pay.configure(text="Do zapłaty\n pozostało:")
        self.frame_money.grid(row=1, columnspan=2)
        self.ten.grid(), self.twenty.grid(), self.fifty.grid(), self.one.grid(), self.two.grid(), self.five.grid(),
        self.ten_zl.grid(), self.twenty_zl.grid()

    def to_payment(self, key):
        self.frame_reg.grid_remove(), self.frame.grid_remove(), self.frame_pay.grid_remove()
        if key == 1:
            self.btn_accept.grid_remove(), self.button_to_choice.grid_remove()
            self.button_to_pay.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 2:
            self.btn_accept1.grid_remove(), self.button_to_choice1.grid_remove()
            self.button_to_pay1.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        if key == 3:
            self.btn_accept2.grid_remove(), self.button_to_choice2.grid_remove()
            self.button_to_pay2.grid(row=0, column=1, pady=5, padx=10, sticky='se')

        self.label.configure(text="Wybierz sposób płatności")
        self.button_cash.grid(row=1, column=0, padx=5, sticky='e')
        self.button_card.grid(row=1, column=1, padx=5, sticky='')

    def __setitem__(self, key, value):
        if key == 1:
            self.controller.price = value
        elif key == 2:
            self.controller.sum = value
        elif key == 3:
            self.controller.value = 1


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
