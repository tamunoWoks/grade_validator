# Student Grade Validator (with Exception Handling)

### Description
This Python script validates a student's **name** and **grade** entered by the user.  
It ensures that:
- The student’s name is not empty (cannot be blank or only spaces).
- The grade is an integer within the range `0–100`.
- If the input is valid, a friendly message is displayed with the student’s name and grade.
- If the input is invalid, the program raises and catches an **exception**, printing a clean error message instead of crashing.

This script demonstrates:
- Using **`raise Exception`** for input validation.
- Using **`assert`** for debugging and type checking.
- Wrapping logic inside **`try/except`** for graceful error handling.

### Features
- ✅ Validates that the name is not empty or whitespace.
- ✅ Validates that the grade is an integer between 0 and 100.
- ✅ Uses `assert` to ensure the grade type is always an integer.
- ✅ Friendly error messages instead of Python tracebacks.
- ✅ Modular structure with `valid()` and `main()` functions.
