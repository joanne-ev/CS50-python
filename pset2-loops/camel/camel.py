def main():
   user_input = input("camelCase: ")
   snake_case_converter(user_input)


def snake_case_converter(camelCase):
   # Check if the word has an uppercase
   if camelCase == camelCase.lower():
      print(f'snake_case: {camelCase}')

   # If an uppercase letter is present,
   else:
      # go through all letters
      for letter in camelCase:

         # Check if letter is uppercase
         if letter.isupper():

            # Find index of uppercase letter
            upper_index = camelCase.index(letter)

            # Include '_' at the index of the uppercase letter
            camelCase = camelCase[:upper_index] + '_' + camelCase[upper_index:]

      print(f'snake_case: {camelCase.lower()}')

main()
