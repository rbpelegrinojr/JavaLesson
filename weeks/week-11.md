# Week 11 — Java If…Else

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

The `if-else` statement lets your program choose between paths based on a condition.

### Basic Forms

```java
// if only
if (condition) {
    // runs if true
}

// if-else
if (condition) {
    // runs if true
} else {
    // runs if false
}

// if-else if-else chain
if (score >= 90)      { grade = "A"; }
else if (score >= 80) { grade = "B"; }
else if (score >= 70) { grade = "C"; }
else if (score >= 60) { grade = "D"; }
else                  { grade = "F"; }
```

### Nested `if`

```java
if (isLoggedIn) {
    if (isAdmin) {
        System.out.println("Welcome, Admin!");
    } else {
        System.out.println("Welcome, User!");
    }
}
```

### Ternary Operator (shorthand if-else)

```java
String status = (age >= 18) ? "Adult" : "Minor";
```

### Common Mistakes

```java
// WRONG: assignment instead of comparison
if (x = 5) { ... }   // does not compile

// WRONG: comparing strings with ==
if (name == "Alice") { ... }

// RIGHT:
if (name.equals("Alice")) { ... }
```

---

## 🔑 Key Concepts

- `if`, `if-else`, `if-else if-else`
- Nested conditions
- Ternary operator
- Comparing values correctly (`.equals()` for Strings)
- Avoiding `=` vs `==` mistakes

---

## 💻 Code Sample 1 — Grade Classifier

```java
// File: GradeClassifier.java
public class GradeClassifier {
    public static void main(String[] args) {
        int score = 85;

        String grade;
        if      (score >= 90) grade = "A — Excellent";
        else if (score >= 80) grade = "B — Good";
        else if (score >= 70) grade = "C — Average";
        else if (score >= 60) grade = "D — Below Average";
        else                  grade = "F — Failed";

        System.out.println("Score: " + score);
        System.out.println("Grade: " + grade);

        String result = (score >= 60) ? "PASSED" : "FAILED";
        System.out.println("Result: " + result);
    }
}
```

---

## 💻 Code Sample 2 — Nested If (Login)

```java
// File: LoginCheck.java
public class LoginCheck {
    public static void main(String[] args) {
        boolean isLoggedIn  = true;
        boolean isAdmin     = false;

        if (isLoggedIn) {
            if (isAdmin) {
                System.out.println("Welcome, Administrator! Full access.");
            } else {
                System.out.println("Welcome, User! Limited access.");
            }
        } else {
            System.out.println("Please log in to continue.");
        }
    }
}
```

---

## ✏️ Activity 1 — Decision Tree Lab

Write `SeasonChecker.java`:
1. Store a month number (1–12)
2. Use if-else if to print the season (Dec/Jan/Feb=Winter, etc.)
3. Also print whether the month is in the first or second half of the year
4. Test with at least 3 different months

---

## 🎯 Activity 2 — BMI Calculator

Write `BMICalculator.java`:
1. Store `weight` (kg) and `height` (m) as doubles
2. Calculate BMI: `weight / (height * height)`
3. Classify: < 18.5 Underweight, 18.5–24.9 Normal, 25–29.9 Overweight, ≥ 30 Obese
4. Print BMI to 2 decimal places and the classification

---

## 📝 Quiz — Week 11

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What does the `else` block execute?
- A) Always
- B) When the `if` condition is true
- C) When the `if` condition is false ✓
- D) Only once at startup

**2.** What is the ternary operator syntax?
- A) `if (cond) val1 else val2`
- B) `cond ? val1 : val2` ✓
- C) `cond -> val1 : val2`
- D) `cond | val1 | val2`

**3.** How many `else if` blocks can you have in a chain?
- A) 0
- B) 1
- C) 2
- D) As many as needed ✓

**4.** How should you compare two String objects?
- A) `str1 == str2`
- B) `str1.equals(str2)` ✓
- C) `str1.compareTo(str2) == 0` (also valid, but .equals is simpler)
- D) `str1 = str2`

**5.** Given `int x = 75;`, which condition is `true`?
- A) `x > 80`
- B) `x == 80`
- C) `x < 70`
- D) `x >= 60` ✓

---

## ✅ Weekly Outcome

By the end of Week 11, you can:
- Write single, chained, and nested if-else statements
- Use the ternary operator correctly
- Build real decision-making programs
