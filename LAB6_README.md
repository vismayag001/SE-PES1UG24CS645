# L6_L7_37 – Irrigation Scheduler

## Lab 6: Code and Branch Coverage Analysis

### 1. About the Project

The Irrigation Scheduler is a Python application that determines when agricultural field zones require watering, calculates the required water volume, and generates an irrigation schedule based on the available water budget.

### 2. Application Features

The application contains three main functions:

- **should_irrigate():** Determines whether a field zone requires irrigation based on soil moisture, rainfall, and plant growth stage.
- **water_volume():** Calculates the required water volume based on field area, growth stage, and temperature.
- **schedule():** Generates an irrigation plan while considering the available water budget.

### 3. Project Files

| File | Description |
|---|---|
| `irrigation_scheduler.py` | Main application code |
| `test_irrigation_scheduler.py` | Original starter test cases |
| `CodeCoverageTest_L6_L7_37_irrigation_scheduler.py` | Tests for line coverage |
| `BranchCoverageTest_L6_L7_37_irrigation_scheduler.py` | Tests for branch coverage |
| `screenshots/` | Coverage analysis screenshots |

### 4. Software Requirements

- Python 3.13
- pytest
- coverage.py
- Visual Studio Code

Install the required packages:

```bash
python -m pip install pytest coverage
```

### 5. Code Coverage Analysis

The code coverage test file contains 16 test cases.

**Result:**
- Total statements: 38
- Missing statements: 0
- Line coverage achieved: 100%
- Tests passed: 16/16

Run code coverage:

```bash
coverage erase
coverage run -m pytest CodeCoverageTest_L6_L7_37_irrigation_scheduler.py
coverage report -m irrigation_scheduler.py
```

### 6. Branch Coverage Analysis

The branch coverage test file contains 16 test cases covering alternative decision paths in the application.

**Result:**
- Total statements: 38
- Missing statements: 0
- Total branches: 28
- Partial branches: 0
- Branch coverage achieved: 100%
- Tests passed: 16/16

Run branch coverage:

```bash
coverage erase
coverage run --branch -m pytest BranchCoverageTest_L6_L7_37_irrigation_scheduler.py
coverage report -m irrigation_scheduler.py
```

### 7. Evidence

The `screenshots/` directory contains:

- `Code_Coverage_100.png` – Final line coverage report.
- `Branch_Coverage_100.png` – Final branch coverage report.

### 8. Conclusion

The Irrigation Scheduler application was tested using pytest and coverage.py. The test cases achieved 100% line coverage and 100% branch coverage, with all 16 tests passing in each stage.