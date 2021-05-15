from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import random
import func


class HomeScreen(Screen):
    pass


class ProductPage(Screen):
    pass


class HaveHelp(Screen):
    pass


class ProductAddPage(Screen):
    pass


class ProductEditDeletePage(Screen):
    pass


class AccountLoginPage(Screen):
    pass


class AccountDetailPage(Screen):
    pass


class AccountSignupPage(Screen):
    pass


class EditAccountPage(Screen):
    pass


class OTPConfirmPage(Screen):
    pass


# class for functions
class ImageButton(ButtonBehavior, Image):
    pass


GUI = Builder.load_file('main.kv')

# Global Variables
accountUserId = False
CurrentScreen = "AccountDetailPage"


class MainApp(App):
    def build(self):
        return GUI

    # Change's the screen
    def change_screen(self, screen_name):
        global screen_manager
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    # Generate's OTP and change screen to OTPConfirmPage
    def signupNewAccount(self):
        accountEmail = self.root.ids["AccountSignupPage"].ids["accountEmail"].text

        global OTPgenerated
        OTPgenerated = random.randint(100001, 999999)

        func.sendMail(accountEmail, OTPgenerated)
        MainApp.change_screen(self, "OTPConfirmPage")

    # Checks the OTP, then adds the data to the database
    def CheckEmailAddAccount(self):
        OTPRecieved = self.root.ids["OTPConfirmPage"].ids["accountOTP"].text
        accountName = self.root.ids["AccountSignupPage"].ids["accountName"].text
        accountEmail = self.root.ids["AccountSignupPage"].ids["accountEmail"].text
        accountPhoneNumber = self.root.ids["AccountSignupPage"].ids["accountPhoneNumber"].text
        accountBio = self.root.ids["AccountSignupPage"].ids["accountBio"].text
        accountAddress = self.root.ids["AccountSignupPage"].ids["accountAddress"].text
        accountLandmark = self.root.ids["AccountSignupPage"].ids["accountLandmark"].text
        accountPassword = self.root.ids["AccountSignupPage"].ids["accountPassword"].text
        accountConfirmPassword = self.root.ids["AccountSignupPage"].ids["accountConfirmPassword"].text

        if str(OTPgenerated) == str(OTPRecieved):
            func.callDatabase()
            global accountUserId
            accountUserId = func.newUserSignup(accountEmail, accountPassword, accountName, accountPhoneNumber,
                                               accountBio,
                                               accountAddress, accountLandmark)
            MainApp.updateAcountDetialUI(self)
            MainApp.change_screen(self, "AccountDetailPage")
        else:
            print("wrong OTP")
            print(OTPgenerated, OTPRecieved, sep=",  ")

    def LoginEmailPasswordCheck(self):
        AccountLoginEmail = self.root.ids["AccountLoginPage"].ids["AccountLoginEmail"].text
        AccountLoginPassword = self.root.ids["AccountLoginPage"].ids["AccountLoginPassword"].text

        func.callDatabase()
        global accountUserId
        accountUserId = func.LoginCheck(AccountLoginEmail, AccountLoginPassword)
        self.root.ids["AccountLoginPage"].ids["AccountLoginEmail"].text = ""
        self.root.ids["AccountLoginPage"].ids["AccountLoginPassword"].text = ""
        if not accountUserId:
            pass
        else:
            if CurrentScreen == "HaveHelp":
                MainApp.UpdateProductListOnHaveHelp(self)
            else:
                MainApp.updateAcountDetialUI(self)
            MainApp.change_screen(self, CurrentScreen)

    def updateAcountDetialUI(self):
        if not accountUserId:
            return None

        UserUIInfo = func.UpdateAccountDetails(accountUserId)
        accountDetailText = f"NAME OF SELLER : {UserUIInfo[0]}\nEMAIL : {UserUIInfo[1]}\nPHONE NO. : {UserUIInfo[2]}\nADDRESS : {UserUIInfo[3]}"
        self.root.ids["AccountDetailPage"].ids["accountDetail"].text = accountDetailText

    def setProductType(self, productType):
        global ProductType
        ProductType = productType

    def addNewProduct(self):
        if not accountUserId:
            print("First please login")
            return None

        productAddress = self.root.ids["ProductAddPage"].ids["productAddress"].text
        if productAddress == "":
            productAddress = func.giveSellerAddress(accountUserId)

        productType = ProductType
        productName = self.root.ids["ProductAddPage"].ids["productName"].text
        productDescription = self.root.ids["ProductAddPage"].ids["productDescription"].text
        productQuantity = self.root.ids["ProductAddPage"].ids["productQuantity"].text
        productLandmark = self.root.ids["ProductAddPage"].ids["productLandmark"].text

        func.newProduct(accountUserId, productType, productQuantity, productDescription, productAddress,
                        productLandmark, productName)

        MainApp.UpdateProductListOnHaveHelp(self)
        MainApp.change_screen(self, "HaveHelp")

    def onClickAccount(self, screen_name):
        global CurrentScreen
        CurrentScreen = screen_name
        if not accountUserId:
            MainApp.change_screen(self, "AccountLoginPage")
        else:
            if CurrentScreen == "HaveHelp":
                MainApp.UpdateProductListOnHaveHelp(self)
            else:
                MainApp.updateAcountDetialUI(self)
            MainApp.change_screen(self, screen_name)

    def AccountLogout(self):
        global accountUserId
        accountUserId = False
        MainApp.change_screen(self, "AccountLoginPage")

    def UpdateProductListOnHaveHelp(self):
        if not accountUserId:
            pass
        else:
            global listOfProducts
            listOfProducts = func.giveProductInfo(accountUserId)
            productNumber = -1
            for productNumber in range(len(listOfProducts)):
                product = listOfProducts[productNumber]
                self.root.ids["HaveHelp"].ids[f"Product{str(productNumber+1)}"].text = f"NAME:    {str(product[8])}\n" \
                                                                                     f"PRODUCT:    {str(product[4])}\n" \
                                                                                     f"LandMark:    {str(product[7])} "
            for i in range(productNumber+1, 10):
                self.root.ids["HaveHelp"].ids[f"Product{str(i + 1)}"].text = "Not Available"

    def updateProductPageUI(self, productNumber):
        productData = listOfProducts[productNumber-1]
        sellerUserId = productData[2]
        sellerAllData = func.giveSellerData(sellerUserId)

        self.root.ids["ProductPage"].ids["sellerName"].text = f"NAME OF SELLER : {sellerAllData[4]}"
        self.root.ids["ProductPage"].ids["productName"].text = f"PRODUCT NAME : {productData[8]}"
        self.root.ids["ProductPage"].ids["productType"].text = f"PRODUCT TYPE : {productData[3]}"
        self.root.ids["ProductPage"].ids["quantity"].text = f"QUANTITY : {productData[4]}"
        self.root.ids["ProductPage"].ids["productDescription"].text = f"PRODUCT DESCRIPTION : {productData[5]}"
        self.root.ids["ProductPage"].ids["productAddress"].text = f"PRODUCT ADDRESS : {productData[6]}"
        self.root.ids["ProductPage"].ids["landmark"].text = f"LANDMARK : {productData[7]}"
        self.root.ids["ProductPage"].ids["sellerNumber"].text = f"SELLER PHONE NO : {sellerAllData[5]}"
        self.root.ids["ProductPage"].ids["sellerEmail"].text = f"E-MAIL : {sellerAllData[2]}"

        MainApp.change_screen(self, "ProductPage")


MainApp().run()
