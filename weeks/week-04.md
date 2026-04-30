# Week 04 — Java Output & Comments

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

**Output** is how a Java program communicates results to the user via the console.

### Output Methods

| Method | Behaviour |
|--------|-----------|
| `System.out.println(x)` | Prints `x` then moves to a **new line** |
| `System.out.print(x)` | Prints `x` **without** a new line |
| `System.out.printf(format, args)` | **Formatted** output |

### printf Format Specifiers

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `%d` | Integer | `printf("%d", 42)` → `42` |
| `%f` | Float | `printf("%.2f", 3.14)` → `3.14` |
| `%s` | String | `printf("%s", "hi")` → `hi` |
| `%n` | New line | `printf("a%nb")` |
| `%c` | Character | `printf("%c", 'A')` → `A` |

### Escape Sequences

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |

### Comments

| Type | Syntax | Use |
|------|--------|-----|
| Single-line | `// text` | Brief notes |
| Multi-line | `/* text */` | Longer explanations |
| Javadoc | `/** text */` | Official documentation |

**Good commenting habits:** Comment *why* you did something, not *what* (the code already shows what).

---

## 🔑 Key Concepts

- `println` vs `print` vs `printf`
- Escape sequences
- Format specifiers for `printf`
- Single-line, multi-line, and Javadoc comments
- Why meaningful comments matter

---

## 💻 Code Sample 1 — Three Output Methods

```java
// File: OutputDemo.java
public class OutputDemo {
    public static void main(String[] args) {

        // println: new line after each call
        System.out.println("First line");
        System.out.println("Second line");

        // print: stays on same line
        System.out.print("A");
        System.out.print("B");
        System.out.print("C");
        System.out.println();  // just a newline

        // printf: formatted output
        String name = "Juan";
        int age = 19;
        double gpa = 3.75;
        System.out.printf("Name: %s%n", name);
        System.out.printf("Age:  %d%n", age);
        System.out.printf("GPA:  %.2f%n", gpa);
    }
}
```

**Expected Output:**
```
First line
Second line
ABC
Name: Juan
Age:  19
GPA:  3.75
```

---

## 💻 Code Sample 2 — Escape Sequences & Comments

```java
// File: EscapeAndComments.java
/**
 * Demonstrates escape sequences and all three comment types.
 */
public class EscapeAndComments {
    public static void main(String[] args) {

        // Escape sequences
        System.out.println("She said, \"Java is fun!\"");
        System.out.println("Path: C:\\Users\\Student");
        System.out.println("Col1\tCol2\tCol3");

        /*
         * Multi-line comment:
         * The next line prints a farewell.
         */
        System.out.println("Goodbye!");
    }
}
```

---

## ✏️ Activity 1 — Output Formatting Lab

Write `StudentCard.java` that prints a formatted student record card using `printf`:
```
=============================
       STUDENT RECORD
=============================
Name    : [Your Name]
ID No.  : [Your ID]
Course  : BS Computer Science
GPA     : 1.75
=============================
```
Use at least one `printf` with a `%` format specifier for the GPA.

---

## 🎯 Activity 2 — Comment the Code

Add meaningful comments to every line/section of this program:

```java
public class Unannotated {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        int sum = a + b;
        int diff = a - b;
        int product = a * b;
        double quotient = (double) a / b;
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + diff);
        System.out.println("Product: " + product);
        System.out.printf("Quotient: %.4f%n", quotient);
    }
}
```

---

## 📝 Quiz — Week 04

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** Which method prints text AND moves to a new line?
- A) `System.out.print()`
- B) `System.out.printf()`
- C) `System.out.println()` ✓
- D) `System.out.write()`

**2.** What does `\t` represent in a String?
- A) Newline
- B) Tab ✓
- C) Backslash
- D) Quote

**3.** Which format specifier prints a decimal number?
- A) `%s`
- B) `%c`
- C) `%d` ✓
- D) `%b`

**4.** Which comment style generates API documentation?
- A) `// comment`
- B) `/* comment */`
- C) `/** comment */` ✓
- D) `## comment`

**5.** What is the output of: `System.out.printf("%.1f", 3.567);`
- A) `3.567`
- B) `3.6` ✓
- C) `3.5`
- D) `4.0`

---

## ✅ Weekly Outcome

By the end of Week 4, you can:
- Use `println`, `print`, and `printf` correctly
- Apply escape sequences in strings
- Write meaningful single-line, multi-line, and Javadoc comments
