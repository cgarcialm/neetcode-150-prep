---
layout: default
title: Two Sum
topic: Arrays & Hashing
difficulty: Easy
date: 2025-05-28
leetcode_url: https://leetcode.com/problems/two-sum/
neetcode_url: https://neetcode.io/problems/two-integer-sum/
github_code_path: /code/arrays-hashing/two-sum.py
---

## Problem Description

Find two numbers in `nums` that sum to `target`. Return their positions. One solution exists, no element reuse.

**Examples:** `[2,7,11,15], 9` -> `[0,1]`; `[3,2,4], 6` -> `[1,2]`

## My Optimal Solution (Two-Pass Dictionary)

My solution uses a dictionary. First, I fill it with numbers and their positions. Then, in a second pass, I check for the `diff = target - current_number` to find the pair, handling duplicates.

## Improvement: One-Pass Hash Map

A faster way is a single-pass approach. As I go through `nums`, I check if the `complement` (`target - current_number`) is already in the dictionary. If yes, I found the pair. If not, I add the current number to the dictionary.

## Key Learnings & Complexity

* **Dictionaries (Hash Maps):** Essential for quick lookups (`O(1)` average).
* **One-Pass vs. Two-Pass:** Single pass is often more efficient by combining steps.
* **Time:** `O(N)`.
* **Space:** `O(N)`.
