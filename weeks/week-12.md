# Week 12 — Java Switch

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

The `switch` statement is an alternative to long `if-else if` chains when comparing **one variable** against **multiple specific values**.

### Syntax

```java
switch (expression) {
    case value1:
        // code
        break;        // prevents fall-through
    case value2:
        // code
        break;
    default:
        // runs if no case matches
}
```

> ⚠️ **Fall-through:** Omitting `break` causes execution to continue into the next case!

### What can go in `switch`?
- `int`, `char`, `String` (since Java 7), `enum`

### Intentional Fall-through Example

```java
int month = 4;
switch (month) {
    case 4: case 6: case 9: case 11:
        System.out.println("30 days"); break;
    case 2:
        System.out.println("28 or 29 days"); break;
    default:
        System.out.println("31 days");
}
```

### `if-else` vs `switch`

| Use `switch` when… | Use `if-else` when… |
|--------------------|---------------------|
| One variable, exact values | Comparing ranges |
| 3+ discrete cases | Complex boolean conditions |
| int, char, String | Multiple variables |

---

## 🔑 Key Concepts

- `switch`, `case`, `break`, `default`
- Fall-through behaviour
- Intentional fall-through for grouping cases
- Switch with String values
- When to choose switch over if-else

---

## 💻 Code Sample 1 — Day of Week

```java
// File: DayOfWeek.java
public class DayOfWeek {
    public static void main(String[] args) {
        int day = 3;

        switch (day) {
            case 1: System.out.println("Monday");    break;
            case 2: System.out.println("Tuesday");   break;
            case 3: System.out.println("Wednesday"); break;
            case 4: System.out.println("Thursday");  break;
            case 5: System.out.println("Friday");    break;
            case 6: System.out.println("Saturday");  break;
            case 7: System.out.println("Sunday");    break;
            default: System.out.println("Invalid (use 1-7)");
        }
    }
}
```

**Expected Output:** `Wednesday`

---

## 💻 Code Sample 2 — String Switch (Menu)

```java
// File: MenuSwitch.java
public class MenuSwitch {
    public static void main(String[] args) {
        String command = "START";

        switch (command.toUpperCase()) {
            case "START": System.out.println("Game starting…");  break;
            case "STOP":  System.out.println("Game stopped.");    break;
            case "PAUSE": System.out.println("Game paused.");     break;
            case "QUIT":  System.out.println("Goodbye!");         break;
            default:      System.out.println("Unknown command.");
        }
    }
}
```

---

## ✏️ Activity 1 — Month Days Calculator

Write `MonthDays.java` using switch with fall-through to print:
- How many days are in each month (1–12)
- Assume February = 28 days
- For invalid numbers print an error

---

## 🎯 Activity 2 — Simple ATM Menu

Write `ATMMenu.java` simulating an ATM:
- `1` → "Checking balance…"
- `2` → "Processing withdrawal…"
- `3` → "Processing deposit…"
- `4` → "Printing mini-statement…"
- `0` → "Thank you. Goodbye!"
- Default → "Invalid option."

Test with at least 4 different values.

---

## 📝 Quiz — Week 12

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What is the purpose of `break` in a switch statement?
- A) Exits the program
- B) Prevents fall-through to the next case ✓
- C) Skips the current case
- D) Marks the default case

**2.** Which data type CANNOT be used in a switch expression?
- A) `int`
- B) `String`
- C) `char`
- D) `double` ✓

**3.** What runs when no `case` matches?
- A) The first case
- B) Nothing
- C) The `default` block ✓
- D) A compile error

**4.** What is "fall-through" in a switch?
- A) The program crashes
- B) Execution continues to the next case without a break ✓
- C) The default block runs
- D) The loop restarts

**5.** How many `default` labels can a switch have?
- A) 0
- B) 1 ✓
- C) Any number
- D) Equal to the number of cases

---

## ✅ Weekly Outcome

By the end of Week 12, you can:
- Write correct switch statements with break and default
- Control fall-through intentionally
- Use switch with integers and strings
- Decide when switch is better than if-else
