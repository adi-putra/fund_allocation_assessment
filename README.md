# Fund Allocation Assessment

Author: Muhammad Adiputra  
Date: 22/9/2025  

---

## Overview
This project allocates customer deposits into two portfolios: "High Risk" and "Retirement".  
It uses **one-time** and **monthly plans** and handles:

- Happy case: deposits match required amounts  
- Not enough deposits: Plan Order (High Risk first)  
- Too much deposits: caps at required amounts  
- Empty deposits / zero plans: returns zero allocation  
- Optional proportional split (commented in code for future use)  

---

## Files
- `fund_allocation.py` – main script with allocation functions and demo  
- `test.py` – unit tests covering all scenarios  

---

## How to Run

### Demo
```bash
python fund_allocation.py
````

Example output:

```
Happy case: deposits=[10500, 100] -> allocation={'High Risk': 10000, 'Retirement': 600}
Not enough deposits: deposits=[5000] -> allocation={'High Risk': 5000, 'Retirement': 0}
Partial enough: deposits=[10500] -> allocation={'High Risk': 10000, 'Retirement': 500}
Too much deposits: deposits=[12000] -> allocation={'High Risk': 10000, 'Retirement': 600}
Empty deposits: deposits=[] -> allocation={'High Risk': 0, 'Retirement': 0}
Zero plans: deposits=[0, 0] -> allocation={'High Risk': 0, 'Retirement': 0}
```

### Unit Tests

```bash
python test.py
```

All tests should pass if the allocation logic works correctly.

---

## Functions

**calc\_final\_alloc(onetime, monthly, deposits)**

* Allocates deposits across "High Risk" and "Retirement" portfolios
* Parameters:

  * `onetime` – dict for one-time deposit amounts
  * `monthly` – dict for monthly deposit amounts
  * `deposits` – list of deposit amounts
* Returns: dict with final allocation

**plan\_order\_alloc(highrisk\_required, retirement\_required, deposits)**

* Helper function: allocates using **Plan Order** (High Risk first)

---

## Notes

* Allocation amounts are rounded to 2 decimals
* Proportional split logic is included as comments for future use
* Demo block in `fund_allocation.py` only runs when executing the file directly

```

This format:  
- Uses **plain headings** and minimal bullets  
- Shows **commands and outputs** clearly  
- Reads top to bottom without extra sections