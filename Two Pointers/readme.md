# Two Pointers Pattern

The **Two Pointers** technique is one of the most common DSA patterns used for solving problems efficiently with **O(1) extra space** and often reducing time complexity from **O(n²)** to **O(n)**.

## Where It Is Applicable

Primarily used with:

- Arrays
- Strings
- Linked Lists

Generally not the first choice for:

- Graphs
- Trees
- Dynamic Programming
- Stack/Queue-based problems

---

## When Should You Think About Two Pointers?

### 1. Sorted Data

If the input is already sorted, or can be easily sorted, two pointers is often a strong candidate.

**Examples:**
- Two Sum II
- 3Sum
- 4Sum
- Remove Duplicates from Sorted Array

---

### 2. Finding Pairs, Triplets, or Quadruplets

Problems that ask for:

- Pairs
- Triplets
- Quadruplets

often become much simpler using two pointers after sorting.

**Examples:**
- Two Sum II
- 3Sum
- 4Sum

---

### 3. Removing Duplicates

When duplicate elements need to be removed from a sorted structure.

**Examples:**
- Remove Duplicates from Sorted Array
- Remove Duplicates from Sorted List

---

### 4. Rearranging Elements

Useful when elements need to be partitioned or moved into specific regions.

**Examples:**
- Move Zeroes
- Sort Colors
- Partition Array

---

### 5. Merging Operations

When combining two sorted structures.

**Examples:**
- Merge Sorted Array
- Merge Two Sorted Lists

---

### 6. Cycle Detection in Linked Lists

A special variation called **Fast & Slow Pointers (Floyd's Algorithm)** is used to detect cycles.

**Examples:**
- Linked List Cycle
- Find the Duplicate Number

---

## Key Characteristics

### Coordinate Multiple Indices

If a problem can be solved by moving two indices (`i`, `j`) in a coordinated manner, consider the Two Pointers pattern.

### Avoid Extra Space

Many Two Pointer solutions achieve:

- O(1) extra space
- In-place modifications

### Return Indexes Carefully

If a problem requires returning **original indices**, sorting may not be directly applicable unless index information is preserved.

---

## Common Pointer Configurations

### Opposite Ends

```text
left  ->        <- right
[1,2,3,4,5,6]
```

Used in:
- Pair sum problems
- Sorted arrays

---

### Fast & Slow Pointers

```text
slow -> one step
fast -> two steps
```

Used in:
- Cycle detection
- Middle of linked list

---

### Same Direction

```text
slow -> tracks valid position
fast -> scans array
```

Used in:
- Remove duplicates
- Move zeroes
- Sliding window variations

---

## Termination Condition

For opposite-end pointers:

```Python
while (left < right)
```

Once the pointers meet or cross:

```text
left >= right
```

the search space is exhausted and processing should stop.

---

## Quick Checklist

Before solving a problem, ask:

- Is the data sorted?
- Can sorting simplify the problem?
- Am I looking for pairs/triplets?
- Do I need to remove duplicates?
- Can I solve it without extra space?
- Is this a linked-list cycle problem?
- Can two indices move in a coordinated way?
- Do the problem asking for rearrangement?

If the answer to any of these is **yes**, the Two Pointers pattern is worth considering.