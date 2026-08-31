<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">This work by Robert Fulkerson is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" vel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0&nbsp;<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

# Lecture 03

## Summary

Today's lecture was all about looking at basic output and basic input. This summary is not comprehensive of all of the topics covered in the book or lecture, but is meant to be representative of the highlights of discussions that took place.

### Basic Output with `print()`
Basic output is accompished with the `print()` function.

By default, the `print()` statement will print a newline at the end of whatever the statement is printing, which means that the next print statement would start it's content at the beginning of a new line.

```python
print("Hello world!")
print("How are you today?!")
```

### Using `end=` with `print()` to Modify Output Behavior
This behavior can be changed by using the `end=""` parameter for the print statement which changes the last output of the print statement to whatever the `end` parameter is.

For example, the following two statements are identical:

```python
print("Hello world!")
print("Hello world!", end="\n")
```

If the `end` parameter is omitted, then it defaults to a newline escape sequence (`\n`).  Usually, at least in CS1, the `end` parameter is either an empty string or a space to keep the output on the same line:

```python
print("Hello", end=" ")
print("world!")

# identical output below; notice where the space is ... inside the string
# literal instead of in the end parameter:
print("Hello ", end="")
print("world!")
```

The `end` parameter can also be used to put *anything* at the end of a line, such as ... ellipses.

```python
print("Hello", end="...")
print("world!")

# this code would print:   Hello...world!
```

### Getting User Input with `input()`
We also talked about basic input using the `input()` function.  Without a parameter (something inside the parentheses), the `input()` function just waits for the user of the program to type some input. With a parameter (a string), the string is used as a prompt to tell the user what to enter.

The results of an `input()` function call need to be stored into a variable so that the value can be used later in the program.

```python
# no prompt, store the result of the input into variable my_value
my_value = input()
print("You entered:", my_value)

# this time a prompt, store the result of the input into variable my_other
my_other = input("Please enter something:")
print("You entered:", my_other)
```

All input, by default, is textual or string data. If you need a value to be processed arithmetically later in your program as a number, you need to cast the input to the appropriate data type. To convert textual input to an integer, whole number value, use the `int()` function:

```python
my_age = int(input("Please enter your age:"))
print("You are", age, "years old.")

# because my_age is a number, you can do basic math with it, like this
print("In 10 years, you will be", age + 10, "years old.")
```

If you attempt to do arithmetic with a value read from the user that hasn't been converted to an integer or other type of number, you will receive a TypeError:

```python
# the "number" is read as a string because that's what input() does
my_number = input("Enter a number please:")

# the statement below will fail because Python doesn't know how to operate
# with a string on the lefthand side of the addition operator and an integer
# on the righthand side
print(my_number + 6)
```

### Three types of errors

There are three main types of errors you could run into while writing code:

* Syntax errors
* Runtime errors
* Logic (semantic) errors

**Syntax Errors**

Syntax errors are the easist to find and fix because they are caught by the Python interpreter. They prevent the code from actually running. 

Here are some examples:

```python
print{"Hello")  # incorrect opening parenthesis; should be ( instead of {
print("Hello)   # missing closing double quote for string literal
print('Hello")  # mis-matched quotes; either use both "" or '' for string literal
Print("Hello")  # print() function is capitalized; Python is case-sensitive
```

**Runtime Errors**

A runtime error occurs when the syntax of the code is perfect so the code runs, but while running the code experiences something that causes the program to crash.

Here are some examples. There are many more that we'll encounter as we move forward with Python.

```python
value = 18
print(value / 0)      # division (talked about in next lecture) by zero
                      # ZeroDivisionError: division by zero
print("Hello" + 5)    # Python can't add a string and an integer
                      # TypeError: can only concatenate str (not "int") to str
```

**Logic (semantic) errors**

The final type of error you'll encounter this semester is a logic (or semantic/meaning) error. These are the most difficult errors to locate and fix. The syntax of the code is correct, so the code runs. There aren't any runtime errors lurking in the code, so it never crashes. Yet, the code ends up generating incorrect output. You need to do extensive and thorough testing of your code, knowing what inputs should generate as output and accounting for all possible situations in your code. Testing is incredibly important in determine the correctness of your solution.

Here are a couple of examples:

```python
print("Five plus two is", 5 + 3)        # should output 7 but outputs 8 instead

base = 5
height = 10
triangle_area = 1 // 2 * base * height  # almost correct, but using // instead of /
```

## The topics for this lecture:

* Basic Output
  - `print()`
  - Basic outputting options
* Basic Input
  - `input()`
  - Input types and prompts
* Errors
  - 3 main types of errors

## The highlighted topics for this lecture:

* `print()`
* String literal
* `print("A",2)`
* `print("Hello", end=" ")`
* Newline character `\n`
* whitespace
* `input()`
* `input("prompt")`
* String input
* Data type
* `int()`
* Syntax error
* Runtime error
* Logic error
* Bug
* Crash

## Music played before class

* [Act Like Your Title](https://www.youtube.com/watch?v=RRFlCNSKEmE) by Rocket
* [couldn't run forever](https://www.youtube.com/watch?v=yNSEYbN9CAM) by Better Joy
* [Wreck](https://www.youtube.com/watch?v=qt-zMEpM7F8) by Neko Case
* [Be Around](https://www.youtube.com/watch?v=uTQZ7HMDEOc) by Ocie Elliott
* [Nothing I Need](https://www.youtube.com/watch?v=AErKzVIdb3I) by Lord Huron
* [bob dylan's 115th haircut](https://www.youtube.com/watch?v=iHUpk3ymbRM) by Ada Lea
* [Accidentally in Love](https://www.youtube.com/watch?v=GEo7W-uJNkc) by Counting Crows