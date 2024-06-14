# #division corrector
# num1=int(input("enter the first number :"))
# num2=int(input("enter the second number :"))
# try:
#     product=num1/num2
# except:
#     if num2==0 :
#         product="undefined"
# print(product)     
# #input corrector
# num=input("enter your desired input : ")
# try: 
#     num=int(num)
# except:
#    num="enter a number input "
   
# print(num)
# print("pascal")
# #printing the maximum
# big=max("pascal mugishav" )
# print(big)
# bigint=max(1,2,3)
# print(bigint)
# small=min("pascal mugishav")
# print(small) 
# #using while loop
# n=5
# while n>0:
#     print("this is pascal")
#     n=n-1
##finding the largest number
# array=[1,2,3,4,5,6,7,8,9,10] 
# max=0
# for element in array :
#     if element>max : 
#         max=element
# print(max)
# #1.looking through the string
# name="pascal"
# for letter in name : 
#     print(letter)
# #2.looking through the string
# name2="pascal"
# index=0
# while index<len(name2):
#     letter=name2[index]
#     print(letter)
#     index=index+1
##counting the number of times a letter exists
# name3="pascal"
# count=0
# for letter in name3:
#     if letter=="a":
#         count=count+1
# print(count)
# #slicing strings
# name4="mugisha pascal"
# print(name4[:])
# #in operator
# name5="pascal"
# bool='m' not in name5
# print(bool)
# #lower() method 
# name6="PASCAL"
# name6l=name6.lower()
# print(name6l)
# #upper method
# name7="pascal"
# name7u=name7.upper()
# print(name7u)
# #dir method ??
# di="pascal"
# dirname=dir(di)
# print(dirname)
# #type method
# name8="pascal"
# print(type(name8))
# #capitalize method
# name9="pascal"
# # print(name9.capitalize())
# cp=name9.capitalize()
# print(cp)
# #casefold method
# name10="PASCAL"
# print(name10.casefold())
# #center method
# name11="pascal"
# print(name11.center(30))
# #count method
# name12="pascal"
# print(name12.count("a",0,20))
# #encode method
# name13="pascal"
# print(name13.encode(encoding="utf-8"))
# #endswith method
# name14="pascal"
# print(name14.endswith("m"))
# #expandtabs method
# name15="pascal\tmugisha"
# print(name15.expandtabs(20))
# #find method
# name16="pascal"
# print(name16.find("l"))
# #format method
# name17="for {price} dollars"
# print(name1"7.format(price=300))
# #index method
# name18="pascal"
# print(name18.index("l"))
# #isalnum method 
# name19="pascal"
# print(name19.isalnum())
# #isapha method
# name20="pascal?"
# print(name20.isalpha())
# #isdigit method , unicode ?? 
# name21="\u0030"
# print(name21.isdigit())
# #isidentifier method
# name22="pascal"
# name23="2mugisha"
# print(name22.isidentifier())
# print(name23.isidentifier())
# #isnumeric method
# name24="123"
# print(name24.isnumeric())
# #isspace method
# name25="  "
# print(name25.isspace())
# #join method
# names=("mugisha","pascal","daddy")
# myname=" ".join(names)
# print(myname) 
# #ljust method
# name26="pascal"
# txt=name26.ljust(10)
# print(txt,"this is my name")
# #lstrip method
# name27="  pascal  "
# stripname=name27.lstrip()
# # print("my first name is" ,stripname,"and it is my name")
# #maketrans method
# text="mugisha pasual daddy"
# mx="pm"
# my="dp"
# mz="ug"
# tr=str.maketrans(mx,my,mz)
# print(text.translate(tr))
# #partition method
# name28="mugisha pascal daddy"
# text=name28.partition("pascal")
# print(text)
# # replace method
# name29="pascal pascal pascal"
# print(name29.replace("pascal","mugisha",1))
# #rfind method
# name30="pascal"
# print(name30.rfind("a"))
# print(name30.rindex("a"))
# #rjust method
# name31="pascal"
# just=name31.rjust(20)
# print(just ,"my name too")
# #rsplit method
# text="mugisha , pascal , daddy"
# print(text.rsplit(",",1))
# #rstrip method
# name32="  pascal  "
# print("mugisha",name32.rstrip(),"daddy")
# #splitlines method
# name33="mugisha \n pascal"
# print(name33.splitlines())
# #swapcase method
# name34="PAScal"
# print(name34.swapcase())
# #title method
# name35="mugisha pascal daddy"
# print(name35.title())
# #zfill method
# name36="pascal"
# print(name36.zfill(10))
# #1.reading a file 
# rea=open('file.txt')
# inp=rea.read()
# print(inp)
# #2.reading through a file
# rea2=open("file.txt")
# count=0
# for line in rea2:
#     print(line)
#     count=count+1
# print(count)
# #searching through a file
# rea3=open("file.txt")
# for line in rea3:
#     line=line.rstrip()
#     if line.startswith("m"):
#         print(line)
# #skipping with continue
# rea4=open("file.txt")
# for line in rea4 :
#     line=line.rstrip()
#     if not line.startswith("m"):
#         continue
#     print(line)
# #using in to search for lines
# rea5=open("file.txt")
# for line in rea5:
#     line=line.rstrip()
#     if "mug" in line :
#         print(line)
# #using in together with continue to search for lines
# rea6=open("file.txt")
# for line in rea6:
#     line=line.rstrip()
#     if not "mug" in line:
#         continue
#     print(line)
# #prompting for the user to enter the filename
# filename=input("enter the filename : ")
# file=open(filename)
# print(file.read())
# #using try with file handling
# filename=input("enter the filename : ")
# try:
#     file=open(filename)
# except:
#     print("the file execution failed",filename," file name")
#     quit()
    
# print(file.read())
# #prompting for file name and the starting word of the line
# filename=input("enter the filename : ")
# startingword=input("enter the starting word of the line : ")
# try:
#     file=open(filename)
# except:
#     print("failed to execute",filename)
#     quit()
# for line in file:
#     line=line.rstrip()
#     if line.startswith(startingword):
#         print(line)
# #prompting for the filename and also the word contined in the line we want
# filename=input("enter the filename : ")
# word=input("search for the line(using this inputted word): ")
# try:
#     file=open(filename)
# except:
#     print("failed to execute : ",filename)
#     quit()
# for line in file:
#     line=line.rstrip()
#     if word in line :
#         print(line)
# #lists mutability
# mynames=["mugisha","pascal","daddy"]
# print(mynames)
# mynames[0]="mbappe"
# print(mynames)
# #range method
# mynames2=["mugisha","pascal","daddy"]
# print(range(len(mynames2)))
# #range method2 
# rg2=range(3)
# print(rg2)
# #a loop using range
# list=["pascal","mugisha"]
# for index in range(len(list)):
#    element=list[index]   
#    print(element)
# #concatinating lists 
# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c) 
# #slicing lists
# list2=["mugisha","pascal","daddy"]
# print(list2[:])
# print(list2[:2])
# print(list2[1:2])
# #knowing methods for a given type 
# string="pascal"
# print(type(string))
# print(dir(string))
# list3=["pascal"]
# print(type(list3))
# print(dir(list3))
# number=1
# print(type(number))
# print(dir(number))
# #building a list from scratch
# mynames3=list()
# mynames3.append("pascal")
# mynames3.append("mugisha")
# print(mynames3)
# #is something in a list
# list4=["pascal","mugisha","daddy"]
# print("pascal" in list4)
# print("pascal" not in list4)
# #sort method
# list5=[1,3,5,6,7]
# list5.sort()
# print(list5)
# list6=["a","c","b","B","A"]
# list6.sort()
# print(list6)
# #making max , min and an average of a list
# list7=[1,2,3,4,5,6,7,8,9,10]
# print(max(list7))
# print(min(list7))
# print(sum(list7)/len(list7))
# #prompting the user for items(list) for calculating average
# list8=list()
# print("note:type done if you done inputting the items\n")
# while True :
#     item=input("enter the elements of the list : ")
#     if item=="done": break
#     try :
#         item=float(item)
#     except:
#         print("invalid item")
#     list8.append(item)
# print("the average is : ",sum(list8)/len(list8))
# #how lists and strings interrelated (calculating average by prompting the user for string containing numbers)
# string2=input("enter the string containing the numbers(with out commas) : ")
# list9=string2.split()
# list10=list()
# for item in list9: 
#     item=float(item)
#     list10.append(item)
# print("the average is : ",sum(list10)/len(list10))
# #specifying the delimiter in splitting the string
# mynames="mugisha;pascal;daddy"
# list11=mynames.split(";")
# print(list11)
# #selecting a given word from the file
# file=open("file.txt")
# for line in file :
#     line=line.rstrip()
#     word=line.split()
#     print(word[1])
# #double split 
# file=open("file.txt")
# for line in file :
#     line=line.rstrip()
#     word=line.split()
#     gword=word[1]
#     piece=gword.split("a")
#     print(piece)
# #1. guardian in file handling
# file=open("file.txt")
# for line in file:
#     line=line.rstrip()
#     word=line.split()
#     if len(word)<1:
#         continue
#     if word[0]!="mugisha":
#         continue
#     print(line)
# #2. guardian in file handling
# file=open("file.txt")
# for line in file:
#     line=line.rstrip()
#     if line=="":
#         continue
#     word=line.split()
#     if word[0]=="mugisha":
#         continue
#     print(line)
# # 3. stronger guardian in file handling(guardian comes before)
# file=open("file.txt")
# for line in file:
#     line=line.rstrip()
#     word=line.split()
#     if len(word)<1 or word[0] != "mugisha" :
#         continue
#     print(line)
# #making of the dictionary
# mynamesdict=dict()
# mynamesdict["mugisha"]="hospital"
# mynamesdict["pascal"]="school"
# mynamesdict["daddy"]="home"
# print(mynamesdict)
# print(mynamesdict["pascal"])
# print(mynamesdict["daddy"])
# #methods for dictionary
# dict1={"pascal":"school","daddy":"home"}
# print(dir(dict1))
# print(type(dict1))
# #adding values to items in the dictionary
# dict2=dict()
# dict2["number1"]=1
# dict2["number2"]=2
# dict2["number1"]=dict2["number1"]+1
# print(dict2)   
# #checking if an item is in the dictionary
# dict3=dict()
# print("pascal" in dict3)
# #making a dict that stores the  counts for the names in a list 
# names=["pascal","mugisha","daddy","pascal","mugisha"]
# count=dict()
# for name in names : 
#     if name not in count :
#         count[name]=1
#     else :
#         count[name]=count[name]+1
# print(count) 
# #using get method to solve the above problem 
# names=["mugisha","pascal","daddy","pascal","daddy"]
# counts=dict()
# for name in names :
#     counts[name]=counts.get(name,0)+1
# print(counts)   
# #counting the number of times the word exists in a file
# file=open("file.txt")
# counts=dict()
# for line in file:
#     line=line.rstrip()
#     words=line.split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1
# print(counts)        
# #definite loops with dictionaries
# dict4={"daddy":1,"pascal":2,"mugisha":3}
# for key in dict4:
#     print(key,dict4[key])
# #checking the video program
# counts={"chuck":1,"fred":42,"jan":100}
# for key in counts :
#     print(key,counts[key])
# #various ways to retrieve keys and values 
# dict5={"daddy":1,"pascal":2,"mugisha":3}
# print(list(dict5))
# print(dict5.values())
# print(dict5.keys())
# print(dict5.items())
# #two iteration loops
# dict6={"daddy":1,"pascal":2,"mugisha":3}
# for key,value in dict6.items():
#     print(key,value)
# #finding the word with the biggest count in the file using two iteration loops 
# file=open("file.txt")
# counts=dict()
# for line in file: 
#     line=line.rstrip()
#     words=line.split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1

# bigcount=None
# bigword=None
# for word,count in counts.items():
#     if bigcount is None or count>bigcount:
#         bigword=word
#         bigcount=count
# print(bigword,bigcount)
# #adding comments to counting of words in the file
# filename=input("enter the file name : ")
# file=open(filename)
# counts=dict()
# for line in file:
#     line=line.rstrip()
#     words=line.split()
#     for word in words:
#         if word in counts:
#             counts[word]=counts[word]+1
#             print("**existing**")
#         else:
#             counts[word]=1
#             print("**new**")
#         print(word,counts[word])       
# #using get method to return the new and old count of the file
# filename=input("enter the file name : ")
# file=open(filename)
# counts=dict()
# for line in file : 
#     line=line.rstrip()
#     words=line.split()
#     for word in words : 
#         oldcount=counts.get(word,0)
#         print(word,"old",oldcount)
#         newcount=oldcount+1
#         counts[word]=newcount
#         print(word,"new",counts[word])
# #finding the word which occurs most frequently in file
# filename=input("enter the filename : ")
# file=open(filename)
# counts=dict()
# for line in file :
#     line=line.rstrip()
#     words=line.split()
#     for word in words :
#         counts[word]=counts.get(word,0)+1
# bigword=None
# largest=-1
# for key,value in counts.items():
#     if value>largest :
#         largest=value
#         bigword=key
# print(bigword,largest)
# #tuples declaration ,methods ,type and the difference between a tuple ,string and a list 
# tuple1=(1,2,3,"pascal")
# print(tuple1)
# print(type(tuple1))
# print(dir(tuple1))
# #same as strings
# # tuple1[3]=5 
# list12=[1,2,4,"mugisha"]
# list12[3]=4
# list12[2]=3
# print(list12)
# #reverse method
# list13=[2,3,1,4]
# list13.sort()
# print(list13)
# list13.reverse()
# print(list13)
# #append method
# list14=[1,2,3,4]
# list14.append(5)
# print(list14)
# #assignment between two containers 
# #with lists
# [x,y]=[1,2]
# print(x)
# #with tuples
# (w,z)=(1,2)
# print(z)
# #comparision between tuples
# print((1,2,3)<(4,3,5))
# print(("a","b","c")<("d","e","f","g"))
# #sorting list of tuples
# dict7={"a":3,"b":1,"c":2}
# sorted(dict7)
# print(dict7)
# #1. reversed method
# dict7={"d":1,"c":3,"a":2}
# reversed(dict7)
# print(dict7)
# #2. reversing  a list of tuples 
# dict8={"a":1,"b":2,"c":3}
# dict8=sorted(dict8,reverse=True)
# print(dict8)
# #making a list from a dictionary
# dict8={"a":1,"b":2,"c":3}
# list98=list()
# for k,v in dict8.items():
#     list98.append((k,v))
# print(list98)
# #sorting of a dictionary basing on value
# dict8={"a":1,"b":2,"c":3}
# temp=list()
# for (key,value) in dict8.items():
#     temp.append((value,key))
# temp=sorted(temp,reverse=True)
# print(temp)
# #iterating through a list with tuples
# dict8={"a":1,"b":2,"c":3}
# temp=list()
# for (key,value) in dict8.items():
#     temp.append((value,key))
# temp=sorted(temp,reverse=True)
# print(temp)
# for val,key in temp[:2] :
#     print( key,val )
# #shorter version for sorting a list of tuples basing on values 
# dict8={"a":1,"b":2,"c":3}
# dict8=sorted([(v,k) for k,v in dict8.items()],reverse=True)
# print(dict8)
# #1. arranging the dictionary by value by prompting the user for filename
# filename=input("enter the filename : ")
# file=open(filename)
# counts=dict()
# for line in file : 
#     line=line.rstrip()
#     words=line.split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1
# temp=list()
# for key,value in counts.items():
#     temp.append((value,key))

# temp=sorted(temp,reverse=True)
# print(temp)
# #2. arranging the dictionary by value by prompting the user for filename
# filename=input("enter the filename : ")
# file=open(filename)
# counts=dict()
# for line in file : 
#     line=line.rstrip()
#     words=line.split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1
# print(sorted([(value,key)for key,value in counts.items()],reverse=False))
# #using find method in file handling 
# filename=input("enter the file name : ")
# file=open(filename)
# for line in file:
#     line=line.rstrip()
#     if line.find("daddy")>=0:
#         print(line)
# #using regular expressions to search in the file
# import re 
# file=open("file.txt")
# for line in file:   
#     line=line.rstrip()
#     if re.search("pascal",line):
#         print(line)
# #using startwith method in file handling
# file=open("file.txt")
# for line in file :
#     line=line.rstrip()
#     if line.startswith("mugisha"):
#         print(line)
# #using regular expressions to search the line which start with the given string
# import re
# file=open("file.txt")
# for line in file : 
#     line=line.rstrip()
#     if re.search("^mugisha",line):
#         print(line)
# #wind card characters
# import re
# file=open("file.txt")
# for line in file :
#     line=line.rstrip()
#     if re.search("^mugisha.*",line) :
#         print(line)
# #fine tuning your match
# import re
# file=open("file.txt")
# for line in file :
#     line=line.rstrip()
#     if re.search("^mugisha\S+",line):       
#         print(line)
# #matching and extracting of data(numbers)
# import re
# x="1,2,3 mugissha 4,5,6,12"
# y=re.findall("[0-9]+",x)
# print(y)
# #matching and extracting of data(text)
# import re
# x="mugisha3pascal daddy"
# y=re.findall("[a-c]+",x)
# print(y)
# #greedy matching
# import re
# x="mugisha@pascal@daddy"
# y=re.findall("^m.+@",x)
# print(y)
# #non-greedy matching
# import re
# x="mugisha@pascal@daddy"
# y=re.findall("^m.+?@",x)
# print(y)
# #fine tuning string extraction
# import re
# x="from mugishapascal2008@gmail.com email"
# y=re.findall("\S+@\S+",x)
# print(y)
# #parentheses functionality in fine tuning string extraction
# import re
# x="from mugishapascal2008@gmail.com email"
# y=re.findall("^from (\S+@\S+)",x)
# print(y)
# #finding the hostname using find and string slicing
# email="from mugishapascal2008@gmail.com email"
# index1=email.find("@")
# index2=email.find(" ",index1)
# hostname=email[index1+1:index2]
# print(hostname)
# #double split pattern to get the hostname
# email="from mugishapascal2008@gmail.com email"
# words=email.split()
# realemail=words[1]
# words2=realemail.split("@")
# hostname=words2[1] 
# print(hostname)
# #1. regular expression version to find the hostname
# import re
# email="from mugishapascal2008@gmail.com email"
# hostname=re.findall("@(\S+)",email)
# print(hostname)
# #2. regular expression version to find the hostname(precise)
# import re
# email="from mugishapascal2008@gmail.com email"
# hostname=re.findall("@([^ ]+)",email)
# print(hostname)
# #3. even cooler regular expression version to find the hostname
# import re
# email="from mugishapascal2008@gmail.com email"
# hostname=re.findall("^from.+@([^ ]+)",email)
# print(hostname)
# #program to prompt a user for the file name and printing the number 
# import re
# numbers=list()
# filename=input("enter the file name  : ")
# file=open(filename)
# for line in file: 
#     line=line.rstrip()
#     if len(line) <=0:continue 
#     words=line.split()
#     for word in words:
#         numberstring=re.findall("number=([0-9]+)",word)
#         for number in numberstring:
#             number=int(number)
#             numbers.append(number)
# try:
#     maximum=max(numbers)
#     print("the maximum is ",maximum," and the average is ",sum(numbers)/len(numbers))
# except:
#     print("unable to get the numbers")
# #matching and extracting floats
# import re
# x="0.1, 2.3"
# y=re.findall("[0-9.]+",x)
# print(y)
# #escape characters in matching and extracting of data
# import re
# x="$1200.1200 dollars"
# y=re.findall("\$([0-9.]+)",x)
# print(y)
# #sockets in python
# import socket
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# #simple browser in python
# import socket
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data=mysock.recv(512)
#     if (len(data)<1):
#         break
#     print(data.decode())
# mysock.close()
# #printing the ascii number value in python
# print(ord("a"))
# print(ord("1"))
# #unicodes types
# x=u"pascal"
# print(type(x))
# #urllib in python to make a browser
# import urllib.request,urllib.parse,urllib.error
# fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# for line in fhand:
#     print(line.decode().strip())
# #treating a urllib browser as a file
# import urllib.request,urllib.parse,urllib.error
# fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# count=dict()
# for line in fhand :
#     words=line.decode().split()
#     for word in words :
#         count[word]=count.get(word,0)+1
# print(count)
# #reading webpages using urllib
# import urllib.request,urllib.parse,urllib.error
# fhand=urllib.request.urlopen("http://data.pr4e.org/page1.htm")
# for line in fhand :
#     print(line.decode().strip())
# #beautifulsoup functionality in python 
# import urllib.request,urllib.parse,urllib.error
# from bs4 import BeautifulSoup
# url=input("enter - ")
# html=urllib.request.urlopen(url).read()
# soup=BeautifulSoup(html,"html.parser")
#       #retrieve all of the anchor tags
# tags=soup('a')
# for tag in tags:
#     print(tag.get('href',None))
# #extracting data from xml data format
# import xml.etree.ElementTree as ET
# data='''
# <person>
#  <name>pascal</name>
#  <id>7</id>
#  <email hide="yes"/>
# </person>
# '''
# tree=ET.fromstring(data)
# print("my name is : ",tree.find("name").text)
# print("my id is : ",tree.find("id").text)
# print("my email is : ",tree.find("email").get("hide"))
# #extracting data from xml data format from many users
# import xml.etree.ElementTree as ET
# data='''
# <stuff>
#   <users>
#     <user x="1">
#       <name>Mugisha pascal</name>
#       <email hide="mugishapascal2008@gmail.com"/>
#     </user>
#      <user x="2">
#       <name>Mugisha daddy</name>
#       <email hide="mugishapascal2024@gmail.com"/>
#     </user>
#   </users>
# </stuff>
# '''
# tree=ET.fromstring(data)
# users=tree.findall("users/user")
# print("the users length is : ",len(users))
# for user in users:
#     print("the user count is : ",user.get("x"))
#     print("the name is : ",user.find("name").text)
#     print("the user email is : ",user.find("email").get("hide"))
# #accessing data using json format(dictionaries)
# import json
# data='''{
#     "name" : "pascal",
#     "nicknames" : {
#         "home":"daddy",
#         "school":"pascal",
#         "hospital":"mugisha"
#     },
#     "email":"mugishapascal2008@gmail.com"
# }'''
# info=json.loads(data)
# print("my name is : ",info["name"])
# print("my nickiname at the hospital is : ",info["nicknames"]["hospital"])
# print("my email is : ",info["email"])
# #accessing data using json format(lists)
# import json
# data='''[
# {
#     "name":"mugisha",
#     "count":"1",
#     "position":"hospital"
# },
# {
#     "name":"pascal",
#     "count":"2",
#     "position":"school"
# },
# {
#     "name":"daddy",
#     "count":"3",
#     "position":"home"
# }
# ]'''   
# info=json.loads(data)
# print("the count of users is : ", len(info) ) 
# for user in info :
#     print("the name of the user , count ,position is : ",user["name"],",",user["count"],",",user["position"])
# #reading a json data from a given url over the internet and return some of its content
# import urllib.request,urllib.parse,urllib.error
# import json 
# serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"
# while True: 
#     address = input("enter the address : ")
#     if len(address)<1:break
#     url=serviceurl+urllib.parse.urlencode({"address":address})
#     print(url)
#     data=urllib.request.urlopen(url)
#     gdata=data.read().decode()
#     print(len(gdata))
#     try:
#         js=json.loads(gdata)
#     except:
#         js=None
#     if not js or "status" not in js or js["status"]!="OK" :
#         print("failed to retrieve")
#         continue
#     print("the latitude is ",js["results"][0]["geometry"]["location"]["lat"])
#     print("the longitude is ",js["results"][0]["geometry"]["location"]["lng"])
#     print("the location is ",js["results"][0]["formatted_address"])
# # objects in python(introduction)
# class partyanimal():
#     x=0
#     def party(self): 
#         self.x=self.x+1
#         print("so far",self.x)
# an=partyanimal()
# print(dir(an))
# print(type(an))
# #creating and destroying objects 
# class partyanimal():
#     x=0
#     def __init__(self):
#         print("iam constructed")
#     def party(self):
#         self.x=self.x+1
#         print("so far ", self.x)
#     def __del__(self):
#         print("iam destructed",self.x)
# an=partyanimal()
# an.party()
# an.party()
# print("an contains ",an.x)
# an=7
# print("an contains ",an)
# #inheritance in python
# class partyanimal():
#     x=0
#     name=""
#     def __init__(self,z):
#         self.name=z
#         print("iam constructed")
#     def party(self):
#         self.x=self.x+1
#         print("so far ", self.x)
# class footballfan(partyanimal):
#     points=0
#     def touchdown(self):
#         self.points=self.points + 1
#         self.party()
#         print(self.name,"this is ",self.points)
# p=partyanimal("pascal")
# p.party()
# p.party()
# m=footballfan("mugisha")
# m.party()
# m.touchdown()
# m.touchdown()
# #database in python 
# import sqlite3
# conn=sqlite3.connect("email.db")
# cur=conn.cursor()
# filename=input("enter the filename : ")
# file=open(filename)
# for line in file:
#     line=line.rstrip()
#     pieces=line.split()
#     email=pieces[1]
#     cur.execute("select count from counts where email = ?",(email,))
#     row=cur.fetchone()
#     if row is None:
#         cur.execute('''insert into counts (email,count) values (?,1)''',(email,))
#     else:
#         cur.execute("update counts set count = count + 1 where email= ?",(email,))
#     conn.commit()
# sqlstr='select email , count from counts order by count desc limit 10'
# for row in cur.execute(sqlstr):
#     print(str(row[0]),row[1])
# cur.close()
# #tracks.py
# import xml.etree.ElementTree as ET 
# import sqlite3
# conn=sqlite3.connect("trackdb.sqlite")
# cur=conn.cursor()
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Tracks;

# CREATE TABLE Artist(
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
#     name TEXT UNIQUE
# );
 
# CREATE TABLE Album(
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
#     artist_id INTEGER,
#     title TEXT UNIQUE
#     );
    
# CREATE TABLE Track (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title TEXT UNIQUE,
#     album_id INTEGER,
#     len INTEGER , rating INTEGER ,count INTEGER 
#     );
# ''')
# fname=input("enter the filename : ")
# def lookup(d,key):
#     found=False
#     for child in d :
#         if found :return child.text
#         if child.tag == 'key' and child.text == key :
#             found = True
#     return None
# stuff=ET.parse(fname)
# all=stuff.findall('dict/dict/dict')
# print("dict count : ",len(all))
# for entry in all :
#     if(lookup(entry,'Track ID')is None): continue
    
    
#     name=lookup(entry,'Name')
#     artist=lookup(entry,"Artist")
#     album=lookup(entry,"Album")
#     count=lookup(entry,"Play Count")
#     rating=lookup(entry,"Rating")
#     length=lookup(entry,"Total Time")
    
#     if name is None or artist is None or album is None:
#         continue
    
#     print(name,artist,album,count,rating,length)
    
#     cur.execute('''INSERT OR IGNORE INTO Artists (name)
#                 VALUES(?)''',(artist,))
#     cur.execute('SELECT id FROM Artist WHERE name =?',(artist,))
#     artist_id=cur.fetchone()[0]
    
#     cur.execute(''' INSERT OR IGNORE INTO Album(title,artist_id)
#                 VALUES(?,?)''',(album,artist_id))
#     cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
#     album_id=cur.fetchone()[0]
#     cur.execute('''INSERT OR REPLACE INTO Track (title,album_id,len,rating,count)
#                 VALUES (?,?,?,?,?)''',(name,album_id,length,rating,count))
#     conn.commit()
# #counting up program
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# #counting down program
# i=10
# while i>0:
#     print(i)
#     i=i-1
# #guessing game with no iteration 
# guess=int(input("enter your desired number : "))
# correct=7
# while guess!=correct:
#     print("please the enter correct number")
#     break
# while guess==correct:
#     print("the guessed number is correct ")
#     break
# #guessing game with iteration
# correct=7
# guess=0
# while guess!=correct:
#     try:
#          guess=int(input("enter a number between 1 to 10 : "))
#     except:
#         print("retry please")
#     if guess<correct: 
#         print("the guess is low")
#     elif guess>correct:
#         print("the guess is high ")
#     else:
#         print("the guess is correct")
# print("finished")
# #sum of numbers
# sum=0
# number=float(input("enter the number : "))
# while number!=0:
#     sum=sum+number
#     number=float(input("enter the number : "))
# print(sum)
# #prime number checker using inbuilt function
# import sympy
# number=int(input("enter the number to check : "))
# if sympy.isprime(number):
#     print(f"the {number} is prime number")
# else:
#     print(f"the {number} is not prime number")
# #prime number checker using while loop
# import math
# number=int(input("enter the number to check : "))
# sq=math.sqrt(number)
# while sq>=2:
#     if number==sq**2 :
#         print("the square root is : ",int(sq))
#     sq=sq-1
# #multiplication table program
# number=int(input("enter a number : "))
# multiplicant=1
# while multiplicant<=10 :
#     product=multiplicant*number
#     print(number," * ",multiplicant," = ",product)
#     multiplicant=multiplicant+1
# #factorial program
# number=int(input("enter a number : "))
# factorial=1
# while number>=1:
#     factorial=number*factorial   
#     number=number-1
# print(factorial)
# #password validator
# password=input("enter password please : ")
# while len(password)!=8:
#     if len(password)>=8:
#         print("your passwprd is long enough")
#         break
#     else :
#         print("your password is short try again")
#         break

# def hasspecial(psw):
#     import re 
#     return bool(re.search(r"[^\w\s]",psw))

# if (hasspecial(password)):
#     print("the password has special characters ,great password")
# else:
#     print("the password has no special characters")

# def hasuppercaseandlow(psw):
#     return any(char.isupper() for char in psw)
    
# if(hasuppercaseandlow(password)):
#     print("the password has upper case letters,the password is precise")
# else:
#     print("the password has no uppercase letters , try again ")

# def hasdigits(psw):
#     return any(char.isdigit() for char in psw )
# if hasdigits(password) :
#     print("the password has digits , its precise ")
# else :
#     print("the password has no digits , its not precise")
# #countdown timer program innacurate
# count="40seconds"
# import re 
# numberstr=re.findall("[0-9]+",count)
# for number in numberstr:
#     number=int(number)
# while number>=0:
#     print("the remaining seconds are ",number,"seconds")
#     number=number-1         
# #count down timer program accurate 
# def countdown(tseconds):
#     while tseconds>0:
#         import time
#         mins,secs=divmod(tseconds,60)
#         print(f"{mins:02d}:{secs:02d}",end="\r")
#         tseconds-=1
#         time.sleep(1)
#     print("timer completed")
# targetsec=int(input("enter the time duration in seconds : "))
# countdown(targetsec)    
# #text analyser program using dictionaries
# text="pascal"
# import re
# listo=re.findall("[a-z]",text)
# counts=dict()
# for letter in listo :
#     counts[letter]=counts.get(letter,0)+1
# for key,value in counts.items():
#     print(key,"count is ",value)
# #text analyser using while loop
# text="pascal"
# i=0
# digits=0
# alphabets=0
# specialchars=0
# while len(text)>i:
#     char=text[i]
#     if char.isalpha():
#         alphabets+=1
#     elif char.isdigit():
#         digits+=1
#     else:
#         specialchars+=1
#     i+=1
# print(digits)
# print(alphabets)
# print(specialchars)
# #list statistics program 
# numlist=list()
# while True:
#     try :
#         number=int(input("enter a number (press enter if done): "))
#     except:
#         break
#     numlist.append(number)
#     if number == None: 
#         break
# sum=0
# for num in numlist:
#     sum+=num
# average=sum/len(numlist)
# maxi=max(numlist)
# mini=min(numlist)
# print("the average is ",average," the maximum is ",maxi," and the minimum is ",mini)
# #list filtering program
# text=input("enter the sentence : ")
# words=text.split()
# counts=dict()
# for word in words:
#     counts[word]=counts.get(word,0)+1
# for key,value in counts.items():
#     if value!=1:
#         print("the word is",key)
# #data validation program
# target="pascal"
# while True :
#     inputi=input("guess the sentence : ")
#     if inputi==target:
#         break
# #palindrome checker program
# def ispalindrome(txt):
#     i=0
#     j=len(txt)-1
#     if txt[i]!=txt[j]:
#         return False    
#     i+=1
#     j-=1
#     return True
# text="nan"
# if ispalindrome(text):
#     print(text,"is a palindrome")
# else:
#     print(text,"is not a palindrome")
# #caesar cipher program
# def ciphering(msg,key):
#     i=0
#     cy=""
#     while i<len(msg):
#         char=msg[i]
#         if char.isalpha():
#             if char.isupper():
#                 newchar=chr((ord(char)-ord("A")+key)%26+ord("A"))
#             else :
#                 newchar=chr((ord(char)-ord("a")+key)%26+ord("a"))
#         else:
#             newchar=char
#         cy+=newchar
#         i+=1
#     print(cy)
# ciphering("nyqayj",2)
# #printing numbers in python 1-10
# for num in range(1,11):
#   print(num)
# #printing numbers from 1-20
# for numb in range(2,20):
#   print(numb)
# #summing numbers program
# sum=0
# input=int(input("enter a number to sum up : "))  
# for num in range(1,input):
#   sum+=num
# print("the sum is : ",sum) 
# #list iteration program
# filename="exe.txt"
# file=open(filename)
# for line in file:
#   line=line.rstrip()
#   words=line.split('=')
#   for word in words:
#     print(word)
# #factorial program
# last=4
# factorial=1
# for num in range(1,last+1):
#   factorial*=num
# print(f"the factorial of {last} is {factorial}")
# #prime number check 
# def primenumbercheck(num):
#   """
#   This function checks if a given number is prime.

#   Args:
#       num: The number to check for primality.
#   """
#   import math
#   sq = math.sqrt(num)
#   sq = int(sq)
#   for numi in range(2, sq + 1):
#     if num % numi == 0:  # Check for divisibility
#       print(f"{num} is not a prime number")
#       return  # Exit the function after finding a divisor

#   print(f"{num} is a prime number")

# number = int(input("Enter the number : "))
# primenumbercheck(number)
# #list comprehensions to print numbers 1-10[]
# num=[num for num in range(1,11)  ]
# print(num)
# #list comphension to sum up numbers
# number=int(input("enter a number : "))
# sumofnum=sum(range(1,number+1))
# print(sumofnum)
# #string reversal program
# name="pascal"
# name2=""
# for char in name[::-1]:
#   name2+=char
# print (name2)
# #multiplication table program
# num=2
# for nux in range(1,11): 
#   product=num*nux
#   print(f"{num}*{nux}={product}")
# #pyramid program
# for i in range(1,5+1):
#     for j in range(5-i,0,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# #egypt pyramid 
# for row in range(1,5+1):
#     for j in range(5-row,0,-1):
#         print(" ",end="")
#     for j in range(1,row+1):
#         print("*",end="")
#     for j in range(2,row+1):
#         print("*",end="")
#     print()
# #file processing program in python 
# filename="exe.txt"
# with open(filename,"r") as file:
#     filey=file.read()
# print(filey)
# #string length program in python 
# name="pascal"
# print("the length of name pascal is",len(name))
# #character access and string slicing program 
# name="pascal"
# print(name[0])
# print(name[:])
# print(name[:-1])
# print(name[:-2])
# print(name[::-1])
# print(name[::-2])
# print(name[::-3])
# print(name[1:3])
# #greeting program
# name="pascal"
# def greet(nm):
#     print("hello"+' '+nm)
# greet(name)
# #escape sequences program
# name="pascal"
# print(name+"\n"+"pascal")
# print(name+"\t"+"pascal")
# #uppercase and lowercase conversion 
# name="pascal"
# print(name.upper())
# name2="PASCAL"
# print(name2.lower())
# print(name2)
# if name.islower():
#     print("fine")
# if name2.isupper():
#     print("fine2")
# #string searching program
# name="pascal"
# search=name.find("l")
# search2=name.find("as")
# #string replacement program
# stri="pascal pascal pascal pascal"
# stri2=stri.replace("pascal","mugisha",1)
# str3=stri.replace("pascal", "daddy", 2)
# print(stri)
# print(stri2)
# print(str3)
# #string formating program
# name="pascal"
# print(f"my name is {name}")
# #strings methods for common tasks program
# name="mugisha pascal daddy" 
# list1=name.split()
# print(list1)
# name2="mugisha@pascal"
# list2=name2.split("@")
# name3="  pascal  "
# name4=name3.strip()
# print(name4)
# name5=name3.rstrip()
# print(name5)
# name6=name3.lstrip()
# print(name6)
# name7=name.rsplit()
# name8="name12"
# if name8.isalnum():
#     print(name8)
# #email validation program
# email="mugishapascal2008@gmail.com"
# def isspecialc(stri):
#     import re
#     trth=bool(re.search(r"[^\w\s]",stri))
#     return trth
    
# if any([l.isdigit() for l in email]) :
#     print("email contains numbers")
# if email.isalnum():
#     print("the email contains numbers and text (but no special characters)")
# if isspecialc(email):
#     print("the email contains special characters")
# #palindrome program using string slicing
# name="pascal"
# name2=name[::-1]
# if name==name2:
#     print(f"{name} is palindrome")
# #updated version
# word=input("enter a word to check : ")
# pali=list()
# for l in word[::-1]:
#     pali.append(l)
#     paliv="".join(pali)
# if paliv==word :
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")
# #Text Analysis (Word Counting, Frequency) program
# #first word analysis program
# line="pascal is my name as pascal"
# count=dict()
# words=list()
# linee=line.split()
# for word in linee:
#     words.append(word)
#     count[word]=count.get(word,0)
# print(count)
# #letter analysis program 
# line="my name is mugisha pascal"
# count=dict()
# for let in line:
#     count[let]=count.get(let,0)+1
# for key,value in count.items():
#     print(f"{key} : {value}")
#regular expression programs
# #pattern matching program
# import re
# name="my name is mugisha pascal"
# match=re.search("pascal",name)
# if match :
#     print("this is perfect")
# #extracting phone number program in re
# phone="my phone number is 0786493844"
# import re
# tel="".join(re.findall("[0-9]",phone))
# print(f"my number is {tel}")
# #extracting an email address program in re
# emailmix="my email is mugishapascal2008@gmail.com "
# import re
# email=re.findall("\S+@\S+",emailmix)
# #match alphanumeric program in re
# stri="my_stringism123"
# import re
# match=re.findall(r"^\w+$",stri)
# print(match)
# #accurete program for email extraction
# import re
# emailmix="my email is mugishapascal-2008@gmail.com ,there it is"
# email="".join(re.findall(r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",emailmix))
# print(f"my email is {email}")
# #phone number validation format(xxx-xxx-xxxx)
# myphone="0786493844 and 078-649-3844 078-987-6543"
# import re
# tel=re.findall(r"\d{3}-\d{3}-\d{4}",myphone)
# #program to replace html tags 
# html=r"<p> mugisha pascal <\p>"
# import re
# uhtml=re.sub(r"<[\\]*\w>","",html)
# print(uhtml)
# #extracting dates program format(xx/xx/xxxx)
# datemix="the date of this day is 23/04/2024"
# import re
# date="".join(re.findall(r"\d{2}\/\d{2}\/\d{4}",datemix)) 
# print(date)  
# #strong password validation
# password="Mama2010@"
# import re
# #digits
# if re.search(r"\d",password):
#     print("the password contains digits")
# else:
#     print("the password contains no digits")
# #capital letter
# if re.search(r"[A-Z]",password):
#     print("the password contains uppercase")
# else :
#     print("the password contains no uppercase")
# #special characters
# if re.search(r"[^\w\s]",password):
#     print("the password contains special characters")
# else :
#     print("the password contains no special characters")
# #lowercase letter
# if re.search(r"[a-z]",password):
#     print("the password contains lowercase")
# else :
#     print("the password contains no lowercase")#
# #extrecting dates in format(dd-mm-yyyy)
# datemix="the date today is 23-04-2024"
# import re
# date="".join(re.findall(r"\d{2}-\d{2}-\d{4}",datemix))
# print(date)
# #anagram check program
# name="pascal"
# name2="lascap"
# count1=dict()
# for let in name:
#     count1[let]=count1.get(let,0)+1
# count2=dict()
# for let in name2:
#     count2[let]=count2.get(let,0)+1
# sortc1=dict(sorted(count1.items()))
# sortc2=dict(sorted(count2.items()))
# if sortc1==sortc2:
#     print(f"{name} and {name2} are anagram to each other")
# else :
#     print(f"{name} and {name2} are not anagram to each other")
# #sorting a string
# nm="cba"
# nms="".join(sorted(nm))
# print(nms)
# #string compression program
# name="pascal"
# count=dict()
# for let in name:
#     count[let]=count.get(let,0)+1
# comp=list()
# for key,value in count.items():
#     comp.append(key)
#     value=str(value)
#     comp.append(value)
# comp="".join(comp)
# print(comp)
# # text cleaning program
# import re
# text="mugisha , pascal "
# txto=str.maketrans("","",",")
# text=text.translate(txto).upper()
# print(text)
# #reading through a file
# file=open("exe.txt")
# for line in file:
#     print(line)
# #writing a message to file
# with open("write.txt","w") as file:
#     file.write("iam mugisha pascal")
# file=open("write.txt")
# for line in file:
#     print(line)
# #copying content btn files program
# file=open("exe.txt")
# with open("write2.txt","w") as file2:
#     for line in file:
#         file2.write(line)
# file2=open("write2.txt")
# for line in file2:
#     print(line)
# # counting no of lines (file) program
# name="file.txt"
# file=open(name)
# count=0
# for line in file:
#     line=line.rstrip()
#     count+=1
#     if line=="":
#         count-=1
        
# print(f"the number of lines in {name} is {count}")
# #readline method in file handling
# file=open("file.txt")
# line=file.readline()
# line2=file.readline()
# #using len() to count number of lines in a file
# name="write2.txt"
# file=open(name)
# linelist=[line for line in file ]
# count=len(linelist)
# if file.readline()=="":
#     count-=1 
# print(f"the number of lines in {name} is {count}")
# #counting the number of lines using readline
# file=open("file.txt")
# count=0
# while lino:=file.readline():
#     count+=1
# print(f"the count of lines is {count}")
# #append a file program
# name="write.txt"
# with open(name , "a") as file:
#     file.write("mugisha pascal")
# file=open("write.txt")
# for line in file:
#     print(line)
# #searching a word in a file program
# file=open("file.txt")
# target="daddy"
# count=0
# for line in file:
#     line=line.rstrip()
#     words=line.split()
#     count+=1
#     for word in words:
#         if word==target:
#             print(f"{word} is found on number {count}")
# #doing the above program using readline
# file=open("file.txt")
# target="pascal"
# count=0
# while line:=file.readline():
#     line=line.rstrip()
#     words=line.split()
#     count+=1
#     for word in words:
#         if word==target:
#             print(f"{word} is found on number {count}")
# # modifying a file// not running
# name="file.txt"
# tempname=f"{name}.temp"
# with open(name,"r") as orgfile ,open(tempname,"w") as tempfile:
#     for line in orgfile:
#         modified=line.replace("mugisha","pascal")
#         tempname.write(modified)
#     import os
#     os.replace(tempname,name)
# for line in open(name):
#     print(line)
# #read csv file program(not extension of csv)
# file=open("csv.txt")
# for line in file:
#     line=line.rstrip()
#     words=line.split(",")
# print(words)
# #reading actual csv file//not running
# with open("pas.csv","r") as csvfile:
#     import csv
#     csvread=csv.reader(csvfile)
#     for row in csvread:
#         print(row)
##writing to csv file program
# with open("pas.csv","w") as csvfile:
#     import csv
#     csvread=csv.writer(csvfile)
#     csvread.writerow(["ggg","kkk","lll"])
#     csvread.writerows(["p12","pqw","kjj"])
# #access list element program
# index=int(input("enter the index : "))
# list=["mugisha","pascal"]
# print(f"the value at index {index} is {list[index]}")
# #modifying content at index program
# index=int(input("enlist=["mugisha","pascal"]ter the index : "))
# word=input("enter the word to put to the index : ")
# list=["mugisha","pascal"]
# list[index]=word
# #list concantenation program
# list1=["mugisha","pascal"]
# list2=["mugisha","pascal"]
# list=list1+list2
# print(list)
# #list slicing program
# list=[1,2,3,4,5,6,7]
# print(list[1:3])
# #list membership program
# list=["mugisha","pascal"]
# if "mugisha" in list:
#     print("pascal")
# #list duplicate removal program
# list1=[1,2,3,3,2]
# list2=list(set(list1))
# list3=set(list1)
# print(type(list1))
# #remove method in python
# list=[1,2,3,4]
# list.remove(4)    
# print(list)
# #list comprehension with lists
# list=[1,2,3,4,5,6,7]
# pr=[num for num in list]
# print(pr)
# #tips and tricks in python
# #changing color
# print("\033[90m this is pascal")
# print("\033[96m this is mugisha")
# #multiplication shortcut
# nmber=5*5
# nmber2=5**2
# print(nmber)
# print(nmber2)
# #rounding numbers
# print(round(11.5))
# #writing money
# mybank=999_999_999+1
# print(mybank)
# #moving to a web browser (opening a url)
# import webbrowser
# webbrowser.open("https//www.google.com")
# #writing a string (many lines)
# text="mugisha "\
# "pascal"
# print(text)

# text2='''
# mugisha2 pascal2
# '''
# print(text2)

# text3="mugisha \
# pascal"
# print(text3)
# #dealing with list indexes(reversing)
# list=[1,2,3]
# list.reverse()
# print(list)
# print(list[::-1])
# print(list[-1])
# # indexes of substrings of strings
# if 'you' in 'youtube':
#     print('youtube'.index('tube'))
# print('youtube'.index('tube'))
# # finding in a string
# print('youtube'.find('tube'))
# #id of dictionaries ?? 
# data={'pascal':5}
# print(id(data))
# #destructering with dict id
# data1={"mugisha":7}
# data2=data1
# data2["pascal"]=6
# print(id(data1))
# print(id(data2))
# print(data1)
# print(data2)
# #reversing lists with ids
# data=[3,2,1]
# print(id(data))
# data.reverse()
# print(id(data))
# print(data)
# #changing content of a list
# list=["mugisha","pascal"]
# def changelist(lst):
#     lst=["daddy"]
# def changelistitems(lst):
#     lst[:]=["daddy"]
# print(list)
# changelist(list)
# print(list)
# changelistitems(list)
# print(list)
# #copying content of list with ids
# list=["pascal","mugisha"]
# list2=list[:]
# print(id(list),id(list2))
# #using copy method with ids
# list=["mugisha","pascal"]
# list2=list.copy()
# print(id(list),id(list2))
# #ids for inner lists
# list=["pascal","mugisha",[1,2]]
# list2=list[:]
# print(id(list[-1]),id(list2[-1]))
# list[-1][-1]="wow"
# print(list2)
# # deepcopy with list ids
# from copy import deepcopy
# list=["pascal","mugisha",[1,2]]
# list2=deepcopy(list)
# print(list2)
# # diff btn deepcopy and copy method ?
# # not keyword
# data=list()
# # print(not data)
# data=[]
# print(data is None)
# data2=None
# print(data2 is None)
# #len with None ?
# data=None
# print(len(data)==0)
# # none with not keyword
# data=None
# print(not data)
# # globals and locals methods
# data=[]
# print('data' in locals(),'data' in globals())
# listo=list()
# for num in range(1,10):
#     listo.append(num)
# print('listo' in globals())
# print('num' in globals())
# def func():
#     dt=list()
#     print(dt)
# print('dt' in globals())
# # end keyword 
# for num in range(1,11):
#     print(num,end=" ")
# print("hello")
# print("")
# print("yoyo")
# # tuple creation from multiple datatypes 
# data="pascal"
# d2=2
# msg=d2,data
# print(msg)
# # concatenating datatypes
# d1=1
# d2=3
# d3=str(d1)+" "+str(d2)
# print(d3)
# #destructering of function
# def getpos():
#     return 1,2,3,4
# x,y,z,a =getpos()
# print(x,y,z,a)
# v=getpos()
# print(v)
# #reduction of an if statement
# rep=7
# sta="leader" if rep>5 else "worker"
# print(sta)
# # in keyword
# number=[1,2,3,4]
# print("nope" if 4 in number else "fine")
# #range functionality
# print(list(range(15)))
# print(range(15))
# print(type(range(15)))
# print(list(range(10,100,10)))
# for i in range(5):
#     print(i)
# #* keyword
# def  returning(x,y,z):
#     print(f"returning {x} {y} {z}")
# data=[1,2,3]  
# returning(*data)
# returning(data[0],data[1],data[2])
# # or replacement 
# weather ="stormy"
# if weather in ['rainy','stormy','snowy']:
#     print('cancel')
# # list of conditions
# age=21
# reputation=20
# conditions=[
#     age>=21,
#     reputation>=20
# ]
# if all(conditions):
#     print('admin')
# else:print("standard user")
# #firstname and lastname program
# print("give me your names : ")
# firstname,lastname=input().split()
# print(firstname,lastname)
# # list loop
# names=["mugisha "," pascal"]
# cleaned=[name for name in names if name not in["mugisha "]]
# print(cleaned)
# #choosing through a list
# while True:
#     print('''choose an option:
#           1.play game
#           2.load game
#           3.high scores
#           4.quit          
#           ''')
#     if input()=="4":
#         break
# #recursive functions
# def done():
#     print("done")
# def dosomething(func):
#     print("do something...")
#     func()
# dosomething(done) 
# #recursive with time module
# def done():
#      print("mugisha pascal")
# def dosomething(func):
#     import time
#     print("loading man")
#     time.sleep(3)
#     func() 
# dosomething(done)
# #enumerate method
# names=["mugisha","pascal"]
# for num,name in enumerate(names):
#     print(name,num)
# #enumerate method updated
# names=["mugisha","pascal"]
# for num,name in enumerate(names):
#     print(name,names[num-1])
# #loop shortcut
# list=[[1,2],[3,4]]
# items=[item for pair in list for item in pair]
# print(items) 
#  #non blank character regex search using [^ ]
# name="mugisha pascal"
# import re
# firstname=re.findall("m[^ ]*",name)
# print(firstname)
# #xml1
# import xml.etree.ElementTree as ET
# data='''
# <person>
#     <name>mugisha</name>
#     <class>year c </class>
#     <email hide="good"/>
# </person>
# '''
# tree=ET.fromstring(data)
# print(tree.find('name').text)
# print(tree.find("class").text)
# print(tree.find('email').get('hide'))
# # multiple users xml
# import xml.etree.ElementTree as ET 
# users='''
# <users>
#     <user>
#         <name>mugisha</name>
#         <email hide="mumu"/> 
#     </user>
#     <user>
#         <name>pascal</name>
#         <email hide="papa"/>
#     </user>
# </users>
# '''
# tree=ET.fromstring(users)
# list=tree.findall('user')
# print(len(list))
# for user in list:
#     print(user.find('name').text)
#     print(user.find('email').get('hide'))
# #json1 
# import json 
# data='''{
#     "name":"mugisha",
#     "email":"mp@gmail.com",
#     "class":{
#         "1":"year1b",
#         "2":"year1d"
#     }
# }'''
# data1=json.loads(data)
# print(data1["name"])
# print(data1["class"]["1"]) 
# #enumerate method with start 
# names=["mugisha","pascal"]
# for value ,name in enumerate(names,start=1):
#     print(value ,name)
# #zip method
# names=["mugisha","pascal"]
# locs=["hospital","school"]
# sps=["sp1","sp2"]
# for name,loc,sp in zip(names,locs,sps):
#     print(f"{name} in {loc} also {sp}")
# #tuple manipulation(unpackaging)
# a,b=(1,2)
# print(a)
# print(b)
# x,y,*z=(1,2,3,4)
# print(x,y,z)
# p,s,*_=(1,2,3,4)
# print(p,s,_)
# b,*c,d,e=(1,2,3,4,5,6)
# print(b,c,d,e)
# #class 1
# class name():
#     name=""
#     def __init__(self):
#         print("class constructed")
#     def printo(self):
#         name="pascal"
#         print(f"this is a class of {name}")
#     def __del__(self):
#         print("class is destroyed")
# np=name()
# np.printo()
# #setattr and getattr methods
# class printnum():
#     name=""
#     def __init__(self,nam):
#         print("starting")
#         self.name=nam
#     def printn(self):
#         print(self.name)
# pn=printnum("pascal") 
# printc=""
# setattr(pn,printc,"1")
# print(getattr(pn,printc))
#connecting a class with a dict
# class person():
#     pass
# person=person()
# dic={"mugisha":1,"pascal":2,"daddy":3}
# for key,value in dic.items():
#     setattr(person,key,value)
# print(person.pascal)
# #key manipulation in a dict
# dic={"mugisha":1,"pascal":2}
# for key in dic.keys():
#     print(key)
# #value manipulation
# dic={"mugisha":1,"pascal":2}
# for val in dic.values():
#     print(val)
# #getpass method 
# from getpass import getpass
# name=input("enter a number : ")
# pwd=getpass("enter a password : ")
# print("loading")
# #datetime module
# from datetime import datetime
# print(datetime.today()) 
#dealing with csv
import pandas as pd
ds=pd.read_csv("vgsales.csv")
ds.shape