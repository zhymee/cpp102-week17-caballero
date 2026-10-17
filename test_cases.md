# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Klee Caballero
Date: (date you tested)

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 |  |  |
| TC02 | Choose 2, enter 33 | "Reading added successfully." |  |  |
| TC03 | Choose 2, enter abc | Rejected; list unchanged |  |  |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged |  |  |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged |  |  |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING |  |  |
| TC07 | Choose 3 | 35 °C -> WARNING |  |  |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED |  |  |
| TC09 | Enter 9 | Error message; menu shown again |  |  |
| TC10 | Choose 5 | Exit message; program ends |  |  |

## Bugs Found and Fixed

-(No program bugs were found. The hardest tests to run correctly were TC06 and TC08. TC08 had to be run on a fresh start so the data was still the original five readings, and TC06 had to be entered as menu choice 2 and then the value 30, not typed together.)