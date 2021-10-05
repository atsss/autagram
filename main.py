from bin.bot import Bot
from bin.message import message

targets = ['a_i_c_moment','a_i_p_moment']

def init():
	Bot('username', 'password', targets, message)
	input("DONE")

if __name__ == '__main__':
    init()
