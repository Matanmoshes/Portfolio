import smtplib, ssl, os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "matan.moshe66@gmail.com"
    #password = "rzgrqbacdtxawurf"
    password = os.getenv("PASSWORD")
    receiver = "matan.moshe66@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
