# 🎓 20-Week Java Lesson Plan (Introductory Level)

> **Course:** Introduction to Java Programming  
> **Duration:** 20 Weeks (Midterm at Week 10, Final at Week 20)  
> **Level:** Beginner / Introductory  
> **Prerequisites:** Basic computer literacy; no prior programming experience required

---

## 📋 Table of Contents

| Week | Topic | Milestone |
|------|-------|-----------|
| [Week 01](#week-01--java-introduction) | Java Introduction | — |
| [Week 02](#week-02--java-get-started) | Java Get Started | — |
| [Week 03](#week-03--java-syntax) | Java Syntax | — |
| [Week 04](#week-04--java-output--comments) | Java Output & Comments | — |
| [Week 05](#week-05--java-variables) | Java Variables | — |
| [Week 06](#week-06--java-data-types) | Java Data Types | — |
| [Week 07](#week-07--java-type-casting) | Java Type Casting | — |
| [Week 08](#week-08--java-operators) | Java Operators | — |
| [Week 09](#week-09--java-strings--java-math) | Java Strings & Java Math | — |
| [Week 10](#week-10--java-booleans--midterm-review) | Java Booleans + **MIDTERM** | 🏆 Midterm Exam |
| [Week 11](#week-11--java-ifelse) | Java If…Else | — |
| [Week 12](#week-12--java-switch) | Java Switch | — |
| [Week 13](#week-13--java-while-loop) | Java While Loop | — |
| [Week 14](#week-14--java-for-loop) | Java For Loop | — |
| [Week 15](#week-15--java-breakcontinue) | Java Break / Continue | — |
| [Week 16](#week-16--java-arrays-part-1) | Java Arrays — Part 1 | — |
| [Week 17](#week-17--java-arrays-part-2) | Java Arrays — Part 2 | — |
| [Week 18](#week-18--arrays-mini-project--integration) | Arrays Mini-Project & Integration | — |
| [Week 19](#week-19--comprehensive-review) | Comprehensive Review | — |
| [Week 20](#week-20--final-exam-week) | **FINAL EXAM** | 🏆 Final Exam |

---

## 📌 Legend

- 📖 **Lesson** — Core teaching content
- 🔑 **Key Concepts** — Must-know terms and ideas
- 💻 **Code Sample** — Working Java code for students to study and run
- ✏️ **Activity 1** — First hands-on activity (lab, drill, or worksheet)
- 🎯 **Activity 2** — Second hands-on activity (quiz, mini-project, or challenge)
- ✅ **Weekly Outcome** — What a student should be able to do by the end of the week

---

## Week 01 — Java Introduction

### 📖 Lesson

Java is one of the most popular programming languages in the world. It was created by **James Gosling** at Sun Microsystems in **1995** and is now owned by Oracle. Java follows the principle of **"Write Once, Run Anywhere"** — meaning code written on one machine can run on any machine that has Java installed.

**Why learn Java?**
- Used in Android app development, web back-ends, enterprise software, and games
- Object-oriented from the ground up
- Strongly typed, which helps beginners learn disciplined coding habits
- Huge community and job market demand

**Java's three-layer architecture:**

| Layer | Full Name | Role |
|-------|-----------|------|
| JDK | Java Development Kit | Tools to *write and compile* Java programs (includes JRE + compiler) |
| JRE | Java Runtime Environment | Libraries needed to *run* Java programs |
| JVM | Java Virtual Machine | The engine that *executes* Java bytecode on your specific OS |

When you write `Hello.java`, the **compiler** (part of JDK) turns it into `Hello.class` (bytecode). The **JVM** (part of JRE) reads and runs that bytecode on your machine.

### 🔑 Key Concepts
- Java language history and use cases
- JDK vs JRE vs JVM distinction
- What "platform independence" means
- Difference between compiled vs interpreted languages (briefly)

### 💻 Code Sample — Your Very First Java Program

```java
// File: HelloWorld.java
// This is the classic "Hello, World!" program in Java.

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Expected Output:**
```
Hello, World!
```

**Line-by-line explanation:**
- `public class HelloWorld` — Every Java program lives inside a **class**. The class name must match the filename.
- `public static void main(String[] args)` — This is the **entry point**. Java always starts executing here.
- `System.out.println(...)` — Prints text to the console followed by a new line.
- `"Hello, World!"` — A **String literal** (text in double quotes).

### ✏️ Activity 1 — Research Worksheet
Answer the following questions in your notebook or a text file:
1. What does JVM stand for, and what is its job?
2. Name three real-world applications built with Java.
3. What is the difference between the JDK and the JRE?
4. Why is Java called "platform independent"?
5. What file extension does compiled Java bytecode use?

### 🎯 Activity 2 — "Hello, Me!" Program
Write a Java program that prints:
```
Hello, I am [Your Name]!
I am learning Java.
Today is Week 1.
```
Replace `[Your Name]` with your actual name. Each sentence must be on its own line. Save the file as `HelloMe.java` and run it.

### ✅ Weekly Outcome
By the end of Week 1, students can explain what Java is, describe the JDK/JRE/JVM relationship, write a minimal Java program, compile it from the command line, and run it successfully.

---

## Week 02 — Java Get Started

### 📖 Lesson

Before writing serious Java code you need a proper development environment. This week you will install the tools and write your first program from scratch without any tutorial help.

**Step 1 — Install the JDK**
1. Go to [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)
2. Download **JDK 17** (Long-Term Support) for your operating system.
3. Run the installer and follow the prompts.
4. Verify installation by opening a terminal and typing:
   ```
   java -version
   javac -version
   ```

**Step 2 — Choose an IDE**
An **Integrated Development Environment (IDE)** makes coding much easier. Popular choices:

| IDE | Best For | Download |
|-----|----------|----------|
| IntelliJ IDEA (Community) | Beginners → professionals | jetbrains.com |
| Eclipse | University courses | eclipse.org |
| VS Code + Extension Pack for Java | Lightweight setup | code.visualstudio.com |

**Step 3 — Understand the compile-run cycle**
```
Source code (.java) → javac compiler → Bytecode (.class) → java JVM → Output
```

**Step 4 — Java file naming rules**
- The **file name** must exactly match the **public class name** (case-sensitive).
- File name: `MyProgram.java` → Class name: `MyProgram`
- No spaces in file names. Use PascalCase (capitalize each word).

### 🔑 Key Concepts
- Installing and verifying JDK
- IDE setup and basic navigation
- Compile-run cycle (`javac` and `java` commands)
- File naming conventions and class name rules
- Understanding error messages from the compiler

### 💻 Code Sample — Testing Your Setup

```java
// File: SetupTest.java
// Run this program to confirm your Java environment works correctly.

public class SetupTest {
    public static void main(String[] args) {
        System.out.println("Java setup is working!");
        System.out.println("JDK is installed correctly.");
        System.out.println("Ready to start coding.");
    }
}
```

**How to run from the command line:**
```bash
# Step 1: Compile
javac SetupTest.java

# Step 2: Run
java SetupTest
```

**Expected Output:**
```
Java setup is working!
JDK is installed correctly.
Ready to start coding.
```

### 💻 Code Sample — Intentional Error (Learn to Read Errors)

```java
// File: BrokenProgram.java
// This program has a deliberate error. Try to find and fix it!

public class BrokenProgram {
    public static void main(String[] args) {
        System.out.println("This will not compile")  // Missing semicolon!
    }
}
```

The compiler will say something like:
```
BrokenProgram.java:4: error: ';' expected
```
Fix: Add a semicolon at the end of the `println` line.

### ✏️ Activity 1 — Environment Setup Lab
1. Install JDK 17 on your computer (or verify it is already installed).
2. Install IntelliJ IDEA Community Edition (or your preferred IDE).
3. Create a new Java project called `Week02Lab`.
4. Write and run `SetupTest.java` from the code sample above.
5. Take a screenshot of the successful output and include it in your submission.

### 🎯 Activity 2 — Fix the Bugs Drill
Each snippet below has one bug. Identify and fix each one:

```java
// Bug 1
public class Bug1 {
    public static void main(String[] args) {
        System.out.println("Fix me)
    }
}

// Bug 2
public class bug2 {                      // Hint: check the class name vs file name
    public static void main(String[] args) {
        System.out.println("Class name issue");
    }
}

// Bug 3
public class Bug3 {
    public static void main(String[] args)   // Hint: something is missing here
        System.out.println("Missing something");
    }
}
```

### ✅ Weekly Outcome
By the end of Week 2, students have a fully working Java development environment, can compile and run programs from both the IDE and command line, and can read basic compiler error messages.

---

## Week 03 — Java Syntax

### 📖 Lesson

**Syntax** is the set of rules that defines how a Java program must be written. If you break a syntax rule, the compiler will refuse to compile your code and will give you an error.

**Core syntax rules:**

1. **Every statement ends with a semicolon (`;`)**
   ```java
   System.out.println("Hello");  // ✅ correct
   System.out.println("Hello")   // ❌ missing semicolon
   ```

2. **Code blocks use curly braces (`{ }`)**
   - A class body is wrapped in `{ }`
   - A method body is wrapped in `{ }`

3. **Java is case-sensitive**
   ```java
   String name = "Alice";   // ✅
   string name = "Alice";   // ❌ 'string' is not 'String'
   ```

4. **Whitespace is mostly ignored** (except inside strings)
   ```java
   System.out.println("Hello");
   System.out   .println(  "Hello"  );   // Also valid, but ugly
   ```

5. **Every program needs a `main` method**
   ```java
   public static void main(String[] args) { }
   ```

**Anatomy of a Java program:**
```
public class ClassName {           // Class declaration
    public static void main(...) { // Main method (entry point)
        // statements go here
    }
}
```

**Naming conventions (follow these always):**

| Item | Convention | Example |
|------|------------|---------|
| Class | PascalCase | `StudentRecord` |
| Method | camelCase | `calculateTotal()` |
| Variable | camelCase | `firstName` |
| Constant | UPPER_SNAKE_CASE | `MAX_SIZE` |

### 🔑 Key Concepts
- Semicolons as statement terminators
- Curly braces to define code blocks
- Case sensitivity
- Java naming conventions
- The structure: class → method → statements

### 💻 Code Sample — Syntax in Action

```java
// File: SyntaxDemo.java
// Demonstrates proper Java syntax with multiple statements.

public class SyntaxDemo {
    public static void main(String[] args) {
        // Each line below is one statement, ending with a semicolon
        System.out.println("Line 1: Java syntax is strict.");
        System.out.println("Line 2: Every statement ends with a semicolon.");
        System.out.println("Line 3: Curly braces define code blocks.");

        // This is a blank line — Java ignores blank lines
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

### 💻 Code Sample — Naming Convention Example

```java
// File: NamingConventions.java
// Shows proper naming conventions in practice.

public class NamingConventions {
    // Constant: UPPER_SNAKE_CASE
    static final int MAX_STUDENTS = 40;

    public static void main(String[] args) {
        // Variables: camelCase
        String studentName = "Maria Santos";
        int studentAge = 20;
        double gradeAverage = 92.5;

        System.out.println("Student: " + studentName);
        System.out.println("Age: " + studentAge);
        System.out.println("Average: " + gradeAverage);
        System.out.println("Max class size: " + MAX_STUDENTS);
    }
}
```

### ✏️ Activity 1 — Syntax Correction Worksheet
Rewrite each of the following broken programs so they compile and run correctly. Explain what was wrong with each one.

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
        System.out.println("Line three")
    }
}

// Program C
public class ProgramC
    public static void main(String[] args) {
        System.out.println("Where is the class brace?");
    }
```

### 🎯 Activity 2 — Structure Blueprint Challenge
Write a Java program *from scratch* (no copy-paste) that:
1. Has a class named `MyProfile`
2. Prints your name, city, and favorite hobby on separate lines
3. Uses correct naming conventions for any variables you create
4. Compiles and runs without errors

### ✅ Weekly Outcome
By the end of Week 3, students can identify and correct common Java syntax errors, follow naming conventions, and explain the structural components of a Java program.

---

## Week 04 — Java Output & Comments

### 📖 Lesson

**Output** is how a Java program communicates results to the user. The most common way is printing to the **console** (terminal window).

#### Output Methods

| Method | Behavior |
|--------|----------|
| `System.out.println(x)` | Prints `x` and then moves to a **new line** |
| `System.out.print(x)` | Prints `x` **without** moving to a new line |
| `System.out.printf(format, args)` | Prints with **formatted** output (like `%d`, `%s`, `%f`) |

#### printf Format Specifiers

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `%d` | Integer | `printf("%d", 42)` → `42` |
| `%f` | Floating-point | `printf("%.2f", 3.14159)` → `3.14` |
| `%s` | String | `printf("%s", "hi")` → `hi` |
| `%n` | New line (platform-safe) | `printf("line1%nline2")` |
| `%c` | Character | `printf("%c", 'A')` → `A` |

#### Comments

Comments are **notes in your code** that the compiler completely ignores. They exist only for humans reading the code.

| Type | Syntax | Use |
|------|--------|-----|
| Single-line | `// text` | Brief notes on one line |
| Multi-line | `/* text */` | Longer explanations spanning multiple lines |
| Javadoc | `/** text */` | Generates official API documentation |

**Good commenting habits:**
- Comment *why* you did something, not *what* (the code shows what)
- Every class and method should have a short description comment
- Avoid obvious comments like `// add 1 to i` for `i = i + 1`

### 🔑 Key Concepts
- `println` vs `print` vs `printf`
- Escape sequences (`\n`, `\t`, `\\`, `\"`)
- Format specifiers for printf
- Single-line, multi-line, and Javadoc comments
- Why good comments matter

### 💻 Code Sample — Output Methods Compared

```java
// File: OutputDemo.java
// Demonstrates the three main output methods in Java.

public class OutputDemo {
    public static void main(String[] args) {

        // println: prints and goes to a new line
        System.out.println("--- println examples ---");
        System.out.println("First line");
        System.out.println("Second line");

        // print: stays on the same line
        System.out.println("\n--- print examples ---");
        System.out.print("A");
        System.out.print("B");
        System.out.print("C");
        System.out.println(); // just a newline

        // printf: formatted output
        System.out.println("\n--- printf examples ---");
        String name = "Juan";
        int age = 19;
        double gpa = 3.75;
        System.out.printf("Name: %s%n", name);
        System.out.printf("Age: %d%n", age);
        System.out.printf("GPA: %.2f%n", gpa);
    }
}
```

**Expected Output:**
```
--- println examples ---
First line
Second line

--- print examples ---
ABC

--- printf examples ---
Name: Juan
Age: 19
GPA: 3.75
```

### 💻 Code Sample — Escape Sequences

```java
// File: EscapeDemo.java
// Shows how escape sequences are used in strings.

public class EscapeDemo {
    public static void main(String[] args) {
        System.out.println("She said, \"Java is fun!\"");  // prints quotes
        System.out.println("Path: C:\\Users\\Student");    // prints backslash
        System.out.println("Line1\nLine2\nLine3");          // newlines
        System.out.println("Col1\tCol2\tCol3");             // tabs
    }
}
```

### 💻 Code Sample — Comments

```java
// File: CommentsDemo.java
/**
 * This class demonstrates different types of Java comments.
 * It is an example of a Javadoc comment at the class level.
 */
public class CommentsDemo {

    /**
     * The main entry point of the program.
     * @param args command-line arguments (not used here)
     */
    public static void main(String[] args) {

        // Single-line comment: prints a greeting
        System.out.println("Hello, comments!");

        /*
         * Multi-line comment:
         * This block explains that the next line
         * prints a farewell message.
         */
        System.out.println("Goodbye!");
    }
}
```

### ✏️ Activity 1 — Output Formatting Lab
Write a program called `StudentCard.java` that prints a neatly formatted student information card using `printf`. The card should look like:

```
=============================
       STUDENT RECORD
=============================
Name    : [Your Name]
ID No.  : [Your ID]
Course  : BS Computer Science
GPA     : [e.g., 1.75]
=============================
```
Use at least one `printf` with a format specifier for the GPA.

### 🎯 Activity 2 — Comment the Code Quiz
You will be given a 20-line program with **no comments**. Add appropriate single-line and multi-line comments explaining what each section does. Your comments will be graded for accuracy and clarity.

```java
// Add comments to explain every part of this program:
public class Unannoted {
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

### ✅ Weekly Outcome
By the end of Week 4, students can produce formatted console output using `println`, `print`, and `printf`, use escape sequences, and write meaningful comments in all three styles.

---

## Week 05 — Java Variables

### 📖 Lesson

A **variable** is a named storage location in memory that holds a value. Think of it as a labelled box where you can store something and retrieve it later.

**Declaring a variable:**
```java
dataType variableName = value;
```

- `dataType` — What kind of data will be stored (int, String, etc.)
- `variableName` — A name you choose (follow camelCase)
- `= value` — Optional initial value (if omitted, the variable is **uninitialized**)

**Types of variables by location:**

| Type | Where it lives | Example |
|------|---------------|---------|
| Local variable | Inside a method | `int x = 5;` inside `main` |
| Instance variable (field) | Inside a class, outside methods | Used in OOP (later weeks) |
| Static variable | Belongs to the class itself | `static int count = 0;` |

**Constants (final variables):**
```java
final double PI = 3.14159;  // Cannot be changed after assignment
```

**Multiple declarations:**
```java
int x = 1, y = 2, z = 3;    // Declare multiple in one line
```

**Variable naming rules (must follow):**
1. Start with a letter, `$`, or `_`
2. No spaces
3. No reserved keywords (`int`, `class`, `if`, etc.)
4. Case-sensitive (`age` ≠ `Age`)

### 🔑 Key Concepts
- What a variable is (memory storage)
- Declaration vs initialization
- `final` keyword for constants
- Variable naming rules and best practices
- Local vs class-level scope (brief introduction)

### 💻 Code Sample — Variable Basics

```java
// File: VariableDemo.java
// Demonstrates declaring, initializing, and using variables.

public class VariableDemo {
    public static void main(String[] args) {

        // Integer variable
        int score = 95;

        // Double variable
        double price = 49.99;

        // String variable
        String city = "Manila";

        // Boolean variable
        boolean isStudent = true;

        // Character variable
        char grade = 'A';

        // Constant
        final int MAX_SCORE = 100;

        // Print all variables
        System.out.println("Score: " + score);
        System.out.println("Price: " + price);
        System.out.println("City: " + city);
        System.out.println("Is a student: " + isStudent);
        System.out.println("Grade: " + grade);
        System.out.println("Max possible score: " + MAX_SCORE);

        // Modify a variable
        score = 98;
        System.out.println("Updated Score: " + score);

        // This would cause an error (uncomment to see):
        // MAX_SCORE = 200;
    }
}
```

**Expected Output:**
```
Score: 95
Price: 49.99
City: Manila
Is a student: true
Grade: A
Max possible score: 100
Updated Score: 98
```

### 💻 Code Sample — Variable Swap

```java
// File: SwapVariables.java
// Classic exercise: swap the values of two variables.

public class SwapVariables {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        System.out.println("Before swap: a = " + a + ", b = " + b);

        // Swap using a temporary variable
        int temp = a;
        a = b;
        b = temp;

        System.out.println("After swap:  a = " + a + ", b = " + b);
    }
}
```

### ✏️ Activity 1 — Variable Declaration Drill
Create a program `MyVariables.java` that declares and prints variables for:
- Your full name (`String`)
- Your age (`int`)
- Your height in meters (`double`)
- Whether you wear glasses (`boolean`)
- Your name initial (`char`)
- Your lucky number as a constant (`final int`)

Print each variable with a descriptive label.

### 🎯 Activity 2 — Variables Quiz
Answer without running the code. Write what each program prints or explain the error:

```java
// Quiz A
int x = 5;
x = x + 3;
System.out.println(x);

// Quiz B
final int Y = 10;
Y = 20;  // What happens?
System.out.println(Y);

// Quiz C
int a = 7, b = 3;
int result = a * b - a + b;
System.out.println(result);
```

### ✅ Weekly Outcome
By the end of Week 5, students can declare and initialize variables of different types, use constants with `final`, update variable values, and follow naming conventions.

---

## Week 06 — Java Data Types

### 📖 Lesson

Java is a **strongly typed** language — every variable must be declared with a specific type. Java data types are split into two categories:

#### Primitive Data Types (8 total)

| Type | Size | Range / Values | Default | Example |
|------|------|----------------|---------|---------|
| `byte` | 1 byte | -128 to 127 | 0 | `byte b = 100;` |
| `short` | 2 bytes | -32,768 to 32,767 | 0 | `short s = 1000;` |
| `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 | 0 | `int n = 50000;` |
| `long` | 8 bytes | Very large integers | 0L | `long l = 1234567890L;` |
| `float` | 4 bytes | ~7 decimal digits precision | 0.0f | `float f = 3.14f;` |
| `double` | 8 bytes | ~15 decimal digits precision | 0.0 | `double d = 3.14159;` |
| `boolean` | 1 bit | `true` or `false` | false | `boolean flag = true;` |
| `char` | 2 bytes | Unicode character | '\u0000' | `char c = 'Z';` |

> **Note:** `long` literals require an `L` suffix. `float` literals require an `f` suffix.

#### Reference Data Types

These store a *reference* (memory address) to an object, not the value directly.
- `String` — a sequence of characters
- Arrays
- Classes (covered in later weeks)

**Key difference:** Primitive variables hold the **actual value**. Reference variables hold the **address** of where the data lives in memory.

#### Overflow Example
What happens when you exceed a type's range?
```java
byte b = 127;
b++;        // b becomes -128 (wraps around — overflow!)
```
This is why choosing the right type matters.

### 🔑 Key Concepts
- 8 primitive types and their sizes
- Reference types vs primitive types
- When to use `int` vs `long`, `float` vs `double`
- Integer overflow concept
- Default values for uninitialized fields

### 💻 Code Sample — All Primitive Types

```java
// File: DataTypesDemo.java
// Declares a variable of every primitive type and prints them.

public class DataTypesDemo {
    public static void main(String[] args) {

        byte  myByte    = 100;
        short myShort   = 5000;
        int   myInt     = 100000;
        long  myLong    = 15000000000L;   // L suffix required for long literals
        float  myFloat  = 5.99f;          // f suffix required for float literals
        double myDouble = 19.99;
        boolean myBool  = true;
        char   myChar   = 'J';

        System.out.println("byte:    " + myByte);
        System.out.println("short:   " + myShort);
        System.out.println("int:     " + myInt);
        System.out.println("long:    " + myLong);
        System.out.println("float:   " + myFloat);
        System.out.println("double:  " + myDouble);
        System.out.println("boolean: " + myBool);
        System.out.println("char:    " + myChar);

        // String is a reference type
        String myString = "Hello Java";
        System.out.println("String:  " + myString);
    }
}
```

### 💻 Code Sample — Overflow Demonstration

```java
// File: OverflowDemo.java
// Shows what happens when a byte overflows its range.

public class OverflowDemo {
    public static void main(String[] args) {
        byte b = 127;
        System.out.println("Before overflow: " + b);   // 127

        b++;   // 127 + 1 wraps around
        System.out.println("After overflow:  " + b);   // -128

        // int range test
        int maxInt = Integer.MAX_VALUE;
        System.out.println("Max int value: " + maxInt);
        System.out.println("Max int + 1:   " + (maxInt + 1));  // wraps to MIN_VALUE
    }
}
```

### ✏️ Activity 1 — Data Type Selection Worksheet
For each scenario, choose the best data type and justify your choice:
1. Storing a student's age (0–150)
2. Storing a country's population (up to 8 billion)
3. Storing a product price like ₱1,299.95
4. Storing whether a student passed or failed
5. Storing a student's middle initial
6. Storing a student's full name
7. Storing the distance between stars (extremely large number)
8. Storing a person's exact weight with 2 decimal places

### 🎯 Activity 2 — Data Type Coding Challenge
Write a program `ItemReceipt.java` that uses appropriate data types to store and display:
- Item name (String)
- Quantity bought (int or short)
- Unit price (double)
- Discount percentage (float)
- Total price after discount (double — calculate it in code)
- Whether tax is included (boolean)

Print a formatted receipt using `printf`.

### ✅ Weekly Outcome
By the end of Week 6, students can name all 8 primitive types, choose the correct type for a given scenario, understand primitive vs reference types, and handle type suffixes (`L`, `f`).

---

## Week 07 — Java Type Casting

### 📖 Lesson

**Type casting** is converting a value from one data type to another. Java has two kinds:

#### 1. Widening (Implicit) Casting — Automatic

Java automatically converts a *smaller* type to a *larger* type because there is no risk of data loss.

**Order (smallest → largest):**
```
byte → short → int → long → float → double
```

```java
int myInt = 100;
double myDouble = myInt;   // Automatically converted — no cast needed
System.out.println(myDouble);  // 100.0
```

#### 2. Narrowing (Explicit) Casting — Manual

Converting a *larger* type to a *smaller* type **requires** you to explicitly tell Java to do it, because data may be lost (truncated).

```java
double myDouble = 9.99;
int myInt = (int) myDouble;   // Explicit cast — decimal part is dropped
System.out.println(myInt);    // 9  (not 10 — it truncates, not rounds)
```

**Syntax:**
```java
targetType variableName = (targetType) originalValue;
```

#### Common Casting Scenarios

| Situation | Type | Risk |
|-----------|------|------|
| `int` → `double` | Widening | None |
| `double` → `int` | Narrowing | Decimal part lost |
| `char` → `int` | Widening | None (gives Unicode value) |
| `int` → `char` | Narrowing | Only valid if value is a valid char code |
| `int` → `String` | Use `String.valueOf(n)` | N/A |
| `String` → `int` | Use `Integer.parseInt(s)` | NumberFormatException if not numeric |

#### String-to-Number Conversions (very common)

```java
String numStr = "42";
int number = Integer.parseInt(numStr);    // String → int
double d = Double.parseDouble("3.14");    // String → double
String s = String.valueOf(100);           // int → String
```

### 🔑 Key Concepts
- Widening vs narrowing casting
- Implicit vs explicit cast syntax
- Truncation (not rounding) on narrowing
- `parseInt`, `parseDouble`, `String.valueOf`
- Why casting is needed (type safety)

### 💻 Code Sample — Widening and Narrowing

```java
// File: TypeCastingDemo.java
// Demonstrates both widening (automatic) and narrowing (explicit) casting.

public class TypeCastingDemo {
    public static void main(String[] args) {

        // ---- Widening casting (automatic) ----
        int myInt = 200;
        long myLong = myInt;      // int → long
        float myFloat = myLong;   // long → float
        double myDouble = myFloat;// float → double

        System.out.println("--- Widening ---");
        System.out.println("int:    " + myInt);
        System.out.println("long:   " + myLong);
        System.out.println("float:  " + myFloat);
        System.out.println("double: " + myDouble);

        // ---- Narrowing casting (explicit) ----
        double price = 9.99;
        int truncatedPrice = (int) price;   // 9 (decimal part dropped)

        double bigNumber = 12345.6789;
        int narrowed = (int) bigNumber;     // 12345

        System.out.println("\n--- Narrowing ---");
        System.out.println("Original double: " + price);
        System.out.println("Cast to int:     " + truncatedPrice);
        System.out.println("bigNumber cast:  " + narrowed);

        // ---- char ↔ int ----
        char letter = 'A';
        int unicode = letter;          // char → int (widening)
        System.out.println("\n--- char ↔ int ---");
        System.out.println("'A' as int: " + unicode);    // 65

        int code = 90;
        char fromCode = (char) code;   // int → char (narrowing)
        System.out.println("90 as char: " + fromCode);   // Z
    }
}
```

### 💻 Code Sample — String/Number Conversions

```java
// File: ParseDemo.java
// Shows how to convert between Strings and numbers.

public class ParseDemo {
    public static void main(String[] args) {

        // String → int
        String strAge = "21";
        int age = Integer.parseInt(strAge);
        System.out.println("Parsed age: " + age);
        System.out.println("Age in 10 years: " + (age + 10));

        // String → double
        String strPrice = "199.95";
        double price = Double.parseDouble(strPrice);
        System.out.printf("Price with 10%% tax: %.2f%n", price * 1.10);

        // int → String
        int score = 95;
        String scoreStr = String.valueOf(score);
        System.out.println("Score as String: " + scoreStr);
        System.out.println("String length: " + scoreStr.length() + " characters");
    }
}
```

### ✏️ Activity 1 — Casting Prediction Worksheet
Predict the output of each code snippet *without* running it. Then run it to verify.

```java
// Predict A
double x = 8.9;
int y = (int) x;
System.out.println(y);

// Predict B
int a = 65;
char c = (char) a;
System.out.println(c);

// Predict C
String s = "150";
int n = Integer.parseInt(s);
System.out.println(n + 50);

// Predict D
int p = 7, q = 2;
System.out.println(p / q);
System.out.println((double) p / q);
```

### 🎯 Activity 2 — GPA Calculator (Type Casting Focus)
Write a program `GPACalculator.java` that:
1. Stores 5 subject grades as `int` values (e.g., 85, 90, 78, 92, 88)
2. Calculates the total as `int`
3. **Casts** appropriately to compute the average as a `double`
4. Prints the average formatted to 2 decimal places
5. Prints the average rounded down to the nearest `int` (use casting)

### ✅ Weekly Outcome
By the end of Week 7, students understand the difference between widening and narrowing casts, can perform explicit type casts correctly, and can convert between String and numeric types using parse methods.

---

## Week 08 — Java Operators

### 📖 Lesson

**Operators** are special symbols that perform operations on one or more values (called **operands**). Java has many categories of operators.

#### 1. Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3` (integer division!) |
| `%` | Modulus (remainder) | `10 % 3` | `1` |

> ⚠️ **Integer division:** `10 / 3` gives `3`, not `3.333`. To get the decimal, cast: `(double) 10 / 3`

#### 2. Assignment Operators

| Operator | Meaning | Equivalent |
|----------|---------|------------|
| `=` | Assign | `x = 5` |
| `+=` | Add and assign | `x = x + 5` |
| `-=` | Subtract and assign | `x = x - 5` |
| `*=` | Multiply and assign | `x = x * 5` |
| `/=` | Divide and assign | `x = x / 5` |
| `%=` | Modulus and assign | `x = x % 5` |

#### 3. Comparison (Relational) Operators
Return `true` or `false`.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `5 == 5` → `true` |
| `!=` | Not equal to | `5 != 3` → `true` |
| `>` | Greater than | `7 > 3` → `true` |
| `<` | Less than | `2 < 8` → `true` |
| `>=` | Greater than or equal | `5 >= 5` → `true` |
| `<=` | Less than or equal | `4 <= 3` → `false` |

#### 4. Logical Operators

| Operator | Name | Meaning |
|----------|------|---------|
| `&&` | AND | Both must be `true` |
| `\|\|` | OR | At least one must be `true` |
| `!` | NOT | Reverses the boolean |

#### 5. Increment / Decrement

| Operator | Meaning |
|----------|---------|
| `++x` | Increment before use (pre-increment) |
| `x++` | Increment after use (post-increment) |
| `--x` | Decrement before use |
| `x--` | Decrement after use |

### 🔑 Key Concepts
- Integer vs floating-point division
- Modulus for remainder/even-odd checks
- Compound assignment operators
- Short-circuit evaluation (`&&` and `||`)
- Pre vs post increment/decrement

### 💻 Code Sample — Arithmetic & Assignment

```java
// File: OperatorsDemo.java
// Comprehensive demo of Java operators.

public class OperatorsDemo {
    public static void main(String[] args) {

        // ---- Arithmetic ----
        int a = 17, b = 5;
        System.out.println("=== Arithmetic ===");
        System.out.println("a + b = " + (a + b));   // 22
        System.out.println("a - b = " + (a - b));   // 12
        System.out.println("a * b = " + (a * b));   // 85
        System.out.println("a / b = " + (a / b));   // 3 (integer division)
        System.out.println("a % b = " + (a % b));   // 2 (remainder)
        System.out.printf("a / b (double) = %.2f%n", (double) a / b);  // 3.40

        // ---- Compound Assignment ----
        System.out.println("\n=== Compound Assignment ===");
        int x = 10;
        x += 5;  System.out.println("After x += 5: " + x);   // 15
        x -= 3;  System.out.println("After x -= 3: " + x);   // 12
        x *= 2;  System.out.println("After x *= 2: " + x);   // 24
        x /= 4;  System.out.println("After x /= 4: " + x);   // 6
        x %= 4;  System.out.println("After x %= 4: " + x);   // 2

        // ---- Increment / Decrement ----
        System.out.println("\n=== Increment / Decrement ===");
        int i = 5;
        System.out.println("i = " + i);
        System.out.println("i++ = " + i++);  // prints 5, then i becomes 6
        System.out.println("i = " + i);       // 6
        System.out.println("++i = " + (++i)); // i becomes 7, prints 7

        // ---- Comparison ----
        System.out.println("\n=== Comparison ===");
        System.out.println("10 > 5:  " + (10 > 5));
        System.out.println("10 == 5: " + (10 == 5));
        System.out.println("10 != 5: " + (10 != 5));

        // ---- Logical ----
        System.out.println("\n=== Logical ===");
        boolean isAdult = true;
        boolean hasID = false;
        System.out.println("isAdult && hasID: " + (isAdult && hasID));
        System.out.println("isAdult || hasID: " + (isAdult || hasID));
        System.out.println("!isAdult: " + (!isAdult));
    }
}
```

### ✏️ Activity 1 — Operator Expression Evaluation Worksheet
Without running code, evaluate each expression. Show your work step by step.

```java
int x = 10, y = 3;

// Evaluate each:
1. x + y * 2          // (operator precedence!)
2. (x + y) * 2
3. x % y
4. x / y
5. (double) x / y
6. x++ + y            // what is x after this?
7. ++x + y            // starting from fresh x = 10
8. x > 5 && y < 5
9. x == 10 || y == 10
10. !(x > y)
```

### 🎯 Activity 2 — Calculator Program
Write a program `SimpleCalculator.java` that:
1. Declares two `double` variables `num1 = 25.0` and `num2 = 4.0`
2. Calculates and prints: sum, difference, product, quotient (double division), remainder (cast to int first), and the quotient as a percentage (multiply by 100)
3. Uses compound assignment to double `num1` and print the result
4. Checks if `num1` is greater than `num2` and prints a boolean result
5. Uses all six arithmetic operators at least once

### ✅ Weekly Outcome
By the end of Week 8, students can use all arithmetic, assignment, comparison, and logical operators correctly, understand operator precedence, and explain the difference between pre- and post-increment.

---

## Week 09 — Java Strings & Java Math

### 📖 Lesson

### Part A — Java Strings

A `String` in Java is a **sequence of characters**. It is a **reference type** (an object), not a primitive. Strings are **immutable** — once created, the characters inside cannot be changed; any operation that seems to modify a String actually creates a new one.

#### Common String Methods

| Method | Description | Example |
|--------|-------------|---------|
| `length()` | Number of characters | `"Hello".length()` → `5` |
| `toUpperCase()` | All uppercase | `"hi".toUpperCase()` → `"HI"` |
| `toLowerCase()` | All lowercase | `"HI".toLowerCase()` → `"hi"` |
| `charAt(i)` | Character at index `i` | `"Java".charAt(1)` → `'a'` |
| `indexOf(s)` | First position of substring | `"Hello".indexOf("l")` → `2` |
| `substring(a, b)` | Characters from `a` (inclusive) to `b` (exclusive) | `"Hello".substring(1,4)` → `"ell"` |
| `contains(s)` | Does it contain this? | `"Hello".contains("ell")` → `true` |
| `replace(old, new)` | Replace occurrences | `"aaa".replace("a","b")` → `"bbb"` |
| `trim()` | Remove leading/trailing spaces | `"  hi  ".trim()` → `"hi"` |
| `equals(s)` | Compare content (case-sensitive) | `"Hi".equals("hi")` → `false` |
| `equalsIgnoreCase(s)` | Compare ignoring case | `"Hi".equalsIgnoreCase("hi")` → `true` |
| `isEmpty()` | Is the string empty? | `"".isEmpty()` → `true` |

> ⚠️ Never compare Strings with `==`. Use `.equals()`.

#### String Concatenation
```java
String first = "Hello";
String second = "World";
String result = first + " " + second;   // "Hello World"
```

### Part B — Java Math

The `Math` class provides mathematical functions as **static methods** (no object needed).

| Method | Description | Example |
|--------|-------------|---------|
| `Math.abs(x)` | Absolute value | `Math.abs(-5)` → `5` |
| `Math.max(a,b)` | Larger of two | `Math.max(3,7)` → `7` |
| `Math.min(a,b)` | Smaller of two | `Math.min(3,7)` → `3` |
| `Math.pow(base,exp)` | Power | `Math.pow(2,10)` → `1024.0` |
| `Math.sqrt(x)` | Square root | `Math.sqrt(16)` → `4.0` |
| `Math.round(x)` | Round to nearest int | `Math.round(4.6)` → `5` |
| `Math.floor(x)` | Round down | `Math.floor(4.9)` → `4.0` |
| `Math.ceil(x)` | Round up | `Math.ceil(4.1)` → `5.0` |
| `Math.random()` | Random number 0.0–0.999… | `Math.random()` |
| `Math.PI` | π constant | `Math.PI` → `3.14159...` |

### 🔑 Key Concepts
- String immutability
- String comparison with `.equals()` (not `==`)
- Index-based String operations (0-indexed)
- Math class static methods
- Generating random numbers

### 💻 Code Sample — String Operations

```java
// File: StringDemo.java
// Demonstrates commonly used String methods.

public class StringDemo {
    public static void main(String[] args) {
        String name = "  Maria Clara  ";

        // Trim whitespace
        String trimmed = name.trim();
        System.out.println("Trimmed: '" + trimmed + "'");

        // Case operations
        System.out.println("Upper: " + trimmed.toUpperCase());
        System.out.println("Lower: " + trimmed.toLowerCase());

        // Length
        System.out.println("Length: " + trimmed.length());

        // Characters and substrings
        System.out.println("First char: " + trimmed.charAt(0));
        System.out.println("Substring(6,11): " + trimmed.substring(6, 11));

        // Search
        System.out.println("Index of 'Clara': " + trimmed.indexOf("Clara"));
        System.out.println("Contains 'Maria': " + trimmed.contains("Maria"));

        // Replace
        String replaced = trimmed.replace("Clara", "Santos");
        System.out.println("Replaced: " + replaced);

        // Comparison
        String s1 = "Java";
        String s2 = "java";
        System.out.println("\ns1.equals(s2): " + s1.equals(s2));
        System.out.println("s1.equalsIgnoreCase(s2): " + s1.equalsIgnoreCase(s2));
    }
}
```

### 💻 Code Sample — Math Operations

```java
// File: MathDemo.java
// Demonstrates the Java Math class methods.

public class MathDemo {
    public static void main(String[] args) {
        System.out.println("Math.abs(-42):      " + Math.abs(-42));
        System.out.println("Math.max(15, 27):   " + Math.max(15, 27));
        System.out.println("Math.min(15, 27):   " + Math.min(15, 27));
        System.out.println("Math.pow(2, 8):     " + Math.pow(2, 8));
        System.out.println("Math.sqrt(144):     " + Math.sqrt(144));
        System.out.println("Math.round(3.7):    " + Math.round(3.7));
        System.out.println("Math.floor(3.9):    " + Math.floor(3.9));
        System.out.println("Math.ceil(3.1):     " + Math.ceil(3.1));
        System.out.printf("Math.PI:            %.5f%n", Math.PI);

        // Random number between 1 and 6 (like a dice roll)
        int dice = (int)(Math.random() * 6) + 1;
        System.out.println("Dice roll: " + dice);

        // Circle area
        double radius = 7.5;
        double area = Math.PI * Math.pow(radius, 2);
        System.out.printf("Circle area (r=%.1f): %.4f%n", radius, area);
    }
}
```

### ✏️ Activity 1 — String Manipulation Lab
Write a program `StringLab.java` that:
1. Asks (via hardcoded String) for a sentence: `"the quick brown fox jumps"`
2. Prints the sentence in ALL CAPS
3. Prints the number of characters
4. Replaces `"fox"` with `"cat"`
5. Prints the first word (characters 0 to the first space)
6. Prints whether the sentence contains the word `"quick"`

### 🎯 Activity 2 — Math Challenge
Write a program `MathChallenge.java` that:
1. Calculates the hypotenuse of a right triangle with legs 6 and 8 (`Math.sqrt`, `Math.pow`)
2. Generates 5 random integers between 10 and 99 (print each on one line)
3. Computes and prints the area and circumference of a circle with radius 5 using `Math.PI`
4. Finds the larger of two numbers entered as variables (use `Math.max`)

### ✅ Weekly Outcome
By the end of Week 9, students can manipulate Strings using built-in methods, compare Strings correctly, and use the Math class for common calculations including random number generation.

---

## Week 10 — Java Booleans + Midterm Review

### 📖 Lesson

### Part A — Java Booleans

A `boolean` variable holds exactly one of two values: `true` or `false`. Booleans are the backbone of all decision-making in Java.

```java
boolean isRaining = true;
boolean hasUmbrella = false;
```

**Boolean expressions** are any expression that evaluates to `true` or `false`:
```java
int age = 18;
boolean isAdult = age >= 18;    // true
boolean isChild = age < 13;     // false
```

**Combining booleans (logical operators recap):**
```java
boolean a = true, b = false;
System.out.println(a && b);    // false — both must be true
System.out.println(a || b);    // true  — at least one true
System.out.println(!a);        // false — negation
```

**Truth tables:**

| `a` | `b` | `a && b` | `a \|\| b` | `!a` |
|-----|-----|---------|----------|------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

**Short-circuit evaluation:**
- `&&` — if the **left side is false**, the right side is **never evaluated**
- `||` — if the **left side is true**, the right side is **never evaluated**

```java
int x = 0;
// Safe because of short-circuit: if x == 0 is false, 10/x is never evaluated
if (x != 0 && 10 / x > 2) {
    System.out.println("Greater than 2");
}
```

### Part B — Midterm Review

**Midterm Coverage (Weeks 1–10):**

| Week | Topic | Key Things to Review |
|------|-------|----------------------|
| 1 | Java Introduction | JDK/JRE/JVM, platform independence |
| 2 | Java Get Started | Compile-run cycle, IDE setup, error reading |
| 3 | Java Syntax | Semicolons, braces, case sensitivity, naming |
| 4 | Output & Comments | println/print/printf, comment types |
| 5 | Variables | Declaration, initialization, constants |
| 6 | Data Types | 8 primitives, reference types, overflow |
| 7 | Type Casting | Widening/narrowing, parseInt, parseDouble |
| 8 | Operators | Arithmetic, assignment, comparison, logical |
| 9 | Strings & Math | String methods, Math class methods |
| 10 | Booleans | Boolean logic, truth tables, short-circuit |

**Sample Midterm Questions:**
1. What is the output of `System.out.println((int) 9.99 + 1)`?
2. Which primitive type stores a single character?
3. Write code to check if a String `s` contains the word `"Java"` (case-insensitive).
4. What is the result of `10 % 3`?
5. Explain the difference between `print` and `println`.

### 🔑 Key Concepts
- Boolean type and boolean expressions
- Logical operators and truth tables
- Short-circuit evaluation
- Review of Weeks 1–9 material

### 💻 Code Sample — Boolean Logic

```java
// File: BooleanDemo.java
// Demonstrates boolean variables, expressions, and logic.

public class BooleanDemo {
    public static void main(String[] args) {

        // Boolean variables
        boolean isLoggedIn = true;
        boolean isPremiumUser = false;
        boolean hasExpired = false;

        // Compound conditions
        boolean canAccess = isLoggedIn && !hasExpired;
        boolean seesAds = !isPremiumUser || hasExpired;

        System.out.println("Can access content: " + canAccess);  // true
        System.out.println("Sees advertisements: " + seesAds);   // true

        // Comparing numbers returns boolean
        int score = 75;
        boolean passed = score >= 60;
        boolean honor  = score >= 90;
        boolean failed = !passed;

        System.out.println("\nScore: " + score);
        System.out.println("Passed: " + passed);
        System.out.println("Honor:  " + honor);
        System.out.println("Failed: " + failed);

        // Boolean from String comparison
        String input = "YES";
        boolean accepted = input.equalsIgnoreCase("yes");
        System.out.println("\nInput accepted: " + accepted);
    }
}
```

### ✏️ Activity 1 — Boolean Logic Worksheet (Midterm Prep)
Fill in the truth table and predict outputs:

```java
// Evaluate (true or false):
boolean p = true,  q = false, r = true;

1. p && q
2. p || q
3. !p && q
4. p && (q || r)
5. !(p || q) && r
6. p == q
7. p != q
8. (p && !q) || (!p && q)   // This is XOR — what does it do?
```

### 🎯 Activity 2 — Midterm Practice Exam
**Timed: 60 minutes | Total: 50 points**

**Part I — Multiple Choice (20 pts, 2 pts each)**
1. Which of the following is NOT a primitive type? `a) int  b) String  c) boolean  d) char`
2. What is the output of `System.out.println(7 % 2)`? `a) 3  b) 3.5  c) 1  d) 0`
3. What keyword makes a variable constant? `a) static  b) final  c) const  d) fixed`
4. `"Hello".charAt(1)` returns: `a) H  b) e  c) l  d) 1`
5. Widening casting is: `a) manual  b) automatic  c) not allowed  d) only for strings`

**Part II — Code Analysis (20 pts, 4 pts each)**  
Write the output for each snippet.

**Part III — Coding (10 pts)**  
Write a complete Java program that:
- Declares a student name, subject, and two exam scores
- Calculates and prints the average with 2 decimal places
- Prints whether the student passed (average ≥ 60)

### ✅ Weekly Outcome
By the end of Week 10, students understand boolean logic completely, complete the midterm exam, and identify any knowledge gaps for remediation in the second half of the course.

---

## 🏆 MIDTERM EXAM — Week 10

**Coverage:** Weeks 1–10  
**Topics:** Java Intro, Get Started, Syntax, Output, Comments, Variables, Data Types, Type Casting, Operators, Strings, Math, Booleans  
**Format:** Written/practical exam (as designed in Activity 2 above)

---

## Week 11 — Java If…Else

### 📖 Lesson

Decision-making is at the heart of programming. The `if-else` statement lets your program choose between different paths based on a condition.

#### Basic `if` Statement
```java
if (condition) {
    // Code runs only if condition is true
}
```

#### `if-else` Statement
```java
if (condition) {
    // Runs if condition is true
} else {
    // Runs if condition is false
}
```

#### `if-else if-else` Chain
```java
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else if (score >= 70) {
    grade = "C";
} else if (score >= 60) {
    grade = "D";
} else {
    grade = "F";
}
```

#### Nested `if`
```java
if (isLoggedIn) {
    if (isAdmin) {
        System.out.println("Welcome, Admin!");
    } else {
        System.out.println("Welcome, User!");
    }
}
```

#### Ternary Operator (shorthand if-else)
```java
// Syntax: condition ? valueIfTrue : valueIfFalse
String status = (age >= 18) ? "Adult" : "Minor";
```

**Common Mistakes:**
```java
// WRONG: using = instead of ==
if (x = 5) { ... }    // Assignment, not comparison! Won't compile

// WRONG: comparing strings with ==
if (name == "Alice") { ... }  // Use .equals() instead

// RIGHT
if (name.equals("Alice")) { ... }
```

### 🔑 Key Concepts
- `if`, `if-else`, `if-else if-else`
- Nested conditions
- Ternary operator
- Comparing values correctly
- Avoiding `=` vs `==` mistakes

### 💻 Code Sample — Grade Classifier

```java
// File: GradeClassifier.java
// Determines a letter grade based on a numeric score.

public class GradeClassifier {
    public static void main(String[] args) {

        int score = 85;

        // if-else if-else chain
        String letterGrade;
        if (score >= 90) {
            letterGrade = "A (Excellent)";
        } else if (score >= 80) {
            letterGrade = "B (Good)";
        } else if (score >= 70) {
            letterGrade = "C (Average)";
        } else if (score >= 60) {
            letterGrade = "D (Below Average)";
        } else {
            letterGrade = "F (Failed)";
        }

        System.out.println("Score: " + score);
        System.out.println("Grade: " + letterGrade);

        // Ternary for pass/fail
        String result = (score >= 60) ? "PASSED" : "FAILED";
        System.out.println("Result: " + result);
    }
}
```

### 💻 Code Sample — Nested if (Login System)

```java
// File: LoginCheck.java
// Demonstrates nested if statements.

public class LoginCheck {
    public static void main(String[] args) {
        boolean isLoggedIn = true;
        boolean isAdmin = false;
        int loginAttempts = 1;

        if (isLoggedIn) {
            if (loginAttempts > 3) {
                System.out.println("Account locked. Too many attempts.");
            } else if (isAdmin) {
                System.out.println("Welcome, Administrator!");
                System.out.println("You have full system access.");
            } else {
                System.out.println("Welcome, regular user.");
                System.out.println("Limited access granted.");
            }
        } else {
            System.out.println("Please log in to continue.");
        }
    }
}
```

### ✏️ Activity 1 — Decision Tree Lab
Write a program `SeasonChecker.java` that:
1. Stores a month number (1–12) in a variable
2. Uses if-else if to determine and print the season:
   - Dec, Jan, Feb → Winter
   - Mar, Apr, May → Spring
   - Jun, Jul, Aug → Summer
   - Sep, Oct, Nov → Autumn
3. Also prints if the month is in the first or second half of the year
4. Test with at least 3 different month values

### 🎯 Activity 2 — BMI Calculator
Write a program `BMICalculator.java` that:
1. Stores `weight` (kg) and `height` (m) as doubles
2. Calculates BMI: `weight / (height * height)`
3. Uses if-else if to classify:
   - BMI < 18.5 → Underweight
   - 18.5–24.9 → Normal weight
   - 25–29.9 → Overweight
   - ≥ 30 → Obese
4. Prints BMI formatted to 2 decimal places and the classification

### ✅ Weekly Outcome
By the end of Week 11, students can write single, chained, and nested if-else statements, use the ternary operator, and build real decision-making programs.

---

## Week 12 — Java Switch

### 📖 Lesson

The `switch` statement is an alternative to long `if-else if` chains when you are comparing **one variable against multiple specific values**.

#### Traditional `switch` Syntax

```java
switch (expression) {
    case value1:
        // code
        break;        // ← IMPORTANT: prevents "fall-through"
    case value2:
        // code
        break;
    default:
        // runs if no case matches
}
```

> ⚠️ **Fall-through:** If you omit `break`, execution continues into the next `case`. This can be intentional or a bug!

#### What can go in `switch`?
- `int` and `char` (always)
- `String` (since Java 7)
- `enum` types

#### Fall-through Example (intentional)
```java
int month = 4;
switch (month) {
    case 4:
    case 6:
    case 9:
    case 11:
        System.out.println("30 days");
        break;
    case 2:
        System.out.println("28 or 29 days");
        break;
    default:
        System.out.println("31 days");
}
```

#### `if-else` vs `switch` — When to Use Which?

| Use `switch` when… | Use `if-else` when… |
|--------------------|---------------------|
| Comparing one variable to exact values | Comparing ranges (`> 90`, `< 18`) |
| 3+ discrete cases | Complex boolean conditions |
| Using String, int, or char | Comparing multiple variables |

### 🔑 Key Concepts
- switch, case, break, default
- Fall-through behavior
- Switch with String
- When to choose switch over if-else

### 💻 Code Sample — Day of Week

```java
// File: DayOfWeek.java
// Uses switch to print the name of a day given its number.

public class DayOfWeek {
    public static void main(String[] args) {
        int day = 3;

        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day number (use 1-7)");
        }
    }
}
```

### 💻 Code Sample — String Switch (Menu)

```java
// File: MenuSwitch.java
// Demonstrates switch with String values.

public class MenuSwitch {
    public static void main(String[] args) {
        String command = "START";

        switch (command.toUpperCase()) {
            case "START":
                System.out.println("Game is starting...");
                break;
            case "STOP":
                System.out.println("Game stopped.");
                break;
            case "PAUSE":
                System.out.println("Game paused.");
                break;
            case "QUIT":
                System.out.println("Exiting game. Goodbye!");
                break;
            default:
                System.out.println("Unknown command: " + command);
        }
    }
}
```

### ✏️ Activity 1 — Month Days Calculator
Write a program `MonthDays.java` using switch with fall-through to print:
- How many days are in each month (1–12)
- Assume February always has 28 days
- For invalid numbers, print an error message

### 🎯 Activity 2 — Simple ATM Menu
Write a program `ATMMenu.java` that simulates an ATM menu using switch:
- Option `1` → "Checking balance..."
- Option `2` → "Processing withdrawal..."
- Option `3` → "Processing deposit..."
- Option `4` → "Printing mini-statement..."
- Option `0` → "Thank you. Goodbye!"
- Default → "Invalid option. Please try again."
Test it with at least 4 different menu options (change the variable value).

### ✅ Weekly Outcome
By the end of Week 12, students can write correct switch statements, control fall-through with `break`, use switch with both integers and strings, and decide when to use switch vs if-else.

---

## Week 13 — Java While Loop

### 📖 Lesson

A **loop** runs a block of code repeatedly. The `while` loop keeps running **as long as its condition is true**. It checks the condition **before** each iteration.

#### `while` Syntax
```java
while (condition) {
    // body — runs repeatedly while condition is true
    // must have something that eventually makes condition false!
}
```

#### `do-while` Loop
Runs the body **at least once**, then checks the condition.
```java
do {
    // body — runs at least once
} while (condition);
```

**Key difference:**
- `while` — condition checked **before** first run (body may never execute)
- `do-while` — condition checked **after** first run (body executes at least once)

#### Infinite Loops (avoid unless intentional)
```java
// INFINITE LOOP — dangerous if you don't have a break
while (true) {
    System.out.println("This runs forever!");
}
```

#### Loop Control Variables
Always make sure the loop will eventually stop:
```java
int count = 0;           // Initialize
while (count < 5) {      // Condition
    System.out.println(count);
    count++;             // Update — this is what prevents infinite loop
}
```

#### Common Patterns with while
```java
// Pattern 1: Counting up
int i = 1;
while (i <= 10) { System.out.println(i); i++; }

// Pattern 2: Counting down
int j = 10;
while (j > 0) { System.out.println(j); j--; }

// Pattern 3: Accumulator (sum)
int sum = 0, n = 1;
while (n <= 100) { sum += n; n++; }
System.out.println("Sum 1-100: " + sum);
```

### 🔑 Key Concepts
- `while` loop structure (init, condition, update)
- `do-while` and when to use it
- Infinite loop danger and prevention
- Counter patterns, accumulator patterns
- Tracing loop execution by hand

### 💻 Code Sample — Counting and Accumulating

```java
// File: WhileLoopDemo.java
// Demonstrates while and do-while loops with common patterns.

public class WhileLoopDemo {
    public static void main(String[] args) {

        // ---- Pattern 1: Print 1 to 5 ----
        System.out.println("=== Count 1 to 5 ===");
        int count = 1;
        while (count <= 5) {
            System.out.print(count + " ");
            count++;
        }
        System.out.println();

        // ---- Pattern 2: Sum of 1 to 100 ----
        System.out.println("\n=== Sum of 1 to 100 ===");
        int sum = 0;
        int i = 1;
        while (i <= 100) {
            sum += i;
            i++;
        }
        System.out.println("Sum = " + sum);   // 5050

        // ---- Pattern 3: Countdown ----
        System.out.println("\n=== Countdown ===");
        int rocket = 5;
        while (rocket > 0) {
            System.out.println(rocket + "...");
            rocket--;
        }
        System.out.println("Blast off!");

        // ---- do-while: Runs at least once ----
        System.out.println("\n=== do-while example ===");
        int x = 10;
        do {
            System.out.println("do-while body, x = " + x);
            x++;
        } while (x < 10);   // condition is false but body ran once
    }
}
```

### 💻 Code Sample — Multiplication Table

```java
// File: MultiplicationTable.java
// Prints the multiplication table for a given number.

public class MultiplicationTable {
    public static void main(String[] args) {
        int number = 7;
        int multiplier = 1;

        System.out.println("=== Multiplication Table of " + number + " ===");
        while (multiplier <= 12) {
            System.out.printf("%d x %2d = %d%n", number, multiplier, number * multiplier);
            multiplier++;
        }
    }
}
```

### ✏️ Activity 1 — Loop Tracing Worksheet
Trace through each loop by hand. Write the value of the variable at the end of each iteration.

```java
// Trace A
int n = 1, total = 0;
while (n <= 5) {
    total = total + n;
    n++;
}
// What is total? What is n?

// Trace B
int x = 16;
while (x > 1) {
    x = x / 2;
    System.out.println(x);
}
// List the exact output lines.

// Trace C
int a = 1;
do {
    System.out.println(a);
    a *= 3;
} while (a < 100);
// How many lines are printed? What are they?
```

### 🎯 Activity 2 — Number Guessing Hint (While Simulation)
Write a program `GuessSimulator.java` that simulates a guessing game *without user input* using a pre-set "secret number":
1. Set `int secret = 42;`
2. Use a while loop starting at `guess = 1`
3. Each iteration, check if `guess == secret`
4. If not, print `"Trying: [guess]"` and increment guess
5. When found, print `"Found the number! Took [count] tries."`

### ✅ Weekly Outcome
By the end of Week 13, students can write correct while and do-while loops, trace loop execution, implement counter and accumulator patterns, and avoid infinite loops.

---

## Week 14 — Java For Loop

### 📖 Lesson

The `for` loop is the most structured loop in Java. It is ideal when you **know in advance how many times** the loop should run. All three parts (init, condition, update) are on one line.

#### `for` Syntax
```java
for (initialization; condition; update) {
    // body
}
```

| Part | Runs when | Example |
|------|-----------|---------|
| `initialization` | Once, at the start | `int i = 0` |
| `condition` | Before each iteration | `i < 10` |
| `update` | After each iteration | `i++` |

#### Comparison: `for` vs `while`
```java
// for loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// Equivalent while loop
int i = 0;
while (i < 5) {
    System.out.println(i);
    i++;
}
```

Use `for` when you know the exact iteration count. Use `while` when you don't.

#### Nested `for` Loops
```java
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= 3; col++) {
        System.out.print("(" + row + "," + col + ") ");
    }
    System.out.println();
}
```

#### Enhanced for-each Loop (preview)
Used to iterate over arrays and collections (details in Arrays week):
```java
int[] numbers = {10, 20, 30, 40};
for (int num : numbers) {
    System.out.println(num);
}
```

### 🔑 Key Concepts
- for loop three-part structure
- `for` vs `while` — when to use each
- Nested for loops and how they work
- Enhanced for-each loop (preview)
- Counting by different step sizes (`i += 2`, `i *= 2`)

### 💻 Code Sample — For Loop Patterns

```java
// File: ForLoopDemo.java
// Shows various for loop patterns.

public class ForLoopDemo {
    public static void main(String[] args) {

        // Basic: 1 to 10
        System.out.println("=== 1 to 10 ===");
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Counting by 2s (even numbers)
        System.out.println("\n=== Even numbers 2–20 ===");
        for (int i = 2; i <= 20; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Countdown
        System.out.println("\n=== Countdown 10 to 1 ===");
        for (int i = 10; i >= 1; i--) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Powers of 2
        System.out.println("\n=== Powers of 2 ===");
        for (int i = 1; i <= 1024; i *= 2) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Sum of first 10 numbers
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        System.out.println("\nSum 1-10 = " + sum);
    }
}
```

### 💻 Code Sample — Nested For Loops (Star Pattern)

```java
// File: StarPattern.java
// Uses nested for loops to print a right-angle triangle of stars.

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

        // Multiplication table 1-5
        System.out.println("\n=== Multiplication Table (5x5) ===");
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 5; j++) {
                System.out.printf("%4d", i * j);
            }
            System.out.println();
        }
    }
}
```

### ✏️ Activity 1 — Pattern Drawing Lab
Write a program `PatternDraw.java` using nested for loops to print each pattern:

```
Pattern A (5 rows):     Pattern B (inverted):   Pattern C:
* * * * *               * * * * *               1
* * * * *               * * * *                 1 2
* * * * *               * * *                   1 2 3
* * * * *               * *                     1 2 3 4
* * * * *               *                       1 2 3 4 5
```

### 🎯 Activity 2 — FizzBuzz Challenge
Write a program `FizzBuzz.java` using a for loop (1–50) that:
- Prints `Fizz` if the number is divisible by 3
- Prints `Buzz` if the number is divisible by 5
- Prints `FizzBuzz` if divisible by both 3 and 5
- Otherwise prints the number itself

(Hint: Use the modulus operator `%` and check `FizzBuzz` first before `Fizz` or `Buzz`)

### ✅ Weekly Outcome
By the end of Week 14, students can write for loops with custom step sizes, use nested for loops for 2D patterns, explain the difference between for and while, and solve classic problems like FizzBuzz.

---

## Week 15 — Java Break / Continue

### 📖 Lesson

`break` and `continue` are loop control statements that change the normal flow of a loop.

#### `break`
Immediately **exits** the loop (or switch). No more iterations run.

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) {
        break;         // Stop the loop when i reaches 5
    }
    System.out.print(i + " ");  // Prints: 1 2 3 4
}
```

#### `continue`
**Skips** the rest of the current iteration and jumps to the next one.

```java
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;      // Skip even numbers
    }
    System.out.print(i + " ");  // Prints: 1 3 5 7 9
}
```

#### Labeled Loops (breaking out of nested loops)
```java
outer:
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (j == 2) {
            break outer;   // Breaks BOTH loops
        }
        System.out.println("i=" + i + " j=" + j);
    }
}
```

#### When to Use Each

| Statement | Use When |
|-----------|----------|
| `break` | Found what you're looking for (search), menu exit, error |
| `continue` | Skipping certain elements (filtering), avoiding processing |

#### Common Pattern — Linear Search with break

```java
int[] data = {5, 12, 8, 99, 3, 47};
int target = 99;
boolean found = false;
int position = -1;

for (int i = 0; i < data.length; i++) {
    if (data[i] == target) {
        found = true;
        position = i;
        break;    // No need to keep searching once found
    }
}
System.out.println("Found: " + found + " at index " + position);
```

### 🔑 Key Concepts
- `break` to exit a loop early
- `continue` to skip an iteration
- Labeled break for nested loops
- Search pattern with break
- Filter pattern with continue

### 💻 Code Sample — Break and Continue

```java
// File: BreakContinueDemo.java
// Demonstrates break and continue in loops.

public class BreakContinueDemo {
    public static void main(String[] args) {

        // ---- break: stop when condition met ----
        System.out.println("=== break example ===");
        for (int i = 0; i < 10; i++) {
            if (i == 6) {
                System.out.println("Breaking at i=" + i);
                break;
            }
            System.out.print(i + " ");
        }
        System.out.println();

        // ---- continue: skip multiples of 3 ----
        System.out.println("\n=== continue example (skip multiples of 3) ===");
        for (int i = 1; i <= 15; i++) {
            if (i % 3 == 0) {
                continue;   // Skip 3, 6, 9, 12, 15
            }
            System.out.print(i + " ");
        }
        System.out.println();

        // ---- break in while: sum until limit ----
        System.out.println("\n=== break in while: sum until > 50 ===");
        int sum = 0;
        int n = 1;
        while (true) {
            sum += n;
            if (sum > 50) {
                System.out.println("Sum exceeded 50 at n=" + n + ", sum=" + sum);
                break;
            }
            n++;
        }

        // ---- labeled break ----
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

### ✏️ Activity 1 — Loop Tracing with Break/Continue
Trace through and write the exact output of each snippet:

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

### 🎯 Activity 2 — Prime Number Finder
Write a program `PrimeFinder.java` that prints all prime numbers from 2 to 50.
- Use a nested loop: outer loop iterates numbers 2–50, inner loop checks divisibility
- Use `break` when a divisor is found (the number is not prime)
- Use `continue` or a flag variable to skip printing composite numbers

Expected output starts with: `2 3 5 7 11 13 17 19 23...`

### ✅ Weekly Outcome
By the end of Week 15, students can use `break` and `continue` to control loop execution, implement search patterns with break, implement filter patterns with continue, and explain labeled breaks.

---

## Week 16 — Java Arrays — Part 1

### 📖 Lesson

An **array** is a container that holds a **fixed number of values** of the **same data type**. Each value is stored in a numbered slot called an **index** (starting at 0).

#### Declaring and Creating an Array

```java
// Method 1: Declare and create empty array
int[] numbers = new int[5];     // Creates array of 5 integers (all 0 by default)

// Method 2: Declare and initialize with values
int[] grades = {90, 85, 78, 92, 88};

// Method 3: Separate declaration and creation
String[] names;
names = new String[3];
```

#### Accessing Elements

```java
int[] arr = {10, 20, 30, 40, 50};
System.out.println(arr[0]);    // 10  (first element, index 0)
System.out.println(arr[4]);    // 50  (last element, index 4)
arr[2] = 99;                   // Change index 2 from 30 to 99
```

> ⚠️ Accessing index -1 or index ≥ length causes `ArrayIndexOutOfBoundsException`

#### Array Length

```java
int[] arr = {1, 2, 3, 4, 5};
System.out.println(arr.length);   // 5 (property, NOT a method — no parentheses)
```

#### Iterating with for Loop

```java
int[] arr = {10, 20, 30, 40, 50};

// Standard for loop
for (int i = 0; i < arr.length; i++) {
    System.out.println("Index " + i + ": " + arr[i]);
}

// Enhanced for-each
for (int value : arr) {
    System.out.println(value);
}
```

#### Arrays of Different Types

```java
String[] fruits = {"Apple", "Banana", "Cherry"};
double[] prices = {1.50, 0.75, 2.25};
boolean[] flags = {true, false, true};
```

### 🔑 Key Concepts
- Array declaration, creation, initialization
- Zero-based indexing
- `array.length` property
- ArrayIndexOutOfBoundsException
- Iterating with standard for vs for-each
- Default values (0, 0.0, false, null)

### 💻 Code Sample — Array Basics

```java
// File: ArrayBasics.java
// Demonstrates array creation, access, and iteration.

public class ArrayBasics {
    public static void main(String[] args) {

        // Create and initialize an array
        int[] scores = {88, 95, 72, 60, 84, 91, 78};

        // Print array length
        System.out.println("Number of scores: " + scores.length);

        // Access individual elements
        System.out.println("First score: " + scores[0]);
        System.out.println("Last score:  " + scores[scores.length - 1]);

        // Modify an element
        scores[2] = 80;   // Replace 72 with 80
        System.out.println("Updated index 2: " + scores[2]);

        // Print all using standard for
        System.out.println("\n--- All scores (standard for) ---");
        for (int i = 0; i < scores.length; i++) {
            System.out.println("scores[" + i + "] = " + scores[i]);
        }

        // Print all using for-each
        System.out.println("\n--- All scores (for-each) ---");
        for (int score : scores) {
            System.out.print(score + " ");
        }
        System.out.println();
    }
}
```

### 💻 Code Sample — Find Min, Max, and Average

```java
// File: ArrayStats.java
// Calculates minimum, maximum, and average of an array.

public class ArrayStats {
    public static void main(String[] args) {
        int[] data = {34, 67, 12, 89, 45, 22, 78, 55};

        int min = data[0];   // Start with first element
        int max = data[0];
        int total = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i] < min) min = data[i];
            if (data[i] > max) max = data[i];
            total += data[i];
        }

        double average = (double) total / data.length;

        System.out.println("Array: ");
        for (int val : data) System.out.print(val + " ");
        System.out.println();
        System.out.println("Minimum: " + min);
        System.out.println("Maximum: " + max);
        System.out.println("Total:   " + total);
        System.out.printf("Average: %.2f%n", average);
    }
}
```

### ✏️ Activity 1 — Array Initialization and Access Drill
Write a program `ArrayDrill.java` that:
1. Creates a String array of 5 student names
2. Creates an int array of their corresponding test scores
3. Prints each student and their score side by side: `[Name]: [Score]`
4. Changes the second student's score to a new value and reprints
5. Prints the score at the last index using `arr.length - 1`

### 🎯 Activity 2 — Gradebook Program
Write a program `Gradebook.java` that:
1. Stores 8 exam scores in an array: `{72, 88, 65, 91, 77, 84, 59, 93}`
2. Finds and prints the highest and lowest scores
3. Calculates and prints the class average
4. Counts how many students scored 80 or above ("passed with merit") and prints the count
5. Counts how many scored below 60 ("failed") and prints the count

### ✅ Weekly Outcome
By the end of Week 16, students can declare, create, initialize, and iterate over 1D arrays, access and modify elements, and compute basic statistics (min, max, average, count).

---

## Week 17 — Java Arrays — Part 2

### 📖 Lesson

This week builds on the basics with more array algorithms and introduces **2D arrays**.

#### Linear Search

Searching an array one element at a time:

```java
int[] arr = {15, 42, 8, 77, 23};
int target = 77;
int foundIndex = -1;

for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
        foundIndex = i;
        break;
    }
}

if (foundIndex != -1) {
    System.out.println("Found at index: " + foundIndex);
} else {
    System.out.println("Not found.");
}
```

#### Copying an Array

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = new int[original.length];

for (int i = 0; i < original.length; i++) {
    copy[i] = original[i];
}
```

> ⚠️ **Never do** `int[] copy = original;` — that makes both variables point to the **same** array!

#### Reversing an Array

```java
int[] arr = {1, 2, 3, 4, 5};
int left = 0, right = arr.length - 1;
while (left < right) {
    int temp = arr[left];
    arr[left] = arr[right];
    arr[right] = temp;
    left++;
    right--;
}
// arr is now {5, 4, 3, 2, 1}
```

#### 2D Arrays

A 2D array is like a **table with rows and columns**:

```java
// Declare and initialize a 3x3 matrix
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Access element at row 1, column 2 (0-indexed)
System.out.println(matrix[1][2]);   // 6

// Iterate with nested for loops
for (int row = 0; row < matrix.length; row++) {
    for (int col = 0; col < matrix[row].length; col++) {
        System.out.printf("%3d", matrix[row][col]);
    }
    System.out.println();
}
```

#### `Arrays` Utility Class (brief intro)
```java
import java.util.Arrays;

int[] arr = {5, 3, 8, 1, 9};
Arrays.sort(arr);                         // Sort in ascending order
System.out.println(Arrays.toString(arr)); // [1, 3, 5, 8, 9]
```

### 🔑 Key Concepts
- Linear search algorithm
- Array copy vs reference copy
- Array reversal algorithm
- 2D array declaration, initialization, access
- Nested loops for 2D traversal
- `Arrays.sort()` and `Arrays.toString()`

### 💻 Code Sample — Search and Reverse

```java
// File: ArrayAlgorithms.java
// Demonstrates linear search and array reversal.

import java.util.Arrays;

public class ArrayAlgorithms {
    public static void main(String[] args) {
        int[] numbers = {42, 15, 88, 7, 33, 65, 21, 90};

        // ---- Linear Search ----
        int target = 65;
        int foundAt = -1;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == target) {
                foundAt = i;
                break;
            }
        }
        System.out.println("Searching for: " + target);
        System.out.println(foundAt != -1
            ? "Found at index " + foundAt
            : "Not found");

        // ---- Sort ----
        System.out.println("\nBefore sort: " + Arrays.toString(numbers));
        Arrays.sort(numbers);
        System.out.println("After sort:  " + Arrays.toString(numbers));

        // ---- Reverse (after sort, so we see descending) ----
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int temp = numbers[left];
            numbers[left] = numbers[right];
            numbers[right] = temp;
            left++;
            right--;
        }
        System.out.println("Reversed:    " + Arrays.toString(numbers));
    }
}
```

### 💻 Code Sample — 2D Array Matrix

```java
// File: MatrixDemo.java
// Demonstrates 2D arrays with row and column iteration.

public class MatrixDemo {
    public static void main(String[] args) {
        // 3x4 matrix of student scores
        // Rows = students, Columns = subjects
        int[][] scores = {
            {85, 90, 78, 92},   // Student 0
            {72, 68, 80, 75},   // Student 1
            {95, 88, 91, 97}    // Student 2
        };

        String[] subjects = {"Math", "Science", "English", "History"};

        // Print formatted table
        System.out.printf("%-10s", "Student");
        for (String subj : subjects) System.out.printf("%-10s", subj);
        System.out.printf("%-10s%n", "Average");
        System.out.println("-".repeat(60));

        for (int row = 0; row < scores.length; row++) {
            System.out.printf("%-10s", "Student " + row);
            int rowTotal = 0;
            for (int col = 0; col < scores[row].length; col++) {
                System.out.printf("%-10d", scores[row][col]);
                rowTotal += scores[row][col];
            }
            System.out.printf("%-10.2f%n", (double) rowTotal / scores[row].length);
        }
    }
}
```

### ✏️ Activity 1 — Search and Sort Lab
Write a program `SearchSortLab.java`:
1. Create an int array of 10 numbers
2. Print the array using `Arrays.toString()`
3. Ask the user to search for a value (use a hardcoded variable)
4. Perform linear search — print position or "not found"
5. Sort the array and print again
6. Reverse the sorted array manually (using a loop, not `Collections.reverse`) and print

### 🎯 Activity 2 — 2D Grade Sheet
Write a program `GradeSheet.java` with a 4×5 2D array (4 students, 5 subjects):
1. Initialize with your own scores
2. Print the full grade table with headers
3. Calculate and print each student's average (row average)
4. Calculate and print each subject's class average (column average)
5. Find and print the highest single score in the entire 2D array

### ✅ Weekly Outcome
By the end of Week 17, students can implement linear search, copy and reverse arrays, declare and traverse 2D arrays, compute row and column statistics, and use `Arrays.sort()` and `Arrays.toString()`.

---

## Week 18 — Arrays Mini-Project & Integration

### 📖 Lesson

This week is an **integration week**. The focus is on combining everything learned so far — especially arrays, loops, conditionals, and output formatting — into a meaningful small project.

**Review Topics Combined:**
- Variables and data types (Weeks 5–6)
- Operators and type casting (Weeks 7–8)
- If-else and switch (Weeks 11–12)
- While and for loops (Weeks 13–14)
- Break/continue (Week 15)
- Arrays Part 1 & 2 (Weeks 16–17)

**Mini-Project — Student Grade Management System**

You will build a console-based grade management program. The project ties together:
- Arrays to store names and scores
- Loops to process all students
- Conditionals to classify grades
- Output formatting for a clean report

### 🔑 Key Concepts (Review)
- Combining arrays, loops, and conditions
- Designing a complete program from scratch
- Code organization and commenting
- Edge cases (empty array, all same score, etc.)

### 💻 Code Sample — Grade Management System

```java
// File: GradeManagement.java
// A complete student grade management program using arrays and loops.
// Demonstrates integration of Weeks 5–17 concepts.

public class GradeManagement {
    public static void main(String[] args) {

        // ---- Data ----
        String[] students = {
            "Ana Reyes", "Ben Santos", "Carla Lim", "Dan Cruz",
            "Eva Torres", "Felix Ong", "Grace Tan", "Henry Sy"
        };

        int[] scores = {88, 72, 95, 61, 84, 57, 90, 79};

        // ---- Report Header ----
        System.out.println("=".repeat(55));
        System.out.println("         STUDENT GRADE REPORT");
        System.out.println("=".repeat(55));
        System.out.printf("%-20s %-8s %-12s %s%n", "Name", "Score", "Grade", "Status");
        System.out.println("-".repeat(55));

        // ---- Statistics Variables ----
        int total = 0;
        int highest = scores[0];
        int lowest  = scores[0];
        String topStudent = students[0];
        int passCount = 0, failCount = 0;

        // ---- Process Each Student ----
        for (int i = 0; i < students.length; i++) {
            int s = scores[i];
            total += s;

            // Find highest and lowest
            if (s > highest) { highest = s; topStudent = students[i]; }
            if (s < lowest)  { lowest  = s; }

            // Determine letter grade
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

        // ---- Summary ----
        double avg = (double) total / students.length;
        System.out.println("=".repeat(55));
        System.out.printf("Total students: %d | Passed: %d | Failed: %d%n",
                           students.length, passCount, failCount);
        System.out.printf("Class average:  %.2f%n", avg);
        System.out.printf("Highest score:  %d (%s)%n", highest, topStudent);
        System.out.printf("Lowest score:   %d%n", lowest);
        System.out.println("=".repeat(55));
    }
}
```

### ✏️ Activity 1 — Extend the Grade System
Extend `GradeManagement.java` with the following features:
1. Add a second array for a second exam. Compute a final score as `(exam1 + exam2) / 2`.
2. Sort students by their final score descending (use bubble sort or selection sort using loops).
3. Print rank numbers (1st, 2nd, …) in the report.

### 🎯 Activity 2 — Personal Project: Inventory System
Create a new program `Inventory.java` that manages a simple product inventory:
- Arrays for: product names (String), quantities (int), unit prices (double)
- At least 6 products
- Print a formatted inventory table
- Calculate total inventory value (`quantity × price` for each item, sum all)
- Find most expensive and least expensive product
- List all products with quantity < 5 (low stock warning)

### ✅ Weekly Outcome
By the end of Week 18, students have built a complete multi-array program, applied all control flow and array operations in an integrated context, and practiced clean formatting and code organization.

---

## Week 19 — Comprehensive Review

### 📖 Lesson

This is the final review week before the Final Exam. The goal is to consolidate everything from Weeks 1–18, identify remaining weak spots, and practice exam-style questions.

### 📋 Complete Course Summary

| Topic | Key Items to Remember |
|-------|----------------------|
| Java Intro | JDK/JRE/JVM, platform independence, main method |
| Get Started | Compile-run cycle, IDE, naming rules |
| Syntax | Semicolons, braces, case sensitivity, conventions |
| Output | println/print/printf, escape sequences, format specifiers |
| Variables | Declaration, initialization, final, scope |
| Data Types | 8 primitives, reference types, sizes, overflow |
| Type Casting | Widening/narrowing, parseInt, parseDouble, valueOf |
| Operators | Arithmetic, assignment, comparison, logical, increment |
| Strings | Methods: length, charAt, substring, equals, contains, replace |
| Math | abs, max, min, pow, sqrt, round, floor, ceil, random, PI |
| Booleans | Boolean logic, truth tables, short-circuit |
| If-Else | if, if-else, if-else-if, ternary, nested |
| Switch | case, break, fall-through, default, String switch |
| While Loop | while, do-while, infinite loop prevention |
| For Loop | for syntax, nested loops, for-each |
| Break/Continue | break (exit), continue (skip), labeled break |
| Arrays Pt 1 | Declaration, indexing, length, iterate, min/max/avg |
| Arrays Pt 2 | Search, copy, reverse, 2D arrays, Arrays.sort |

### 💻 Code Sample — Comprehensive Review Problems

```java
// File: ReviewProblems.java
// Mini-challenges covering the full course syllabus.

import java.util.Arrays;

public class ReviewProblems {
    public static void main(String[] args) {

        // ---- Problem 1: Classify a number ----
        int number = 17;
        System.out.println("=== Problem 1: Classify " + number + " ===");
        if (number > 0) {
            System.out.println("Positive");
        } else if (number < 0) {
            System.out.println("Negative");
        } else {
            System.out.println("Zero");
        }
        System.out.println("Even or Odd: " + (number % 2 == 0 ? "Even" : "Odd"));

        // ---- Problem 2: String analysis ----
        String phrase = "Java Programming";
        System.out.println("\n=== Problem 2: String Analysis ===");
        System.out.println("Length:     " + phrase.length());
        System.out.println("Upper:      " + phrase.toUpperCase());
        System.out.println("First word: " + phrase.substring(0, phrase.indexOf(' ')));
        System.out.println("Contains 'gram': " + phrase.contains("gram"));

        // ---- Problem 3: Sum of odd numbers 1–99 ----
        System.out.println("\n=== Problem 3: Sum of odd numbers 1–99 ===");
        int oddSum = 0;
        for (int i = 1; i <= 99; i += 2) {
            oddSum += i;
        }
        System.out.println("Sum of odd numbers: " + oddSum);

        // ---- Problem 4: Find first negative number ----
        int[] values = {5, 12, -3, 8, -7, 20};
        System.out.println("\n=== Problem 4: Find first negative ===");
        for (int val : values) {
            if (val < 0) {
                System.out.println("First negative: " + val);
                break;
            }
        }

        // ---- Problem 5: 2D array diagonal sum ----
        int[][] grid = {{1,2,3},{4,5,6},{7,8,9}};
        int diagSum = 0;
        for (int i = 0; i < grid.length; i++) {
            diagSum += grid[i][i];
        }
        System.out.println("\n=== Problem 5: Diagonal sum ===");
        System.out.println("Main diagonal sum: " + diagSum);  // 1+5+9=15
    }
}
```

### ✏️ Activity 1 — Final Exam Practice Set
Complete these 10 short coding challenges (implement each as a separate method or in separate files):
1. Reverse a string character by character
2. Count vowels in a sentence
3. Find the second-largest number in an array
4. Print a diamond pattern using nested loops
5. Check if an array is sorted in ascending order
6. Calculate factorial of n using a while loop
7. Print all numbers divisible by both 3 and 7 between 1–200
8. Find duplicates in an array (print any value that appears more than once)
9. Count words in a sentence (split on spaces)
10. Build a string of asterisks of a given length using a for loop

### 🎯 Activity 2 — Peer Code Review
Exchange your code from Activity 1 with a classmate.
Review their code for:
- [ ] Correct logic and output
- [ ] Proper naming conventions
- [ ] Adequate comments
- [ ] No unnecessary code duplication
- [ ] Correct handling of edge cases (empty array, zero, negative input)

Write a short review note (3–5 sentences) for each piece of code reviewed.

### ✅ Weekly Outcome
By the end of Week 19, students have reviewed every major topic, solved representative exam-style problems, and identified personal weak spots to focus on before the final.

---

## Week 20 — Final Exam Week

### 📖 Lesson

The final exam covers the entire course (Weeks 1–19). There is no new material this week. Students should focus on:
- Completing the practice set from Week 19
- Re-reading weekly code samples that were difficult
- Tracing through programs on paper (no IDE)
- Reviewing common pitfalls listed below

**Common Final Exam Pitfalls:**
1. Comparing Strings with `==` instead of `.equals()`
2. Off-by-one errors in array loops (`< length` vs `<= length`)
3. Forgetting `break` in switch cases
4. Integer division when decimal result is needed (cast first)
5. Modifying a loop variable inside the loop (causes incorrect count)
6. Confusing `=` (assignment) with `==` (comparison) in conditions
7. Forgetting that `char` to `int` gives Unicode value
8. Using `length()` for arrays (arrays use `.length` without parentheses)

### 📋 Final Exam Coverage

| Category | Topics | % of Exam |
|----------|--------|-----------|
| Foundations | Syntax, Output, Variables, Types, Casting | 20% |
| Operators & Logic | Operators, Booleans | 10% |
| Strings & Math | String methods, Math class | 15% |
| Control Flow | If-Else, Switch | 20% |
| Loops | While, For, Break/Continue | 20% |
| Arrays | 1D & 2D Arrays, Algorithms | 15% |

### 💻 Final Exam Sample Problems

```java
// FINAL EXAM SAMPLE — Attempt these before looking at solutions

// --- Question 1 (10 pts) ---
// Write a method that takes an int array and returns the count of
// even numbers in the array.

// --- Question 2 (15 pts) ---
// Write a program that reads a sentence (hardcoded String) and:
//   a) Prints the number of characters
//   b) Prints the number of uppercase letters
//   c) Replaces all spaces with underscores and prints the result

// --- Question 3 (20 pts) ---
// Write a program to find all pairs of numbers in an array whose
// sum equals a given target value.
// Example: array = {2, 7, 11, 15, 3, 6}, target = 9
// Output: (2, 7) and (3, 6)

// --- Question 4 (25 pts) ---
// Write a complete gradebook program:
//   - 5 students, each with 3 test scores stored in a 2D array
//   - Calculate each student's average
//   - Print a formatted table with names, scores, average, and pass/fail
//   - Print the overall class average

// --- Question 5 (30 pts — comprehensive) ---
// Write a program that:
//   a) Creates a String array of 8 words
//   b) Prints them in reverse order (last to first, using a loop)
//   c) Counts how many words have more than 4 letters
//   d) Prints all words that start with a vowel (A, E, I, O, U)
//   e) Builds a single String joining all words with commas
```

### ✏️ Activity 1 — Final Exam Simulation
**Timed: 120 minutes | Total: 100 points**

Attempt the 5 Sample Problems above under timed, closed-book conditions. Write your solutions on paper first (no IDE), then type them in and verify.

### 🎯 Activity 2 — Portfolio Reflection
After the exam, write a short reflection (1 page):
1. What was the most challenging topic for you? Why?
2. Which topic do you feel most confident about?
3. How has your understanding of programming changed since Week 1?
4. What would you do differently if you were starting the course again?
5. What Java topic do you most want to learn next?

### ✅ Weekly Outcome (Course Outcome)
By the end of Week 20, students have:
- Demonstrated mastery of introductory Java from syntax through arrays
- Written complete Java programs that integrate multiple concepts
- Developed problem-solving habits (trace first, code second)
- Built a foundation for intermediate Java (OOP, collections, files)

---

## 🏆 FINAL EXAM — Week 20

**Coverage:** Weeks 1–19 (Full Course)  
**Topics:** Java Intro through Arrays (all topics listed in the Table of Contents)  
**Format:** Written + practical coding exam

---

## 📊 Grade Distribution

| Component | Weight |
|-----------|--------|
| Weekly Activities (2 per week × 18 active weeks) | 40% |
| Midterm Exam (Week 10) | 25% |
| Final Exam (Week 20) | 35% |
| **Total** | **100%** |

---

## 📈 Learning Progression

```
Week 1-2   → Environment & Foundations
Week 3-4   → Language Basics (syntax, output)
Week 5-6   → Data (variables, types)
Week 7-8   → Operations (casting, operators)
Week 9-10  → Utility + MIDTERM
Week 11-12 → Decision Making (if-else, switch)
Week 13-15 → Repetition (while, for, break)
Week 16-17 → Data Structures (arrays)
Week 18    → Integration Project
Week 19-20 → Review + FINAL
```

---

## 📚 Recommended Resources

| Resource | Type | URL / Notes |
|----------|------|-------------|
| W3Schools Java Tutorial | Website | w3schools.com/java |
| Oracle Java Documentation | Official Docs | docs.oracle.com/en/java |
| MOOC.fi Java Programming | Free Course | mooc.fi/en |
| Codecademy Learn Java | Interactive | codecademy.com |
| Exercism Java Track | Practice Problems | exercism.org/tracks/java |

---

*Last updated: 2026 | Course level: Introductory | Language: Java 17*
