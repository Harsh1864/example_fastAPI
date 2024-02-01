s1="15"
n1=1
n2=9.9
cast=int(s1)         #it is explicit typecasting done via developer

sum=cast+n1

print("sum is typecasting : " , sum)
print("sum of casting implicit : " , (n1+n2))   #it is explicit typecasting done via compiler it self
print(type(n1))
print(type(n2))
print(type(n1+n2))