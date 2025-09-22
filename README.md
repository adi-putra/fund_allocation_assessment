# Fund Allocation Assessment

**Author:** Muhammad Adiputra  
**Date:** 22/9/2025  

---

## Overview
This Python project allocates customer deposits to two portfolios: `"High Risk"` and `"Retirement"` based on **one-time** and **monthly deposit plans**.  

The allocation handles multiple scenarios:
- **Happy case:** deposits exactly match the required amounts  
- **Not enough deposits:** allocates using **Plan Order** (High Risk first)  
- **Too much deposits:** caps allocation at required amounts  
- **Empty deposits / zero plans:** returns zero allocation  
- **Optional proportional split** (commented for future use)  

---

## Files
- `fund_allocation.py` – main module with allocation functions and a demo block  
- `test.py` – unit tests covering all scenarios including edge cases  

---

## Usage

### Run the Demo
Execute the main script to see allocation examples:

```bash
python fund_allocation.py

Example output:

Happy case: deposits=[10500, 100] -> allocation={'High Risk': 10000, 'Retirement': 600}
Not enough deposits: deposits=[5000] -> allocation={'High Risk': 5000, 'Retirement': 0}
Partial enough: deposits=[10500] -> allocation={'High Risk': 10000, 'Retirement': 500}
Too much deposits: deposits=[12000] -> allocation={'High Risk': 10000, 'Retirement': 600}
Empty deposits: deposits=[] -> allocation={'High Risk': 0, 'Retirement': 0}
Zero plans: deposits=[0, 0] -> allocation={'High Risk': 0, 'Retirement': 0}

Run Unit Tests
python test.py


All tests should pass if the module works correctly.

Functions
calc_final_alloc(onetime: dict, monthly: dict, deposits: list) -> dict

Calculates final allocation of deposits across "High Risk" and "Retirement" portfolios.

Parameters:

onetime – dict with one-time deposit requirements per portfolio

monthly – dict with monthly deposit requirements per portfolio

deposits – list of deposit amounts from the customer

Returns:
A dictionary:

{"High Risk": <amount>, "Retirement": <amount>}

plan_order_alloc(highrisk_required: float, retirement_required: float, deposits: float) -> dict

Helper function that allocates deposits using Plan Order (High Risk first, then Retirement)

Notes

Type hints are used for clarity

Allocation amounts are rounded to 2 decimals

Proportional split logic is included as comments for potential future use

The demo block in fund_allocation.py only runs when executing the file directly