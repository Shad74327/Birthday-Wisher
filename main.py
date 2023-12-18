import pandas
import random
import smtplib
import datetime as dt

MY_MAIL = "rafishadali@gmail.com"
PASSWORD = "ibdb tszb tkdb ppao"

today = (dt.datetime.now().month, dt.datetime.now().day)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in birthday_data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_choice = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_choice}.txt") as letter:
        content = letter.read()
        personalised_letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Happy Birthday!\n\n{personalised_letter}")
