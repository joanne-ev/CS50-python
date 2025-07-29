def main():
	user_input = input('Hello! ')
	convert(user_input)

def convert(conversation):
	emojified_convo = conversation.replace(':)', '🙂').replace(':(', '🙁')
	print(emojified_convo)

main()
