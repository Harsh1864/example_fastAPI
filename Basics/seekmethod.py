# # with open("myfile.txt","r") as f:
# #     f.seek(10)

# #     data = f.read()
# #     print(data)

# with open('myfile.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(15)

#   # Save the current position
#   current_position = f.tell()
#   print(current_position)
#   # Seek to the saved position
# #   f.seek(current_position)


with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())