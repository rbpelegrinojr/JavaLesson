# Week 10 — Java Booleans & Midterm Review

> **Course:** Introduction to Java Programming | **Level:** Beginner  
> 🏆 **MIDTERM EXAM THIS WEEK**

---

## 📖 Lesson — Part A: Java Booleans

A `boolean` variable holds exactly **`true`** or **`false`**. Booleans drive all decision-making in Java.

```java
boolean isRaining  = true;
boolean hasUmbrella = false;
```

**Boolean expressions** — any expression that evaluates to true/false:
```java
int age = 18;
boolean isAdult = age >= 18;   // true
boolean isChild = age < 13;    // false
```

**Logical operators:**

| Op | Name | Meaning |
|----|------|---------|
| `&&` | AND | Both must be true |
| `\|\|` | OR | At least one must be true |
| `!` | NOT | Reverses |

**Truth table:**

| `a` | `b` | `a && b` | `a \|\| b` | `!a` |
|-----|-----|---------|----------|------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

**Short-circuit evaluation:**
- `&&` — if left side is `false`, right side is **never evaluated**
- `||` — if left side is `true`, right side is **never evaluated**

---

## 📖 Lesson — Part B: Midterm Review

**Topics Covered (Weeks 1–10):**

| Week | Topic |
|------|-------|
| 1 | Java Introduction — JDK/JRE/JVM |
| 2 | Java Get Started — compile-run cycle |
| 3 | Java Syntax — semicolons, braces, conventions |
| 4 | Output & Comments — println/printf, comment types |
| 5 | Variables — declaration, initialization, final |
| 6 | Data Types — 8 primitives, overflow |
| 7 | Type Casting — widening/narrowing, parseInt |
| 8 | Operators — arithmetic, logical, increment |
| 9 | Strings & Math — methods, Math class |
| 10 | Booleans — logic, truth tables, short-circuit |

---

## 🔑 Key Concepts

- Boolean type and boolean expressions
- Logical operators and truth tables
- Short-circuit evaluation
- Review of all Weeks 1–9 topics

---

## 💻 Code Sample — Boolean Logic

```java
// File: BooleanDemo.java
public class BooleanDemo {
    public static void main(String[] args) {
        boolean isLoggedIn  = true;
        boolean isPremium   = false;
        boolean hasExpired  = false;

        boolean canAccess = isLoggedIn && !hasExpired;
        boolean seesAds   = !isPremium || hasExpired;

        System.out.println("Can access: " + canAccess);  // true
        System.out.println("Sees ads:   " + seesAds);    // true

        int score = 75;
        boolean passed = score >= 60;
        boolean honor  = score >= 90;
        System.out.println("Passed: " + passed);  // true
        System.out.println("Honor:  " + honor);   // false

        // Boolean from String comparison
        String input = "YES";
        boolean accepted = input.equalsIgnoreCase("yes");
        System.out.println("Accepted: " + accepted);  // true
    }
}
```

---

## ✏️ Activity 1 — Boolean Logic Worksheet (Midterm Prep)

Evaluate each expression (`p = true`, `q = false`, `r = true`):
```java
1. p && q
2. p || q
3. !p && q
4. p && (q || r)
5. !(p || q) && r
6. p == q
7. p != q
8. (p && !q) || (!p && q)   // What does this pattern represent?
```

---

## 🎯 Activity 2 — Midterm Practice Exam (60 min, 50 pts)

**Part I — Multiple Choice (20 pts)**

1. Which is NOT a primitive type? `a) int  b) String  c) boolean  d) char`
2. Output of `System.out.println(7 % 2)`? `a) 3  b) 3.5  c) 1  d) 0`
3. Which keyword makes a constant? `a) static  b) final  c) const  d) fixed`
4. `"Hello".charAt(1)` returns: `a) H  b) e  c) l  d) 1`
5. Widening casting is: `a) manual  b) automatic  c) not allowed  d) only for strings`

**Part II — Code Analysis (20 pts)** — write the output:
```java
int x = 5;
x += 3;
System.out.println(x * 2);
```
```java
double d = 9.7;
int i = (int) d;
System.out.println(i);
```

**Part III — Coding (10 pts)** — Write a complete Java program that:
- Declares a student name, subject, and two exam scores
- Calculates and prints the average with 2 decimal places
- Prints whether the student passed (average ≥ 60)

---

## 📝 Quiz — Week 10

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What value can a `boolean` variable hold?
- A) 0 or 1
- B) yes or no
- C) true or false ✓
- D) on or off

**2.** What does `&&` do?
- A) Returns true if at least one operand is true
- B) Returns true only if both operands are true ✓
- C) Reverses a boolean
- D) Compares two numbers

**3.** What is the result of `true || false`?
- A) `false`
- B) `true` ✓
- C) `null`
- D) Compile error

**4.** What is short-circuit evaluation for `&&`?
- A) Evaluates left side only if right is true
- B) Skips right side if left side is false ✓
- C) Always evaluates both sides
- D) Only works with integers

**5.** What is the result of `!(true && false)`?
- A) `false`
- B) `true` ✓
- C) `null`
- D) `0`

---

## ✅ Weekly Outcome

By the end of Week 10, you:
- Understand boolean logic completely
- Have completed the midterm exam
- Can identify knowledge gaps for the second half of the course

---

## 🏆 MIDTERM EXAM

**Coverage:** Weeks 1–10  
**Topics:** Java Intro through Booleans (all topics listed in Midterm Review above)
