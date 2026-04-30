# Week 06 — Java Data Types

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

Java is a **strongly typed** language — every variable must be declared with a type. Types fall into two categories.

### Primitive Data Types (8 total)

| Type | Size | Range / Values | Example |
|------|------|----------------|---------|
| `byte` | 1 byte | -128 to 127 | `byte b = 100;` |
| `short` | 2 bytes | -32,768 to 32,767 | `short s = 1000;` |
| `int` | 4 bytes | ~-2 billion to 2 billion | `int n = 50000;` |
| `long` | 8 bytes | Very large integers | `long l = 1234567890L;` |
| `float` | 4 bytes | ~7 decimal digits | `float f = 3.14f;` |
| `double` | 8 bytes | ~15 decimal digits | `double d = 3.14159;` |
| `boolean` | 1 bit | `true` or `false` | `boolean b = true;` |
| `char` | 2 bytes | Unicode character | `char c = 'Z';` |

> **Note:** `long` literals need an `L` suffix. `float` literals need an `f` suffix.

### Reference Data Types

Store a *reference* (memory address) to an object.
- `String` — a sequence of characters
- Arrays
- Objects (classes)

**Key difference:** Primitives hold the **actual value**; reference types hold an **address**.

### Integer Overflow

```java
byte b = 127;
b++;        // b becomes -128 (wraps around!)
```

---

## 🔑 Key Concepts

- 8 primitive types and their sizes
- Reference types vs primitive types
- When to use `int` vs `long`, `float` vs `double`
- Integer overflow
- Default values (0, 0.0, false, '\u0000', null)

---

## 💻 Code Sample 1 — All Primitive Types

```java
// File: DataTypesDemo.java
public class DataTypesDemo {
    public static void main(String[] args) {
        byte    myByte    = 100;
        short   myShort   = 5000;
        int     myInt     = 100000;
        long    myLong    = 15000000000L;
        float   myFloat   = 5.99f;
        double  myDouble  = 19.99;
        boolean myBool    = true;
        char    myChar    = 'J';

        System.out.println("byte:    " + myByte);
        System.out.println("short:   " + myShort);
        System.out.println("int:     " + myInt);
        System.out.println("long:    " + myLong);
        System.out.println("float:   " + myFloat);
        System.out.println("double:  " + myDouble);
        System.out.println("boolean: " + myBool);
        System.out.println("char:    " + myChar);

        String myString = "Hello Java";
        System.out.println("String:  " + myString);
    }
}
```

---

## 💻 Code Sample 2 — Overflow

```java
// File: OverflowDemo.java
public class OverflowDemo {
    public static void main(String[] args) {
        byte b = 127;
        System.out.println("Before: " + b);    // 127
        b++;
        System.out.println("After:  " + b);    // -128  (overflow!)

        int maxInt = Integer.MAX_VALUE;
        System.out.println("Max int:     " + maxInt);
        System.out.println("Max int + 1: " + (maxInt + 1));  // wraps to MIN_VALUE
    }
}
```

---

## ✏️ Activity 1 — Data Type Selection Worksheet

For each scenario, choose the best type and justify:
1. Storing a student's age (0–150)
2. Storing a country's population (up to 8 billion)
3. Storing a product price like ₱1,299.95
4. Storing whether a student passed or failed
5. Storing a student's middle initial
6. Storing a student's full name
7. Storing the distance between stars
8. Storing a weight with 2 decimal places

---

## 🎯 Activity 2 — Coded Receipt

Write `ItemReceipt.java` using appropriate types for:
- Item name, quantity, unit price, discount %, total after discount, tax included?

Print a formatted receipt using `printf`.

---

## 📝 Quiz — Week 06

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** Which data type stores a single character?
- A) `String`
- B) `char` ✓
- C) `byte`
- D) `int`

**2.** Which suffix is required for `float` literals?
- A) `d`
- B) `L`
- C) `f` ✓
- D) No suffix

**3.** What is the default value of a `boolean` field?
- A) `true`
- B) `null`
- C) `0`
- D) `false` ✓

**4.** Which type can store 15 billion?
- A) `int`
- B) `short`
- C) `long` ✓
- D) `byte`

**5.** What happens when a `byte` variable holding 127 is incremented?
- A) It becomes 128
- B) A compile error occurs
- C) It wraps around to -128 ✓
- D) It becomes null

---

## ✅ Weekly Outcome

By the end of Week 6, you can:
- Name all 8 primitive types and their sizes
- Choose the correct type for a given scenario
- Explain primitive vs reference types
- Handle type suffixes (`L`, `f`)
