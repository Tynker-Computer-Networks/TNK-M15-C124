import smtplib
import ssl


def sendEmail(message):
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "vishal18@navgurukul.org"
        password = "pefv qjse dvsd buyn"
        receiver_email = "vishal18@navgurukul.org"

        context = ssl.create_default_context()

        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.ehlo()
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()
