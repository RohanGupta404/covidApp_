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
def newUserLogin(email, password, name, phoneNumber, bio, address):
    userid = random.randint(1000000000000000, 9999999999999999)
    newPassword = hashlib.sha256(b"rohan").hexdigest()

    mycursor = mydb.cursor()
    mycursor.execute("use covidApp")
    mycursor.execute(f"INSERT INTO sellerInfo "
                     f"(userid, email, password, name, phoneNumber, bio, address) VALUES "
                     f"({userid}, '{email}', '{newPassword}', '{name}', {phoneNumber}, '{bio}', '{address}')")
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


import mysql.connector as A
database = A.connect(host='localhost',database='v123',username='root',passwd='#ello')
if database.is_connected():
    print('Main Databse is Succesfully Connected')
else:
    print('Database Not Connected')
c=database.cursor()
try:
    c.execute('Create Table Login_Info(ID decimal(30),User_ID decimal(30),Name char(30),Email_ID Char(30),Password char(50),Phone_No decimal(12),Bio text(500),Address text(500),Land_Mark text(50))')
    print('Database 1 Created')
except:
    print('Database 1 Retrived')
def Login_Info():
    print('*#*#*#* Login Page *#*#*#*')
    print()
    n=input('ID : ')
    p=int(input('User_ID : '))
    Na=input('Name : ')
    EI=input('Enter Emil ID OF The Customer : ')
    PW=input('Password : ')
    CID=input('Phone No : ')
    CI=input('Bio : ')
    C_O=input('Address : ')
    NLM=input('Nearest Landmark : ')
    t=(n,p,Na,EI,PW,CID,CI,C_O,NLM)
    print("('ID','User_ID','Name','Email_ID','Password','Phone_No','Bio','Address','Land_Mark')")
    print(t)
    c.execute(f"Insert into Login_Info values({n},{p},{Na},{EI},{PW},{CID},{CI},{C_O},{NLM})")
    database.commit()
    print()
    print('Successfully Checked-In')
    print()
    print('#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#')
    print()
Login_Info()



