import smtplib

my_email = "przemassoprzemo@gmail.com"
email_to_send = "przemoszadkowski@o2.pl"
password = "Jonathan21#"


def send_message(message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to_send,
            msg=message,
        )