# Python Day 05 – Strings

## Date

02/07/2026

## Topic Covered

Strings in Python

---

## Concepts Learned

### 1. What is a String?

A string is a sequence of characters used to store text data.

Example:

```python
name = "Sanjeev"
```

---

### 2. String Indexing

Each character in a string has an index.

```text
S a n j e e v
0 1 2 3 4 5 6
```

Example:

```python
name = "Sanjeev"

print(name[0])
```

Output:

```text
S
```

---

### 3. Negative Indexing

```python
name = "Sanjeev"

print(name[-1])
```

Output:

```text
v
```

---

### 4. Length of a String

```python
name = "Kiran"

print(len(name))
```

Output:

```text
5
```

---

### 5. Convert to Uppercase

```python
name = "sanjeev kumar"

print(name.upper())
```

Output:

```text
SANJEEV KUMAR
```

---

### 6. Convert to Lowercase

```python
name = "SANJEEV KUMAR"

print(name.lower())
```

Output:

```text
sanjeev kumar
```

---

### 7. Counting Characters

```python
word = "banana"

total = 0

for ch in word:
    if ch == "a":
        total += 1

print(total)
```

Output:

```text
3
```

---

## Problems Solved

### Q1. Print Name

```python
name = input()
print(name)
```

### Q2. Print First Character

```python
name = input()
print(name[0])
```

### Q3. Print Last Character

```python
name = input()
print(name[-1])
```

### Q4. Print Length

```python
name = input()
print(len(name))
```

### Q5. Convert to Uppercase

```python
name = input()
print(name.upper())
```

### Q6. Convert to Lowercase

```python
name = input()
print(name.lower())
```

### Q7. Count Occurrences of 'a'

```python
word = input()

total = 0

for ch in word:
    if ch == "a":
        total += 1

print(total)
```

---

## Challenge Problem – Reverse a String

```python
name = "Sanjeev"

print(name[::-1])
```

Output:

```text
veejnaS
```

---

## Mini Project – Name Analyzer

```python
name = "Sanjeev"

print("Name:", name)
print("Length:", len(name))
print("First Character:", name[0])
print("Last Character:", name[-1])
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
```

### Features

* Display name
* Find length
* First character
* Last character
* Uppercase conversion
* Lowercase conversion

---

## LeetCode Completed

### 58. Length of Last Word

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
```

---

## HackerRank Completed

### Find a String

```python
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count
```

---

## Skills Learned Today

* Strings
* Indexing
* Negative Indexing
* String Length
* Uppercase Conversion
* Lowercase Conversion
* Character Counting
* String Reversal
* String Traversal using Loops

---

## Day 5 Summary

Today I learned Python Strings and how to work with text data. I practiced indexing, finding string length, converting case, counting characters, and reversing strings. I also completed a LeetCode problem and a HackerRank problem related to string manipulation.

## Progress So Far

Completed Topics:

* Input / Output
* Variables
* Operators
* Conditions
* for Loop
* while Loop
* Functions
* Strings

## Author

Sanjeev Kumar

B.Tech CSE (AIML)

Aspiring AI Developer
