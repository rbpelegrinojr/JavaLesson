# Week 20 — Final Exam Week

> **Course:** Introduction to Java Programming | **Level:** Beginner  
> 🏆 **FINAL EXAM THIS WEEK**

---

## 📖 Lesson — Final Review

No new material this week. Focus on:
- Re-reading code samples from difficult weeks
- Tracing programs on paper (no IDE)
- Fixing your common pitfalls list

### Common Final Exam Pitfalls

1. Comparing Strings with `==` instead of `.equals()`
2. Off-by-one errors in array loops
3. Forgetting `break` in switch
4. Integer division when decimal is needed — cast first
5. Using `=` (assignment) instead of `==` (comparison) in conditions
6. Forgetting `char` → `int` gives Unicode value, not a digit
7. Calling `.length()` on arrays (arrays use `.length` — no parentheses)
8. Modifying loop counter inside the loop body (unintended behaviour)

---

## 📋 Final Exam Coverage

| Category | Topics | Weight |
|----------|--------|--------|
| Foundations | Syntax, Output, Variables, Types, Casting | 20% |
| Operators & Logic | Operators, Booleans | 10% |
| Strings & Math | String methods, Math class | 15% |
| Control Flow | If-Else, Switch | 20% |
| Loops | While, For, Break/Continue | 20% |
| Arrays | 1D & 2D, Algorithms | 15% |

---

## 💻 Final Exam Sample Problems

```java
// --- Question 1 (10 pts) ---
// Write code that counts the even numbers in an int array
// and prints the count.
// Example: {2, 5, 8, 3, 10} → 3 even numbers

// --- Question 2 (15 pts) ---
// Given String sentence = "Hello World from Java";
// a) Print the number of characters
// b) Print the number of uppercase letters
// c) Replace spaces with underscores and print

// --- Question 3 (20 pts) ---
// Find all pairs of numbers in an array whose sum equals a target.
// array = {2, 7, 11, 15, 3, 6}, target = 9
// Output: Pair found: (2, 7) and (3, 6)

// --- Question 4 (25 pts) ---
// 5 students, 3 test scores each (2D array).
// Print a formatted table: names, scores, average, pass/fail.
// Print the overall class average.

// --- Question 5 (30 pts) ---
// String[] words = {"apple","banana","cherry","fig","kiwi","mango","date","pear"};
// a) Print them in reverse order
// b) Count words with more than 4 letters
// c) Print words starting with a vowel (a, e, i, o, u)
// d) Join all words with commas into one String and print
```

---

## 💻 Code Sample — Final Exam Reference Solutions

```java
// File: FinalExamSolutions.java
public class FinalExamSolutions {
    public static void main(String[] args) {

        // Q1: Count even numbers
        int[] arr = {2, 5, 8, 3, 10};
        int evenCount = 0;
        for (int v : arr) if (v % 2 == 0) evenCount++;
        System.out.println("Even count: " + evenCount);   // 3

        // Q2: String analysis
        String sentence = "Hello World from Java";
        System.out.println("Length: " + sentence.length());

        int upperCount = 0;
        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            if (c >= 'A' && c <= 'Z') upperCount++;
        }
        System.out.println("Uppercase letters: " + upperCount);
        System.out.println("Underscored: " + sentence.replace(" ", "_"));

        // Q5: Word operations
        String[] words = {"apple","banana","cherry","fig","kiwi","mango","date","pear"};

        System.out.print("Reversed: ");
        for (int i = words.length - 1; i >= 0; i--) System.out.print(words[i] + " ");
        System.out.println();

        int longWords = 0;
        for (String w : words) if (w.length() > 4) longWords++;
        System.out.println("Words > 4 chars: " + longWords);

        System.out.print("Starts with vowel: ");
        for (String w : words) {
            char first = Character.toLowerCase(w.charAt(0));
            if ("aeiou".indexOf(first) >= 0) System.out.print(w + " ");
        }
        System.out.println();

        String joined = String.join(", ", words);
        System.out.println("Joined: " + joined);
    }
}
```

---

## ✏️ Activity 1 — Final Exam Simulation

**Timed: 120 minutes | Closed-book | Total: 100 points**

Attempt the 5 Sample Problems above:
1. Write solutions on paper first (no IDE)
2. Type them into your IDE and verify
3. Fix any errors and understand why they occurred

---

## 🎯 Activity 2 — Portfolio Reflection

After the exam, write a 1-page reflection:
1. What was the most challenging topic? Why?
2. Which topic are you most confident about?
3. How has your understanding of programming changed since Week 1?
4. What would you do differently if starting the course again?
5. What Java topic do you most want to learn next?

---

## 📝 Quiz — Week 20 (Final Comprehensive)

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What is the output of `System.out.println((int) 9.99 + 1)`?
- A) 10.99
- B) 11
- C) 10 ✓
- D) 9

**2.** Which correctly compares two String objects `s1` and `s2`?
- A) `s1 == s2`
- B) `s1.equals(s2)` ✓
- C) `s1 = s2`
- D) `compare(s1, s2)`

**3.** What does `arr.length` give for `int[] arr = {1,2,3,4,5}`?
- A) 4
- B) 5 ✓
- C) 6
- D) `arr.length()`

**4.** Which statement prints only the ODD numbers from 1 to 10?
- A) `for(int i=1;i<=10;i++) if(i%2==0) System.out.println(i);`
- B) `for(int i=1;i<=10;i+=2) System.out.println(i);` ✓
- C) `for(int i=2;i<=10;i++) System.out.println(i);`
- D) `for(int i=1;i<=10;i++) System.out.println(i%2);`

**5.** What is `matrix[1][0]` if `matrix = {{1,2},{3,4},{5,6}}`?
- A) 2
- B) 1
- C) 4
- D) 3 ✓

---

## ✅ Course Completion Outcome

By the end of Week 20, you have:
- Demonstrated mastery of introductory Java from syntax through arrays
- Written complete Java programs integrating multiple concepts
- Developed problem-solving habits (trace first, code second)
- Built a foundation for intermediate Java (OOP, collections, files)

---

## 🏆 FINAL EXAM

**Coverage:** Weeks 1–19 (Full Course)  
**Topics:** Java Intro through Arrays  
**Format:** Written + practical coding exam

---

## 📊 Final Grade Distribution

| Component | Weight |
|-----------|--------|
| Weekly Activities (2/wk × 18 active weeks) | 40% |
| Midterm Exam (Week 10) | 25% |
| Final Exam (Week 20) | 35% |
| **Total** | **100%** |
