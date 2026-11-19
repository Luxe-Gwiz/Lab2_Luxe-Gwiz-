# Student Grade Evaluation System

## Project Description
This Python project focuses on developing a grade evaluation system for ALU students. It processes student assessment information, calculates academic performance and generates a grade report.

## System Requirements
The system should be able to:
- Receive student and assessment information.
- Interpret assignment scores, categories and weights.
- Calculate subject performance based on assessment weights.
- Determine students' GPA and Pass/Fail status.
- Identify eligible formative assignments for resubmission.
- Generate and save student grade reports.

*Currently, the program collects student information through user input.*

## Three Main Functions

1. **`validate_weights()`** – Checks that total assessment weight is 100%, with 60% Formative and 40% Summative.
2. **`calculate_grade()`** – Calculates the student's total weighted grade and GPA.
3. **`evaluate_student()`** – Coordinates the evaluation process, determines Pass/Fail status and identifies resubmission options.

## Calculation Formulas

**Weighted Grade:**

`(Assignment Score × Assignment Weight) / 100`

**Total Grade:**

`Sum of all weighted assignment grades`

**GPA:**

`(Total Grade / 100) × 5`

**Category Performance:**

`(Total Weighted Category Grade / Category Weight) × 100`

A student passes when both Formative and Summative performance are at least 50%.

## Error Handling
The system uses:
- `try/except` to handle invalid numerical inputs and file errors.
- `ValueError` handling to prevent invalid score and weight entries.
- Validation checks to ensure scores and assessment weights meet the required conditions.

## Data Storage and Archiving
Student results are saved in CSV files using `save_results()`.

The Bash script `organizer.sh` automates archiving by:
- Creating an `archive` directory if it does not exist.
- Renaming and moving `grades.csv` using a timestamp.
- Creating a new empty `grades.csv`.
- Recording each archiving operation in `organizer.log`.

## How to Run

Run the Python program:

```bash
python3 grade.py
```

Run the archive script:

```bash
chmod +x organizer.sh
./organizer.sh
```
