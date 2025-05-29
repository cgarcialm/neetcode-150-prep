---
layout: default
title: Valid Anagram
topic: Arrays & Hashing
difficulty: Easy
date: 2025-05-28
leetcode_url: https://leetcode.com/problems/valid-anagram/
neetcode_url: https://neetcode.io/problems/is-anagram/
github_code_path: /code/arrays-hashing/is-anagram.py
---

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, `false` otherwise.

**Examples:** `"anagram", "nagaram"` -> `true`; `"rat", "car"` -> `false`

## Optimal Solution (Character Frequency Counting)

The most efficient approach is to count the frequency of each character in both strings. If `s` and `t` have different lengths, return `false`. Otherwise, populate two frequency arrays (or hash maps) by iterating through `s` and `t`. Then, compare these frequency counts. If all counts match, the strings are anagrams.

## Key Learnings & Complexity

* **Frequency Arrays/Hash Maps:** Excellent for character counting problems with fixed/limited character sets.
* **Time Complexity:** `O(N)` (N = string length).
* **Space Complexity:** `O(1)` (fixed size of frequency array).