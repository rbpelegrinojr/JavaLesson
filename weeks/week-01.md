# Week 01 — Java Introduction

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

Java is one of the most popular programming languages in the world. It was created by **James Gosling** at Sun Microsystems in **1995** and is now owned by Oracle. Java follows the principle of **"Write Once, Run Anywhere"** — meaning code written on one machine can run on any machine that has Java installed.

**Why learn Java?**
- Used in Android app development, web back-ends, enterprise software, and games
- Object-oriented from the ground up
- Strongly typed, which helps beginners learn disciplined coding habits
- Huge community and job market demand

**Java's three-layer architecture:**

| Layer | Full Name | Role |
|-------|-----------|------|
| JDK | Java Development Kit | Tools to *write and compile* Java programs |
| JRE | Java Runtime Environment | Libraries needed to *run* Java programs |
| JVM | Java Virtual Machine | Executes Java bytecode on your specific OS |

When you write `Hello.java`, the **compiler** (part of JDK) turns it into `Hello.class` (bytecode). The **JVM** reads and runs that bytecode on your machine.

---

## 🔑 Key Concepts

- Java language history and use cases
- JDK vs JRE vs JVM distinction
- What "platform independence" means
- Difference between compiled vs interpreted languages

---

## 💻 Code Sample — Your Very First Java Program

```java
// File: HelloWorld.java
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
- `public class HelloWorld` — every Java program lives inside a class
- `public static void main(String[] args)` — the entry point; Java always starts here
- `System.out.println(...)` — prints text followed by a new line
- `"Hello, World!"` — a String literal (text in double quotes)

---

## ✏️ Activity 1 — Research Worksheet

Answer the following questions in your notebook or a text file:

1. What does JVM stand for, and what is its job?
2. Name three real-world applications built with Java.
3. What is the difference between the JDK and the JRE?
4. Why is Java called "platform independent"?
5. What file extension does compiled Java bytecode use?

---

## 🎯 Activity 2 — "Hello, Me!" Program

Write a Java program that prints:
```
Hello, I am [Your Name]!
I am learning Java.
Today is Week 1.
```
- Replace `[Your Name]` with your actual name.
- Each sentence must be on its own line.
- Save the file as `HelloMe.java` and run it.

---

## 📝 Quiz — Week 01

**Instructions:** Choose the best answer for each question. (10 points total — 2 pts each)

**1.** Who created Java?
- A) Bill Gates
- B) Linus Torvalds
- C) James Gosling ✓
- D) Dennis Ritchie

**2.** What does JVM stand for?
- A) Java Variable Machine
- B) Java Virtual Machine ✓
- C) Java Verified Module
- D) Java Visual Manager

**3.** What does "Write Once, Run Anywhere" mean?
- A) You can write Java code once without comments
- B) Java code can run on any OS that has a JVM ✓
- C) You only need to run a Java program once
- D) Java programs write themselves

**4.** Which component converts `.java` source code into `.class` bytecode?
- A) JRE
- B) JVM
- C) IDE
- D) Compiler (part of JDK) ✓

**5.** What is the entry point method in a Java program?
- A) `start()`
- B) `run()`
- C) `main()` ✓
- D) `begin()`

---

## ✅ Weekly Outcome

By the end of Week 1, you can:
- Explain what Java is and where it is used
- Describe the JDK/JRE/JVM relationship
- Write a minimal Java program and run it successfully
