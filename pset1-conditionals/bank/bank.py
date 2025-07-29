def main():
   user_input = input('Greeting: ')
   bank_hello(user_input)


def bank_hello(greeting):
   # Standardising the input
   final_greeting = greeting.lower().strip()

   # Determine whether 'hello' is present in the word
   if final_greeting.rfind('hello') >= 0:
      print('$0')

   # Determine whether 'h' is the first letter of the word
   elif final_greeting.rfind('h', 0, 1) == 0:
      print('$20')

   else:
      print('$100')

main()
