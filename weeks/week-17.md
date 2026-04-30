# Week 17 — Java Arrays — Part 2

> **Course:** Introduction to Java Programming | **Level:** Beginner

---

## 📖 Lesson

### Linear Search

Searching element by element:

```java
int[] arr = {15, 42, 8, 77, 23};
int target = 77, foundAt = -1;

for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) { foundAt = i; break; }
}

System.out.println(foundAt != -1 ? "Found at " + foundAt : "Not found");
```

### Copying an Array

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = new int[original.length];
for (int i = 0; i < original.length; i++) copy[i] = original[i];
```

> ⚠️ **Never do** `int[] copy = original;` — that makes both point to the **same** array!

### Reversing an Array

```java
int[] arr = {1, 2, 3, 4, 5};
int left = 0, right = arr.length - 1;
while (left < right) {
    int temp = arr[left]; arr[left] = arr[right]; arr[right] = temp;
    left++; right--;
}
// arr is now {5, 4, 3, 2, 1}
```

### 2D Arrays

A 2D array is like a table with rows and columns.

```java
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

System.out.println(matrix[1][2]);   // 6 (row 1, col 2)

// Iterate
for (int row = 0; row < matrix.length; row++) {
    for (int col = 0; col < matrix[row].length; col++) {
        System.out.printf("%3d", matrix[row][col]);
    }
    System.out.println();
}
```

### `Arrays` Utility Class

```java
import java.util.Arrays;

int[] arr = {5, 3, 8, 1, 9};
Arrays.sort(arr);
System.out.println(Arrays.toString(arr));  // [1, 3, 5, 8, 9]
```

---

## 🔑 Key Concepts

- Linear search algorithm
- Array copy (element-by-element) vs reference copy
- Array reversal algorithm
- 2D array declaration, initialization, access
- Nested loops for 2D traversal
- `Arrays.sort()` and `Arrays.toString()`

---

## 💻 Code Sample 1 — Search and Reverse

```java
// File: ArrayAlgorithms.java
import java.util.Arrays;

public class ArrayAlgorithms {
    public static void main(String[] args) {
        int[] numbers = {42, 15, 88, 7, 33, 65, 21, 90};

        // Linear Search
        int target = 65, foundAt = -1;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == target) { foundAt = i; break; }
        }
        System.out.println("Search for " + target + ": " +
            (foundAt != -1 ? "Found at index " + foundAt : "Not found"));

        // Sort
        System.out.println("Before: " + Arrays.toString(numbers));
        Arrays.sort(numbers);
        System.out.println("Sorted: " + Arrays.toString(numbers));

        // Reverse
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int temp = numbers[l]; numbers[l] = numbers[r]; numbers[r] = temp;
            l++; r--;
        }
        System.out.println("Reversed: " + Arrays.toString(numbers));
    }
}
```

---

## 💻 Code Sample 2 — 2D Array Grade Sheet

```java
// File: MatrixDemo.java
public class MatrixDemo {
    public static void main(String[] args) {
        // Rows = students, Columns = subjects
        int[][] scores = {
            {85, 90, 78, 92},   // Student 0
            {72, 68, 80, 75},   // Student 1
            {95, 88, 91, 97}    // Student 2
        };
        String[] subjects = {"Math", "Science", "English", "History"};

        System.out.printf("%-10s", "Student");
        for (String s : subjects) System.out.printf("%-10s", s);
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

---

## ✏️ Activity 1 — Search and Sort Lab

Write `SearchSortLab.java`:
1. Create an int array of 10 numbers
2. Print it with `Arrays.toString()`
3. Search for a hardcoded target value — print index or "not found"
4. Sort and print
5. Reverse manually (loop, not `Collections`) and print

---

## 🎯 Activity 2 — 2D Grade Sheet

Write `GradeSheet.java` with a 4×5 2D array (4 students, 5 subjects):
1. Initialize with your own scores
2. Print a formatted table with column headers
3. Calculate each student's average (row average)
4. Calculate each subject's class average (column average)
5. Find the highest single score in the entire 2D array

---

## 📝 Quiz — Week 17

**Instructions:** Choose the best answer. (10 points — 2 pts each)

**1.** What is the worst-case number of comparisons for a linear search on an array of 100 elements?
- A) 1
- B) 50
- C) 100 ✓
- D) 10

**2.** What is the problem with `int[] copy = original;`?
- A) Compile error
- B) Both variables reference the same array ✓
- C) Creates a proper deep copy
- D) Works only for primitives

**3.** In `int[][] arr = new int[3][4];`, how many elements does it hold?
- A) 7
- B) 3
- C) 4
- D) 12 ✓

**4.** What does `Arrays.toString(arr)` return?
- A) The memory address
- B) A formatted String representation of the array ✓
- C) The length of the array
- D) The sorted array

**5.** What is `matrix[2][1]` if `matrix = {{1,2},{3,4},{5,6}}`?
- A) 5
- B) 6 ✓
- C) 3
- D) 2

---

## ✅ Weekly Outcome

By the end of Week 17, you can:
- Implement linear search correctly
- Copy arrays element-by-element
- Reverse an array in-place
- Declare and traverse 2D arrays
- Use `Arrays.sort()` and `Arrays.toString()`
