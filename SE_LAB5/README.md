# Lab 5: Static Code Analysis — Campus Parking Permit Manager

## 1. Project Overview

The Campus Parking Permit Manager is a Python application that manages vehicle parking permits across campus parking zones. It supports permit registration, revocation, expiry checking, and the identification of vehicles that are not authorized to park in a specified zone.

This lab demonstrates how static code analysis tools can identify code quality, style, maintainability, and security issues, and how those issues can be addressed through systematic code improvements.

## 2. Features

- Register parking permits for vehicles.
- Assign permits to campus parking zones A, B, and C.
- Generate permit numbers and expiry dates.
- Revoke existing parking permits.
- Check whether a permit has expired.
- Scan a parking zone and flag vehicles with missing, invalid-zone, or expired permits.
- Save and load permit information using JSON.

## 3. Technologies and Tools

- **Python 3.13** — Programming language.
- **Pylint** — Identifies programming errors, code quality issues, and maintainability problems.
- **Flake8** — Checks Python style and coding convention violations.
- **Bandit** — Identifies potential security issues in Python code.
- **Git and GitHub** — Version control and project submission.
- **Visual Studio Code** — Development environment.

## 4. Project Structure

```text
L5_10_parking_permits/
├── parking_system.py
├── parking_system_before.py
├── permits.json
├── pylint_report.txt
├── flake8_report.txt
├── bandit_report.txt
└── reports/
    ├── before/
    │   ├── pylint_report.txt
    │   ├── flake8_report.txt
    │   └── bandit_report.txt
    └── after/
        ├── pylint_report.txt
        ├── flake8_report.txt
        └── bandit_report.txt
```

**Note:** The report files record the static analysis results before and after the code improvements. The `parking_system_before.py` file preserves the original implementation for comparison.

## 5. Installation

Ensure Python is installed and available from the terminal.

Install the required static analysis tools:

```bash
python -m pip install pylint flake8 bandit
```

## 6. Running the Application

Run the parking permit manager:

```bash
python parking_system.py
```

The application loads the permit database, performs sample permit operations, scans a parking zone, asks for a vehicle plate to revoke, and saves the updated permit information.

Press Enter when prompted to skip revoking a permit.

## 7. Static Code Analysis

The project uses three static analysis tools.

### Pylint

Pylint evaluates code quality, naming conventions, documentation, exception handling, and other programming practices.

Generate a report:

```bash
python -m pylint parking_system.py --output-format=text > pylint_report.txt
```

### Flake8

Flake8 checks Python style, line length, indentation, and related coding convention violations.

Generate a report:

```bash
python -m flake8 parking_system.py --output-file=flake8_report.txt
```

### Bandit

Bandit scans Python code for potential security vulnerabilities.

Generate a report:

```bash
python -m bandit -r parking_system.py -f txt -o bandit_report.txt
```

## 8. Before-and-After Comparison

The original implementation is preserved in `parking_system_before.py`.

The `reports/before/` directory contains the original static analysis reports, while `reports/after/` contains the reports generated after the code improvements.

These reports can be compared to evaluate changes in code quality, style compliance, and potential security issues.

The final version achieved a **Pylint score of 10.00/10** in the recorded analysis run. The recorded Bandit report identified no issues, and the Flake8 report was empty, indicating that no Flake8 violations were reported in that run.

## 9. Issues Identified and Fixed

The original implementation was examined using Pylint, Flake8, and Bandit.

The improvements addressed issues such as:

- Missing module and function docstrings.
- Incorrect naming conventions.
- Overly long lines.
- Broad exception handling.
- Mutable default arguments.
- File handling without context managers.
- File encoding not being explicitly specified.
- Potential security concerns related to random number generation.

The original and final reports provide evidence of the analysis results. The exact fixes should be documented in the project's `issues.md` file.

## 10. Deliverables

The project includes:

1. **`parking_system.py`** — Improved parking permit manager.
2. **`parking_system_before.py`** — Original implementation before fixes.
3. **`permits.json`** — Stored parking permit data.
4. **`issues.md`** — Documentation of identified issues and their fixes, if included in the project.
5. **`reflection.md`** — Answers to the lab's reflection questions, if included in the project.
6. **`reports/before/`** — Original static analysis reports.
7. **`reports/after/`** — Final static analysis reports.
8. **Root-level report files** — Additional reports generated during the analysis process.

## 11. Conclusion

This lab demonstrates how static code analysis can improve the quality, readability, maintainability, and security of a Python application.

Using Pylint, Flake8, and Bandit helped identify potential weaknesses in the original implementation and verify the results of subsequent improvements.

The project also demonstrates the importance of preserving the original implementation and recording before-and-after analysis results for comparison.