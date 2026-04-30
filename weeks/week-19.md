# Week 19 — Comprehensive Review

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

This is the **final review week** before the Final Exam. The goal is to consolidate everything from Weeks 1–18.

### Complete Course Summary

| Topic | Key Items |
|-------|-----------|
| Java Intro | JDK/JRE/JVM, platform independence |
| Get Started | Compile-run cycle, IDE, naming rules |
| Syntax | Semicolons, braces, case sensitivity, conventions |
| Output | println/print/printf, escape sequences, format specifiers |
| Variables | Declaration, initialization, final, scope |
| Data Types | 8 primitives, reference types, sizes, overflow |
| Type Casting | Widening/narrowing, parseInt, parseDouble, valueOf |
| Operators | Arithmetic, assignment, comparison, logical, increment |
| Strings | length, charAt, substring, equals, contains, replace |
| Math | abs, max, min, pow, sqrt, round, floor, ceil, random, PI |
| Booleans | Logic, truth tables, short-circuit |
| If-Else | if, else if, ternary, nested |
| Switch | case, break, fall-through, default |
| While Loop | while, do-while, patterns |
| For Loop | for syntax, nested, for-each |
| Break/Continue | break (exit), continue (skip), labeled |
| Arrays Pt 1 | 1D arrays, index, length, iterate, stats |
| Arrays Pt 2 | Search, copy, reverse, 2D, Arrays.sort |

---

## 🔑 Common Pitfalls Checklist

- [ ] Comparing Strings with `==` (use `.equals()`)
- [ ] Off-by-one in array loops (`< length` vs `<= length`)
- [ ] Forgetting `break` in switch
- [ ] Integer division when decimal is needed (cast first)
- [ ] Mixing `=` (assignment) with `==` (comparison)
- [ ] `char` to `int` gives Unicode value
- [ ] Arrays use `.length` (no parentheses); Strings use `.length()`

---

## 💻 Code Sample — Comprehensive Mini-Challenges

```java
// File: ReviewProblems.java
import java.util.Arrays;

public class ReviewProblems {
    public static void main(String[] args) {

        // Problem 1: Classify a number
        int number = 17;
        System.out.println("=== Classify " + number + " ===");
        System.out.println(number > 0 ? "Positive" : number < 0 ? "Negative" : "Zero");
        System.out.println(number % 2 == 0 ? "Even" : "Odd");

        // Problem 2: String analysis
        String phrase = "Java Programming";
        System.out.println("\n=== String Analysis ===");
        System.out.println("Length: " + phrase.length());
        System.out.println("Upper:  " + phrase.toUpperCase());
        System.out.println("First word: " + phrase.substring(0, phrase.indexOf(' ')));
        System.out.println("Contains 'gram': " + phrase.contains("gram"));

        // Problem 3: Sum of odd numbers 1–99
        int oddSum = 0;
        for (int i = 1; i <= 99; i += 2) oddSum += i;
        System.out.println("\nSum of odds 1–99: " + oddSum);

        // Problem 4: First negative in array
        int[] values = {5, 12, -3, 8, -7, 20};
        for (int val : values) {
            if (val < 0) { System.out.println("\nFirst negative: " + val); break; }
        }

        // Problem 5: 2D diagonal sum
        int[][] grid = {{1,2,3},{4,5,6},{7,8,9}};
        int diagSum = 0;
        for (int i = 0; i < grid.length; i++) diagSum += grid[i][i];
        System.out.println("Diagonal sum: " + diagSum);  // 1+5+9=15
    }
}
```

---

## ✏️ Activity 1 — Final Exam Practice Set (10 Challenges)

Implement each as a separate Java program or method:

1. Reverse a string character by character
2. Count vowels in a sentence
3. Find the second-largest number in an array
4. Print a diamond pattern using nested loops
5. Check if an array is sorted ascending
6. Compute factorial of n using a while loop
7. Print all numbers divisible by both 3 and 7 between 1–200
8. Find duplicates in an array (values that appear more than once)
9. Count words in a sentence (split on spaces)
10. Build a string of `n` asterisks using a for loop

---

## 🎯 Activity 2 — Peer Code Review

Exchange your Activity 1 solutions with a classmate and review their code for:

- [ ] Correct logic and expected output
- [ ] Proper naming conventions
- [ ] Adequate comments
- [ ] No unnecessary code duplication
- [ ] Edge case handling (empty input, zero, negative)

Write a short review note (3–5 sentences) for each solution reviewed.

---

## 📝 Quiz — Week 19 (Comprehensive)

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What is the output of `"Hello".length()`?
- A) 4
- B) 6
- C) 5 ✓
- D) 0

**2.** What is `(int) 9.9 + 1`?
- A) 10.9
- B) 11
- C) 10 ✓
- D) 9

**3.** Given `int[] arr = {3, 1, 4, 1, 5};`, what is `arr[arr.length - 1]`?
- A) 3
- B) 1
- C) 4
- D) 5 ✓

**4.** Which loop structure guarantees at least one execution of its body?
- A) for
- B) while
- C) do-while ✓
- D) for-each

**5.** What does `Arrays.sort(arr)` do to an int array?
- A) Reverses the array
- B) Sorts ascending ✓
- C) Sorts descending
- D) Returns a sorted copy

---

## ✅ Weekly Outcome

By the end of Week 19, you:
- Have reviewed every major topic in the course
- Have solved representative exam-style problems
- Can identify personal weak spots for last-minute study
- Are ready for the Final Exam
