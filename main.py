from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bin.bot import Bot
from config.credentials import credentials
from config.message import message
from config.targets import targets

driver = webdriver.Chrome(ChromeDriverManager().install())

def init():
    Bot(driver, credentials[0]['name'], credentials[0]['password'], targets[:2], message, False)
    print('DONE: {0}'.format(credentials[0]['name']))

    Bot(driver, credentials[1]['name'], credentials[1]['password'], targets[2:4], message)
    print('DONE: {0}'.format(credentials[1]['name']))

    # Bot(driver, credentials[2]['name'], credentials[2]['password'], targets[4:], message)
    # print('DONE: {0}'.format(credentials[2]['name']))

    driver.quit()

    print('ALL DONE')

if __name__ == '__main__':
    init()
