# Simulated Device Monitoring and Alert System

**Student Name:** Klhean Zhyme Caballero
**Student Number:** 2600405
**Section:** 1-CpE-C

## Project Description
This program monitors simulated device temperature readings. It stores the readings in a list, accepts new valid readings, and classifies each one as NORMAL, WARNING, or CRITICAL. It also generates a numerical summary and an overall monitoring status. It was built as the Week 17 integrative project for CPP102.

## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading as NORMAL, WARNING, or CRITICAL
- Generate a summary: number of readings, total, average, minimum, maximum, category counts and percentages, and overall status
- Reject invalid menu choices and invalid readings without crashing

## Requirements
- Python 3 (no external packages)

## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`

   (On macOS or Linux, type: `python3 device_monitor.py`)

## Sample Output
```
MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

## Test Cases
I performed 10 tests. 10 passed and 0 failed. Full details are in [test_cases.md](test_cases.md).

## Known Limitations
- Readings are lost when the program closes, because nothing is saved to a file.
- Readings cannot be edited or deleted after they are added.
- The temperature limits (30 and 35) are fixed for this classroom simulation and are not real device-safety standards.
- (add your own if you notice more)

## Reflection
The hardest part of this project was not the code itself but getting everything onto GitHub, because Git was not installed on my computer and the terminal kept saying it did not recognize the command. I learned that a terminal opened before an installation does not see the new program, so I had to close and reopen VS Code. While testing, I also made mistakes such as typing notes like "add 30" into the menu, which my program correctly rejected as an invalid choice, and I learned that test inputs must be typed exactly as the program asks. I also learned that the summary test must be run on a fresh start, because adding readings changes the total and average. Next time, I would commit after each milestone while coding so my commit history builds up naturally, and I would improve the program by saving the readings to a file so they are not lost when it closes.