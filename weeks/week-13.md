# Week 13 — Java While Loop

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

A **loop** runs a block of code repeatedly. The `while` loop keeps running **as long as its condition is true**. The condition is checked **before** each iteration.

### `while` Syntax

```java
while (condition) {
    // body
    // must have something that eventually makes condition false!
}
```

### `do-while` Loop

Runs the body **at least once**, then checks the condition.

```java
do {
    // runs at least once
} while (condition);
```

**Key difference:**
| Loop | When condition checked | Min runs |
|------|------------------------|----------|
| `while` | Before each iteration | 0 |
| `do-while` | After each iteration | 1 |

### Loop Structure: Init, Condition, Update

```java
int count = 0;       // Initialize
while (count < 5) {  // Condition
    System.out.println(count);
    count++;         // Update — prevents infinite loop
}
```

### Common Patterns

```java
// Count up
int i = 1;
while (i <= 10) { System.out.println(i); i++; }

// Accumulator (sum)
int sum = 0, n = 1;
while (n <= 100) { sum += n; n++; }
System.out.println("Sum: " + sum);  // 5050
```

---

## 🔑 Key Concepts

- `while` loop structure (init, condition, update)
- `do-while` and when to use it
- Infinite loop danger and prevention
- Counter patterns, accumulator patterns
- Tracing loop execution by hand

---

## 💻 Code Sample 1 — Counting, Summing, Countdown

```java
// File: WhileLoopDemo.java
public class WhileLoopDemo {
    public static void main(String[] args) {

        // Count 1 to 5
        System.out.println("=== Count 1 to 5 ===");
        int count = 1;
        while (count <= 5) {
            System.out.print(count + " ");
            count++;
        }
        System.out.println();

        // Sum 1 to 100
        int sum = 0, i = 1;
        while (i <= 100) { sum += i; i++; }
        System.out.println("\nSum 1–100 = " + sum);

        // Countdown
        System.out.println("\n=== Countdown ===");
        int rocket = 5;
        while (rocket > 0) {
            System.out.println(rocket + "...");
            rocket--;
        }
        System.out.println("Blast off!");

        // do-while: body runs even when condition is false
        System.out.println("\n=== do-while (runs once) ===");
        int x = 10;
        do {
            System.out.println("x = " + x);
            x++;
        } while (x < 10);
    }
}
```

---

## 💻 Code Sample 2 — Multiplication Table

```java
// File: MultiplicationTable.java
public class MultiplicationTable {
    public static void main(String[] args) {
        int number = 7, multiplier = 1;
        System.out.println("=== Table of " + number + " ===");
        while (multiplier <= 12) {
            System.out.printf("%d x %2d = %d%n",
                              number, multiplier, number * multiplier);
            multiplier++;
        }
    }
}
```

---

## ✏️ Activity 1 — Loop Tracing Worksheet

Trace each loop by hand. Write variable values at every iteration.

```java
// Trace A
int n = 1, total = 0;
while (n <= 5) { total = total + n; n++; }
// What are total and n when the loop ends?

// Trace B
int x = 16;
while (x > 1) { x = x / 2; System.out.println(x); }
// List the exact output lines.

// Trace C
int a = 1;
do { System.out.println(a); a *= 3; } while (a < 100);
// How many lines? What are they?
```

---

## 🎯 Activity 2 — Number Guessing Simulation

Write `GuessSimulator.java` (no user input needed):
1. Set `int secret = 42;`
2. Use a while loop starting at `guess = 1`
3. Each iteration: if `guess != secret`, print `"Trying: [guess]"` and increment
4. When found, print `"Found! Took [count] tries."`

---

## 📝 Quiz — Week 13

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** When is the condition of a `while` loop checked?
- A) After the body runs
- B) Once, at the start only
- C) Before each iteration ✓
- D) Never

**2.** What is a key difference between `while` and `do-while`?
- A) `do-while` can't be infinite
- B) `do-while` always runs the body at least once ✓
- C) `while` runs faster
- D) There is no difference

**3.** What causes an infinite loop?
- A) Missing semicolons
- B) The condition never becomes false ✓
- C) Using `++` instead of `--`
- D) A `break` inside the loop

**4.** What is the output of this loop: `int i=3; while(i>0){System.out.print(i+" "); i--;}`?
- A) `1 2 3`
- B) `3 2 1` ✓
- C) `3 3 3`
- D) Infinite

**5.** Which pattern uses a variable that accumulates a running total?
- A) Counter
- B) Flag
- C) Accumulator ✓
- D) Swap

---

## ✅ Weekly Outcome

By the end of Week 13, you can:
- Write correct while and do-while loops
- Trace loop execution step by step
- Implement counter and accumulator patterns
- Avoid infinite loops
