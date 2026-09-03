<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">This work by Robert Fulkerson is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" vel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0&nbsp;<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

# Lecture 04

## Summary

We started our last class with a brief discussion of the [UNO Counseling and Psychological Services](https://www.unomaha.edu/counseling-and-psychological-services/index.php) resource on campus.

----

Today we talked about variables, assignment statements, objects, mutability, immutability, and different numeric data types.

### Naming Variables
When naming variables, Python best practices indicate that you should start your variables with a letter, followed by meaningful letters, digits and underscores. Underscores should be used for spaces for readability and all letters should be lowercase. Naming conventions are discussed in [PEP8](https://peps.python.org/pep-0008/#naming-conventions), the Python Enhancement Proposal.  PEP8 also discusses coding styles, etc. Here are some examples of valid identifiers used as variable names:

```python
the_first_number = 1
yellow = 2112.0
first_name = "Jessica"
last_name = "Smith"
```

### Assignmenet Statements
Assignment statements use the assignment operator `=` and, at least for right now, have a single variable on the lefthand side and an expression on the righthand side. The expression on the right is evaluated to a single value (for now) and is stored/assigned to the variable on the lefthand side. We briefly touched on this in [Lecture 03](../Lecture_03/) in class.  Here are some examples:

```python
the_first_number = 1
yellow = 2112.0
first_name = "Jessica"
last_name = "Smith"
```

Yup, those same statements from the variable examples are all valid assignment statements. We're assigning the values on the righthand side to the variables on the lefthand side. Assignment statements can be more complex, however, like this (which isn't too complex for now):

```python
my_value = int(input("Enter a value: "))
final_value = my_value * 10
```

Two assignment statements, one which takes user input and converts it to an integer value, and another that multiplies that input value (stored in `my_value`) by 10 to store it into `final_value`.

If you have assignment statements that assign to the same variable, the value stored in the variable will always be the last assignment in the statement sequence.  So, for example:

```python
tax_rate = 0.07
print(tax_rate)      # prints 0.07
tax_rate = 0.065
print(tax_rate)      # prints 0.065
```

An analogy for this is if you have a time written down to meet someone for coffee as 9:00am and then you have to push that time back to 9:30am, you'll always use the last value for that coffee date. You could certainly show up for coffee at 9:00am, but the person you're meeting won't be there until 9:30am because that was the updated, agreed-upon time for the meeting.

### Variables as Objects
We also briefly talked about every variable being an object and each object in Python having a value (what's stored in the variable) and the `type()` (such as integer, float, or string), and the `id()`, which is where the variable is stored in memory.

For a little more context, the id of a variable helps to demonstrate the last concept we talked about, which is mutability. Variables that are integers, floats, or strings are *immutable*, which means that when you store a value into a variable and then change that value, the variable name stays the same but Python allocates an entirely different location in memory for the new value to be stored in. 

It's kind of like having a sticky note with a title of "Important Phone Number" having a value of 1-800-555-1111 and then, if you change the important phone number on the sticky note to 1-800-555-1112 the location of the sticky note needs to move from its original position. This is a rough analogy -- you don't *have* to move the sticky note -- but assuming that you would have to take the sticky note off the wall to change the number, you probaby wouldn't get it back in *exactly* the same place it was before.  This is immutability.  You can change the value of a variable, but it will keep moving around in memory as you do that.

```python
my_x = 2112
print(x,id(x))     # this will print the value of x and it's memory location
my_x = my_x + 1
print(x,id(x))     # this will print the new value and the new memory location
```

We'll see mutable variables later in the semester and be able to better compare and contrast why there are mutable and immutable objects in Python.

### Floating-point Values
Lastly, we talked about `float()` and floating point values, as well as a basic overview of f-strings (formatted strings):

```python
# regardless of what's entered (3 or 3.12), it will be converted to a floating point value
my_neat_value = float(input("Enter a number: "))

value_of_pi = 3.14159

# print values with different levels of digits after decimal
print(f"{value_of_pi}")
print(f"{value_of_pi:.4f}")
print(f"{value_of_pi:.3f}")
print(f"{value_of_pi:.2f}")
print(f"{value_of_pi:.1f}")
```

### After-class Question about Integer vs. Float Usage
Finally, there was a great question after class about why you would ever use integer values when floating-point values are more precise and can represent any integer value.

There's an in-depth discussion that can be had about this, but the general reasons for using an integer (i.e., whole number value like `600`) over a float (i.e., value with decimal point like `600.663`) are:

* ***Exact precision***<br>Integers provide exact, whole number values. Floating point values are usually approximations of the number you're actually trying to represent (e.g., `0.1` + `0.2` does not always exactly equal `0.3` for reasons resulting from their underlying implementation).
* ***Avoiding accumulating errors***<br>Because of the underlying implementation just mentioned, cumulative arithmetic operations can introduce small rounding errors, which can lead to unexpected or incorrect results.
* ***Logical fit for the data***<br>Many real-world quantities are inherently whole numbers, lke the count of items (number of people, pages in a book) and currency calculations (such as the number of cents).
* ***Faster arithmetic***<br>Because of the way integers are stored, arithmetic is generally faster for integer values than floating-point values.
* ***Arbitrary size***<br>Because integers have unlimited precision, limited by available system memory, they can be arbitrarily large. Floating-point values have upper and lower boundaries that will result in overflow or underflow situations if the number stored or calculated is too large or small.

Compared to other languages like C/C++/Java, Python's implementation of integer values is incredibly flexible, but at the cost of taking up arbitrarily large amounts of memory. Integers in C/C++/Java are fixed-size entities (i.e., they take up a fixed-size of memory) and are thus have upper and lower boundaries for the values they can store. 

## The topics for this lecture

* Variables and Assignments
* Identifiers
  - Naming rules and style guidelines
* Objects
  - Name binding / Memory
  - Object properties
* Numeric Types
  - Integers and Floats
  - Formatting output


## The highlighted topics for this lecture

* Variables
* Valid identifiers
  - Letters
  - Digits
  - Underscores
  - Case-sensitive
  - PEP 8
* Reserved Keywords

* Assignment statements
* Incrementing a variable's value

* Object
  - Value
  - Type … `type()`
  - Identity … `id()`

* Mutability
* Immutable

* Scientific notation

* Floating point values
* Floating point literals
* `float()`
* Formatting floating point output

## Music played before class

* [She Came Through the Chimney](https://www.youtube.com/watch?v=LyJuAnv9TvM) by amon düül II
* [Lookin Away](https://www.youtube.com/watch?v=mMRGM_rbvOA) by Monotronic
* [The Fantastic Four: First Steps Main Theme](https://www.youtube.com/watch?v=XoZpg1tSDR8) by Michael Giacchino
* [Secret Tunnel](https://www.youtube.com/watch?v=yBXbGHfs0kE) by Jeremy Zuckerman
* [Upside Down & Inside Out](https://www.youtube.com/watch?v=LWGJA9i18Co) by OK Go
* [Wild and Clear and Blue](https://www.youtube.com/watch?v=X2g2f6DgF8c) by I'm With Her
