# Week 08 — Java Operators

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

**Operators** perform operations on one or more values (operands).

### 1. Arithmetic Operators

| Op | Name | Example | Result |
|----|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3` (integer division!) |
| `%` | Modulus | `10 % 3` | `1` |

> ⚠️ `10 / 3 = 3` (not 3.33). To get decimal: cast first: `(double) 10 / 3`

### 2. Assignment Operators

| Op | Example | Equivalent |
|----|---------|------------|
| `=` | `x = 5` | assign |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `%=` | `x %= 5` | `x = x % 5` |

### 3. Comparison Operators — return `true`/`false`

| Op | Meaning | Example |
|----|---------|---------|
| `==` | Equal to | `5 == 5` → `true` |
| `!=` | Not equal | `5 != 3` → `true` |
| `>` | Greater | `7 > 3` → `true` |
| `<` | Less | `2 < 8` → `true` |
| `>=` | Greater or equal | `5 >= 5` → `true` |
| `<=` | Less or equal | `4 <= 3` → `false` |

### 4. Logical Operators

| Op | Name | Meaning |
|----|------|---------|
| `&&` | AND | Both must be `true` |
| `\|\|` | OR | At least one must be `true` |
| `!` | NOT | Reverses the boolean |

### 5. Increment / Decrement

| Op | Name | Behaviour |
|----|------|-----------|
| `++x` | Pre-increment | Increment then use |
| `x++` | Post-increment | Use then increment |
| `--x` | Pre-decrement | Decrement then use |
| `x--` | Post-decrement | Use then decrement |

---

## 🔑 Key Concepts

- Integer vs floating-point division
- Modulus for remainder/even-odd checks
- Compound assignment operators
- Short-circuit evaluation (`&&` and `||`)
- Pre vs post increment/decrement

---

## 💻 Code Sample 1 — All Operators

```java
// File: OperatorsDemo.java
public class OperatorsDemo {
    public static void main(String[] args) {
        int a = 17, b = 5;

        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));       // integer division
        System.out.println("a % b = " + (a % b));
        System.out.printf("a / b (double) = %.2f%n", (double) a / b);

        // Compound assignment
        int x = 10;
        x += 5;  System.out.println("x += 5 → " + x);
        x -= 3;  System.out.println("x -= 3 → " + x);
        x *= 2;  System.out.println("x *= 2 → " + x);

        // Increment
        int i = 5;
        System.out.println("i++: " + i++); // prints 5, then i becomes 6
        System.out.println("i:   " + i);   // 6
        System.out.println("++i: " + (++i)); // i becomes 7, prints 7

        // Logical
        boolean adult = true, hasID = false;
        System.out.println("adult && hasID: " + (adult && hasID));
        System.out.println("adult || hasID: " + (adult || hasID));
        System.out.println("!adult:         " + (!adult));
    }
}
```

---

## 💻 Code Sample 2 — Even/Odd Checker

```java
// File: EvenOdd.java
public class EvenOdd {
    public static void main(String[] args) {
        int number = 17;
        // Modulus trick: if remainder of division by 2 is 0, number is even
        if (number % 2 == 0) {
            System.out.println(number + " is Even");
        } else {
            System.out.println(number + " is Odd");
        }
    }
}
```

---

## ✏️ Activity 1 — Operator Expression Worksheet

Evaluate without running. Show your work:

```java
int x = 10, y = 3;
// 1. x + y * 2
// 2. (x + y) * 2
// 3. x % y
// 4. x / y
// 5. (double) x / y
// 6. x++ + y     (what is x after?)
// 7. ++x + y     (fresh x = 10)
// 8. x > 5 && y < 5
// 9. x == 10 || y == 10
// 10. !(x > y)
```

---

## 🎯 Activity 2 — Calculator Program

Write `SimpleCalculator.java` with `double num1 = 25.0` and `double num2 = 4.0`:
- Print: sum, difference, product, quotient (double), remainder (cast to int), quotient as %
- Use compound assignment to double `num1` and print
- Check if `num1 > num2` and print the boolean result

---

## 📝 Quiz — Week 08

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What is the result of `10 / 3` in Java (both are `int`)?
- A) `3.33`
- B) `3` ✓
- C) `4`
- D) Compile error

**2.** What does `%` do?
- A) Percentage
- B) Division
- C) Remainder ✓
- D) Power

**3.** What is the value of `x` after `int x = 5; x += 3;`?
- A) `5`
- B) `3`
- C) `8` ✓
- D) `53`

**4.** What does `++i` do (where `i = 5`)?
- A) Prints 5 then sets i to 6
- B) Sets i to 6 then uses 6 ✓
- C) Decrements i
- D) Creates a new variable

**5.** Which expression returns `true` only if BOTH conditions are true?
- A) `a || b`
- B) `a && b` ✓
- C) `!a`
- D) `a ^ b`

---

## ✅ Weekly Outcome

By the end of Week 8, you can:
- Use all arithmetic, assignment, comparison, and logical operators
- Understand operator precedence
- Explain the difference between pre- and post-increment
