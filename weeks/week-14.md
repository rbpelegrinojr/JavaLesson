# Week 14 — Java For Loop

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

The `for` loop is ideal when you **know in advance how many times** the loop should run. All three control parts are on one line.

### Syntax

```java
for (initialization; condition; update) {
    // body
}
```

| Part | Runs When | Example |
|------|-----------|---------|
| `initialization` | Once, at start | `int i = 0` |
| `condition` | Before each iteration | `i < 10` |
| `update` | After each iteration | `i++` |

### `for` vs `while`

```java
// for loop
for (int i = 0; i < 5; i++) { System.out.println(i); }

// Equivalent while
int i = 0;
while (i < 5) { System.out.println(i); i++; }
```

Use **`for`** when you know the exact count. Use **`while`** when you don't.

### Custom Step Sizes

```java
for (int i = 0; i <= 20; i += 2)   // even numbers
for (int i = 10; i >= 1; i--)      // countdown
for (int i = 1; i <= 1024; i *= 2) // powers of 2
```

### Nested `for` Loops

```java
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= 3; col++) {
        System.out.print("(" + row + "," + col + ") ");
    }
    System.out.println();
}
```

### Enhanced For-Each (Preview)

```java
int[] numbers = {10, 20, 30};
for (int num : numbers) {
    System.out.println(num);
}
```

---

## 🔑 Key Concepts

- For loop three-part structure
- `for` vs `while` — when to use each
- Custom step sizes
- Nested for loops and 2D patterns
- Enhanced for-each loop

---

## 💻 Code Sample 1 — For Loop Patterns

```java
// File: ForLoopDemo.java
public class ForLoopDemo {
    public static void main(String[] args) {

        // 1 to 10
        System.out.println("=== 1 to 10 ===");
        for (int i = 1; i <= 10; i++) System.out.print(i + " ");
        System.out.println();

        // Even numbers 2–20
        System.out.println("\n=== Evens 2–20 ===");
        for (int i = 2; i <= 20; i += 2) System.out.print(i + " ");
        System.out.println();

        // Countdown
        System.out.println("\n=== Countdown ===");
        for (int i = 10; i >= 1; i--) System.out.print(i + " ");
        System.out.println();

        // Powers of 2
        System.out.println("\n=== Powers of 2 ===");
        for (int i = 1; i <= 1024; i *= 2) System.out.print(i + " ");
        System.out.println();

        // Sum of first 10 numbers
        int sum = 0;
        for (int i = 1; i <= 10; i++) sum += i;
        System.out.println("\nSum 1–10 = " + sum);
    }
}
```

---

## 💻 Code Sample 2 — Nested Loops (Star Pattern & Table)

```java
// File: StarPattern.java
public class StarPattern {
    public static void main(String[] args) {

        // Right triangle
        System.out.println("=== Right Triangle ===");
        for (int row = 1; row <= 5; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // Multiplication table 5×5
        System.out.println("\n=== Multiplication Table 5x5 ===");
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 5; j++) {
                System.out.printf("%4d", i * j);
            }
            System.out.println();
        }
    }
}
```

---

## ✏️ Activity 1 — Pattern Drawing Lab

Write `PatternDraw.java` using nested for loops for each:

```
Pattern A:          Pattern B (inverted): Pattern C (numbers):
* * * * *           * * * * *             1
* * * * *           * * * *               1 2
* * * * *           * * *                 1 2 3
* * * * *           * *                   1 2 3 4
* * * * *           *                     1 2 3 4 5
```

---

## 🎯 Activity 2 — FizzBuzz (1–50)

Write `FizzBuzz.java` using a for loop (1–50):
- Print `Fizz` if divisible by 3
- Print `Buzz` if divisible by 5
- Print `FizzBuzz` if divisible by both
- Otherwise print the number

(Hint: Check FizzBuzz **before** Fizz or Buzz)

---

## 📝 Quiz — Week 14

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** In `for (int i = 0; i < 5; i++)`, how many times does the body run?
- A) 4
- B) 5 ✓
- C) 6
- D) 0

**2.** Which part of the for loop runs AFTER each iteration?
- A) Initialization
- B) Condition
- C) Update ✓
- D) Body

**3.** What does `for (int i = 0; i <= 10; i += 3)` print first?
- A) 1
- B) 3
- C) 0 ✓
- D) 10

**4.** What is `for (;;)` ?
- A) A compile error
- B) An infinite loop ✓
- C) A loop that runs once
- D) A for-each loop

**5.** In a nested for loop with outer 3 iterations and inner 4 iterations, how many total body executions?
- A) 7
- B) 3
- C) 4
- D) 12 ✓

---

## ✅ Weekly Outcome

By the end of Week 14, you can:
- Write for loops with custom step sizes
- Use nested for loops for 2D patterns
- Explain when to use for vs while
- Solve classic problems like FizzBuzz
