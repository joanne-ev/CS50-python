def main():
   adieu()


def adieu():
   names = []

   while True:
      try:
         user_input = input('Name: ')
         names.append(user_input)

      except EOFError:
         break

   for i in range(len(names)):
      names[i] = names[i] + ','


   if len(names) == 1:
      print(f'\nAdieu, adieu, to {names[0][:-1]}')

   elif len(names) == 2:
      before_and = names[0][:-1]
      after_and = names[-1][:-1]
      print(f'\nAdieu, adieu, to {before_and} and {after_and}')

   elif len(names) > 2:
      before_and = names[:-1]
      after_and = names[-1][:-1]
      print(f'\nAdieu, adieu, to {' '.join(before_and)} and {after_and}')


main()
