# Week 18 — Arrays Mini-Project & Integration

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

This week is **integration week** — combining everything learned so far into a meaningful mini-project.

**Topics Combined:**
- Variables and data types (Weeks 5–6)
- Operators and type casting (Weeks 7–8)
- If-else and switch (Weeks 11–12)
- While and for loops (Weeks 13–14)
- Break/continue (Week 15)
- Arrays Part 1 & 2 (Weeks 16–17)

### Program Design Checklist

When writing a complete program, ask:
1. What data do I need? → choose variables / arrays
2. What decisions does the program make? → if-else / switch
3. What repetition is needed? → for / while
4. What output format is expected? → printf / println
5. Are there edge cases? → empty array, zero, negative

---

## 🔑 Key Concepts (Review)

- Combining arrays, loops, and conditions
- Designing a complete program from scratch
- Clean code organization and commenting
- Edge case handling

---

## 💻 Code Sample — Student Grade Management System

```java
// File: GradeManagement.java
// Integrates: arrays, loops, conditionals, formatted output.
public class GradeManagement {
    public static void main(String[] args) {

        String[] students = {
            "Ana Reyes", "Ben Santos", "Carla Lim", "Dan Cruz",
            "Eva Torres", "Felix Ong", "Grace Tan", "Henry Sy"
        };
        int[] scores = {88, 72, 95, 61, 84, 57, 90, 79};

        System.out.println("=".repeat(55));
        System.out.println("         STUDENT GRADE REPORT");
        System.out.println("=".repeat(55));
        System.out.printf("%-20s %-8s %-12s %s%n",
                          "Name", "Score", "Grade", "Status");
        System.out.println("-".repeat(55));

        int total = 0, highest = scores[0], lowest = scores[0];
        String topStudent = students[0];
        int passCount = 0, failCount = 0;

        for (int i = 0; i < students.length; i++) {
            int s = scores[i];
            total += s;
            if (s > highest) { highest = s; topStudent = students[i]; }
            if (s < lowest)    lowest = s;

            String grade;
            if      (s >= 90) grade = "A";
            else if (s >= 80) grade = "B";
            else if (s >= 70) grade = "C";
            else if (s >= 60) grade = "D";
            else              grade = "F";

            String status = (s >= 60) ? "PASSED" : "FAILED";
            if (s >= 60) passCount++; else failCount++;

            System.out.printf("%-20s %-8d %-12s %s%n",
                              students[i], s, grade, status);
        }

        System.out.println("=".repeat(55));
        System.out.printf("Students: %d | Passed: %d | Failed: %d%n",
                           students.length, passCount, failCount);
        System.out.printf("Average: %.2f  |  High: %d (%s)  |  Low: %d%n",
                           (double) total / students.length, highest,
                           topStudent, lowest);
        System.out.println("=".repeat(55));
    }
}
```

---

## ✏️ Activity 1 — Extend the Grade System

Extend `GradeManagement.java`:
1. Add a second array for a second exam; compute `finalScore = (exam1 + exam2) / 2`
2. Sort students by final score (descending) using a simple nested loop (bubble sort)
3. Print rank numbers (1st, 2nd, …) in the report

---

## 🎯 Activity 2 — Inventory System

Write `Inventory.java` managing a product inventory:
- Arrays for: product names (String), quantities (int), prices (double)
- At least 6 products
- Print a formatted inventory table
- Calculate total inventory value for each item and sum all
- Find most and least expensive products
- List all products with quantity < 5 (low stock warning)

---

## 📝 Quiz — Week 18

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What should you do FIRST when designing a new program?
- A) Start coding immediately
- B) Understand what data and operations are needed ✓
- C) Write comments only
- D) Import all libraries

**2.** Which code computes the total of an int array named `vals`?
- A) `int sum = vals;`
- B) `int sum = 0; for (int v : vals) sum += v;` ✓
- C) `int sum = vals.sum();`
- D) `int sum = Arrays.total(vals);`

**3.** A bubble sort compares adjacent elements and swaps them. How many outer loop passes are needed for an array of `n` elements?
- A) 1
- B) n/2
- C) n-1 ✓
- D) n²

**4.** What is an "edge case"?
- A) A case that is always handled correctly
- B) An unusual or boundary input that could cause incorrect behavior ✓
- C) A case at the end of a switch
- D) An exception in the JVM

**5.** Which `printf` format prints a String left-aligned in 15 characters?
- A) `%15s`
- B) `%-15s` ✓
- C) `%s15`
- D) `%+15s`

---

## ✅ Weekly Outcome

By the end of Week 18, you can:
- Build a complete multi-array program
- Apply all control flow and array operations in an integrated context
- Produce clean formatted output
- Handle common edge cases
