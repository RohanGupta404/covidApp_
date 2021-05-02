import random
import hashlib

mydb = 0


# This function will be used to call the database
def callDatabase():
    import mysql.connector

    global mydb
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="Alooboy47")


# This function will add a new user(seller) to the database
def newUserLogin(email, password, name, phoneNumber, bio, address, landmark):
    userid = random.randint(1000000000000000, 9999999999999999)
    newPassword = hashlib.sha256(password).hexdigest()

    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")
    mycursor.execute(f"INSERT INTO sellerInfo "
                     f"(userid, email, password, name, phoneNumber, bio, address, landmark) VALUES "
                     f"({userid}, '{email}', '{newPassword}', '{name}', {phoneNumber}, '{bio}', '{address}', '{landmark}')")
    mydb.commit()


# This function will add a new product
def newProduct(user_id, product_type, quantity, product_description, address, landmark):
    product_id = random.randint(1000000000000000, 9999999999999999)

    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")
    mycursor.execute(f"INSERT INTO sellerInfo "
                     f"(product_id, user_id, product_type, quantity, product_description, address, landmark) VALUES "
                     f"({product_id}, {user_id}, '{product_type}', {quantity}, '{product_description}', '{address}', '{landmark}')")
    mydb.commit()


# This function will send e-mail
def sendMail(recMail, message):
    import smtplib

    senderMail = "sshaswat36@gmail.com"
    password = "87654321.ss"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderMail, password)
    print("login successful")
    server.sendmail(senderMail, recMail, message)





