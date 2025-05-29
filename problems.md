---
layout: default
title: All NeetCode Problems Solved
---

# All Solved Problems

Here's a complete list of problems I've solved and documented:

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