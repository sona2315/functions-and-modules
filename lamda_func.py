#lambda Function
#lambda argument:expression
print("----------lambda function---------")
#1. Add two numbers

add=lambda a,b:a+b
print (add(2,3))

#2. Square a number

square=lambda x:x*x
print(square(4))

#map function
#map(function,iterable)
print("------------map function-----------")
#square of num(using lambda)
nums=[1,2,3,4,5,6]
square=list(map(lambda x:x*x ,nums))
print("squares of given list using map and lambda function:",square)

#square of num
def square_no(a):
    return a*a
squares=list(map(square_no,nums))
print("squares of given list sing map function:",squares)

#filter function
#filter(function,sequence)
print("-----------filter function----------")
#filter even no.s from the list(using lambda)
even_no=list(filter(lambda x:x%2==0,nums))
print("even nos from given list using filter and lambda fuction:",even_no)

#filter function 
def even(a):
    return a%2==0
even_nos=list(filter(even,nums))
print("even nos from given list using filter fuction:",even_nos)
