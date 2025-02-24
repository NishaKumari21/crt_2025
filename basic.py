print("Hello world!")
print("komal ji")
# variables
a=4
print(type(a))
str="python is a simple language"
print(str)
print(type(str))
print(str[0])
# first element
print(str[-1])
# last element
# word  string slicing
print(str[0:6])
# reverse the string
print(str[::-1])
# negative slicing
print(str[-4:-1])
# string methods:----
str1="myself nisha  "
print(str1.upper())
print(str1.lower())
# removes extra spaces from string from before and after the string
print(str1.strip())
# split the string
print(str1.split())
# replace function
print(str1.replace('myself','i am'))
print(str1.find('nisha'))
# to concatenate the string
print(str+str1)
# to add some space btw two different strings
print(str+" "+str1)
# tuple
tup=('nisha',23,34.67,1+2j,True)
print(tup)
print(type(tup))
# indexing and slicing
# indexing 2 types:positive and negative indexing
print(tup[1])
print(tup[0])
print(tup[0:6])
print(tup[-1:3])
# revsering the tuple
print(tup[::-1])
# print(tup.replace('nisha','ayesha'))-------- tuple is immutable cannot be changed!
# concatenate the tupless
tup1=(13,"nisha",4,45,3,4,3,6,7)
print(tup+tup1)
print(tup1*2)
# 2 functions of tuple
# count function:give the number of count present in that specific tuple
print(tup1.count(3))
# index function:give the index
print(tup1.index("nisha"))
# list:------------
l=[2,3,4,"nisha","arya",3]
print(l)
print(type(l))
# list indexing
# reverse indexing
print(l[::-1])
# indexing
print(l[0])
# index slicing
print(l[1:4])
print(l[2:])
# list modification using methods:---
print(l[3])
l[3]="ayesha"
print(l)
# append function
l.append("upflairs")
l.append(34)
print(l)
# insert the element at any index
l.insert(3,3)
print(l)
# remove
l.remove(34)
print(l)
# pop function:to remove the last element
l.pop()
print(l)
# to reverse the list
l.reverse()
print(l)
# sort function:into ascending
l2=[3,34,12,1]
l2.sort()
print(l2)