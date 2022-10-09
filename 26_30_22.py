q1 -> Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


Expected - {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
l1=["Ten","Twenty","Thirty"]
l2=[10,20,30]
d1={}
c=0
for i in l2:
  d1[l1[c]]=i
  c+=1
print(d1)
q2 -> Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Expected - {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dicto={}
for i in dict1.items():
  dicto[i[0]]=i[1]
for i in dict2.items():
  dicto[i[0]]=i[1]
print(dicto)
q3 -> Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
sampleDict = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80 } } } }
for i in sampleDict:
  for j in sampleDict[i]:
    for k in (sampleDict[i])[j]:
      for a in (((sampleDict[i])[j])[k]):
        if(a=="history"):
          print((((sampleDict[i])[j])[k])[a])

q4 -> Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

Expected - > {'city': 'New york', 'age': 25}

sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
rkey=["name","salary"]
l1=[]
l2=[]
for i in sample_dict:
    print(i)
    fl=0
    for j in rkey:
        if(i==j):
            fl=1
    if(fl==0):
        l1.append(i)
        l2.append(sample_dict[i])
c=0
sample_dict={}
for i in l1:
    sample_dict[i]=l2[c]
    c+=1
print(sample_dict)
q5 -> Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}

Check if 200 exists or not
sample_dict = {'a': 100, 'b': 200, 'c': 300}
for i in sample_dict:
    if(sample_dict[i]==200):
        print("it exists")
        break
q6 -> Rename key of a dictionary

Write a program to rename a key city to a location in the following dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

Expected -> {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
sample_dict = {"name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}
s={}
for i in sample_dict:
    if(i=="city"):
        s["location"]=sample_dict[i]
    else:
        s[i]=sample_dict[i]
sample_dict=s
print(sample_dict)
q7 -> Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

Expected -> "Math"
sample_dict = {'Physics': 82,'Math': 65,'history': 75}
min=1000000000
st=""
for i in sample_dict:
    if(sample_dict[i]<min):
        min=sample_dict[i]
        st=i
print(st)
q8 -> Change value of a key in a nested dictionary

Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

Expected - > {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
sample_dict = {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},'emp3': {'name': 'Brad', 'salary': 500}}
for i in sample_dict:
    for j in sample_dict[i].items():
        a,b=j
        if(b=="Brad"):
            (sample_dict[i])["salary"]=8500
print(sample_dict)
q9 -> Concatenate two lists index-wise

list1 = ["M", "na", "i", "sa"]
list2 = ["y", "me", "s", "hib"]

['My', 'name', 'is', 'sahib']
list1=["M","na","i","sa"]
list2=["y","me","s","hib"]
c=0
for i in list1:
    list1[c]=list1[c]+list2[c]
    c+=1
print(list1)
q10 -> Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

expected -> ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1= ["Hello ", "take "]
list2= ["Dear", "Sir"]
l3=[]
c=0
for i in list1:
    for j in list2:
        l3.append(i+j)
print(l3)
q11 -> Iterate both lists simultaneously

list1 = [10, 20, 30, 7]
list2 = [100, 200, 300, 700]

Expected ->

10 400
20 300
30 200
7   700
list1 = [10, 20, 30, 7]
list2 = [100, 200, 300, 700]
c=0
for i in list1:
    list1[c]=int(str(list1[c])+str(list2[c]))
    c+=1
print(list1)
q12 -> Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

expected -> ["Mike", "Emma", "Kelly", "Brad"]
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if(i==""):
        list1.remove("")
print(list1)
q13 ->  Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

expected -> ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
l=["h","i","j"]
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
((((list1[2])[1])[2]).append(l))
print(list1)
q14 -> Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]

expected -> [5, 10, 15, 200, 25, 50, 20]
list1=[5,10,15,20,25,50,20]
same=0
c=-1
for i in list1:
    fl=0
    c+=1
    for j in list1:
        if(i==j):
            fl+=1
    if(fl>1):
        list1[c]=200
print(list1)
q15 -> Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

expected -> [5, 15, 25, 50]
list1=[5,20,15,20,25,50,20]
n=(int)(input("enter item to be removed:"))
for i in list1:
    if(i==n):
        list1.remove(n)
print(list1)
q16 -> Append new string in the middle of a given string

Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

expected -> AuKellylt

s1=input("s1:")
s2=input("s2:")
l=len(s1)//2+1
s3=s1[0:l]+s2+s1[l:]
print(s3)
q17 -> Arrange string characters such that lowercase letters should come first

str1 = CoffEE

expected -> offCEE
st1=list(input())
c=0
for i in st1:
    if(i.isupper()):
        st1[c]=i.lower()
    else:
        st1[c]=i.upper()
    c+=1
st2="".join(st1)
print(st2)
q18 -> Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"

Expected -> 2
st1="Welcome to USA. usa awesome, isn't it ?"
occ=input("enter string to be found:")
s=""
l=[]
for i in st1:
    if(i!=" " and i!="." and i!="," and i!="!" and i!="?" and i!="/"):
        s=s+i.lower()
    else:
        l.append(s)
        s=""
c=0
print(l)
for i in l:
    if(i==occ.lower()):
        c+=1
if(c>0):
    print("number of occurances:",c)
else:
    print("no occurance")
q19 -> Calculate the sum and average of the digits present in a string

s1 = 'sahib12singh13'

expected = 7 , 1.75  i.e ( 1+2+1+3 =7 , 7/4 =1.75)
stri="sahib12singh13"
c=0
sum1=0
for i in stri:
    if(i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"):
        sum1=sum1+int(i)
        c+=1
print("sum:",sum1)
avg=sum1/c
print("average:",avg)
q20 -> Write a program to count occurrences of all characters within a string

str1 = "Apple"

expected   -> {'A': 1, 'p': 2, 'l': 1, 'e': 1}
str1="Apple"
dicto={}
for i in str1:
    c=0
    for j in str1:
        if(i==j):
            c+=1
    dicto[i]=c
print(dicto)
q21 -> Split a string on hyphens

str1 = Emma-is-a-data-scientist

Expected ->

Emma
is
a
data
scientist
str1 = "Emma-is-a-data-scientist"
print(str1.split("-"))
q22 -> Removal all characters from a string except integers

str1 = 'I am 25 years and 9 months old'

expected -> 259
from socket import if_nameindex


str1='I am 25 years and 9 months old'
s1=""
for i in str1:
    if(i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"):
        s1=s1+i
print(int(s1))
q23 -> Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

expected -> [6, 12, 18, 4, 12, 20, 28]

l1 = [3, 6, 9, 12, 15, 18, 21]
c=0
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
for i in l1:
    if(c%2!=0):
        l3.append(i)
    c+=1
c=0
for i in l2:
    if(c%2==0):
        l3.append(i)
    c+=1
print(l3)
q24 -> Access value 20 from the tuple

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
x,y,z=tuple1
print(y[1])
q25 -> Copy specific elements from one tuple to a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)

Expected -> tuple2: (44, 55)
tuple1 = (11, 22, 33, 44, 55, 66)
sp=[44,55]
s=()
for i in tuple1:
    for j in sp:
        if(i==j):
            s=s+(i,)
print(s)
q26 -> Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)
Expected -> True
tuple1 = (45, 45, 45, 45)
fl=0
for i in tuple1:
    for j in tuple1:
        if(i!=j):
            fl=1
if(fl==0):
    print("True")
else:
    print("False")
q27 -> Make a function and return division,multiplication and addition from a single function

n1=15
n2 =5

expected -> 3,45,20
def fun(a,b,c):
    if(c=="+"):
        d=a+b
        return (d)
    elif(c=="-"):
        return (a-b)
    elif(c=="*"):
        return (a*b)
    elif(c=="/"):
        return (a/b)
n1=int(input())
n2=int(input())
l1=["+","-","*","/"]
for i in l1:
    print(fun(n1,n2,i))
q28 -> Display float number with 2 decimal places using print()

num = 458.541315

expected =458.54
num=float(input())
fls="{:.2f}".format(num)
print(fls)
q29 ->Accept a list of 5 float numbers as an input from the user
l=[]
for i in range(5):
    l.append(float(input()))
print(l)
q30 -> Remove items from the set at once

Write a Python program to remove items 10, 20, 30 from the following set at once.

set1 = {10, 20, 30, 40, 50}

expected = {40,50}
set1={10,20,30,40,50}
set1=list(sorted(set1))
del set1[0:3]
print(set(set1))
