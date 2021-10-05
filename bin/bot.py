import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Bot:
    def __init__(self, driver, username, password, targets, message, skip_flag=True):
        # initializing the username
        self.username = username

        # initializing the password
        self.password = password

        # passing the list of user or initializing
        self.targets = targets

        # passing the message of user or initializing
        self.message = message

        # initializing the base url.
        self.base_url = 'https://www.instagram.com/'

        # here it calls the driver to open chrome web browser.
        self.bot = driver

        self.skip_flag = skip_flag

        # initializing the login function we will create
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))

        enter_username.send_keys(self.username)

        # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)

        # RETURNING THE PASSWORD and login into the account
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # first pop-up box
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(4)

        # 2nd pop-up box
        if not self.skip_flag:
            self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            time.sleep(2)

        # this will click on message(direct) option.
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(2)

        for target in self.targets:
            # This will click on the pencil icon as shown in the figure.
            self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)

            # enter the username
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(target['id'])
            time.sleep(3)

            # click on the username
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
            time.sleep(2)

            # next button
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(2)

            # click on message area
            element = self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            message_with_name = self.message.replace('hoge', target['id']) if target['name'] == '' else self.message.replace('hoge', target['name'])
            # types message
            for part in message_with_name.split('\n'):
                element.send_keys(part)
                ActionChains(self.bot).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            time.sleep(1)

            # send message
            element.send_keys(Keys.RETURN)
            time.sleep(2)

            print('sent to {0}'.format(target['id']))

        self.bot.delete_all_cookies()
        time.sleep(2)
