from bin.bot import Bot

targets = ['a_i_c_moment','a_i_p_moment']
message = 'testing of a bot'

def init():
	Bot('username', 'password', targets, message)
	input("DONE")

if __name__ == '__main__':
    init()
