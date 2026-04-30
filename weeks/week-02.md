# Week 02 — Java Get Started

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

Before writing serious Java code you need a proper development environment. This week you will install the tools and learn the compile-run cycle.

**Step 1 — Install the JDK**
1. Go to oracle.com/java/technologies/downloads
2. Download **JDK 17** (Long-Term Support) for your OS
3. Run the installer and follow the prompts
4. Verify: open a terminal and type `java -version` and `javac -version`

**Step 2 — Choose an IDE**

| IDE | Best For |
|-----|----------|
| IntelliJ IDEA Community | Beginners to professionals |
| Eclipse | University courses |
| VS Code + Java Extension Pack | Lightweight setup |

**Step 3 — The compile-run cycle**
```
Source (.java) → javac → Bytecode (.class) → java JVM → Output
```

**Step 4 — Java file naming rules**
- File name must **exactly match** the public class name (case-sensitive)
- `MyProgram.java` → class must be named `MyProgram`
- Use PascalCase; no spaces in file names

---

## 🔑 Key Concepts

- Installing and verifying JDK
- IDE setup and basic navigation
- Compile-run cycle (`javac` and `java` commands)
- File naming rules and case sensitivity
- Reading basic compiler error messages

---

## 💻 Code Sample 1 — Setup Test

```java
// File: SetupTest.java
public class SetupTest {
    public static void main(String[] args) {
        System.out.println("Java setup is working!");
        System.out.println("JDK is installed correctly.");
        System.out.println("Ready to start coding.");
    }
}
```

**How to run from command line:**
```bash
javac SetupTest.java   # compile
java SetupTest         # run
```

**Expected Output:**
```
Java setup is working!
JDK is installed correctly.
Ready to start coding.
```

---

## 💻 Code Sample 2 — Intentional Error (Learn to Read Errors)

```java
// File: BrokenProgram.java — has a deliberate error, find and fix it!
public class BrokenProgram {
    public static void main(String[] args) {
        System.out.println("This will not compile")  // Missing semicolon!
    }
}
```
The compiler error: `BrokenProgram.java:4: error: ';' expected`
Fix: add `;` at the end of the println line.

---

## ✏️ Activity 1 — Environment Setup Lab

1. Install JDK 17 (or verify it is installed)
2. Install IntelliJ IDEA Community Edition
3. Create a new Java project called `Week02Lab`
4. Write and run `SetupTest.java` from the sample above
5. Take a screenshot of the successful output and submit it

---

## 🎯 Activity 2 — Fix the Bugs Drill

Each snippet has one bug. Identify and fix each:

```java
// Bug 1 — what is wrong?
public class Bug1 {
    public static void main(String[] args) {
        System.out.println("Fix me)
    }
}

// Bug 2 — hint: class name vs file name
public class bug2 {
    public static void main(String[] args) {
        System.out.println("Class name issue");
    }
}

// Bug 3 — hint: something is missing
public class Bug3 {
    public static void main(String[] args)
        System.out.println("Missing something");
    }
}
```

Write the corrected version of each program and explain what was wrong.

---

## 📝 Quiz — Week 02

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** Which command compiles a Java file named `Hello.java`?
- A) `java Hello.java`
- B) `javac Hello.java` ✓
- C) `compile Hello.java`
- D) `run Hello.java`

**2.** Which command runs a compiled Java class named `Hello`?
- A) `javac Hello`
- B) `run Hello`
- C) `java Hello` ✓
- D) `execute Hello`

**3.** If your class is named `StudentInfo`, what must the file be named?
- A) `studentinfo.java`
- B) `student_info.java`
- C) `StudentInfo.java` ✓
- D) `STUDENTINFO.java`

**4.** What file extension does compiled Java bytecode have?
- A) `.java`
- B) `.exe`
- C) `.jar`
- D) `.class` ✓

**5.** What does a compiler do?
- A) Runs the program
- B) Converts source code to bytecode ✓
- C) Installs the JDK
- D) Checks for logic errors

---

## ✅ Weekly Outcome

By the end of Week 2, you can:
- Set up a working Java development environment
- Compile and run programs from the IDE and command line
- Read and interpret basic compiler error messages
