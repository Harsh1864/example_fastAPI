# # # l  = [1,2,3,4,5,6]

# # # def test(x):
# # #     return x**x
# # # newl = list(map(test(), l))
# # # print(newl)
# # # # print(l)

# # # l = [1,2,3,4,5,6]

# # # newl = list(filter(lambda x:x<4,l))
# # # print(newl)

# # from  functools import reduce
# # l=[1,2,3,4,5,6]

# # def mysum(x,y):
# #     return x+y

# # sum = reduce(mysum,l)

# # print(sum)


# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = list(filter(starts_with_A, fruit))

# print(map_object)

from functools import reduce
list1 = [1,2,3,4,5]

list2 = reduce(lambda x,y:x+y,list1)

print(list2)