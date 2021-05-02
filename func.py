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
database = A.connect(host='localhost',database='c1234',username='root',passwd='#ello')
if database.is_connected():
    print('Main Databse is Succesfully Connected')
else:
    print('Database Not Connected')
c=database.cursor()
try:
    c.execute('Create Table ProductInfo(ID bigint primary key auto_increment,Product_ID bigint,User_ID bigint,Product_type varchar(50),Quantity int,Product_Description text(500),Address text(500))')
    print('Database 1 Created')
except:
    print('Database 1 Retrived')
def ProductInfo():
    print('*#*#*#* Product Page *#*#*#*')
    print()
    n=input('ID : ')
    p=int(input('Product ID : '))
    EI=input('User ID : ')
    RT=input('Product Type : ')
    CID=input('Quantity : ')
    CI=input('Product Description : ')
    RP=input('Address : ')
    t=(n,p,EI,RT,CID,CI,RP)
    print("('ID','Product_ID','User_ID','Product_type','Quantity','Product_Description','Address')")
    print(t)
    s='Insert into ProductInfo values(%s,%s,%s,%s,%s,%s,%s)'
    c.execute(s,t)
    database.commit()
    print()
    print('Successfully Checked-In')
    print()
    print('#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#')
    print()





