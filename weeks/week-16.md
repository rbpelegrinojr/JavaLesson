# Week 16 — Java Arrays — Part 1

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

An **array** is a container that holds a **fixed number of values** of the **same data type**. Each slot is numbered starting from **index 0**.

### Declaring and Creating an Array

```java
// Method 1: Empty array (default values: 0, false, null)
int[] numbers = new int[5];

// Method 2: Initialize with values
int[] grades = {90, 85, 78, 92, 88};

// Method 3: Separate declaration and creation
String[] names;
names = new String[3];
```

### Accessing and Modifying Elements

```java
int[] arr = {10, 20, 30, 40, 50};
System.out.println(arr[0]);   // 10 (first)
System.out.println(arr[4]);   // 50 (last)
arr[2] = 99;                  // change index 2 from 30 to 99
```

> ⚠️ Accessing an invalid index causes `ArrayIndexOutOfBoundsException`

### Array Length

```java
int[] arr = {1, 2, 3, 4, 5};
System.out.println(arr.length);  // 5 (property — no parentheses!)
```

### Iterating

```java
// Standard for loop
for (int i = 0; i < arr.length; i++) {
    System.out.println("Index " + i + ": " + arr[i]);
}

// Enhanced for-each
for (int value : arr) {
    System.out.println(value);
}
```

### Default Values

| Type | Default |
|------|---------|
| `int` | `0` |
| `double` | `0.0` |
| `boolean` | `false` |
| `String` (or any Object) | `null` |

---

## 🔑 Key Concepts

- Array declaration, creation, initialization
- Zero-based indexing
- `array.length` property (no parentheses)
- `ArrayIndexOutOfBoundsException`
- Standard for vs for-each iteration

---

## 💻 Code Sample 1 — Array Basics

```java
// File: ArrayBasics.java
public class ArrayBasics {
    public static void main(String[] args) {
        int[] scores = {88, 95, 72, 60, 84, 91, 78};

        System.out.println("Count: " + scores.length);
        System.out.println("First: " + scores[0]);
        System.out.println("Last:  " + scores[scores.length - 1]);

        scores[2] = 80;  // update index 2
        System.out.println("Updated index 2: " + scores[2]);

        // Standard for
        System.out.println("\n--- Standard for ---");
        for (int i = 0; i < scores.length; i++) {
            System.out.println("scores[" + i + "] = " + scores[i]);
        }

        // For-each
        System.out.println("\n--- For-each ---");
        for (int s : scores) System.out.print(s + " ");
        System.out.println();
    }
}
```

---

## 💻 Code Sample 2 — Min, Max, Average

```java
// File: ArrayStats.java
public class ArrayStats {
    public static void main(String[] args) {
        int[] data = {34, 67, 12, 89, 45, 22, 78, 55};

        int min = data[0], max = data[0], total = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i] < min) min = data[i];
            if (data[i] > max) max = data[i];
            total += data[i];
        }

        System.out.print("Array: ");
        for (int v : data) System.out.print(v + " ");
        System.out.println();
        System.out.println("Min:     " + min);
        System.out.println("Max:     " + max);
        System.out.println("Total:   " + total);
        System.out.printf("Average: %.2f%n", (double) total / data.length);
    }
}
```

---

## ✏️ Activity 1 — Array Initialization and Access Drill

Write `ArrayDrill.java`:
1. Create a String array of 5 student names
2. Create an int array of their scores
3. Print each pair: `[Name]: [Score]`
4. Change the second score and reprint
5. Print the last score using `arr.length - 1`

---

## 🎯 Activity 2 — Gradebook Program

Write `Gradebook.java` with scores `{72, 88, 65, 91, 77, 84, 59, 93}`:
1. Find and print the highest and lowest scores
2. Calculate and print the class average
3. Count how many scored 80+ ("merit") and how many scored below 60 ("failed")
4. Print each count

---

## 📝 Quiz — Week 16

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What is the index of the FIRST element of any Java array?
- A) 1
- B) -1
- C) 0 ✓
- D) Depends on the array

**2.** Given `int[] arr = {10, 20, 30};`, what is `arr.length`?
- A) 2
- B) 3 ✓
- C) 30
- D) 0

**3.** What exception is thrown when you access an invalid array index?
- A) `NullPointerException`
- B) `IllegalArgumentException`
- C) `ArrayIndexOutOfBoundsException` ✓
- D) `IndexError`

**4.** Given `int[] arr = new int[5];`, what is the default value of `arr[2]`?
- A) `null`
- B) `undefined`
- C) `1`
- D) `0` ✓

**5.** Which loop allows you to modify array elements while iterating?
- A) For-each only
- B) Standard for loop ✓
- C) Both are equal
- D) Neither

---

## ✅ Weekly Outcome

By the end of Week 16, you can:
- Declare, create, initialize, and iterate over 1D arrays
- Access and modify individual elements
- Compute basic statistics (min, max, average, count)
