import random


def main():
   level = get_level()
   generate_integer(level)


def get_level():

   # Continue requesting input until a `break` is reached
   while True:

      try:
         level = int(input('Level: '))

      # Check input provided is an integer
      except ValueError:
         pass

      # Check level is either 1, 2 or 3
      else:
         if 0 < level < 4:
            break

   return level



def generate_integer(level):
   # Dictionary of acceptable ranges for each level
   l1 = {'a': 0, 'b': 9}
   l2 = {'a': 10, 'b': 99}
   l3 = {'a': 100, 'b': 999}

   # Identify `a` and `b` values for the `random.randint`
   level_dict = dict()

   if level == 1:
      level_dict = l1
   elif level == 2:
      level_dict = l2
   elif level == 3:
      level_dict = l3

   # Keep track of the total number of wrong answers
   wrong_answers = 0

   # Ask 10 questions
   for i in range(10):
      X = random.randint(level_dict['a'], level_dict['b'])
      Y = random.randint(level_dict['a'], level_dict['b'])
      real_answer = X + Y
      counter = 0    # track the number of time the user gets the same question wrong

      # Continue requesting input until `break`
      while True:
         try:
            user_answer = int(input(f'{X} + {Y} = '))

         # Check input provided is an integer
         except ValueError:
            counter += 1

            # Once three errors are detected give the correct answer
            if counter == 3:
               print(f'{X} + {Y} = {real_answer}')
               wrong_answers += 1
               break

         # If an integer is provided as input carry on the following
         else:
            # Check whether user's input is correct
            if user_answer == real_answer:
               break

            # If user's input is wrong
            else:
               counter += 1
               print('EEE')

               # Once three errors are detected give the correct answer
               if counter == 3:
                  print(f'{X} + {Y} = {real_answer}')
                  wrong_answers += 1
                  break

   print(f'Score: {10 - wrong_answers}')


main()
