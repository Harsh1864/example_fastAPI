import time

time11 = time.strftime('%H:%M:%S')

print(time11)
time1=int(time.strftime('%H'))            #convert into integer otherwise it is string....
print(type(time1))
print(time1)
time2=int(time.strftime('%M'))
print(time2)
time3=int(time.strftime('%S'))
print(time3)

if(time1>=4 and time1<=12):
    print("Good morning")
elif(time1>=13 and time1<=18):
    if(time1==17):
        print("hello ")
    print("Good aftrnoon")
else:
    print("good evening")