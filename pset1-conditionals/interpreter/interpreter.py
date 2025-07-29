def main():
   user_input = input("Enter a calculation: ")
   split_input = user_input.strip().split()
   x, y, z = get_variables(split_input)
   interpreter(x, y, z)

# Create new variables for each component
def get_variables(split):
   x = float(split[0])
   y = split[1]
   z = float(split[2])

   return x, y, z

# Conduct calculations
def interpreter(x, y, z):
   if y == '+':
      print(x + z)
   elif y == '-':
      print(x - z)
   elif y == '*':
      print(x * z)
   else:
      print(x / z)

main()
