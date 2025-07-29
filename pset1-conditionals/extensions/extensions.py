def main():
   user_input = input("What is the name of your file? ")
   extension = user_input.strip().lower().split('.')[-1]
   file_type(extension)


def file_type(file_extension):
   # Handle .jpg and .jpeg edge cases
   if file_extension == 'jpg':
      file_extension = 'jpeg'

   # Match file type according to extension
   match file_extension:
      case 'gif' | 'jpg' | 'jpeg' | 'png':
         print(f'image/{file_extension}')
      case 'pdf':
         print(f'application/{file_extension}')
      case 'txt':
         print(f'text/plain')
      case 'zip':
         print(f'application/{file_extension}')
      case _:
         print('application/octet-stream')

main()
