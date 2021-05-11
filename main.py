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

accountUserID = False

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
            global accountUserID
            accountUserID = func.newUserSignup(accountEmail, accountPassword, accountName, accountPhoneNumber,
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
        if not accountUserId:
            self.root.ids["AccountLoginPage"].ids["AccountLoginEmail"].text = ""
            self.root.ids["AccountLoginPage"].ids["AccountLoginPassword"].text = ""
        else:
            MainApp.updateAcountDetialUI(self)
            MainApp.change_screen(self, "AccountDetailPage")

    def updateAcountDetialUI(self):
        if accountUserId!=False:
            UserUIInfo=func.UpdateAccountDetails(accountUserId)
            accountDetailText = f"NAME OF SELLER : {UserUIInfo[0]}\nEMAIL : {UserUIInfo[1]}\nPHONE NO. : {UserUIInfo[2]}\nADDRESS : {UserUIInfo[3]}"
            self.root.ids["AccountDetailPage"].ids["accountDetail"].text = accountDetailText

MainApp().run()
