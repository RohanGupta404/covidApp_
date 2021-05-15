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
def newUserSignup(email, password, name, phoneNumber, bio, address, landmark):
    userid = random.randint(1000000000000000, 9999999999999999)
    newPassword = hashlib.sha256(str(password).encode('utf-8'))
    newPassword = newPassword.hexdigest()

    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")
    mycursor.execute(f"INSERT INTO sellerInfo "
                     f"(userid, email, password, name, phoneNumber, bio, address, landmark) VALUES "
                     f"({userid}, '{email}', '{newPassword}', '{name}', {phoneNumber}, '{bio}', '{address}', '{landmark}')")
    mydb.commit()
    return userid


# This function will add a new product
def newProduct(user_id, product_type, quantity, product_description, address, landmark, name):
    product_id = random.randint(1000000000000000, 9999999999999999)

    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")
    mycursor.execute(f"INSERT INTO productInfo "
                     f"(product_id, user_id, product_type, quantity, product_description, address, landmark, name) VALUES "
                     f"({product_id}, {user_id}, '{product_type}', {quantity}, '{product_description}', '{address}', '{landmark}', '{name}')")
    mydb.commit()


# This function will send e-mail
def sendMail(recMail, message):
    import smtplib

    senderMail = "tfstwofriendsstudio@gmail.com"
    password = "Grohan111"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderMail, password)
    print("login successful")
    server.sendmail(senderMail, recMail, str(message))


def LoginCheck(Email, Password):
    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")

    mycursor.execute(f"SELECT * "
                     f"FROM sellerInfo "
                     f"WHERE email = '{Email}'")

    Password = hashlib.sha256(str(Password).encode('utf-8'))
    Password = Password.hexdigest()

    try:
        fetchedData = mycursor.fetchone()
        PasswordInDatabase = fetchedData[3]
        UserID = fetchedData[1]

        if PasswordInDatabase == Password:
            return UserID
        else:
            print("Incorrect Password")
            return False

    except TypeError:
        print("Email not found")
        return False


def UpdateAccountDetails(accountUserId):
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")
    mycursor.execute(f"SELECT Name, Email, PhoneNumber, Address FROM sellerInfo WHERE userid={accountUserId} LIMIT 1")
    for i in mycursor:
        return [i[0], i[1], i[2], i[3]]


# Merge giveProductAddress and UpdateAccountDetails
def giveSellerAddress(accountUserId):
    callDatabase()
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")
    mycursor.execute(f"SELECT Address FROM sellerInfo WHERE userid={accountUserId} LIMIT 1")
    for i in mycursor:
        return i[0]


def giveProductInfo(accountUserId):
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")
    mycursor.execute(f"SELECT * FROM productInfo WHERE User_ID={accountUserId} LIMIT 10")
    return mycursor.fetchall()


def giveSellerData(sellerUserId):
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")
    mycursor.execute(f"SELECT * FROM sellerInfo WHERE UserId={sellerUserId} LIMIT 1")
    return mycursor.fetchone()