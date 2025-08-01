def main():
   user_input = input('Item: ')
   fruit_cals(user_input)

def fruit_cals(item):
   item = item.lower()

   # Dictionary of fruits and calories
   fruit_cal_dict = {
      'apple': 130,
      'avocado': 50,
      'banana': 110,
      'cantaloupe': 50,
      'grapefruit': 60,
      'grapes': 90,
      'honeydew melon': 50,
      'kiwifruit': 90,
      'lemon': 15,
      'lime': 20,
      'nectarine': 60,
      'orange': 80,
      'peach': 60,
      'pear': 100,
      'pineapple': 50,
      'plums': 70,
      'strawberries': 50,
      'sweet cherries': 100,
      'tangerine': 50,
      'watermelon': 80
   }

   # Check if item is in dictionary
   if item in fruit_cal_dict:
      print(f'Calories: {fruit_cal_dict[item]}')
   else:
      pass

main()
