# Day 2 Progress (23/06/2026)

## Topics Learned

* if Statement
* if else Statement
* if elif else Statement
* Comparison Operators
* Logical Operators
* Decision Making
* Basic Problem Solving using Conditions

---

## Programs Completed

### 1. Even or Odd

```python
n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 2. Positive, Negative, or Zero

```python
n = int(input())

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

### 3. Pass or Fail

```python
n = int(input())

if n >= 35:
    print("Pass")
else:
    print("Fail")
```

### 4. Voting Eligibility

```python
n = int(input())

if n >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

### 5. Greatest of Two Numbers

```python
a = int(input())
b = int(input())

if a > b:
    print(a, "is Greatest")
else:
    print(b, "is Greatest")
```

### 6. Greatest of Three Numbers

```python
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
```

### 7. Divisible by 5

```python
n = int(input())

if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
```

### 8. Divisible by 3 and 5

```python
n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by 3 and 5")
```

### 9. Student Grade Calculator

```python
marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")
```

---

# Mini Project

## Smart Login System

```python
username = input()
password = input()

if username == "admin" and password == "1234":
    print("Access Granted")
else:
    print("Access Denied")
```

---

# LeetCode

## 9. Palindrome Number

```python
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
```

Status: Completed ✅

---

## 1480. Running Sum of 1D Array

```python
class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums
```

Status: Completed ✅

---

# HackerRank

## Python If-Else

```python
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
```

Status: Completed ✅

---

## Loops

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i * i)
```

Status: Completed ✅

---

# Day 2 Summary

* Completed 9 Conditional Programming Problems
* Built Smart Login System Project
* Solved LeetCode 9
* Solved LeetCode 1480
* Solved HackerRank If-Else
* Solved HackerRank Loops
* Learned Comparison Operators
* Learned Logical Operators
* Learned Decision Making

Day Status: ✅ Completed

Overall Progress:

* Day 1 ✅
* Day 2 ✅
* Day 3 🔒 Next
