
from bs4 import BeautifulSoup
import requests
from tkinter import *
from datetime import date
from tkinter import ttk


def get_number_from_string(string):
    return float(''.join([x for x in string if x.isdigit() or x == '.']))


today = date.today()


def gold_price():

    data = requests.get(
        "https://www.goodreturns.in/gold-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

    soup = BeautifulSoup(data.text, 'html.parser')

    price = soup.find("div", class_="gold_silver_table right-align-content").find(
        "tr", class_="odd_row").findAll("td")

    return price[1].text


def change_price(weight_value):

    g_price = float(weight_value)*get_number_from_string(gold_price())

    gold_price_label.config(text=f"{g_price} Rs")


root = Tk()

root.geometry("700x700")

Label(root, text="TODAY'S GOLD PRICE", font=(
    "Helvetica 15 bold"), fg="blue").pack()


frame1 = Frame(root)
frame1.pack(pady=20)

Label(frame1, text="Today Date:- ", font=("Helvetica 15 bold")).pack(side=LEFT)
Label(frame1, text=today, font=("Helvetica 15")).pack()


frame2 = Frame(root)
frame2.pack(pady=20)

variable = StringVar(root)
variable.set("1")

Label(frame2, text="Select Weight:- ",
      font=("Helvetica 15 bold")).pack(side=LEFT)
w = OptionMenu(frame2, variable, "1", "8", "100",
               "500", "1000", command=change_price)
w.pack(side=LEFT)
Label(frame2, text="gm", font=("Helvetica 15")).pack(side=LEFT)


frame4 = Frame(root)
frame4.pack()

Label(frame4, text="Gold Price:- ", font=("Helvetica 15 bold")).pack(side=LEFT)
gold_price_label = Label(frame4, text="", font=("Helvetica 15"))
gold_price_label.pack(pady=20)


bg = PhotoImage(file="sanketgold.png")

my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg)


root.mainloop()
