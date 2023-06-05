#mx = lambda x,y:x if x>y else y
#print (mx(2,3))

#n =[4,3,2,1]
#print(list(map(lambda x: x**2,n)))

#n = [4,3,2,1]
#print(list(filter(lambda x:x>2,n)))

#from functools import reduce
#n = [3,3,3]
#print(reduce(lambda x,y:x*y,n))

#l = lambda x: x**3
#print(l(5))

#f = lambda x, y, z : x + y + z
#print(f(1,2,3))

#z = (lambda a= 'wolsbane', b = 'georgia', c = 'ginny',d = 'marcus': a + b + c)
#print(z('marcus'))

#def write():
    #title = 'Sir'
    #name = (lambda x : title + ' ' + x)
    #return name
#who = write()
#print(who('hadi majeed'))

#l = [lambda x: x**2,
 #   lambda x: x**3,
  #  lambda x: x**4]
#for f in l:
 #   print(f(3))

# import math 
# def cal_area (r):
#     return math.pi * (r**2)
# radii = [2,5,7.1,0.3,10]
# areas=[]
# for i in radii:
#     a = cal_area(i)
#     areas.append(a)
# print(areas)

# import math 
# def cal_area(r):
#     return math.pi *(r**2)
# radii = [2,5,7.1,0.3,10]
# print(list(map(cal_area,radii)))

# lst = [("hadia",2),
#        ("shaaf",3),
#        ("hafsa",4),
#        ("saneela",5)
#        ]
# l = lambda data: (data[0],9/5*data[1]+32)
# print(list(map(l,lst)))

# import statistics
# data = [1.3,2.7,0.8,4.1,4.3,-0.1]
# avg = statistics.mean(data)
# print(avg)

# print(list(filter(lambda x: x>avg,data)))

# countries =["","","pakistan","","iqbal"]
# print(list(filter(None,countries)))


# from functools import reduce
# data = [2,4,6,8,3,5,8,64,6]
# print(reduce(lambda x, y : x * y, data))

# data = [2,3,5]
# product = 1
# for i in data:
#     product = product *i
# print(product)


# def natsum(x):
#     if x <= 10:
#         return x
#     else:
#         return x + natsum(x-1)
# print(natsum(15))

# def natsum(n):
#     if n==1:
#         return n
#     else:
#         return n+natsum(n-1)
# print(natsum(4))

# def sumdig(x):
#     if x <10:
#         return x
#     else:
#         return (x%10)+sumdig(int(x/10))
# print(sumdig(45))

# def fact(x):
#     if x <= 1:
#         return 1
#     else:
#         return (x) * fact(x-1)
# print(fact(4))

# def fib(x):
#     if x<=0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fib(x-1)+fib(x-2)
# for i in range (20):
#     print(fib(i),end=" ")

# def sqr(a,b):
#     if a == 0:
#         return 0
#     if b == 0:
#         return 1
#     if a == 1:
#         return 1
#     if b == 1:
#         return a
#     else:
#         return a * sqr(a,b-1)
    
# print(sqr(2,3))




# def halfdiamond(n):
#     for i in range (n):
#         for j in range (i+1):
#             print("* ",end="")
#         print()
#     for i in range (n-1,0,-1):
#         for j in range (1,i+1):
#             print("* ",end="")
#         print()
# halfdiamond(4)


# from random import randint
# locX=0
# locY=0
# NORTH = 0
# WEST =1
# EAST= 2
# SOUTH =3
# tries = int(input("Number Of Tries:")) 
# for i in range(tries):
#     direction = randint(0,4)
#     if direction == NORTH:
#         locY+=1
#     elif direction == WEST:
#         locX-=1
#     elif direction == EAST:
#         locX+=1
#     elif direction == SOUTH:
#         locY-=1
    
# print("After", (tries), "intersections") 
# print("the ending locations for the drunk is") 
# print(locX, locY)


# word = str(input("enter a name:"))
# wordLen = len(word)
# subLen= 1
# start =0
# while start + subLen <= wordLen:
#     print(word[start:start+subLen])
#     subLen+=1


# mycontacts = {"Fred": 721,"Mary":123,"hadia":456}

# def prin(mycontacts):
#     for key in sorted(mycontacts):
#         print(key,mycontacts[key])
# prin(mycontacts)


# def time(time1,time2):
#     time1 = input("Please enter the first time: ")
#     time2 = input("Please enter the second time: ")
#     time1_minuites = int(time1[:2])
#     time1_hours = int(time1[2:])
#     time2_minuites = int(time2[:2])
#     time2_hours = int(time2[2:])
#     total_minuties_time1 = time1_hours * 60 + time1_minuites
#     total_minuties_time2 = time2_hours*60 + time2_minuites
#     difference = total_minuties_time2- total_minuties_time1
#     minutes = difference//60
#     hours = difference%60 
#     return f"{hours} hours {minutes} minutes"

# print(time(900, 1730))


# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
# def is_key_present(x):
#     if x in d:
#         print('Key is present in the dictionary')
#     else:
#         d[x]=100
#         print
# is_key_present(7)

# d1={"hadia":3, "mama":2}
# d2 ={"sidra": 6, "khizra":8}
# d1.update(d2)
# print(d1)

# sum = 0
# n = int(input("enter a number"))
# numberdigits = len(str(n))
# for i in range (numberdigits):
#     digit = n % 10
#     if digit % 2 != 0 :
#         sum+=digits
#     n = int(n/10)
# print(sum)

# counter = 1
# while counter <=5:
#     number = int(input ("guess a number:"))
#     if number !=5:
#         print("Try Again")
#     else:
#         print("good Try")
#         break
#     counter = counter + 1
# print("game over")

# def tt(list):
#     list = [1,2,3,4,5,6,7,8,9,10]
#     for i in range (len(list)):
#         if list[i] %2 == 0:
#             list[i]= "hello"
#     return list
# print(tt(list))

# def reverse(list):
#     list = [1,2,3,4,5,6,7,8,9]
#     return list[::-1]
# print(reverse(list))


# list = []
# for i in range (1,21):
#     list.append(i)
# print(list)



# from random import randint
# list = []
# while len(list) <  11:
#     rando = randint(1,101)
#     if rando not in list:
#         list.append(rando)
# print(list)


# list = [1,2,3,4,5]
# productitems = 1
# for i in list:
#     productitems = productitems*i

# print(productitems)

# string = "hadia majeed"
# v = ("a","e",'i','o','u','A','E','I','O','U')
# count = 0
# for i in string:
#     if i in v:
#         count = count+1
# print("a :",string.count("a"))
# print("e :",string.count("e"))
# print("i :",string.count("i"))
# print("o :",string.count("o"))
# print("u :",string.count("u"))
# print ("Tota Occurence", count)



# def midword(word):
#     word = str(input("enter a name:"))
#     n = len(word)
#     mid = n // 2
#     if n % 2 ==0 :
#         return word[0]+ " "+ word[mid -1]+ " "+ word[-1]
#     else: 
#         return word [0]+ " "+ word [mid] + " "+ word [-1]
# print(midword(ord))

# def isAscending (num):
#     numstr = str(num)
#     for i in range(len(numstr)-1):
#         if numstr[i] > numstr[i+1]:
#             return False
#         else:
#             return True
    
# print(isAscending(234))

# def list_sum(num_list):
#     if len(num_list)== 1:
#         return num_list[0]
#     else:
#         return num_list[0] + list_sum(num_list[1:])
# print(list_sum([2,4,3]))

# def islucky(number):
#     if number < 8:
#         return False
#     last_digit = number % 10
#     if last_digit == 8:
#         return True
#     return(islucky(number//10))
# print(islucky(12))

def rev(str):
    if len(str)== 0:
        return str
    else:
        return rev(str[1:]) + str[0]
print(rev("hello"))