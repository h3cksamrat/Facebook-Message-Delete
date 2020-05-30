from selenium import webdriver
from getpass import getpass
import time


class Facebook:

    def __init__(self, emailPhn, passw):
        self.email = emailPhn
        self.password = passw

    @classmethod
    def openBrowser(cls):
        globals()['browser'] = webdriver.Chrome(executable_path=r'path_to_chromedriver.exe')

    def login(self):
        # opens facebook.com
        browser.get('https://www.facebook.com')

        # login credentials
        emailElem = browser.find_element_by_id('email')
        emailElem.send_keys(self.email)
        passwordElem = browser.find_element_by_id('pass')
        passwordElem.send_keys(self.password)
        passwordElem.submit()

    @staticmethod
    def messageDel():
        browser.get('https://www.facebook.com/messages')
        time.sleep(10)
        while True:
            threeDots = browser.find_element_by_id('dots-3-horizontal')
            try:
                threeDots.click()
            except Exception as e:
                try:
                    delMenu = browser.find_element_by_xpath('//button[text()="Delete"]')
                    delMenu.click()
                    continue
                except Exception as e:
                    print("The all messages are deleted ended with", e)
                    break

            delMenu = browser.find_elements_by_link_text('Delete')
            for firstDel in delMenu:
                firstDel.click()

            delMenu = browser.find_element_by_xpath('//button[text()="Delete"]')
            delMenu.click()


email = input("Email: ") or "default_email"
# password = input("Password: ")
password = getpass()

samrat = Facebook(email, password)
if __name__ == '__main__':
    Facebook.openBrowser()
    samrat.login()
    time.sleep(15)
    samrat.messageDel()
