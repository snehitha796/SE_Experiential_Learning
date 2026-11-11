# Lab 5: Static Code Analysis — Reflection

## 1. What did you learn from using static analysis tools?

I learned that static analysis tools can identify code quality, formatting, maintainability, and security problems without requiring the program to be executed. Pylint helped evaluate code quality and naming conventions, Flake8 identified style violations, and Bandit detected potential security concerns.

## 2. What is the difference between Pylint, Flake8, and Bandit?

Pylint evaluates overall Python code quality, including naming conventions, documentation, and potential programming errors. Flake8 checks adherence to Python style guidelines and identifies common programming issues. Bandit focuses on detecting potential security vulnerabilities in Python code. Using all three tools provides a more comprehensive analysis.

## 3. Why is static code analysis important even when a program runs correctly?

A program can produce the expected output and still contain security weaknesses, poor coding practices, or maintainability problems. Static analysis helps identify these issues early, reducing the likelihood of defects and making the code easier to understand, test, and maintain.

## 4. What challenges did you face, and how did you address them?

During this lab, the analysis tools reported issues involving exception handling, line length, code formatting, and security practices. I reviewed the reports, corrected the identified problems in the source code, and reran the tools to verify the results. The final Pylint report showed a score of 10.00/10, the Flake8 report contained no reported violations, and the Bandit report identified no issues.