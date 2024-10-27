##################### Extra Hard Starting Project ######################
import smtplib
import pandas as pd
import datetime as dt
import random
birthdays = pd.read_csv("birthdays.csv")
today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays_dict={(birthdays_row["month"], birthdays_row["day"]):birthdays_row for (index, birthdays_row) in birthdays.iterrows()}
my_email = "serenity.dooley68@ethereal.email"
password = "tbwNCRdFwrS3QBTwqr"
if today in birthdays_dict:
    person_name = birthdays_dict[today]["name"]
    letters = ("letter_1.txt", "letter_2.txt", "letter_3.txt")
    with open (f"./letter_templates/{random.choice(letters)}") as letter_file:
        text = letter_file.read()
        new_text = text.replace("[NAME]", person_name)
    with smtplib.SMTP("smtp.ethereal.email", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject: Happy Birthday!\n\n{new_text}")


# 4. Send the letter generated in step 3 to that person's email address.




