import pandas  # This is an example of external module
import hashlib  # This is an example of built in module

import pandas    #this is pandas module to read some lines of file
print("Hi")
print("hello universe")

print(5)

#this is escape sequence character denoted by "\"
print("hello world i am a \"python developer\"")

#other printing parameter 
print("hello","world",6,9,sep="-",end="byby")


# Read and work with a file named 'words.csv'
df = pandas.read_csv('world.csv')
print(df) # This will display first few rows from the words.csv file
