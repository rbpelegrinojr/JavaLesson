# Week 09 — Java Strings & Java Math

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson — Part A: Strings

A `String` is a **sequence of characters**. It is a **reference type** (an object). Strings are **immutable** — operations create new Strings rather than modifying the original.

### Common String Methods

| Method | Description | Example |
|--------|-------------|---------|
| `length()` | Character count | `"Hello".length()` → `5` |
| `toUpperCase()` | All uppercase | `"hi".toUpperCase()` → `"HI"` |
| `toLowerCase()` | All lowercase | `"HI".toLowerCase()` → `"hi"` |
| `charAt(i)` | Char at index `i` | `"Java".charAt(1)` → `'a'` |
| `indexOf(s)` | First position of substring | `"Hello".indexOf("l")` → `2` |
| `substring(a,b)` | Chars from `a` to `b` (exclusive) | `"Hello".substring(1,4)` → `"ell"` |
| `contains(s)` | Does it contain this? | `"Hello".contains("ell")` → `true` |
| `replace(old,new)` | Replace occurrences | `"aaa".replace("a","b")` → `"bbb"` |
| `trim()` | Remove leading/trailing spaces | `"  hi  ".trim()` → `"hi"` |
| `equals(s)` | Compare content (case-sensitive) | `"Hi".equals("hi")` → `false` |
| `equalsIgnoreCase(s)` | Compare ignoring case | `"Hi".equalsIgnoreCase("hi")` → `true` |
| `isEmpty()` | Is it empty? | `"".isEmpty()` → `true` |

> ⚠️ **Never compare Strings with `==`. Always use `.equals()`.**

---

## 📖 Lesson — Part B: Java Math

The `Math` class provides static methods — no object needed.

| Method | Description | Example |
|--------|-------------|---------|
| `Math.abs(x)` | Absolute value | `Math.abs(-5)` → `5` |
| `Math.max(a,b)` | Larger value | `Math.max(3,7)` → `7` |
| `Math.min(a,b)` | Smaller value | `Math.min(3,7)` → `3` |
| `Math.pow(b,e)` | Power | `Math.pow(2,10)` → `1024.0` |
| `Math.sqrt(x)` | Square root | `Math.sqrt(16)` → `4.0` |
| `Math.round(x)` | Round | `Math.round(4.6)` → `5` |
| `Math.floor(x)` | Round down | `Math.floor(4.9)` → `4.0` |
| `Math.ceil(x)` | Round up | `Math.ceil(4.1)` → `5.0` |
| `Math.random()` | Random 0.0–0.999 | — |
| `Math.PI` | π constant | `3.14159…` |

---

## 🔑 Key Concepts

- String immutability
- String comparison with `.equals()` (not `==`)
- Zero-based index in String operations
- Math class static methods
- Generating random numbers using `Math.random()`

---

## 💻 Code Sample 1 — String Operations

```java
// File: StringDemo.java
public class StringDemo {
    public static void main(String[] args) {
        String name = "  Maria Clara  ";
        String trimmed = name.trim();

        System.out.println("Trimmed:          '" + trimmed + "'");
        System.out.println("Upper:            " + trimmed.toUpperCase());
        System.out.println("Length:           " + trimmed.length());
        System.out.println("First char:       " + trimmed.charAt(0));
        System.out.println("Substring(6,11):  " + trimmed.substring(6, 11));
        System.out.println("Index of 'Clara': " + trimmed.indexOf("Clara"));
        System.out.println("Contains 'Maria': " + trimmed.contains("Maria"));

        String replaced = trimmed.replace("Clara", "Santos");
        System.out.println("Replaced:         " + replaced);

        String s1 = "Java", s2 = "java";
        System.out.println("equals:           " + s1.equals(s2));
        System.out.println("equalsIgnoreCase: " + s1.equalsIgnoreCase(s2));
    }
}
```

---

## 💻 Code Sample 2 — Math Operations

```java
// File: MathDemo.java
public class MathDemo {
    public static void main(String[] args) {
        System.out.println("Math.abs(-42):   " + Math.abs(-42));
        System.out.println("Math.max(15,27): " + Math.max(15, 27));
        System.out.println("Math.pow(2,8):   " + Math.pow(2, 8));
        System.out.println("Math.sqrt(144):  " + Math.sqrt(144));
        System.out.println("Math.round(3.7): " + Math.round(3.7));
        System.out.println("Math.floor(3.9): " + Math.floor(3.9));
        System.out.println("Math.ceil(3.1):  " + Math.ceil(3.1));

        // Dice roll (1–6)
        int dice = (int)(Math.random() * 6) + 1;
        System.out.println("Dice roll: " + dice);

        // Circle area
        double r = 7.5;
        System.out.printf("Circle area (r=%.1f): %.4f%n", r, Math.PI * r * r);
    }
}
```

---

## ✏️ Activity 1 — String Manipulation Lab

Write `StringLab.java` using the sentence `"the quick brown fox jumps"`:
1. Print in ALL CAPS
2. Print the number of characters
3. Replace `"fox"` with `"cat"`
4. Print the first word (0 to first space)
5. Print whether it contains `"quick"`

---

## 🎯 Activity 2 — Math Challenge

Write `MathChallenge.java` that:
1. Calculates hypotenuse of a right triangle with legs 6 and 8
2. Generates 5 random integers between 10 and 99
3. Computes area and circumference of a circle with radius 5
4. Finds the larger of two numbers using `Math.max`

---

## 📝 Quiz — Week 09

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What does `"Hello".charAt(1)` return?
- A) `H`
- B) `e` ✓
- C) `l`
- D) `1`

**2.** How should you compare two String values for equality?
- A) `str1 == str2`
- B) `str1.equals(str2)` ✓
- C) `str1.compare(str2)`
- D) `str1 === str2`

**3.** What does `Math.floor(4.9)` return?
- A) `5.0`
- B) `4.9`
- C) `4.0` ✓
- D) `5`

**4.** What is the result of `"Hello".substring(1, 4)`?
- A) `"Hell"`
- B) `"ello"`
- C) `"ell"` ✓
- D) `"Hello"`

**5.** Which generates a random number between 1 and 10?
- A) `Math.random() * 10`
- B) `(int)(Math.random() * 10) + 1` ✓
- C) `Math.random(1, 10)`
- D) `new Random(10)`

---

## ✅ Weekly Outcome

By the end of Week 9, you can:
- Manipulate Strings using built-in methods
- Compare Strings correctly with `.equals()`
- Use Math class for common calculations including random numbers
