import random
import hashlib

mydb = 0


def callDatabase():
    import mysql.connector

    global mydb
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="Alooboy47")


def newUserLogin(email, password, name, phoneNumber, bio, address):
    userid = random.randint(1000000000000000, 9999999999999999)
    newPassword = hashlib.sha256(b"rohan").hexdigest()

    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")
    mycursor.execute(f"INSERT INTO sellerInfo "
                     f"(userid, email, password, name, phoneNumber, bio, address) VALUES "
                     f"({userid}, '{email}', '{newPassword}', '{name}', {phoneNumber}, '{bio}', '{address}')")
    mydb.commit()


def sendMail(recMail, message):
    import smtplib

    senderMail = "sshaswat36@gmail.com"
    password = "87654321.ss"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderMail, password)
    print("login successful")
    server.sendmail(senderMail, recMail, message)



