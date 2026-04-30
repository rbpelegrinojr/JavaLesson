# Week 15 — Java Break / Continue

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

`break` and `continue` change the normal flow of a loop.

### `break` — Exit the Loop

Immediately **exits** the loop (or switch). No further iterations run.

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) break;
    System.out.print(i + " ");  // prints: 1 2 3 4
}
```

### `continue` — Skip This Iteration

**Skips** the rest of the current iteration and jumps to the next.

```java
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;   // skip even numbers
    System.out.print(i + " ");   // prints: 1 3 5 7 9
}
```

### Labeled Break (for nested loops)

```java
outer:
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (j == 2) break outer;  // breaks BOTH loops
        System.out.println("i=" + i + " j=" + j);
    }
}
```

### When to Use Each

| Statement | Best Use |
|-----------|----------|
| `break` | Search (stop when found), menu exit, error condition |
| `continue` | Filtering (skip unwanted elements) |

### Linear Search Pattern with `break`

```java
int[] data = {5, 12, 8, 99, 3};
int target = 99;
int foundAt = -1;

for (int i = 0; i < data.length; i++) {
    if (data[i] == target) { foundAt = i; break; }
}
System.out.println("Found at: " + foundAt);
```

---

## 🔑 Key Concepts

- `break` to exit a loop early
- `continue` to skip an iteration
- Labeled break for nested loops
- Search pattern with `break`
- Filter pattern with `continue`

---

## 💻 Code Sample — Break and Continue

```java
// File: BreakContinueDemo.java
public class BreakContinueDemo {
    public static void main(String[] args) {

        // break: stop at 6
        System.out.println("=== break at 6 ===");
        for (int i = 0; i < 10; i++) {
            if (i == 6) { System.out.println("Breaking!"); break; }
            System.out.print(i + " ");
        }
        System.out.println();

        // continue: skip multiples of 3
        System.out.println("\n=== skip multiples of 3 ===");
        for (int i = 1; i <= 15; i++) {
            if (i % 3 == 0) continue;
            System.out.print(i + " ");
        }
        System.out.println();

        // break in while: stop sum when > 50
        System.out.println("\n=== sum until > 50 ===");
        int sum = 0, n = 1;
        while (true) {
            sum += n;
            if (sum > 50) {
                System.out.printf("Exceeded 50 at n=%d, sum=%d%n", n, sum);
                break;
            }
            n++;
        }

        // labeled break
        System.out.println("\n=== labeled break ===");
        outer:
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                if (i == 2 && j == 3) {
                    System.out.println("Breaking at (" + i + "," + j + ")");
                    break outer;
                }
                System.out.print("(" + i + "," + j + ") ");
            }
            System.out.println();
        }
    }
}
```

---

## ✏️ Activity 1 — Loop Tracing with Break/Continue

Trace and write the exact output:

```java
// Trace A
for (int i = 1; i <= 10; i++) {
    if (i == 3 || i == 7) continue;
    System.out.print(i + " ");
}

// Trace B
int i = 0;
while (i < 20) {
    i += 3;
    if (i > 12) break;
    System.out.println(i);
}

// Trace C
for (int a = 1; a <= 3; a++) {
    for (int b = 1; b <= 3; b++) {
        if (b == a) continue;
        System.out.println(a + " " + b);
    }
}
```

---

## 🎯 Activity 2 — Prime Number Finder

Write `PrimeFinder.java` printing all primes from 2 to 50:
- Outer loop: numbers 2–50
- Inner loop: check divisibility
- Use `break` when a divisor is found
- Use a flag or `continue` to skip non-primes

Expected start: `2 3 5 7 11 13 17 19 23…`

---

## 📝 Quiz — Week 15

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What does `break` do inside a loop?
- A) Skips the current iteration
- B) Restarts the loop
- C) Exits the loop immediately ✓
- D) Goes to the next loop

**2.** What does `continue` do?
- A) Exits the loop
- B) Skips to the next iteration ✓
- C) Pauses execution
- D) Resets the loop counter

**3.** Which statement is true about a labeled break?
- A) It only works in for loops
- B) It can break out of multiple nested loops ✓
- C) It is required in all nested loops
- D) It causes a compile error

**4.** For searching an array, which statement is most useful after finding the target?
- A) `continue`
- B) `return`
- C) `break` ✓
- D) `exit`

**5.** What is the output of: `for(int i=1;i<=5;i++){if(i==3)continue; System.out.print(i+" ");}`
- A) `1 2 3 4 5`
- B) `1 2 4 5` ✓
- C) `1 2`
- D) `3 4 5`

---

## ✅ Weekly Outcome

By the end of Week 15, you can:
- Use `break` to exit loops early
- Use `continue` to skip iterations
- Implement linear search with `break`
- Explain labeled breaks for nested loops
