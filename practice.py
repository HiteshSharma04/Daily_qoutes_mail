import smtplib
import datetime as dt
import random

EMAIL = "Your Email"
PASSWORD = "Your Password"
now = dt.datetime.now()
week = now.weekday()

if week == 6:
    with open("projects/smtp/quotes.txt") as quotes:
        all = quotes.readlines()
        quote = random.choice(all)
    print(quote)



with smtplib.SMTP("smtp.gmail.com") as connect:
    connect.starttls()
    connect.login(user=EMAIL, password=PASSWORD)
    connect.sendmail(from_addr=EMAIL, to_addrs="4hiteshsharma@gmail.com", msg=f"Subject : Sunday Motivation! \n\n {quote}")
