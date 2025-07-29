def main():
   plate = input('Plate: ')

   if len_num_check(plate) == False:
      print('Invalid')
   elif start_with_two_letters(plate) == False:
      print('Invalid')
   elif alpha_numeric(plate) == False:
      print('Invalid')
   else:
      print('Valid')


# Plates must start with at least two letters
def start_with_two_letters(plate):
   # Identify first two characters of the plate
   character1 = plate[0]
   character2 = plate[1]

   # Conditional depending on whether the two beginning characters are alphabets
   if character1.isalpha() and character2.isalpha():
      return True
   else:
      return False


# Plates must not have periods, spaces, or punctuation marks
def alpha_numeric(plate):
   if plate.isalnum():
      return True
   else:
      return False


def len_num_check(plate):
   validity_score = 0

   # Plates must have a maximum of six and a minimum of two characters
   if 2 <= len(plate) <= 6:

      # Plates must have numbers at the end of the plate and zero should not be the leading number
      adj_len = len(plate) - 1

      for i in range(adj_len):
         curr = plate[i]
         next = plate[i+1]

         if curr.isdigit() and next.isalpha():
            validity_score =+ 1
         elif curr.isalpha() and next == '0':
            validity_score =+ 1
         else:
            pass
   else:
      validity_score =+ 1

   # Compare validity scores
   if validity_score > 0:
      return False
   else:
      return True



main()

