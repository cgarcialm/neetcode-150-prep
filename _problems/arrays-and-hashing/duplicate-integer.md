---
layout: default
title: Duplicate Integer
topic: Arrays & Hashing
difficulty: Easy
date: 2025-05-28
leetcode_url: https://leetcode.com/problems/contains-duplicate/
neetcode_url: https://neetcode.io/problems/duplicate-integer/
github_code_path: /code/arrays-hashing/duplicate-integer.py
---

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice, `false` if all elements are distinct.

**Example 1:** `[1,2,3,1]` -> `true`
**Example 2:** `[1,2,3,4]` -> `false`

## My Initial Approach & Reflection (Bit Manipulation)

My first idea was to use bit manipulation, employing a single integer `res` as a bitmask. The concept was to set a bit (`1 << num`) for each `num` encountered. If the bit was already set, it would signal a duplicate.

**Why it fell short:** This method had critical limitations:
1.  **Integer Range:** It's restricted to a small range of non-negative integers (e.g., 0-63 on a 64-bit system), failing for larger or negative numbers.
2.  **Bitwise Error:** I incorrectly used the `AND` (`&`) operator instead of `OR` (`|`) to set bits, which caused incorrect behavior.

## Optimal Solution (Hash Set)

Recognizing the limitations of the bitmask, I pivoted to a hash set, which is a standard and robust data structure for membership checking.

**Strategy:**
1.  Initialize an empty `set` (e.g., `seen`).
2.  Iterate through each `num` in the input array.
3.  If `num` is found in `seen`, a duplicate exists; return `True`.
4.  Otherwise, add `num` to `seen`.
5.  If the loop completes without finding a duplicate, return `False`.

This strategy leverages the average `O(1)` time complexity of hash set lookups and insertions.

## Key Learnings & Complexity

* **Hash Sets for Membership:** Ideal for `O(1)` average-time duplicate detection and quick membership checks.
* **Space-Time Trade-off:** Achieves optimal `O(N)` average time complexity by using `O(N)` space (for the set), a common and often preferred trade-off.
* **Choosing the Right Tool:** It's vital to understand the constraints of different data structures (e.g., bitmask integer limits) to select the most appropriate and scalable solution for a given problem.