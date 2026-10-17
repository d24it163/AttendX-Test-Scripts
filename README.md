# AttendX-Test-Scripts

Automation test scripts for **AttendX**, a student attendance application.
Scripts are version-controlled here so the three QA engineers stop sharing files by email/pen drive.

## Scripts
| File | Purpose |
|------|---------|
| `login_test.py` | Verifies valid login reaches the dashboard and an invalid password shows an error. |
| `attendance_test.py` | Logs in as a teacher, marks a student present and verifies the "saved" confirmation. |

## Requirements
- Python 3.10+
- `pip install selenium pytest`
- Chrome + ChromeDriver (Selenium 4 manages the driver automatically)

## How to run
```
pytest login_test.py -v
pytest attendance_test.py -v
```

## Team workflow
1. `git pull` before starting work
2. Make changes, `git add`, `git commit -m "clear message"`
3. `git push`
