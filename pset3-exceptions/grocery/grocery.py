def main():
   grocery()


def grocery():
   items_dict = {}

   while True:
      # Handle EOFError when user ends input to program
      try:
         user_input = input("")
      except EOFError:
         break

      # Create a dictionary with unique grocery items and their respective count
      if user_input in items_dict.keys():
         items_dict[user_input] = items_dict[user_input] + 1
      else:
         items_dict[user_input] = 1

   # Sort dictionary by keys
   sorted_items_dict = dict(sorted(items_dict.items()))

   # Print sorted grocery list with count
   for key, value in sorted_items_dict.items():
      print(f'{value} {key.upper()}')


main()
