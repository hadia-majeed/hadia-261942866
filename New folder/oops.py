# # Define a class called Person with attributes name and age. 
# # Create an instance of the class and set the attributes to your own name and age.

# class Person:
#     def __init__(self, name,age):
#         self._name = name
#         self._age = age
# person1 = Person("hadia",15)
# print(person1._name)
# print(person1._age)

# Q2 Define a class called Rectangle with attributes width and height. 
# Add methods to calculate the area and perimeter of the rectangle.
# Create an instance of the class and test your methods

# class Rectanlge:
#     def __init__(self, width,height):
#         self._width = width
#         self._height = height
#     def getwidth(self):
#         return self._width
#     def setwidth (self, width):
#         self._width = width
#     def getheight(self):
#         return self._height
#     def setheight(self,height):
#         self._height = height
#     def area(self):
#         return self._height * self._width
#     def perimeter(self):
#         return 2*(self._height + self._width)
    
# rec1 = Rectanlge(2,4)
# print("w1",rec1.getwidth())
# print("h1",rec1.getheight())
# print('area:', rec1.area())
# print("perimeter:",rec1.perimeter())
# rec1.setheight(1)
# rec1.setwidth (2)
# print("w1",rec1.getwidth())
# print("h1",rec1.getheight())
# print('area:',rec1.area())
# print("perimeter:",rec1.perimeter())

# Q3 Define a class called Animal with attributes name and species. 
# Add a method to print out the animal's name and species. 
# Create an instance of the class and test your method.

# class Animal:
#     def __init__(self, animal,specie):
#         self._animal = animal
#         self._specie = specie
#     def get_animal(self):
#         return self._animal
#     def set_animal(self,animal):
#         self._animal = animal
#     def get_specie(self):
#         return self._specie
#     def set_specie(self,specie):
#         self._specie = specie
# animal1 = Animal("dog","husky")
# animal2 = Animal("cat","persian")
# print("name:",animal1.get_animal())
# print("specie:",animal1.get_specie())
# print("name:",animal2.get_animal())
# print("specie",animal2.get_specie())
# animal2.set_animal("bird")
# animal2.set_specie("sparrow")
# print("name:",animal1.get_animal())
# print("specie",animal1.get_specie())
# print("name:",animal2.get_animal())
# print("specie",animal2.get_specie())

 
# Q4 Define a class called Student with attributes name, age, and grades. 
# Add a method to calculate the average grade. 
# Create an instance of the class and test your method.

# class Student:
#     def __init__(self,name, age , grades):
#         self._name = name
#         self._age = age
#         self._grades = grades
#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         self._name = name
#     def get_age(self):
#         return self._age 
#     def set_age(self,age):
#         self._age = age
#     def get_grades(self):
#         return self._grades
#     def set_grades(self, grades):
#         self._grades = grades
#     def avg_grade (self):
#         return sum(self._grades)/len(self._grades)
# std1 = Student("Hadia",18,[15,6,10,12])
# std2 = Student("Majeed",19,[2,14,8,6])  
# print("Studen1:",std1.get_name()) 
# print("Age:",std1.get_age()) 
# print("Grades:",std1.get_grades())
# print("Average Grade:",std1.avg_grade())

# print("Studen2:",std2.get_name()) 
# print("Age:",std2.get_age()) 
# print("Grades:",std2.get_grades())
# print("Average Grade:",std2.avg_grade())
# std2.set_grades([1,2,3,4])
# print("Studen2:",std2.get_name()) 
# print("Grades:",std2.get_grades())
# print("Average Grade:",std2.avg_grade())








