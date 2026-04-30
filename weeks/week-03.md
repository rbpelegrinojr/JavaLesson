# Week 03 — Java Syntax

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

**Syntax** is the set of rules that defines how a Java program must be written. Breaking a syntax rule causes a compile error.

**Core syntax rules:**

1. **Every statement ends with a semicolon (`;`)**
2. **Code blocks use curly braces `{ }`**
3. **Java is case-sensitive** (`String` ≠ `string`)
4. **Whitespace is mostly ignored** (except inside strings)
5. **Every program needs a `main` method**

**Anatomy of a Java program:**
```
public class ClassName {
    public static void main(String[] args) {
        // statements go here
    }
}
```

**Naming conventions (always follow these):**

| Item | Convention | Example |
|------|------------|---------|
| Class | PascalCase | `StudentRecord` |
| Method | camelCase | `calculateTotal()` |
| Variable | camelCase | `firstName` |
| Constant | UPPER_SNAKE_CASE | `MAX_SIZE` |

---

## 🔑 Key Concepts

- Semicolons as statement terminators
- Curly braces to define code blocks
- Case sensitivity in Java
- Naming conventions (PascalCase, camelCase, UPPER_SNAKE_CASE)
- Structure: class → method → statements

---

## 💻 Code Sample 1 — Syntax in Action

```java
// File: SyntaxDemo.java
public class SyntaxDemo {
    public static void main(String[] args) {
        System.out.println("Line 1: Java syntax is strict.");
        System.out.println("Line 2: Every statement ends with a semicolon.");
        System.out.println("Line 3: Curly braces define code blocks.");
        System.out.println("Line 4: Blank lines are ignored by the compiler.");
    }
}
```

**Expected Output:**
```
Line 1: Java syntax is strict.
Line 2: Every statement ends with a semicolon.
Line 3: Curly braces define code blocks.
Line 4: Blank lines are ignored by the compiler.
```

---

## 💻 Code Sample 2 — Naming Conventions

```java
// File: NamingConventions.java
public class NamingConventions {
    static final int MAX_STUDENTS = 40;   // UPPER_SNAKE_CASE constant

    public static void main(String[] args) {
        String studentName = "Maria Santos"; // camelCase variable
        int   studentAge   = 20;
        double gradeAverage = 92.5;

        System.out.println("Student: "  + studentName);
        System.out.println("Age: "      + studentAge);
        System.out.println("Average: "  + gradeAverage);
        System.out.println("Max size: " + MAX_STUDENTS);
    }
}
```

---

## ✏️ Activity 1 — Syntax Correction Worksheet

Rewrite each broken program so it compiles. Explain what was wrong.

```java
// Program A
Public Class myProgram {
    public static void main(String[] args) {
        System.out.Println("Hello");
    }
}

// Program B
public class ProgramB {
    public static void main(String[] args) {
        System.out.println("Line one")
        System.out.println("Line two")
    }
}

// Program C
public class ProgramC
    public static void main(String[] args) {
        System.out.println("Where is the brace?");
    }
```

---

## 🎯 Activity 2 — Structure Blueprint Challenge

Write a Java program *from scratch* (no copy-paste) that:
1. Has a class named `MyProfile`
2. Prints your name, city, and favourite hobby on separate lines
3. Uses correct naming conventions for any variables
4. Compiles and runs without errors

---

## 📝 Quiz — Week 03

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What character terminates a Java statement?
- A) Colon `:`
- B) Period `.`
- C) Semicolon `;` ✓
- D) Comma `,`

**2.** Which is the correct naming style for a Java class?
- A) `myclass`
- B) `my_class`
- C) `MyClass` ✓
- D) `MY_CLASS`

**3.** Java is:
- A) Case-insensitive
- B) Case-sensitive ✓
- C) Only case-sensitive for class names
- D) None of the above

**4.** Which of these is a valid constant name?
- A) `maxSize`
- B) `MaxSize`
- C) `max-size`
- D) `MAX_SIZE` ✓

**5.** What defines a code block in Java?
- A) Square brackets `[ ]`
- B) Parentheses `( )`
- C) Curly braces `{ }` ✓
- D) Angle brackets `< >`

---

## ✅ Weekly Outcome

By the end of Week 3, you can:
- Identify and correct common syntax errors
- Follow Java naming conventions
- Explain each structural component of a Java program
