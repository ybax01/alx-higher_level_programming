#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))  # This will print: <class '2-square.Square'>
print(my_square_1.__dict__)  # This will print: {'_Square__size': 3}

my_square_2 = Square()
print(type(my_square_2))  # This will print: <class '2-square.Square'>
print(my_square_2.__dict__)  # This will print: {'_Square__size': 0}

try:
    print(my_square_1.size)
except Exception as e:
    print(e)  # This will print: 'Square' object has no attribute 'size'

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)  # This will print: 'Square' object has no attribute '__size'

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)  # This will print: size must be an integer

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)  # This will print: size must be >= 0
