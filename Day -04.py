# Python Day 04 – Functions

## Date

01/07/2026

## Topic Covered

Functions in Python

## Concepts Learned

### 1. What is a Function?

A function is a reusable block of code that performs a specific task.

Example:

```python
def greet():
    print("Hello")

greet()
```

### 2. Function Call

Calling a function executes the code inside the function.

```python
greet()
```

### 3. Parameters and Arguments

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

* Parameters: `a`, `b`
* Arguments: `10`, `20`

### 4. Return Statement

```python
def square(n):
    return n * n
```

The `return` statement sends a value back from the function.

---

## Problems Solved

### Q1. Print Your Name Using Function

```python
def my_name():
    print("Sanjeev")

my_name()
```

### Q2. Print Your Age Using Function

```python
def my_age():
    print("21")

my_age()
```

### Q3. Square of a Number

```python
def square(n):
    return n * n

print(square(5))
```

### Q4. Add Two Numbers

```python
def add(a, b):
    return a + b

print(add(3, 4))
```

### Q5. Even or Odd

```python
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(even_odd(8))
```

### Q6. Greater of Two Numbers

```python
def greater(a, b):
    if a > b:
        return a
    return b

print(greater(10, 15))
```

### Q7. Factorial Using Function

```python
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print(factorial(5))
```

---

## Mini Project – Student Result System

Features:

* Accept student name
* Accept marks
* Calculate grade
* Check pass/fail status

Concepts Used:

* Functions
* Conditions
* Return Statements
* User Input

---

## LeetCode Completed

### 1929. Concatenation of Array

```python
class Solution:
    def getConcatenation(self, nums):
        return nums + nums
```

---

## HackerRank Completed

### Python Functions (Leap Year)

```python
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap
```

---

## Skills Learned Today

* Functions
* Function Calls
* Parameters
* Arguments
* Return Statement
* Reusable Code
* Factorial Logic
* Problem Solving with Functions

---

## Day 4 Summary

Today I learned the fundamentals of Python Functions. I practiced creating functions, passing parameters, returning values, and solving real programming problems using functions. I also completed one LeetCode problem and one HackerRank problem to strengthen my understanding.

## Author

Sanjeev Kumar
B.Tech CSE (AIML)
Aspiring AI Developer
