# Lab 5: Static Code Analysis — Issues and Fixes

## Project: Campus Parking Permit Manager

Static code analysis was performed using Pylint, Flake8, and Bandit to identify code quality, style, and security issues in the parking permit management program.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Missing exception specificity | Code Quality / Reliability | Before: 16, 22, 29, 43 | Bare `except` clauses catch all exceptions, including unexpected system exceptions, making debugging difficult. | Replaced bare exception handlers with appropriate specific exception types. |
| Dangerous default argument | Code Quality | Before: 9 | Using a mutable list as a default argument can cause unintended data sharing between function calls. | Changed the default argument to `None` and initialized the list inside the function. |
| Missing docstrings | Code Quality / Maintainability | Multiple locations | Missing module, function, or method docstrings make the code harder to understand and maintain. | Added appropriate documentation strings. |
| Lines exceeding the style limit | Code Style | Before: 13, 27, 62 | Long lines reduce readability and violate the configured Flake8 line-length limit. | Split long statements into shorter, readable lines. |
| Missing blank lines | Code Style | Multiple locations | Insufficient blank lines between definitions violate Python style conventions. | Added the required blank lines between top-level definitions and classes. |
| Insecure random number generation | Security | Before: 16 | The standard pseudo-random generator is not suitable for security-sensitive token generation. | Used a cryptographically appropriate random generator for permit identifiers where unpredictability is required. |
| File handling without explicit encoding | Code Quality / Portability | Before: 42, 47 | Opening text files without specifying an encoding may produce inconsistent behavior across environments. | Specified an explicit encoding when opening text files. |
| Use of global state | Maintainability | Before: 40 | Modifying global variables makes program behavior harder to trace and test. | Reduced reliance on global state by passing data through functions where appropriate. |

## Verification

After making the changes, the updated program was checked using all three static analysis tools:

- **Pylint:** 10.00/10.
- **Flake8:** No reported violations in the final report.
- **Bandit:** No issues identified in the final report.

The before-and-after reports are retained in the `reports/before/` and `reports/after/` directories.

The final program was intended to preserve the original parking permit management functionality while improving code quality, readability, and security.