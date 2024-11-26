# This is a comment. Python will ignore this. Just like JS

"""
This is how you comment out multiple lines. Triple Double Quotes!
"""

'''
That also includes triple single quotes as well.
These two examples of multi lined comments are referred to as doc strings.
Basically in a nut shell. This is used for documenting 
'''

# This is the console.log(`Hello World!`) from JS but now down below is the python variation.
print('Hello World!')

# In order to get the console to run our file. We call " python3 file_name "

num = 15

# python's variables are dynamic

# movie | If I declare a non variable. Python will mark it as wrong. Why?
# Because python doesn't have " Undefined " as a data type.

movie = 'Sonic'

# This is how you do casing in python. Unlike JS where it's camelCasing.
# Here we use snake_casing
my_number = 10

print(my_number)

my_number = -5

print(my_number)

# We can redeclare/reassign variables over and over again just like in JS

"""
You know how we do not have let's or const's here?
Well the thing is python doesn't run like that.
Although, there is an exception. When someone has their function in CAPS.
It is considered as a CONST while regular casing is let
"""

# This here is considered as a const and other devs will understand to not reassign this value for the variable.
# This is also called SCREAMING_SNAKE_CASE
MY_FAVORITE_NUMBER = 5 

#/=================================================================/#

print(type("Hello World"))
# This will give an output class of str. Just like how data types work in JS

print(type(25))
# Output will be a data type of class num

print(type(3.14159))
"""
Output will return as a float. Same as JS. All decibels in JS are considered non integers but as floats.
Same goes for python.
"""

print(type(False))
print(type(True))
"""
You see something different? Yeah that's right!
Python actually capitalizes the first letter unlike JS
"""

print(type(None))
"""
This here is what we know that is considered as null and undefined from JS.
Again python unfortunately does not use null or undefined but instead it's used as None.
Output? NoneType

Obviously just like JS... there is a document to ALL data types >.> | https://docs.python.org/3/library/stdtypes.html
"""

#/=================================================================/#

"""
Let's get into the juicy bits! Remember how you were able to do this over on JS?

const run () => {
    let age = 19;
    let firstName = "Pedro";

    console.log(${`Hello my name is ${firstName} and I am ${age} years old.`});
}

run();

Yeah that's not possible in python.

def main():
    age_num = 19
    first_name = "Pedro"

    print("Hello there! My name is " + first_name + "and I am " + age_num + " years old!")

main()

This throws an error sadly.

In order to do this python is strict on what you want to do.
If you want a data type be changed into the correct type. We have to pre-define it before hand.
"""

def main():
    age_num = 19
    first_name = "Pedro"

    print("Hello there! My name is " + first_name + " and I am " + str(age_num) + " years old." )

main()