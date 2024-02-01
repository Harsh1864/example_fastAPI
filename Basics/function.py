# def function1(a,b):
#     if(a<b):
#         print(b," is greater than ",a)
#     else:
#         print(a," is greater than ",b)

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# # b=20
# function1(a,b)

# def function2(c,d):
#     pass


# def name(*name):
#     print(name[0],name[1],name[2])

# name("jack","john","jackie")

def name(**name):
    print(name["fname"],name["mname"],name["lname"])

name(mname="harsh",fname="bharoliya",lname="k")