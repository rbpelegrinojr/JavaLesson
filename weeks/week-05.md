# Week 05 — Java Variables

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

A **variable** is a named storage location in memory that holds a value. Think of it as a labelled box.

**Declaring a variable:**
```java
dataType variableName = value;
```

**Types of variables by location:**

| Type | Where it lives | Example |
|------|----------------|---------|
| Local variable | Inside a method | `int x = 5;` inside `main` |
| Static variable | Belongs to the class | `static int count = 0;` |

**Constants (final variables):**
```java
final double PI = 3.14159;  // Cannot be changed after assignment
```

**Variable naming rules:**
1. Start with a letter, `$`, or `_`
2. No spaces
3. No reserved keywords (`int`, `class`, `if`, etc.)
4. Case-sensitive (`age` ≠ `Age`)

---

## 🔑 Key Concepts

- What a variable is (memory storage)
- Declaration vs initialization
- `final` keyword for constants
- Variable naming rules and best practices
- Local vs class-level scope (introduction)

---

## 💻 Code Sample 1 — Variable Basics

```java
// File: VariableDemo.java
public class VariableDemo {
    public static void main(String[] args) {
        int score = 95;
        double price = 49.99;
        String city = "Manila";
        boolean isStudent = true;
        char grade = 'A';
        final int MAX_SCORE = 100;

        System.out.println("Score:       " + score);
        System.out.println("Price:       " + price);
        System.out.println("City:        " + city);
        System.out.println("Is student:  " + isStudent);
        System.out.println("Grade:       " + grade);
        System.out.println("Max score:   " + MAX_SCORE);

        score = 98;   // update variable
        System.out.println("Updated score: " + score);
    }
}
```

**Expected Output:**
```
Score:       95
Price:       49.99
City:        Manila
Is student:  true
Grade:       A
Max score:   100
Updated score: 98
```

---

## 💻 Code Sample 2 — Variable Swap

```java
// File: SwapVariables.java
public class SwapVariables {
    public static void main(String[] args) {
        int a = 10, b = 20;
        System.out.println("Before: a=" + a + ", b=" + b);

        int temp = a;
        a = b;
        b = temp;

        System.out.println("After:  a=" + a + ", b=" + b);
    }
}
```

---

## ✏️ Activity 1 — Variable Declaration Drill

Create `MyVariables.java` declaring and printing:
- Full name (`String`)
- Age (`int`)
- Height in metres (`double`)
- Whether you wear glasses (`boolean`)
- Name initial (`char`)
- Lucky number as a constant (`final int`)

Print each with a descriptive label.

---

## 🎯 Activity 2 — Variables Quiz (Written)

Predict the output or explain the error *without running the code*:

```java
// Quiz A
int x = 5;
x = x + 3;
System.out.println(x);

// Quiz B
final int Y = 10;
Y = 20;   // What happens?
System.out.println(Y);

// Quiz C
int a = 7, b = 3;
int result = a * b - a + b;
System.out.println(result);
```

---

## 📝 Quiz — Week 05

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** Which keyword makes a variable a constant?
- A) `static`
- B) `const`
- C) `final` ✓
- D) `fixed`

**2.** Which is a valid variable name in Java?
- A) `2score`
- B) `my score`
- C) `class`
- D) `myScore` ✓

**3.** What is the default value of an uninitialized `int` field?
- A) `null`
- B) `1`
- C) `0` ✓
- D) Undefined

**4.** What happens when you try to reassign a `final` variable?
- A) Nothing; the value changes
- B) A compile error occurs ✓
- C) A runtime error occurs
- D) The variable becomes `null`

**5.** Which statement declares AND initializes a variable?
- A) `int x;`
- B) `int x = 5;` ✓
- C) `x = 5;`
- D) `declare int x = 5;`

---

## ✅ Weekly Outcome

By the end of Week 5, you can:
- Declare and initialize variables of different types
- Use `final` for constants
- Update variable values correctly
- Follow naming conventions
