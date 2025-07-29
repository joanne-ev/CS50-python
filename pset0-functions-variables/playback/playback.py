def main():
   user_input = input("Enter your input here: ")
   playback(user_input)

def playback(sentences):
   slowed = print(sentences.replace(' ', '...'))
   return slowed

main()
