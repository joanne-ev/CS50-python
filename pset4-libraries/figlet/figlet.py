from pyfiglet import Figlet, figlet_format
from random import randint
import sys


def main():
   figlet_func()


def figlet_func():
   figlet = Figlet()
   font_names_list = figlet.getFonts()

   # Check if command-line arguments are used
   if len(sys.argv) > 1:
      try:
         font_call = sys.argv[1]
         font_name_arg = sys.argv[2]

      except IndexError:
         sys.exit('Invalid usage')

      # Check if the format for the first command-line argument is correct
      else:
         if font_call == '-f' or font_call == '--font':

            # Check if font used is in the list of available Figlet fonts
            font_check = 0
            for font in font_names_list:
               if font == font_name_arg:
                  font_name = font
                  font_check =+ 1

            if font_check == 0:
               sys.exit('Invalid usage')

            # Only ask for user_input when the above checks are correct
            user_input = input('Input: ')
            print(figlet_format(user_input, font = font_name))

         else:
            sys.exit('Invalid usage')

   # Use a random font if no additional command-line arguments were used
   elif len(sys.argv) == 1:
      user_input = input('Input: ')
      random_num = randint(0, 549)
      print(figlet_format(user_input, font = font_names_list[random_num]))


main()
