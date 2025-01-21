
#! Getting started with Python programming
"""
Get Python by installing anaconda. Follow instructions for installing on 
Windows. Use Python 3 if no old code to work with.
"Register Anaconda as the system Python 3.7" - Yes
Add Anaconda to Path - consider troubleshooting this based on own experience

Using python as a calculator - with floating point numbers, precision might 
be a tiny bit off.

 Quotiont is //
 Modulo is %
 
"""

# Manual concatenation
savings = 400
print(type(savings))
print("My savings in a year is:", savings)


# f prefix
print(f"My savings is {savings}!")


"""
\t = tab
\n = new line

Because backslash is escape character, to use it in a string you need to add two

"""

#! Lists and tuples
"""
Lists can contain duplicates, and the order of items in list is significant
because of how we access items in list using index positions 
with list_name[position]

lists are vectors - one dimensional and you use only one index to access 
element within a vector

Use negative values for reading list backwards

Can use index positions to update items in list
to add, use:
list.append(item_to_be_appended)
but you can only append one item

Can use insert to put into the middle of the list, and shift items along

copy function performs a deep copy (entirely new list, so any changes to 
original will not impact copy)

variable = new_variable will create a shallow copy
copy.copy() will create shallow copy, you'll have to use copy.deepcopy()

list slicing
list_name[start_index:end_index] but end index is exclusive
list slicing creates a deep copy

step sizes - slicing using list[::2] will omit start and end indexes and will 
access every alternate element in list

Strings are immutable - cant update items at specific assignments but you can
specify variables to match each character
You can index for actual letters e.g., place = "city"
place.index("c") = [0]

Tuples are immmutable - once made cannot be updated
if you put a list inside a tuple, you can update values within the list 


#! Dictionaries and sets
Mapping of key and value pairs
e.g., 
bike_owners = {"
James": "Ducati", 
"Aiden": "Harley"
}

bike_owners["James"] will have result "Ducati"

and you can check what's in the dictionaries e.g.,
"Aiden" in bike_owners.keys() = True

and list all with bike_owners.keys()
bike_owners.get["key"] = value
add to dictionary with bike_owners["Lisa"] = "bicycle"

Sets have no order and don't support indexing

tuple = immutable so once created, cant be changed

!# Shallow and deep copies
Shallow copies is var_1 = var_2 and if you update one, the other will change

import copy
copy.copy() where first refers to module, second is an activity
copy.deepcopy() will create deep copy

Lists and copies and immutability 
copy.copy creates a deep copy of a list
However, if you have a nested list, changes to one will be reflected in both

!# if-else control structures
Rule of precedence in python, so addition has higger precedence than <

!# For loops
enumerate function will return individual element in a tuple but the index 
for the element within the object iterating over
remember range(num), and with 2 arguments it'll be the start and end 
(exclusive for max). if 3 arguments, it's the steps.

can use _ as the name of variable for element in loop when value of element 
isn't really going to be accessed

break statements

!# functions
funtion_name.__doc__ will give you documentation for that function
kwargs or keyword arguments have the ** in the function brackets. this means
you want your variable-length arguments to be passed in in the form of key
words. Python then packs the variable length arguments into a dictionary, not
a tuple. This dictionary has key value pairs, where the keys are the names of
your variables and the values are the values that you specify.
e.g.,
student_details(name="John") will have just one argument entered into dict.

Functions will prioritise local rather than global variables by default
if you're defining or using a variable within a function but need it to be 
global:
global variable_name
so any future reference to city will be the global version

Modifying a complex data type inside a function also changes it outside the 
function if you accept it as an input into the function.

Example of *args to use functiona s a variable argument:

def calculte(*args, fn): - this will unpack the args tuple and pass arguments in individually
    return fn(*args)
    
where function passed in can be invoked using variable length argument

Lambda functions are anonymous functions - when you define this, you use lambda
not def. For example
lambda <input_arguments>: <expression>
cube_of = lambda x: x * x * x
result = cube_of(5) would then end up with 125 if you called result

def check_if_even(x):
    asset x % 2 == 0
    
so will raise assertion error if check_if_even(3) is run

Lambdas often used with filter function in python
e.g., 
num_list = (1,5,6,7,11,99,320)
greater_than_10_list = list(filter(lambda x: x >10, num_list))
greater_than_10_list

!# Generators and closures
generators is a function which creates iterators over any sequence and can be
used to iterate over infinite sequences. 

e.g.,

def generator()):
    print("one!")
    yield 1
    
    print(two!)
    yield 2
    
    print("three)
    yield 3

g = generator()
g

next(g)
    
generators don't have return statements and instead contain the yield command.
They create a generator object, but when you call them and invoke it the code 
isn't executed. This is an iterator which allows you to iterate over the
yield commands so you can input it into a function.

can amend this code to 
def generator():
    n = 1
    print ("one")
    yield n
    
    n+= 1
    print ("two)
    yield n
    
    
and can use generator for infinite sequences e.g.,
def generate_even_numbers(limit):
    for i in range (0, limit, 2):
        yield i
        
g = generate_even_numbers(7)
next(g)
or l = list(g)

"""

# %%
for num in range (0,3):
    print (num +0.1)
# %%
num_list = (1,5,6,7,11,99,320)
greater_than_10_list = list(filter(lambda x: x >10, num_list))
greater_than_10_list

# %%
