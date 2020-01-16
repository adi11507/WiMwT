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

        for F in (StartPage, Ticket, Card, SeasonTicket, Metro, Info):
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
        self.label_zl_reg = tk.Label(self.frame_reg, text=str(self.controller.price*2) + ' zł', height=1,
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
                             command=lambda: [self.minus_ten_gr()])
        self.twenty = tk.Button(self.frame_money, text=" 20 gr", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_twenty_gr()])
        self.fifty = tk.Button(self.frame_money, text=" 50 gr", font=('Times New Roman', 20, 'bold'),
                               command=lambda: [self.minus_fifty_gr()])
        self.one = tk.Button(self.frame_money, text="  1 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_one()])
        self.two = tk.Button(self.frame_money, text="  2 zł  ", font=('Times New Roman', 20, 'bold'),
                             command=lambda: [self.minus_two()])
        self.five = tk.Button(self.frame_money, text="  5 zł  ", font=('Times New Roman', 20, 'bold'),
                              command=lambda: [self.minus_five()])
        self.ten_zl = tk.Button(self.frame_money, text=" 10 zł ", font=('Times New Roman', 20, 'bold'),
                                command=lambda: [self.minus_ten()])
        self.twenty_zl = tk.Button(self.frame_money, text=" 20 zł ", font=('Times New Roman', 20, 'bold'),
                                   command=lambda: [self.minus_twenty()])

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

    def minus_ten_gr(self):
        if self.controller.sum - 0.10 < 0:
            self.controller.rest = self.controller.sum - 0.10
            self.label_pay_sum.configure(text=str(0.00))
            if self.controller.rest != 0.0:
                self.frame_cash_payment.grid(row=1, columnspan=2, pady=25, sticky='n')
                self.label2.configure(text="Zapłacono. Odbierz bilety i resztę: " +
                                           ("{0:.2f}".format(-self.controller.rest)))
                self.label2.grid()
        else:
            self.controller.sum -= 0.10
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_twenty_gr(self):
        if self.controller.sum - 0.20 < 0:
            self.controller.rest = self.controller.sum - 0.20
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 0.20
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_fifty_gr(self):
        if self.controller.sum - 0.50 < 0:
            self.controller.rest = self.controller.sum - 0.50
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 0.50
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_one(self):
        if self.controller.sum - 1.0 < 0:
            self.controller.rest = self.controller.sum - 1.0
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 1.0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_two(self):
        if self.controller.sum - 2.0 < 0:
            self.controller.rest = self.controller.sum - 2.0
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 2.0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_five(self):
        if self.controller.sum - 5.0 < 0:
            self.controller.rest = self.controller.sum - 5.0
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 5.0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_ten(self):
        if self.controller.sum - 10.0 < 0:
            self.controller.rest = self.controller.sum - 10.0
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 10.0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum)))

    def minus_twenty(self):
        if self.controller.sum - 20.0 < 0:
            self.controller.rest = self.controller.sum - 20.0
            self.label_pay_sum.configure(text=str(0.00))
        else:
            self.controller.sum -= 20.0
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


class Metro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.price_metro = controller.price_metro
        self.controller.sum_metro = controller.sum_metro
        self.controller.cnt_ord_red = controller.cnt_ord_red
        self.controller.cnt_ord_reg = controller.cnt_ord_reg
        self.controller.cnt_ord_red1 = controller.cnt_ord_red1
        self.controller.cnt_ord_reg1 = controller.cnt_ord_reg1

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
        self.label_one_pass_red = tk.Label(self.frame_one_pass_red, text='Jeden przejazd\n linie zwykłe', height=6, width=20,
                                           bg='gold', font=('Times New Roman', 20, 'bold'))
        self.info_opr = tk.Label(self.frame_one_pass_red, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                 font=('Times New Roman', 12, ' bold italic'), width=32)


        """
        self.btn_up_ord_red = tk.Button(self.frame_one_pass_red, text="+", height=2, width=3,
                                        font=('Times New Roman', 21, 'bold'), command=lambda: self.on_click_up(1.70))
        self.btn_down_ord_red = tk.Button(self.frame_one_pass_red, text="-", height=2, width=3,
                                          font=('Times New Roman', 21, 'bold'), command=lambda:
                                          self.on_click_down(1.70))
        self.label_ord_red = tk.Label(self.frame_one_pass_red, text=str(self.controller.cnt_ord_red),
                                      height=2, width=3, bg='white',
                                      font=('Times New Roman', 24, 'bold'))
                                      
        
        # frame of regular one pass
        self.frame_one_pass_reg = tk.Frame(self, bg='blue', bd=3)
        self.label_one_pass_reg = tk.Label(self.frame_one_pass_reg, text='Jeden przejazd\n normalny', height=9,
                                           width=15, bg='gold', font=('Times New Roman', 20, 'bold'))
        self.info_opr1 = tk.Label(self.frame_one_pass_reg, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, ' bold italic'))
      
        self.btn_up_ord_reg = tk.Button(self.frame_one_pass_reg, text="+", height=2, width=3,
                                        font=('Times New Roman', 21, 'bold'),
                                        command=lambda: self.on_click_up_reg(3.40))
        self.btn_down_ord_reg = tk.Button(self.frame_one_pass_reg, text="-", height=2, width=3,
                                          font=('Times New Roman', 21, 'bold'),
                                          command=lambda: self.on_click_down_reg(3.40))
        self.label_ord_reg = tk.Label(self.frame_one_pass_reg, text=0, height=2, width=3, bg='white',
                                      font=('Times New Roman', 24, 'bold'))
                                      """

        # frame of reduced one pass night
        self.frame_one_pass_red1 = tk.Frame(self, bg='blue', bd=1)
        self.label_one_pass_red1 = tk.Label(self.frame_one_pass_red1, text='Jeden przejazd\n linie zwykłe,\n nocne '
                                                                           'i pospieszne',
                                            height=6, width=20, bg='gold', font=('Times New Roman', 20, 'bold'))
        self.info_opr2 = tk.Label(self.frame_one_pass_red1, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, 'bold italic'), width=32)
        """
        self.btn_up_ord_red1 = tk.Button(self.frame_one_pass_red1, text="+", height=2, width=3,
                                         font=('Times New Roman', 21, 'bold'),
                                         command=lambda: self.on_click_up_red1(2.20))
        self.btn_down_ord_red1 = tk.Button(self.frame_one_pass_red1, text="-", height=2, width=3,
                                           font=('Times New Roman', 21, 'bold'),
                                           command=lambda: self.on_click_down_red1(2.20))
        self.label_ord_red1 = tk.Label(self.frame_one_pass_red1, text=0, height=2, width=3, bg='white',
                                       font=('Times New Roman', 24, 'bold'))
       
        # frame of regular one pass night
        self.frame_one_pass_reg1 = tk.Frame(self, bg='blue', bd=3)
        self.label_one_pass_reg1 = tk.Label(self.frame_one_pass_reg1, text='Jeden przejazd\n linie nocne,\n'
                                                                           ' pospieszne \n normalny',
                                            height=9, width=15, bg='gold', font=('Times New Roman', 20, 'bold'))
        self.info_opr3 = tk.Label(self.frame_one_pass_reg1, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, ' bold italic'))
        
        self.btn_up_ord_reg1 = tk.Button(self.frame_one_pass_reg1, text="+", height=2, width=3,
                                         font=('Times New Roman', 21, 'bold'),
                                         command=lambda: self.on_click_up_reg1(4.40))
        self.btn_down_ord_reg1 = tk.Button(self.frame_one_pass_reg1, text="-", height=2, width=3,
                                           font=('Times New Roman', 21, 'bold'),
                                           command=lambda: self.on_click_down_reg1(4.40))
        self.label_ord_reg1 = tk.Label(self.frame_one_pass_reg1, text=0, height=2, width=3, bg='white',
                                       font=('Times New Roman', 24, 'bold'))
                                       """

        # back buttons
        self.button_back = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                     font=('Times New Roman', 20, "bold"),
                                     command=lambda: controller.show_frame("StartPage"))
        self.button_to_metro = tk.Button(self, text="Cofnij", height=1, width=10, bg='gold',
                                         font=('Times New Roman', 20, "bold"),
                                         command=lambda: [self.controller.update(),
                                                          self.back_to_metro()])

        self.btn_accept = tk.Button(self, text="Zapłać", height=2, width=20, bg='gold',
                                    font=('Times New Roman', 20, 'bold'))
        """
        # calculate sum to pay
        self.frame_pay = tk.Frame(self, bg='blue', bd=0.5)
        self.label_pay = tk.Label(self.frame_pay, text='Do zapłaty: ', height=1, width=20,
                                  font=('Times New Roman', 20, 'bold'), bg='gold')

        self.label_pay_sum = tk.Label(self.frame_pay, text=str(self.controller.sum_metro), height=1, width=19,
                                      bg='white', font=('Times New Roman', 20, 'bold'))
                                      """
        # button for 24 hours
        self.frame_thf_comunal = tk.Frame(self, bg='blue', bd=1)
        self.thf_comunal = tk.Button(self.frame_thf_comunal, text="24-godzinny\n komunalny", height=6, width=19,
                                     bg='gold', font=('Times New Roman', 20, "bold"))
        self.info_thf1 = tk.Label(self.frame_thf_comunal, width=33, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, ' bold italic'))

        self.frame_thf_comunal_train = tk.Frame(self, bg='blue', bd=1)
        self.thf_comunal_train = tk.Button(self.frame_thf_comunal_train, text="24-godzinny\n kolejowo-komunalny",
                                           height=6, width=20, bg='gold',
                                           font=('Times New Roman', 20, "bold"))
        self.info_thf2 = tk.Label(self.frame_thf_comunal_train, text='Dwóch organizatorów:\n SKM, PR i '
                                                                     'ZKM Gdynia \nalbo ZTM Gdańsk albo MZK Wejherowo ',
                                  font=('Times New Roman', 12, ' bold italic'), width=35)

        self.frame_thf_all = tk.Frame(self, bg='blue', bd=1)
        self.thf_all = tk.Button(self.frame_thf_all, text="24-godzinny\n kolejowo-komunalny", height=6, width=19,
                                 bg='gold', font=('Times New Roman', 20, "bold"))
        self.info_thf3 = tk.Label(self.frame_thf_all, text='Wszystkich organizatorów:\n SKM, PR i '
                                                           'ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo ',
                                  font=('Times New Roman', 12, ' bold italic'))

        # buttons for 72 hours
        self.frame_shs_comunal = tk.Frame(self, bg='blue', bd=1)
        self.shs_comunal = tk.Button(self.frame_shs_comunal, text="72-godzinny\n komunalny", height=6, width=19,
                                     bg='gold', font=('Times New Roman', 20, "bold"))
        self.info_shs1 = tk.Label(self.frame_shs_comunal, width=33, text='ZKM Gdynia + ZTM Gdańsk\n + MZK Wejherowo',
                                  font=('Times New Roman', 12, ' bold italic'))

        self.frame_shs_all = tk.Frame(self, bg='blue', bd=1)
        self.shs_all = tk.Button(self.frame_shs_all, text="72-godzinny\n kolejowo-komunalny", height=6, width=19,
                                 bg='gold', font=('Times New Roman', 20, "bold"))
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
        self.ten = tk.Button(self.frame_money, text=" 10 gr", font=('Times New Roman', 20, 'bold'))
        self.twenty = tk.Button(self.frame_money, text=" 20 gr", font=('Times New Roman', 20, 'bold'))
        self.fifty = tk.Button(self.frame_money, text=" 50 gr", font=('Times New Roman', 20, 'bold'))
        self.one = tk.Button(self.frame_money, text="  1 zł  ", font=('Times New Roman', 20, 'bold'))
        self.two = tk.Button(self.frame_money, text="  2 zł  ", font=('Times New Roman', 20, 'bold'))
        self.five = tk.Button(self.frame_money, text="  5 zł  ", font=('Times New Roman', 20, 'bold'))
        self.ten_zl = tk.Button(self.frame_money, text=" 10 zł ", font=('Times New Roman', 20, 'bold'))
        self.twenty_zl = tk.Button(self.frame_money, text=" 20 zł ", font=('Times New Roman', 20, 'bold'))

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

    """
    def clear_labels(self):
        self.label_ord_red.configure(text='0')
        self.label_ord_reg.configure(text='0')
        self.label_ord_red1.configure(text='0')
        self.label_ord_reg1.configure(text='0')
        self.label_pay_sum.configure(text='0')
    """

    def check_relief(self):
        self.frame_thf_all.grid_remove, self.frame_thf_comunal_train.grid_remove(), self.frame_thf_comunal.grid_remove()
        self.shs_all.grid_remove(), self.shs_comunal.grid_remove()
        self.frame_one_pass_red1.grid_remove(), self.frame_one_pass_red.grid_remove()
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

    def open_one_pass(self):
        self.button1_1.grid_remove(), self.button1_2.grid_remove(), self.button1_3.grid_remove()
        self.button_back.grid_remove(), self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.frame_one_pass_red.grid(row=1, column=0, padx=5, sticky='e')
        # self.frame_one_pass_reg.grid(row=1, column=0, sticky='e')
        self.frame_one_pass_red1.grid(row=1, column=1, padx=5, sticky='')
        # self.frame_one_pass_reg1.grid(row=1, column=1, padx=80, sticky='e')
        self.info_opr.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        # self.info_opr1.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.info_opr2.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        # self.info_opr3.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.label_one_pass_red.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.label_one_pass_red1.grid(row=1, column=0, padx=0, pady=0, sticky='')

        self.label.configure(text="Wybierz bilet jednorazowy metropolitalny")

        # self.label_one_pass_reg.grid(row=1, column=0, padx=0, pady=0, sticky='')
        # self.label_one_pass_reg1.grid(row=1, column=0, padx=0, pady=0, sticky='')
        """
        self.btn_down_ord_red.grid(row=2, column=0, padx=0, pady=0, sticky='w')
        self.btn_down_ord_red1.grid(row=2, column=0, padx=0, pady=0, sticky='w')
        self.btn_down_ord_reg.grid(row=2, column=0, padx=0, pady=0, sticky='w')
        self.btn_down_ord_reg1.grid(row=2, column=0, padx=0, pady=0, sticky='w')
        self.btn_up_ord_red.grid(row=2, column=0, padx=0, pady=0, sticky='e')
        self.btn_up_ord_red1.grid(row=2, column=0, padx=0, pady=0, sticky='e')
        self.btn_up_ord_reg.grid(row=2, column=0, padx=0, pady=0, sticky='e')
        self.btn_up_ord_reg1.grid(row=2, column=0, padx=0, pady=0, sticky='e')
        self.label_ord_red.grid(row=2, column=0, padx=0, pady=0, sticky='')
        self.label_ord_red1.grid(row=2, column=0, padx=0, pady=0, sticky='')
        self.label_ord_reg.grid(row=2, column=0, padx=0, pady=0, sticky='')
        self.label_ord_reg1.grid(row=2, column=0, padx=0, pady=0, sticky='')
        self.frame_pay.grid(row=2, columnspan=2, padx=5, sticky='n')
    
        self.btn_accept.grid(row=2, columnspan=2, pady=30, sticky='s')

        self.label_pay.grid(row=1, column=1, padx=5, pady=5, sticky='s')
        self.label_pay_sum.grid(row=2, column=1, padx=5, pady=5, sticky='n')
        """
        self.label.configure(text="Wybierz 1-przejazdowy bilet metropolitalny")

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

    """
    def on_click_up(self, price):
        self.controller.cnt_ord_red += 1
        self.label_ord_red.configure(text=str(self.controller.cnt_ord_red))
        self.controller.sum_metro += price
        if self.controller.sum_metro <= 0:
            self.controller.sum_metro = 0
        self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_down(self, price):
        if (self.controller.cnt_ord_red - 1) != -1:
            self.controller.cnt_ord_red -= 1
            self.label_ord_red.configure(text=str(self.controller.cnt_ord_red))
            self.controller.sum_metro -= price
            if self.controller.sum_metro <= 0:
                self.controller.sum_metro = 0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_up_reg(self, price):
        self.controller.cnt_ord_reg += 1
        self.label_ord_reg.configure(text=str(self.controller.cnt_ord_reg))
        self.controller.sum_metro += price
        if self.controller.sum_metro <= 0:
            self.controller.sum_metro = 0
        self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_down_reg(self, price):
        if (self.controller.cnt_ord_reg - 1) != -1:
            self.controller.cnt_ord_reg -= 1
            self.label_ord_reg.configure(text=str(self.controller.cnt_ord_reg))
            self.controller.sum_metro -= price
            if self.controller.sum_metro <= 0:
                self.controller.sum_metro = 0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_up_red1(self, price):
        self.controller.cnt_ord_red1 += 1
        self.label_ord_red1.configure(text=str(self.controller.cnt_ord_red1))
        self.controller.sum_metro += price
        if self.controller.sum_metro <= 0:
            self.controller.sum_metro = 0
        self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_down_red1(self, price):
        if (self.controller.cnt_ord_red1 - 1) != -1:
            self.controller.cnt_ord_red1 -= 1
            self.label_ord_red1.configure(text=str(self.controller.cnt_ord_red1))
            self.controller.sum_metro -= price
            if self.controller.sum_metro <= 0:
                self.controller.sum_metro = 0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_up_reg1(self, price):
        self.controller.cnt_ord_reg1 += 1
        self.label_ord_reg1.configure(text=str(self.controller.cnt_ord_reg1))
        self.controller.sum_metro += price
        if self.controller.sum_metro <= 0:
            self.controller.sum_metro = 0
        self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))

    def on_click_down_reg1(self, price):
        if (self.controller.cnt_ord_reg1 - 1) != -1:
            self.controller.cnt_ord_reg1 -= 1
            self.label_ord_reg1.configure(text=str(self.controller.cnt_ord_reg1))
            self.controller.sum_metro -= price
            if self.controller.sum_metro <= 0:
                self.controller.sum_metro = 0
            self.label_pay_sum.configure(text=str("{0:.2f}".format(self.controller.sum_metro)))
    """
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
        self.button_back.grid_remove(),  self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.label.configure(text="Wybierz bilet 72-godzinny metropolitalny")
        self.frame_shs_all.grid(row=1, column=1, padx=5, sticky='')
        self.frame_shs_comunal.grid(row=1, column=0, padx=5, sticky='e')
        self.shs_all.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.shs_comunal.grid(row=1, column=0, padx=0, pady=0, sticky='')
        self.button_to_metro.grid(row=0, column=1, pady=5, padx=10, sticky='se')
        self.info_shs1.grid(row=1, column=0, padx=0, pady=0, sticky='s')
        self.info_shs3.grid(row=1, column=0, padx=0, pady=0, sticky='s')

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
