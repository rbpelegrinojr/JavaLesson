# Week 03 — Java Syntax

> **Course:** Introduction to Java Programming | **Level:** Beginner  
> **Lesson Duration:** 60 minutes | **Format:** Lecture + Guided Practice + Lab + Quiz

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

1. Identify and name every structural component of a Java program
2. Apply all five core syntax rules without prompting
3. Follow Java naming conventions correctly for classes, methods, variables, and constants
4. Read a short program and spot syntax errors before the compiler does
5. Write a complete, valid Java program from memory

---

## ⏱️ Lesson Timeline (60 minutes)

| Time | Segment | Duration |
|------|---------|----------|
| 0:00 – 0:05 | Warm-Up / Review Quiz | 5 min |
| 0:05 – 0:25 | Instruction — Core Syntax Rules | 20 min |
| 0:25 – 0:40 | Guided Practice — Code Walk-Through | 15 min |
| 0:40 – 0:52 | Activity — Bug Hunt & Blueprint | 12 min |
| 0:52 – 1:00 | Quiz + Wrap-Up | 8 min |

---

## 🔥 Warm-Up (0:00 – 0:05)

*Quick verbal or written check — no marks, just activation.*

Answer from memory (last week's topics):

1. What command compiles a Java file?
2. What file extension does compiled bytecode use?
3. If your class is called `HelloWorld`, what must the file be named?

*(Expected answers: `javac FileName.java` / `.class` / `HelloWorld.java`)*

---

## 📖 Instruction — Core Java Syntax Rules (0:05 – 0:25)

### What is Syntax?

**Syntax** is the complete set of rules that define what a valid Java program looks like. Every programming language has its own syntax — think of it as the *grammar* of the language. The Java **compiler** reads your source file and checks every rule before turning it into bytecode. If even one rule is broken, the compiler stops and reports an error.

> **Key idea:** Syntax errors are *your* errors, caught at compile time — not mysterious bugs that appear at runtime.

---

### Rule 1 — Every Statement Ends with a Semicolon `;`

A **statement** is one complete instruction. The semicolon tells the compiler "this instruction is finished."

```java
System.out.println("Hello, World!");   // ✅ correct
System.out.println("Hello, World!")    // ❌ missing semicolon → compile error
```

> **Analogy:** Think of the semicolon as the period at the end of a sentence. Without it, the compiler doesn't know where one sentence ends and the next begins.

**What the compiler says when you forget:**

```
SyntaxDemo.java:4: error: ';' expected
        System.out.println("Hello")
                                   ^
```

The caret `^` points to *exactly* where the problem is.

---

### Rule 2 — Code Blocks Use Curly Braces `{ }`

A **block** is a group of statements that belong together. Every class body and every method body must be wrapped in `{ }`.

```java
public class Demo {            // ← opens the class block
    public static void main(String[] args) {   // ← opens main
        System.out.println("Inside main!");
    }                          // ← closes main
}                              // ← closes class
```

**Unmatched braces are one of the most common beginner errors.** Develop the habit of always writing the closing `}` immediately after the opening `{`, then filling in the body.

| Brace | Meaning |
|-------|---------|
| `{` | Begin a code block |
| `}` | End a code block |
| Every `{` **must** have a matching `}` | |

---

### Rule 3 — Java is Case-Sensitive

The Java compiler treats uppercase and lowercase letters as completely different characters.

| Correct | Wrong | Why it fails |
|---------|-------|--------------|
| `String` | `string` | `string` is not a recognised type |
| `System.out.println` | `System.out.Println` | `Println` does not exist |
| `public` | `Public` | `Public` is not a keyword |
| `void` | `Void` | `Void` is a different class |

**Practical rule:** If IntelliJ does not auto-complete what you typed, check your capitalisation first.

---

### Rule 4 — Whitespace is Mostly Ignored

You can add any number of spaces, blank lines, or tabs between tokens. The compiler ignores them. Use whitespace to make your code readable.

```java
// These two lines are identical to the compiler:
int x=5;
int    x    =    5;

// Blank lines between methods: fine
public static void main(String[] args) {

    System.out.println("Hello!");

}
```

**Exception:** Whitespace *inside* a String literal (`"  hello  "`) is preserved exactly.

---

### Rule 5 — Every Program Needs a `main` Method

The `main` method is the **entry point** — the first line of your code the JVM executes. The signature must be *exactly*:

```java
public static void main(String[] args)
```

Each keyword has a specific meaning:

| Keyword | Meaning |
|---------|---------|
| `public` | Accessible from anywhere (the JVM needs to call it) |
| `static` | Belongs to the class, not an object (no instance needed to start) |
| `void` | Returns nothing |
| `main` | Special name recognised by the JVM as the starting point |
| `String[] args` | Optional command-line arguments passed to the program |

---

### Anatomy of a Complete Java Program

```
┌──────────────────────────────────────────────┐
│  public class ClassName {                    │  ← class declaration
│                                              │
│      public static void main(String[] args) {│  ← entry point method
│                                              │
│          // statements go here              │  ← program body
│                                              │
│      }                                       │  ← closes main
│  }                                           │  ← closes class
└──────────────────────────────────────────────┘
```

**Three nesting levels (always in this order):**  
`class` → `main method` → `statements`

---

### Naming Conventions — The Unspoken Rules

Naming conventions do **not** cause compile errors if you break them, but they are expected by every Java team in the world. Breaking them makes your code hard to read and marks you as an inexperienced developer.

| Item | Convention | Pattern | Example |
|------|------------|---------|---------|
| Class | PascalCase | First letter of every word uppercase | `StudentRecord`, `MyFirstProgram` |
| Method | camelCase | First word lowercase, rest capitalised | `calculateTotal()`, `printName()` |
| Variable | camelCase | Same as method | `firstName`, `gradeAverage` |
| Constant | UPPER_SNAKE_CASE | All caps, words separated by `_` | `MAX_SIZE`, `PI_VALUE` |
| Package | all lowercase | No capitals, words separated by `.` | `com.school.lesson` |

**How to remember PascalCase vs camelCase:**
- **PascalCase** — every word Starts With A Capital (like a proper noun)
- **camelCase** — the first word is lowercase, then each word Bumps Up like a camel's hump

---

## 🔑 Key Concepts Summary

| # | Rule | Quick Reminder |
|---|------|----------------|
| 1 | Semicolons | End every statement with `;` |
| 2 | Curly braces | Every `{` needs a matching `}` |
| 3 | Case-sensitivity | `String` ≠ `string` — capitalisation matters |
| 4 | Whitespace | Ignored by compiler; use it for readability |
| 5 | `main` method | Must match exact signature; JVM starts here |
| 6 | Naming conventions | PascalCase (class), camelCase (method/var), UPPER_SNAKE (constant) |

---

## 💻 Guided Practice — Code Walk-Through (0:25 – 0:40)

Work through each sample together as a class. Try to predict the output *before* running it.

### Code Sample 1 — All Five Rules in One Program

```java
// File: SyntaxDemo.java
// Demonstrates all 5 core syntax rules in one program.
public class SyntaxDemo {                                  // Rule 2 & 3: class block, PascalCase

    static final int MAX_LINES = 4;                       // Rule 3: UPPER_SNAKE constant
                                                           // Rule 4: blank lines ignored
    public static void main(String[] args) {               // Rule 5: entry point
        System.out.println("Rule 1: ends with semicolon.");  // Rule 1: semicolon
        System.out.println("Rule 2: inside curly braces.");
        System.out.println("Rule 3: correct capitalisation.");
        System.out.println("Rule 4: blank lines above were ignored.");
        System.out.println("Total lines printed: " + MAX_LINES);
    }                                                      // closes main
}                                                          // closes class
```

**Expected Output:**
```
Rule 1: ends with semicolon.
Rule 2: inside curly braces.
Rule 3: correct capitalisation.
Rule 4: blank lines above were ignored.
Total lines printed: 4
```

**Walk-through questions** *(answer before running)*:
1. How many `{` are there? How many `}`?
2. Which identifiers are PascalCase?
3. Which identifier is UPPER_SNAKE_CASE?
4. What would happen if you changed `MAX_LINES` to `maxLines`? (Conventions only — it still compiles)
5. What happens if you remove the `;` after `MAX_LINES = 4`?

---

### Code Sample 2 — Naming Conventions in Practice

```java
// File: NamingConventions.java
public class NamingConventions {                       // PascalCase class

    // Constant — UPPER_SNAKE_CASE
    static final int MAX_STUDENTS = 40;
    static final double PASSING_GRADE = 60.0;

    public static void main(String[] args) {           // camelCase method
        // camelCase variables
        String studentName   = "Maria Santos";
        int    studentAge    = 20;
        double gradeAverage  = 92.5;
        boolean hasScholarship = true;

        // Formatted output
        System.out.println("=== Student Profile ===");
        System.out.println("Name:        " + studentName);
        System.out.println("Age:         " + studentAge);
        System.out.println("GPA:         " + gradeAverage);
        System.out.println("Scholarship: " + hasScholarship);
        System.out.println("Class limit: " + MAX_STUDENTS);
        System.out.println("Pass mark:   " + PASSING_GRADE);
    }
}
```

**Expected Output:**
```
=== Student Profile ===
Name:        Maria Santos
Age:         20
GPA:         92.5
Scholarship: true
Class limit: 40
Pass mark:   60.0
```

**Discussion:** Without running the code, change `studentName` to `StudentName`. Does it compile? Does it follow conventions?

---

### Code Sample 3 — Reading Compiler Errors

```java
// File: BuggyProgram.java — contains 4 deliberate errors
// Can you find them all before looking at the answers?
public class BuggyProgram {
    public static void main(String[] args) {
        String message = "Hello from Java"       // Error 1
        system.out.println(message);              // Error 2
        System.out.Println("Second message");     // Error 3
        String studentName = "Juan"              // Error 4
        System.out.println(studentName)
    }
}
```

**Errors Explained:**

| Error # | Line | Problem | Fix |
|---------|------|---------|-----|
| 1 | `"Hello from Java"` | Missing `;` | Add `;` at end |
| 2 | `system` | Wrong case — `system` ≠ `System` | Change to `System` |
| 3 | `.Println` | Wrong case — `Println` ≠ `println` | Change to `println` |
| 4 | `"Juan"` | Missing `;` | Add `;` at end |

> **Instructor tip:** Show students how to read the compiler error line numbers. The error message and caret `^` will point to the exact location.

---

## ✏️ Activity — Bug Hunt & Blueprint (0:40 – 0:52)

### ✏️ Activity 1 — Bug Hunt (8 minutes)

Each program below has **one or more bugs**. For each:
- Circle / underline the error(s)
- Write what is wrong in plain English
- Rewrite the corrected version

**Program A** (2 errors):
```java
Public Class myProgram {
    public static void main(String[] args) {
        System.out.Println("Hello");
    }
}
```

*Errors:* ___________________________  
*Corrected program:*

```java
// write here
```

---

**Program B** (2 errors):
```java
public class ProgramB {
    public static void main(String[] args) {
        System.out.println("Line one")
        System.out.println("Line two")
    }
}
```

*Errors:* ___________________________  
*Corrected program:*

```java
// write here
```

---

**Program C** (2 errors):
```java
public class programC
    public static void main(String[] args) {
        System.out.println("Where is the brace?");
    }
}
```

*Errors:* ___________________________  
*Corrected program:*

```java
// write here
```

---

**Program D** (3 errors — challenge):
```java
public class GradeReport {
    static final int passingScore = 60;

    Public static void main(String[] args) {
        int studentGrade = 85
        System.out.println("Grade: " + studentGrade);
    }
}
```

*Errors:* ___________________________  
*Corrected program:*

```java
// write here
```

---

### 🎯 Activity 2 — Blueprint Challenge (4 minutes)

Write a Java program **from scratch** (no copy-paste) that:

1. Has a class named `MyProfile`
2. Declares a `final` constant `SCHOOL_YEAR` equal to `2026`
3. Uses three `camelCase` variables: `fullName` (your name), `courseName` (your course), `yearLevel` (an int)
4. Prints a formatted profile card:
   ```
   ============================
        MY STUDENT PROFILE
   ============================
   Name   : [fullName]
   Course : [courseName]
   Year   : [yearLevel]
   S.Y.   : [SCHOOL_YEAR]
   ============================
   ```
5. Compiles and runs without errors

---

## 📝 Quiz — Week 03 (0:52 – 1:00)

**Name:** __________________________ **Score:** _____ / 20

**Instructions:** Choose the **best** answer. (2 points each)

---

**1.** What character terminates a Java statement?
- A) Colon `:`
- B) Period `.`
- C) Semicolon `;` ✓
- D) Comma `,`

---

**2.** Which class name follows Java naming conventions?
- A) `myclass`
- B) `my_class`
- C) `MyClass` ✓
- D) `MY_CLASS`

---

**3.** Java is:
- A) Case-insensitive
- B) Case-sensitive ✓
- C) Only case-sensitive for class names
- D) None of the above

---

**4.** Which of the following is a correctly named constant?
- A) `maxSize`
- B) `MaxSize`
- C) `max-size`
- D) `MAX_SIZE` ✓

---

**5.** What defines a code block in Java?
- A) Square brackets `[ ]`
- B) Parentheses `( )`
- C) Curly braces `{ }` ✓
- D) Angle brackets `< >`

---

**6.** What is the correct signature for the Java program entry point?
- A) `public void main()`
- B) `static main(String[] args)`
- C) `public static void main(String[] args)` ✓
- D) `void static public Main(String args)`

---

**7.** Which of the following variable names follows Java conventions?
- A) `FirstName`
- B) `first_name`
- C) `firstName` ✓
- D) `FIRSTNAME`

---

**8.** Look at this code: `System.out.Println("Hi");`  
What is wrong?
- A) Missing semicolon
- B) `Println` should be `println` — wrong capitalisation ✓
- C) `System` should be `system`
- D) Missing curly braces

---

**9.** Which statement is true about whitespace in Java?
- A) All whitespace causes compile errors
- B) Whitespace inside String literals is ignored
- C) Whitespace between tokens is ignored by the compiler ✓
- D) You cannot have blank lines in a Java file

---

**10.** A student writes: `public class studentProfile { ... }`  
What is wrong with this class declaration?
- A) Missing semicolon after `}`
- B) `studentProfile` should be `StudentProfile` — naming convention violated ✓
- C) `public` should be `Public`
- D) Nothing is wrong

---

## 📋 Answer Key

| Q | Answer | Rule Tested |
|---|--------|-------------|
| 1 | C | Semicolons |
| 2 | C | PascalCase for classes |
| 3 | B | Case-sensitivity |
| 4 | D | UPPER_SNAKE constant |
| 5 | C | Curly braces |
| 6 | C | main signature |
| 7 | C | camelCase for variables |
| 8 | B | Case-sensitivity |
| 9 | C | Whitespace |
| 10 | B | PascalCase for classes |

---

## 🔄 Wrap-Up (last 2 minutes)

**Three things to remember:**

1. 🔴 **Semicolons** — end every statement; missing one stops compilation
2. 🟡 **Braces** — every `{` needs a `}`; mismatch is the #1 beginner error
3. 🟢 **Case** — Java is case-sensitive everywhere; conventions keep code professional

**Preview of Week 4:** We'll dive deeper into output — `print` vs `println` vs `printf`, escape sequences, and how to add meaningful comments to your code.

---

## ✅ Weekly Outcome

By the end of Week 3, you can:
- Identify and correct all common syntax errors
- Name every structural layer of a Java program
- Follow Java naming conventions for classes, methods, variables, and constants
- Write a complete, valid Java program from scratch without syntax errors
