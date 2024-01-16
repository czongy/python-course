import pandas as pd
import datetime as dt
import random as rd
import smtplib
USER = "YOUR_EMAIL_USERNAME"
PASSWORD = "YOUR_EMAIL_PASSWORD"

# 1. Update the birthdays.csv
def add_birthday(name, email, year, month, day):
    birthday = [{
        "name": name,
        "email": email,
        "year": year,
        "month": month,
        "day": day,
    }]
    df2 = pd.DataFrame(birthday)
    df2.to_csv("birthdays.csv", mode="a", index=False, header=False)


# add_birthday("Name", "email@gmail.com", "2000", "10", "11")


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_month = today.month
today_day = today.day

df = pd.read_csv("birthdays.csv")
birthday_list = df.to_dict(orient="records")
for index in birthday_list:
    if index["month"] == today_month and index["day"] == today_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        with open(f"letter_templates/letter_{rd.randint(1,3)}.txt", "r") as data:
            letter = data.read().replace("[NAME]", index["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        connection = smtplib.SMTP("smtp.mail.me.com")
        connection.starttls()
        connection.login(user=USER, passwd=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs=index["TO_EMAIL"], msg=f"Subject:Happy Birthday!\n\n{letter}")
        connection.close()


