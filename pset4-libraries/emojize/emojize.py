from emoji import emojize

def main():
   user_input = input('Input: ')
   get_emoji(user_input)


def get_emoji(emoji_str):
   print(f'Output: {emojize(emoji_str, language='alias')}')


main()
