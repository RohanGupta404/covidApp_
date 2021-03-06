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


def defaultProductListForHomeScreen():
    callDatabase()
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")
    mycursor.execute(f"SELECT * FROM productInfo LIMIT 10")
    return mycursor.fetchall()


def UpdateProductListForHomeScreen(pType, pDistance):
    callDatabase()
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")
    if pType != "None":
        mycursor.execute(f"SELECT * FROM productInfo WHERE Product_type = '{pType}' LIMIT 10")
        return mycursor.fetchall()
    else:
        mycursor.execute(f"SELECT * FROM productInfo LIMIT 10")
        return mycursor.fetchall()


def UpdateAccountDetailDatabase(userid, password, name, phoneNumber, address, landmark):
    callDatabase()
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")

    mycursor.execute("SET SQL_SAFE_UPDATES = 0")

    if password != "":
        password = hashlib.sha256(str(password).encode('utf-8'))
        password = password.hexdigest()
        mycursor.execute(f"UPDATE sellerInfo SET password = '{password}' WHERE userid = {userid}")
    if name != "":
        mycursor.execute(f"UPDATE sellerInfo SET name = '{name}' WHERE userid = {userid}")
    if phoneNumber != "":
        mycursor.execute(f"UPDATE sellerInfo SET phoneNumber = '{phoneNumber}' WHERE userid = {userid}")
    if address != "":
        mycursor.execute(f"UPDATE sellerInfo SET address = '{address}' WHERE userid = {userid}")
    if landmark != "":
        mycursor.execute(f"UPDATE sellerInfo SET landmark = '{landmark}' WHERE userid = {userid}")

    mydb.commit()


def UpdateProductDetailInDatabase(product_id, name, description, quantity, address, landmark):
    callDatabase()
    mycursor = mydb.cursor()
    mycursor.execute("Use covidApp")

    mycursor.execute("SET SQL_SAFE_UPDATES = 0")

    if name != "":
        mycursor.execute(f"UPDATE productInfo SET name = '{name}' WHERE product_id = {product_id}")
    if description != "":
        mycursor.execute(f"UPDATE productInfo SET Product_Description = '{description}' WHERE product_id = {product_id}")
    if quantity != "":
        mycursor.execute(f"UPDATE productInfo SET Quantity = '{quantity}' WHERE product_id = {product_id}")
    if address != "":
        mycursor.execute(f"UPDATE productInfo SET Address = '{address}' WHERE product_id = {product_id}")
    if landmark != "":
        mycursor.execute(f"UPDATE productInfo SET Landmark = '{landmark}' WHERE product_id = {product_id}")

    mydb.commit()


def DeleteProductFromDatabase(product_id):
    callDatabase()
    mycursor = mydb.cursor()
    mycursor.execute("USE covidApp")

    mycursor.execute("SET SQL_SAFE_UPDATES = 0")
    mycursor.execute(f"DELETE FROM productInfo WHERE product_id = {product_id}")

    mydb.commit()
