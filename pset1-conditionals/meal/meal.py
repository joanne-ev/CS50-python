def main():
   user_input = input('What time is it? ')

   # If 12-hour timings are used (e.g., '7:00 a.m.')
   if len(user_input) > 5:
      time_hours = convert_12(user_input)

   # If 24-hour timings are used (e.g., '19:00 ')
   else:
      time_hours = convert(user_input)

   mealtime(time_hours)


# Converts 24-hour time into hours
def convert(time):
   final_time = time.strip().split(':')
   time_hours = float(final_time[0]) + ( float(final_time[1]) / 60 )
   return time_hours


# Converts 12-hour time into hours
def convert_12(time12):

   # Convert 12-hour P.M. timings to 24-hour timings
   if time12.endswith(' p.m.'):
      clean_time = time12.removesuffix(' p.m.').strip().split(':')
      final_time = float(clean_time[0]) + 12 + ( float(clean_time[1]) / 60 )

   # Convert 12-hour A.M. timings to 24-hour timings
   elif time12.endswith(' a.m.'):
      clean_time = time12.removesuffix(' a.m.').strip().split(':')
      final_time = float(clean_time[0]) + ( float(clean_time[1]) / 60 )

   return final_time


# Determines which mealtime the hour belongs to
def mealtime(hours):
   if 7.00 <= hours <= 8.00:
      print('breakfast time')
   elif 12.00 <= hours <= 13.00:
      print('lunch time')
   elif 18.00 <= hours <= 19.00:
      print('dinner time')



if __name__ == "__main__":
   main()



