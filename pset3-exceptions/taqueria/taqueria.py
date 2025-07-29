def main():
   # Dictionary of food items and their prices
   food_prices = {
      "Baja Taco": 4.25,
      "Burrito": 7.50,
      "Bowl": 8.50,
      "Nachos": 11.00,
      "Quesadilla": 8.50,
      "Super Burrito": 8.50,
      "Super Quesadilla": 9.50,
      "Taco": 3.00,
      "Tortilla Salad": 8.00
   }

   felipe_taqueria(food_prices)


def felipe_taqueria(prices):

   price = 0

   while True:

      # Handle EOFError when user ends input to program
      try:
         user_input = input('Item: ')
      except EOFError:
         print('\n', end='')
         break

      # Titlecase food item
      food_choice = user_input.title()

      # Handle KeyError when a food item not on the menu is entered
      try:
         price = price + prices[food_choice]
      except KeyError:
         pass
      else:
         print(f'${price:.2f}')


main()
