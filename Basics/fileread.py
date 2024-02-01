# f = open("myfile.txt","r")
# file = f.read()
# print(file)
# f.close()
# # f.write("Hello sir i am a python developer and ")

# # f= open("myfile.txt","w")
# # f.write("Hello universe i am back just wait n watch")
# # f.close()


f = open("myfile.txt","r")

while True:
    line = f.readline()
    if not line:
        break
    print(line)