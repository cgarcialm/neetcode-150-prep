---
layout: default
title: NeetCode 150 Interview Prep Journey
---

# Welcome to My NeetCode 150 Prep Journey!

This site documents my progress and learnings while tackling the [NeetCode 150](https://neetcode.io/roadmap) problem list, a curated set of problems designed for software engineer interview preparation.

## My Progress

* **Arrays & Hashing:** Completed 9 problems (from the first batch).
* **Current Focus:** Starting **Two Pointers**!

Stay tuned for more problem solutions and detailed breakdowns.

---

## Solved Problems

Here's a list of problems I've solved and documented so far:

<table>
  <thead>
    <tr>
      <th>Date Solved</th>
      <th>Problem</th>
      <th>Topic</th>
      <th>Difficulty</th>
    </tr>
  </thead>
  <tbody>
    {% assign sorted_problems = site.problems | sort: "date" | reverse %}
    {% for problem in sorted_problems %}
    <tr>
      <td>{{ problem.date | date: "%Y-%m-%d" }}</td>
      <td><a href="{{ problem.url | relative_url }}">{{ problem.title }}</a></td>
      <td>{{ problem.topic }}</td>
      <td>{{ problem.difficulty }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

### Useful Links
* [NeetCode Roadmap](https://neetcode.io/roadmap)
* [My GitHub Code Repository (Coming Soon)](/code) # We'll link this later