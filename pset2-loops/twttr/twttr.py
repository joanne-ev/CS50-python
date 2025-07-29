def main():
   user_input = input("Input: ")
   remove_vowels(user_input)


def remove_vowels(phrase):
   vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

   for vowel in vowels:
      if vowel in phrase:
         phrase = phrase.replace(vowel, '')

   print(phrase)

main()
