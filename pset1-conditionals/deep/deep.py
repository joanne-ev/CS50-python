def main():
   user_input = input('What is the Answer to the Great Question Of Life, the Universe and Everything? ')
   great_answer(user_input)

def great_answer(answer):
   # Standardising the input
   final_answer = answer.lower().replace('-', ' ').strip()

   if final_answer == '42' or final_answer == 'forty two':
      print('Yes')
   else:
      print('No')

main()
