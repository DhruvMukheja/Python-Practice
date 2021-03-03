# class Dog():

#     species = 'mammal'

# # This method is used to initialize the attributes of an object
    # def __init__(self,breed,name,spots):

#         self.breed = breed
#         self.name = name
#         self.spots = spots

    # def bark(self):
#         print(f'WOOF! My name is {self.name}')

# my_dog= Dog(breed='Lab', name= 'Pilla', spots= False)
# print(my_dog.name)
# print(my_dog.breed)
# print(my_dog.spots)
# print(my_dog.species)
# print(type(my_dog))
# my_dog.bark()

# class Animal():

#     def __init__(self):
#         print ('Animal created.')

#     def eating(self):
#         print('I am eating.')

#     def who_am_I(self):
#         print('I am an animal.')

# class Dog(Animal):

#     def __init__(self):
#         print('Dog is created.')


# my_animal = Animal()
# my_animal.eating()
# my_animal.who_am_I()

# my_dog = Dog()
# my_dog.eating()

# class Dog():

#     def __init__(self, name):
#         self.name = name 

#     def speak(self):
#         return(self.name + ' says WOOF!')

# class Cat():

#     def __init__(self, name):
#         self.name = name 

#     def speak(self):
#         return(self.name + ' says MEOW!')

# pilla = Dog('pilla')
# billu = Cat('billu')

# print(pilla.speak())
# print(billu.speak())

# for pet in [pilla, billu]:
#     print(pet.speak())

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(pilla)
# pet_speak(billu)

# class Book():

#     def __init__(self, title, writer, pages):
        
#         print("A book is created.")
#         self.title = title
#         self.writer = writer
#         self.pages = pages

#     def __str__(self):

#         return f'"{self.title}" by "{self.writer}"'

#     def __len__(self):

#         return self.pages

#     def __del__(self):

#         print("A book object has been deleted.")

# b = Book('Rudest Book Ever', 'Shewtab Gangwar', 133)

# print(b.title)
# print(len(b))
# del b

# import math
# a= math.sqrt(4)
# print(a)

arr= (7,9,5,8,9,5,4,-10)
arr = set(arr)
arr = sorted(list(arr))
print(arr)
arr.reverse()
y = arr.pop(1)
print(y)

print("Practice for Github.")