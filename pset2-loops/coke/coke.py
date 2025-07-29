def main():
   coke_machine(50)


def coke_machine(price):
   print(f'Amount Due: {price}')

   # Infinite loop
   while True:
      user_input = int(input("Insert Coin: "))

      # Check if user has put in the right coins
      if user_input == 25 or user_input == 10 or user_input == 5:
         # Create new remaining price (i.e., amount due) by deducting coins from price
         price = price - user_input

         # Find change owed if remaining price is less than or equal to zero
         if price <= 0:
            # If price is less than zero multiply by -1 to get a positive number
            print(f'Change Owed: {price * -1}')
            break

         # If remaining price is greater than zero print that price
         else:
            print(f'Amount Due: {price}')

      # If user has not put in the right coins return the remaining price
      else:
         print(f'Amount Due: {price}')

main()
