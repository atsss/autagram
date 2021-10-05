from bin.bot import Bot
from config.credentials import credentials
from config.message import message
from config.targets import targets

def init():
	Bot(credentials[0]['name'], credentials[0]['password'], targets, message)
	input("DONE")

if __name__ == '__main__':
    init()
