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

#/=================================================================/#

def run():
    pow_num = 10 ** 2
    add_num = pow_num + 12
    subtract_num = add_num - 40
    multi_num = subtract_num * 4
    div_num = multi_num / 3
    num_remain = div_num % 13

    print(pow_num, add_num, subtract_num, multi_num, div_num, num_remain)

run()

# Math operators work just exactly as in JS

"""
HOWEVER! As you know when you run this file. 
The dividing and modulo (remainder) actually return a float data type.
"""
div_num = 100 / 3
num_remain = div_num % 13

print(type(div_num), type(num_remain))

"""
See? So what we need to do in order for it to give us a int. we can give the operator the same symbol but instead of once.
It's done twice.
"""

div_num = 100 // 3
# num_remain = div_num %/ 13

# Tried to do some research but modulo does not work like division. This trait only is for division only.

num = num + 1
# Is actually the same as
num += 1
num /= 5
num *= 3

# This is just like JS although incrementing like in JS does not work in python
# num++ does not exist.

my_string = "A double-quoted string."
your_string = 'A single quoted string.'

multiline_string = """This is my string that goes on multiple lines for whatever reason."""
a_new_multiline_string = '''Now this is the other multiline type for whatever reason.'''
# Fun fact. Multiline comments can actually be used as strings.

little_string = "bad"
medium_string = "super"

long_string = medium_string + little_string
print(long_string)

"""
Just like in JS we can concatenate the same data types together. 
Just not when it's two different data types. 
Then you have to predefine it.
"""

today = "26 of November"
year = 2024
state = "Arkansas"
isItSnowing = False

print_me = f"Today is {today}, {year}. Currently, I live at {state} and is there snow here? {isItSnowing}."

print(print_me)

"""
As you remember from reading comments earlier.
You saw how we used this syntax " ${`To put our ${variables} inside here, so we can call our ${functions}.`} "

This is the same thing as what we used here for python's print_me variable.

We instead call our syntax with " f"Then our {variables} are in curly braces. Just that {easy}!" || f'As well {single} quotes work {too}!' "

"""

print("ace of spades".split(" "))

# .split("method") works just as the same as in JS
'''
print("abcd".split(""))
Unforantuely .split("empty") like in JS it would work. Though in python that does not work and it throws an error.
'''

print(list("ABCD"))
# In order to list strings like this example: A B C D. You need to use the list("Function")

print("abcd".index("d"))
# If we think back to JS with dot notation. .index("") is similar to that. Instead of predefining a number from an array like in JS
# Here you just define the characters that you are looking for.

# print("efgh".index("abcd"))
# This is what happens when we use index but define something that isn't present: "ValueError: substring not found"
# The error here is actually a value error

print("abcd".find("e"))
# .find("") is really handy to have in order to check whether you have something in your string. Basically the inverse of what .index("") does but similar
print("abcde".find("e"))

print("hey!".upper())
# This is just like our .upperCase() function from JS. Of course with an uppercase there is lower case.
print("AM I YELLING? DOES THAT BOTHER YOU??".lower())

print("Then I went to the store, but also I bought an ice cream for me!".replace("I", "you"))
# .replace("") seems really nice to know! probably use this in the future. Who knows really.

print("eggs" in "green eggs and ham.")
'''
in here is a new function. This is basically .find(""). Instead we are just looking for whether our input is present in the string.
Then our output will retain a boolean statement. If it is present. It's True, If it does not exist it will return False.
'''

print(len("Cheeseburger"))
# Funny thing is that .length("") has always been a array call back function. In python's case. It works for all data types and will return a int output
# This case the output: 12