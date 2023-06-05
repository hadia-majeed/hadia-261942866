# # def fact(n):
# #     if n==0  or n ==0:
# #         return 1
# #     else:
# #         return n*fact(n-1)
# # print(fact(5))

# # def fib (n):
# #     if n == 1:
# #         return 1
# #     if n == 0:
# #         return 0
# #     else:
# #         return (fib(n-1)+fib(n-2))
# # print(fib(7))

# # def sum(n):
# #     if n == 0:
# #         return 0
# #     else:
# #         return (n% 10+sum(n//10))
# # print(sum(123))

# # def gcd(a,b):
# #     if b == 0:
# #         return a
# #     else:
# #         return gcd(b,a % b)
# # print(gcd(12,18))

# # def reverse (string):
# #     if string == "":
# #         return string
# #     else:
# #         return (reverse(string[1:]) +string)
# # print(reverse("hadia"))

# # def str_length(s):
# #     if s == '':
# #         return 0
# #     else:
# #         return 1 + str_length(s[1:])

# # def sqr (n,x):
# #     if x == 0:
# #         return 1
# #     else:
# #         return n*sqr(n,x-1)
# # print(sqr(2,3))

# # def sum(list):
# #     if len(list)== 0:
# #         return 0
# #     else:
# #         return  sum(list[1:])+list[0]
# # print(sum([1,2,3]))

# # def max(list):
# #     if len(list)== 1:
# #         return list[0]
# #     else:
# #         if list[0] > max(list[1:]):
# #             return list[0]
# #         else:
# #             return max(list[1:])
# # print(max([1,2,3]))

# # def  lislen(list):
# #     if len(list) == 0:
# #         return 0
# #     else:
# #         return 1 + lislen(list[1:])
# # print(lislen(['a','b','c','d']))

# # def palindrome(string):
# #     if len(string) == 1:
# #         return True
# #     else:
# #         if string[0]== string[-1]:
# #             return palindrome(string[1:-1])
# #         else:
# #             return False
# # print(palindrome())

# # def sum(n):
# #     if n == 0:
# #         return 0
# #     else:
# #         return n + sum(n-1)
# # print(sum(5))

# # def occur (lst,x):
# #     if len(lst) == 0:
# #         return 0
# #     elif lst[0] == x:
# #         return 1 + occur(lst[1:],x)
# #     else:
# #         return occur(lst[1:],x)
# # print(occur([1,2,3,2,4,2],2))

# # def vowels(lst):
# #     if len(lst)== 0:
# #         return 0
# #     elif lst[0] not in "aeiouAEIOU":
# #         return 1 + vowels(lst[1:])
# #     else:
# #         return vowels(lst[1:])
# # print(vowels(['h','a','d','i','a',]))

# You are to implement a string compression algorithm with the following specifications:
# •	If a character, ch, occurs n times in a row, then it will be represented by {ch}{n], where {n} is a value of n. For example is there is a substring “aaaa” it would be represented as “a4”. 
# •	If a character, ch occurs exactly one time in a row, then it will be simply represented as {ch}. For example, if the substring is “a”, then it will be represented as “a”. 
# Create a function RLE() to implement this algorithm recursively, this function should take in a string message and return the compressed string as an output. 

# def RLE (string):
#     if not string:
#         return ""
#     if len(string) == 1:
#         return string  
#     count = 1
#     char1 = RLE(string [0])
#     char_rest = string[1:] 
#     if char1 == char_rest[0]:
#         count +=1
#         return char1 + str(count) +  RLE(string[2:])
#     else:
#         return char1 + char_rest
# print(RLE("hhaadd"))

# def sum_list(lst):
#     total = 0
#     if not lst:
#         return ""
#     if len(lst) == 1:
#         return lst
#     for i in lst:
#         if type(i)== list:
#             total+= sum_list(i)
#         else:
#             total += i
#     return total
# print(sum_list([1,2,[3,4],[5,6]]))


# import os
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
# def add_book():
#     title = input("Enter book title: ")
#     author = input("Enter author name: ")
#     price = float(input("Enter book price: "))
#     book = Book(title, author, price)
#     with open('books.txt', 'a') as file:
#         file.write(f"{book.title},{book.author},{book.price}\n")
#     print("Book information added successfully.")
# def display_books():
#     if not os.path.isfile('books.txt'):
#         print("No books found.")
#         return
#     with open('books.txt', 'r') as file:
#         books = file.readlines()
#         if len(books) == 0:
#             print("No books found.")
#             return
#         print("Book Information:")
#         for book in books:
#             title, author, price = book.strip().split(',')
#             print(f"Title: {title}, Author: {author}, Price: {price}")
# def list_books_by_author():
#     author = input("Enter author name: ")
#     found = False
#     if not os.path.isfile('books.txt'):
#         print("No books found.")
#         return
#     with open('books.txt', 'r') as file:
#         books = file.readlines()
#         if len(books) == 0:
#             print("No books found.")
#             return
#         for book in books:
#             title, book_author, price = book.strip().split(',')
#             if book_author == author:
#                 if not found:
#                     print(f"Books by {author}:")
#                     found = True
#                 print(f"Title: {title}, Price: {price}")
#         if not found:
#             print(f"No books found by {author}.")

# def calculate_book_statistics():
#     if not os.path.isfile('books.txt'):
#         print("No books found.")
#         return
#     with open('books.txt', 'r') as file:
#         books = file.readlines()
#         if len(books) == 0:
#             print("No books found.")
#             return
#         prices = [float(book.strip().split(',')[2]) for book in books]
#         print(f"Sum of prices: {sum(prices)}")
#         print(f"Average price: {sum(prices)/len(prices)}")
#         print(f"Maximum price: {max(prices)}")
#         print(f"Minimum price: {min(prices)}")

# while True:
#     print("\nMenu:")
#     print("1. Add book information")
#     print("2. Display book information")
#     print("3. List all books of given author")
#     print("4. Return the sum, average, maximum and minimum of book prices stored in your file.")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         add_book()
#     elif choice == 2:
#         display_books()
#     elif choice == 3:
#         list_books_by_author()
#     elif choice == 4:
#         calculate_book_statistics()
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice. Please try again.")
# def abc(s):
#     if len(s)== 0:
#         return
#     abc(s[1:])
#     abc(s[1:])
#     print(s[0],end="")
# abc("xyz")

