while True:
   user_input = input('Fraction: ')
   frac = user_input.split('/')

   # Handle ValueError
   try:
      numerator = int(frac[0])
      denomenator = int(frac[1])
   except ValueError:
      print("A number was not entered")
   else:
      # Handle ZeroDivisionError
      try:
         division = numerator / denomenator
      except ZeroDivisionError:
         print('Cannot divide by zero')
      # Handle edge cases
      else:
         if 0.99 <= division <= 1:
            print('F')
            break
         elif 0 <= division <= 0.1:
            print('E')
            break
         elif division > 1:
            pass
         else:
            print(f'{int(round((division * 100), 0))}%')
            break
