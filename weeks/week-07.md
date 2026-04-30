# Week 07 — Java Type Casting

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

**Type casting** converts a value from one data type to another.

### 1. Widening (Implicit) Casting — Automatic

Java automatically converts a *smaller* type to a *larger* type (no data loss).

**Order:** `byte → short → int → long → float → double`

```java
int myInt = 100;
double myDouble = myInt;   // automatic — no cast needed
System.out.println(myDouble);  // 100.0
```

### 2. Narrowing (Explicit) Casting — Manual

Converting a *larger* type to *smaller* type **requires** an explicit cast (data may be lost).

```java
double price = 9.99;
int truncated = (int) price;   // decimal part dropped (not rounded)
System.out.println(truncated); // 9
```

**Syntax:** `targetType varName = (targetType) originalValue;`

### Common Casting Scenarios

| Situation | Type | Notes |
|-----------|------|-------|
| `int` → `double` | Widening | Safe |
| `double` → `int` | Narrowing | Decimal lost |
| `char` → `int` | Widening | Unicode value |
| `int` → `char` | Narrowing | Valid if valid char code |
| `int` → `String` | `String.valueOf(n)` | — |
| `String` → `int` | `Integer.parseInt(s)` | May throw exception |

---

## 🔑 Key Concepts

- Widening vs narrowing casting
- Explicit cast syntax `(type)`
- Truncation (NOT rounding) on narrowing
- `parseInt`, `parseDouble`, `String.valueOf`
- Why casting is needed (type safety)

---

## 💻 Code Sample 1 — Widening and Narrowing

```java
// File: TypeCastingDemo.java
public class TypeCastingDemo {
    public static void main(String[] args) {

        // Widening (automatic)
        int myInt = 200;
        long myLong     = myInt;
        float myFloat   = myLong;
        double myDouble = myFloat;
        System.out.println("Widening: " + myDouble); // 200.0

        // Narrowing (explicit)
        double val = 9.99;
        int truncated = (int) val;
        System.out.println("Narrowed: " + truncated); // 9

        // char <-> int
        char letter = 'A';
        int unicode = letter;   // widening
        System.out.println("'A' as int: " + unicode);  // 65

        int code = 90;
        char fromCode = (char) code;   // narrowing
        System.out.println("90 as char: " + fromCode); // Z
    }
}
```

---

## 💻 Code Sample 2 — String/Number Conversions

```java
// File: ParseDemo.java
public class ParseDemo {
    public static void main(String[] args) {
        // String → int
        String strAge = "21";
        int age = Integer.parseInt(strAge);
        System.out.println("Parsed age:         " + age);
        System.out.println("Age in 10 years:    " + (age + 10));

        // String → double
        String strPrice = "199.95";
        double price = Double.parseDouble(strPrice);
        System.out.printf("Price + 10%% tax: %.2f%n", price * 1.10);

        // int → String
        int score = 95;
        String scoreStr = String.valueOf(score);
        System.out.println("Score as String:    " + scoreStr);
        System.out.println("String length:      " + scoreStr.length());
    }
}
```

---

## ✏️ Activity 1 — Casting Prediction Worksheet

Predict the output *without* running the code. Then verify.

```java
// A
double x = 8.9;
int y = (int) x;
System.out.println(y);

// B
int a = 65;
char c = (char) a;
System.out.println(c);

// C
String s = "150";
int n = Integer.parseInt(s);
System.out.println(n + 50);

// D
int p = 7, q = 2;
System.out.println(p / q);
System.out.println((double) p / q);
```

---

## 🎯 Activity 2 — GPA Calculator (Type Casting Focus)

Write `GPACalculator.java` that:
1. Stores 5 grades as `int` values
2. Calculates the total as `int`
3. Casts appropriately to compute average as `double`
4. Prints the average to 2 decimal places
5. Prints the average truncated to the nearest `int` using casting

---

## 📝 Quiz — Week 07

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** Which conversion is widening?
- A) `double` → `int`
- B) `int` → `byte`
- C) `int` → `double` ✓
- D) `long` → `int`

**2.** What is the result of `(int) 7.9`?
- A) 8
- B) 7 ✓
- C) 7.9
- D) Compile error

**3.** Which method converts a String to an int?
- A) `String.toInt()`
- B) `Integer.valueOf()`
- C) `Integer.parseInt()` ✓
- D) `Int.parse()`

**4.** What does `(char) 65` produce?
- A) `"65"`
- B) `65`
- C) `A` ✓
- D) Compile error

**5.** Narrowing casting requires:
- A) No special syntax
- B) The `wide` keyword
- C) An explicit cast `(type)` ✓
- D) Using a helper method

---

## ✅ Weekly Outcome

By the end of Week 7, you can:
- Distinguish widening from narrowing casting
- Write explicit casts correctly
- Convert between `String` and numeric types using parse methods
