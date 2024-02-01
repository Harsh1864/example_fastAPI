import random

com = random.randint(0,2)
user = int(input(" 1. For sanke \n 2. For water \n 3. For gun  \n Enter your input:"))

def check(com,user):
    if com ==user:
     return 0
    
    if(com == 0 and user ==1):
     return -1
    
    if(com == 1 and user ==2):
     return -1
    
    if(com == 2 and user == 0):
     return -1

    return 1


score = check(com,user)

if score==0:
  print("TIE")
elif(score==1):
  print("WON")
else:
  print("FAIL")