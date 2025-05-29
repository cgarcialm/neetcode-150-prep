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
{:.no_toc} # Exclude this heading from TOC if you want

* TOC
{:toc}

Given an integer array `nums`, return `true` if any value appears at least twice, `false` if all elements are distinct.

**Examples:** `[1,2,3,1]` -> `true`; `[1,2,3,4]` -> `false`

## My Initial Approach & Reflection (Bit Manipulation)

My first thought was to use a bitmask to track seen numbers by setting the `num`-th bit. If a bit was already set, it indicated a duplicate.

**Limitations:** This approach fails for numbers outside a small integer range (e.g., 0-63). It also had a logical error in the bitwise operation.

## Optimal Solution (Hash Set)

I then pivoted to using a hash set, a standard and robust data structure for membership checking.

**Strategy:** Iterate through `nums`. For each `num`, if it's already in the `seen` set, return `True`. Otherwise, add `num` to `seen`. If the loop finishes, return `False`.

This leverages `O(1)` average-time complexity for hash set lookups and insertions.

## Key Learnings & Complexity

* **Hash Sets are Ideal:** Excellent for `O(1)` average-time duplicate detection.
* **Space-Time Trade-off:** `O(N)` space (for the set) for `O(N)` average time, a preferred efficiency.
* **Tool Choice:** Understanding data structure limitations (like bitmask range) is crucial for scalable solutions.